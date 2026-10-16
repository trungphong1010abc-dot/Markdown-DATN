# Bảng linh kiện và nối chân PCB SMD — Altium

**Cách đọc:** `U2.30` = IC U2, chân 30. Các điểm cùng tên **net** được nối điện với nhau. Trong bảng linh kiện hai chân, nối lần lượt **đầu 1 → net thứ nhất**, **đầu 2 → net thứ hai**.

| Tra cứu | Nội dung |
|---|---|
| **Nguồn — U1, J1** | Mục 2: linh kiện và kết nối 5 V → 3,3 V |
| **MCU — U2, J2** | Mục 3: nguồn → tín hiệu → clock/reset/SWD |
| **AFE dòng — U3, J3** | Mục 4: BIAS → đệm dòng → lọc ADC |
| **AFE quang — U4, D1** | Mục 5: op-amp → hồi tiếp → photodiode |
| **RS485 — U5, J4** | Mục 6: UART → điều khiển → A/B |
| **Lựa chọn thiết kế** | Mục 8: mã đã chọn, cơ sở tính và điều kiện áp dụng |

> **Căn cứ kết nối:** nhánh CT, BIAS và quang theo mục 4.2, trang 4–6 của PDF kết nối mô-đun. PCB dùng linh kiện SMD và MAX3485 điều khiển chiều qua PB0; bảng dưới đây dùng mã linh kiện PCB.

Số chân IC áp dụng cho đúng package trong bảng, đối chiếu datasheet [1]–[5]. Mã U/R/C/J là quy ước của schematic này.

# 1. Danh sách khối và net liên kết

| Khối | IC chính | Đầu nối | Net liên khối |
|---|---|---|---|
| Nguồn | U1 LD1117S33TR | J1 jack DC | `+5V_IN`, `+3V3`, `GND` |
| MCU và SWD | U2 STM32F103C8T6 | J2 SWD | `ADC_CURRENT`, `ADC_LIGHT`, `UART1_TX`, `UART1_RX`, `RS485_DIR`, `SWDIO`, `SWCLK`, `NRST` |
| AFE dòng | U3 MCP6002-I/SN | J3 CT | `BIAS_1V65`, `ADC_CURRENT` |
| AFE quang | U4 MCP6002-I/SN, D1 VBPW34S | — | `BIAS_1V65`, `ADC_LIGHT` |
| RS485 | U5 MAX3485ESA+ | J4 A/B/`GND` | `UART1_TX`, `UART1_RX`, `RS485_DIR`, `RS485_A`, `RS485_B` |

Adapter 5 V–2 A, ST-Link V2, CT và USB–RS485 CH340 là thiết bị ngoài PCB. PCB dùng nguồn từ adapter; bộ USB–RS485 dùng nguồn USB laptop.

# 2. Khối nguồn

## 2.1. Linh kiện

| Mã | Linh kiện / giá trị | Package | SL | Trạng thái |
|---|---|---|---:|---|
| J1 | Same Sky PJ-102AH, 24 VDC, 5 A | THT theo bản vẽ hãng | 1 | Lắp; adapter tâm dương, phích phù hợp jack |
| U1 | LD1117S33TR, 3,3 V | SOT-223 | 1 | Lắp |
| C1 | 10 µF, 16 V, ±10%, tantalum; T491B106K016AT tham khảo | 3528 | 1 | Có phân cực |
| C2 | KEMET T491C226K016AT; 22 µF, 16 V, ±10% | 6032, case C | 1 | Có phân cực; ESR 1,5 Ω tại 100 kHz, 25°C |

## 2.2. Nối nguồn

| Linh kiện / chân | Nối tới net | Cùng net với |
|---|---|---|
| J1.1 — tiếp điểm tâm (+) | `+5V_IN` | `U1.3` IN, C1 cực + |
| J1.2 — tiếp điểm vỏ (−) | `GND` | `U1.1` `GND`, C1 cực −, C2 cực − |
| `U1.1` `GND` | `GND` | Mass toàn PCB |
| `U1.2` OUT | `+3V3` | C2 cực +, nguồn các IC |
| `U1.3` IN | `+5V_IN` | J1 dương, C1 cực + |
| U1 tab tản nhiệt | `+3V3` | Cùng điện với OUT |

Tab LD1117 nối OUT theo datasheet [2]. Nếu footprint đánh tab là pad 4, ánh xạ pad 4 về +3V3; nếu thư viện dùng chung số 2 cho tab, giữ theo cách đánh số của footprint. J1 dùng PJ-102AH: chân 1 tâm dương → +5V_IN; chân 2 vỏ → GND; chân 3 là tiếp điểm công tắc, để trống. Adapter chọn tâm dương, điện áp 5 V, phích Ø5,5 mm phù hợp trụ tâm Ø2,0 mm của jack.

# 3. Khối MCU và nạp/debug

## 3.1. Linh kiện

| Mã | Linh kiện / giá trị | Package | SL |
|---|---|---|---:|
| U2 | STM32F103C8T6 | LQFP-48 | 1 |
| C3, C4, C5 | 100 nF, X7R, 16 V | 0805 | 3 |
| C6 | 10 µF, X7R, 16 V | 0805 | 1 |
| C7 | 100 nF, X7R, 16 V | 0805 | 1 |
| C8 | 1 µF, X7R, 16 V | 0805 | 1 |
| Y1 | Abracon ABM3B-8.000MHZ-B2-T; 8 MHz, CL = 18 pF | SMD 5,0 × 3,2 mm, 4 pad | 1 |
| C9, C10 | KEMET C0805C270J5GACTU; 27 pF, ±5%, C0G, 50 V | 0805 | 2 |
| R1 | 10 kΩ, 1%, 0,125 W | 0805 | 1 |
| C11 | 100 nF, X7R, 16 V | 0805 | 1 |
| J2 | SWD 1×5, bước chân 2,54 mm | Header | 1 |

## 3.2. Nối chân U2 theo chức năng

### A. Nguồn và mass

| Chân U2 | Tên chân | Net | Điểm nối |
|---:|---|---|---|
| 1 | VBAT | `+3V3` | Nguồn chung, theo cấu hình thiết kế |
| 8 | VSSA | `GND` | Mass phần tương tự |
| 9 | VDDA | `+3V3` | C7, C8 |
| 23 | VSS_1 | `GND` | Mass |
| 24 | VDD_1 | `+3V3` | C3 |
| 35 | VSS_2 | `GND` | Mass |
| 36 | VDD_2 | `+3V3` | C4 |
| 47 | VSS_3 | `GND` | Mass |
| 48 | VDD_3 | `+3V3` | C5 |

### B. ADC và RS485

| Chân U2 | Tên chân | Net | Điểm nối |
|---:|---|---|---|
| 10 | PA0 / ADC_IN0 | `ADC_CURRENT` | Đầu ra bộ lọc dòng |
| 11 | PA1 / ADC_IN1 | `ADC_LIGHT` | Đầu ra AFE quang |
| 18 | PB0 | `RS485_DIR` | `U5.2`, `U5.3`, R7 |
| 30 | PA9 / USART1_TX | `UART1_TX` | `U5.4` DI |
| 31 | PA10 / USART1_RX | `UART1_RX` | `U5.1` RO |

### C. Clock, reset và nạp/debug

| Chân U2 | Tên chân | Net | Điểm nối |
|---:|---|---|---|
| 5 | PD0 / OSC_IN | `HSE_IN` | Đầu dao động Y1, C9 |
| 6 | PD1 / OSC_OUT | `HSE_OUT` | Đầu dao động còn lại Y1, C10 |
| 7 | `NRST` | `NRST` | C11, `J2.5` |
| 34 | PA13 / `SWDIO` | `SWDIO` | `J2.3` |
| 37 | PA14 / `SWCLK` | `SWCLK` | `J2.4` |
| 44 | `BOOT0` | `BOOT0` | R1 đầu 1 |

## 3.3. Chân MCU để trống

Các chân dưới đây để trống ở schematic theo phạm vi chức năng hiện tại; không nối chúng thành cùng một net mang tên NC.

| Số chân | Tên chân |
|---|---|
| 2, 3, 4 | PC13, PC14, PC15 |
| 12, 13, 14, 15, 16, 17 | PA2, PA3, PA4, PA5, PA6, PA7 |
| 19, 20, 21, 22 | PB1, PB2/BOOT1, PB10, PB11 |
| 25, 26, 27, 28, 29 | PB12, PB13, PB14, PB15, PA8 |
| 32, 33 | PA11, PA12 |
| 38, 39, 40, 41, 42, 43 | PA15, PB3, PB4, PB5, PB6, PB7 |
| 45, 46 | PB8, PB9 |

BOOT0 cố định thấp qua R1; PB2/BOOT1 để trống theo cấu hình này.

## 3.4. Nối tụ nguồn, thạch anh và BOOT0/reset

| Linh kiện | Đầu 1 | Đầu 2 | Ghi chú |
|---|---|---|---|
| C3 **(100 nF)** | `+3V3`, tại `U2.24` | `GND` | Tụ VDD_1 |
| C4 **(100 nF)** | `+3V3`, tại `U2.36` | `GND` | Tụ VDD_2 |
| C5 **(100 nF)** | `+3V3`, tại `U2.48` | `GND` | Tụ VDD_3 |
| C6 **(10 µF)** | `+3V3` | `GND` | Tụ nguồn tổng |
| C7, C8 **(100 nF / 1 µF)** | `+3V3`, tại `U2.9` | `GND` | Hai tụ song song cho VDDA |
| Y1.1 | `HSE_IN` | — | Đầu dao động tới U2.5 |
| Y1.3 | `HSE_OUT` | — | Đầu dao động tới U2.6 |
| Y1.2, Y1.4 | `GND` | — | Hai pad vỏ theo Abracon |
| C9 **(27 pF)** | `HSE_IN` | `GND` | CL = 18 pF; ký sinh thiết kế 4,5 pF |
| C10 **(27 pF)** | `HSE_OUT` | `GND` | CL = 18 pF; ký sinh thiết kế 4,5 pF |
| R1 **(10 kΩ)** | `BOOT0` | `GND` | Kéo xuống 10 kΩ |
| C11 **(100 nF)** | `NRST` | `GND` | Tụ reset |

Y1: pad 1 và 3 là hai đầu dao động; pad 2 và 4 nối GND theo bản vẽ Abracon. Chọn C9 = C10 = 27 pF theo $C_X=2(C_L-C_s)=2(18-4,5)=27\ \mathrm{pF}$; $C_s=4,5\ \mathrm{pF}$ là giả thiết ký sinh của chân và PCB. Điện dung ký sinh và khởi động HSE được xác nhận trên bo thực; giá trị lắp thiết kế đã chọn là 27 pF.

## 3.5. Đầu nối J2 SWD

| Chân J2 | Net | Chân MCU |
|---:|---|---|
| 1 | `+3V3` | Nguồn mạch đích |
| 2 | `GND` | `GND` |
| 3 | `SWDIO` | `U2.34` |
| 4 | `SWCLK` | `U2.37` |
| 5 | `NRST` | `U2.7` |

Thứ tự J2 là quy ước cho PCB này, cần ánh xạ theo nhãn ST-Link V2 thực tế. +3V3 là mức nguồn mạch đích; khi PCB đã cấp nguồn từ adapter, không nối thêm một đầu ra nguồn 3,3 V của ST-Link vào để cấp song song. Chân VTref của đầu nạp, nếu có, nhận mức tham chiếu từ mạch đích theo hướng dẫn đầu nạp.

# 4. Khối CT và AFE dòng

## 4.1. Linh kiện

| Mã | Linh kiện / giá trị | Package | SL |
|---|---|---|---:|
| CT1 | DL-CT08CL6-1000/1 | Ngoài PCB | 1 |
| J3 | Phoenix Contact 1715721 — MKDS 1,5/2-5,08; terminal bắt vít 2 cực | THT, bước 5,08 mm | 1 |
| U3 | MCP6002-I/SN | SOIC-8 | 1 |
| R2 | Vishay CRCW0805150RFKEA; 150 Ω, 1%, 0,125 W | 0805 | 1 |
| R3, R4 | 10 kΩ, 1%, 0,125 W | 0805 | 2 |
| C12 | 100 nF, X7R, 16 V | 0805 | 1 |
| R5 | 1 kΩ, 1%, 0,125 W | 0805 | 1 |
| C13 | 100 nF, X7R, 16 V | 0805 | 1 |

Quy ước U3A đệm dòng, U3B đệm BIAS. BIAS_DIV là điểm giữa cầu chia trước đệm; BIAS_1V65 là đầu ra sau đệm. Hai net này nối với nhau thông qua op-amp, không chập trực tiếp trên schematic.

## 4.2. Chân U3 và mạch BIAS

### A. U3B — đệm BIAS

| Chân | Chức năng | Net và điểm nối |
|---:|---|---|
| 5 | IN+ B | `BIAS_DIV` |
| 6 | IN− B | `BIAS_1V65`; nối `U3.7` |
| 7 | OUT B | `BIAS_1V65`; dùng chung hai AFE |

### B. U3A — đệm dòng

| Chân | Chức năng | Net và điểm nối |
|---:|---|---|
| 1 | OUT A | `CURRENT_BUF`; nối `U3.2` và `R5.1` |
| 2 | IN− A | `CURRENT_BUF`; hồi tiếp trực tiếp từ `U3.1` |
| 3 | IN+ A | `CURRENT_SENSE`; nối J3.1 và R2.1 |

### C. Nguồn U3

| Chân | Chức năng | Net và điểm nối |
|---:|---|---|
| 4 | VSS | `GND` |
| 8 | VDD | `+3V3` |


| Linh kiện | Đầu 1 | Đầu 2 |
|---|---|---|
| R3 **(10 kΩ)** | `+3V3` | `BIAS_DIV` |
| R4 **(10 kΩ)** | `BIAS_DIV` | `GND` |
| C12 **(100 nF)** | `+3V3`, tại `U3.8` | `GND` |
| R5 **(1 kΩ)** | `CURRENT_BUF` | `ADC_CURRENT` |
| C13 **(100 nF)** | `ADC_CURRENT` | `GND` |

## 4.3. Nối CT và burden quanh BIAS

| Chân / linh kiện | Nối tới net | Cùng điểm nối |
|---|---|---|
| J3.1 | `CURRENT_SENSE` | R2.1, U3.3 |
| J3.2 | `BIAS_1V65` | R2.2, U3.7 |
| R2.1 | `CURRENT_SENSE` | Đầu thứ nhất burden |
| R2.2 | `BIAS_1V65` | Đầu thứ hai burden |
| CT1 dây đỏ | J3.1 | CURRENT_SENSE → U3.3 |
| CT1 dây đen | J3.2 | BIAS_1V65 → U3.7 |

Burden mắc trực tiếp giữa hai đầu thứ cấp CT, song song với J3. Tín hiệu tại CURRENT_SENSE dao động quanh 1,65 V. Không nối J3.2 xuống GND. Màu dây theo sơ đồ mô-đun: đỏ vào điểm đo, đen về BIAS. Đổi hai dây làm đảo dấu tín hiệu dòng.

Với dòng sơ cấp thiết kế 5 A RMS và giả thiết tỷ số 1000:1: dòng thứ cấp 5 mA RMS, điện áp burden 0,75 V RMS, công suất $P=0,005^2\times150=3,75\ \mathrm{mW}$. Vì vậy chọn R2 0,125 W, 0805. Với sóng sin, đỉnh khoảng 1,061 V, điện áp lý tưởng quanh BIAS nằm trong khoảng 0,589–2,711 V. Các giá trị là mô hình tuyến tính; tỷ số và khả năng chịu tải thứ cấp 150 Ω của CT thực quyết định độ chính xác/dải đo đạt được.

# 5. Khối photodiode và AFE quang

## 5.1. Linh kiện

| Mã | Linh kiện / giá trị | Package | SL |
|---|---|---|---:|
| D1 | VBPW34S | SMD gullwing theo Vishay | 1 |
| U4 | MCP6002-I/SN | SOIC-8 | 1 |
| R6 | 10 kΩ, 1%, 0,125 W | 0805 | 1 |
| C14 | 100 nF, X7R, 16 V | 0805 | 1 |
| C15 | 100 pF, ±5%, C0G/NP0, ≥16 V | 0805 | 1 |

U4A chuyển dòng–áp; U4B đệm BIAS, đầu ra không cấp tải ngoài. D1 nối theo nhánh quang mô-đun, phân cực ngược: A xuống GND, K tại PHOTO_SUM gần BIAS 1,65 V. Khi ánh sáng tăng, dòng quang đi từ K về A; hồi tiếp tạo điện áp đầu ra tăng so với BIAS.

## 5.2. Nối từng kênh U4 và mạng hồi tiếp

### A. U4A — chuyển dòng quang thành áp

| Chân | Chức năng | Net và điểm nối |
|---:|---|---|
| 1 | OUT A | `ADC_LIGHT`; nối `U2.11`, `R6.1`, `C15.1` |
| 2 | IN− A | `PHOTO_SUM`; nối `R6.2`, `C15.2`; nối D1.K |
| 3 | IN+ A | `BIAS_1V65` |

### B. U4B — đệm BIAS, đầu ra không cấp tải ngoài

| Chân | Chức năng | Net và điểm nối |
|---:|---|---|
| 5 | IN+ B | `BIAS_1V65` |
| 6 | IN− B | `OPT_BIAS_BUF`; nối `U4.7` |
| 7 | OUT B | `OPT_BIAS_BUF`; chỉ hồi tiếp về `U4.6` |

### C. Nguồn U4

| Chân | Chức năng | Net và điểm nối |
|---:|---|---|
| 4 | VSS | `GND` |
| 8 | VDD | `+3V3` |


| Linh kiện | Đầu 1 | Đầu 2 | Ghi chú |
|---|---|---|---|
| R6 **(10 kΩ)** | `ADC_LIGHT` | `PHOTO_SUM` | Hồi tiếp 10 kΩ |
| C15 **(100 pF)** | `ADC_LIGHT` | `PHOTO_SUM` | Song song R6 |
| C14 **(100 nF)** | `+3V3`, tại `U4.8` | `GND` | Tụ nguồn |
| D1.A — anode | `GND` | — | Cực A xuống GND |
| D1.K — cathode | `PHOTO_SUM` | — | Cực K tới U4.2, R6.2, C15.2 |

**PHOTO_SUM và BIAS_1V65 là hai net riêng.** Op-amp điều khiển điện áp nút tổng dòng qua hồi tiếp; không nối tắt hai net này. OPT_BIAS_BUF cũng là net riêng, không chập hai đầu ra U3.7 và U4.7.

Thư viện D1 dùng Pin Designator A và K; footprint cũng đặt tên pad A/K, xác định vị trí vật lý theo bản vẽ VBPW34S của Vishay [5]. Cách đặt tên này ánh xạ trực tiếp cực điện mà không phụ thuộc cách đánh số 1/2 của thư viện bên ngoài.

# 6. Khối RS485

## 6.1. Linh kiện

| Mã | Linh kiện / giá trị | Package | SL | Lắp |
|---|---|---|---:|---|
| U5 | MAX3485ESA+ | SOIC-8 | 1 | Có |
| C16 | 100 nF, X7R, 16 V | 0805 | 1 | Có |
| R7 | 10 kΩ, 1%, 0,125 W | 0805 | 1 | Có |
| J4 | Phoenix Contact 1715734 — MKDS 1,5/3-5,08; terminal bắt vít 3 cực | THT, bước 5,08 mm | 1 | Có |
| R8 | 120 Ω, 1%, 0,25 W | 1206 | 1 vị trí | Theo đầu cuối đường truyền |
| R9, R10 | 330 Ω, 1%, 0,125 W | 0805 | 2 vị trí | Theo cấu hình bias |

R8, R9, R10 đánh dấu DNP khi cấu hình đường truyền không yêu cầu lắp; DNP nghĩa là có vị trí trên PCB nhưng không lắp linh kiện.

## 6.2. Chân U5

| Chân U5 | Tên chân | Net | Nối tới |
|---:|---|---|---|
| 1 | RO | `UART1_RX` | `U2.31` PA10 |
| 2 | /RE | `RS485_DIR` | `U2.18` PB0, `U5.3`, `R7.1` |
| 3 | DE | `RS485_DIR` | `U2.18` PB0, `U5.2`, `R7.1` |
| 4 | DI | `UART1_TX` | `U2.30` PA9 |
| 5 | `GND` | `GND` | Mass |
| 6 | A | `RS485_A` | `J4.1`, `R8.1`, `R9.2` |
| 7 | B | `RS485_B` | `J4.2`, `R8.2`, `R10.1` |
| 8 | VCC | `+3V3` | `C16.1` |

## 6.3. Điện trở và đầu nối

| Linh kiện | Đầu 1 | Đầu 2 | Chức năng |
|---|---|---|---|
| C16 **(100 nF)** | `+3V3`, tại `U5.8` | `GND` | Tụ nguồn |
| R7 **(10 kΩ)** | `RS485_DIR` | `GND` | Mặc định nhận |
| R8 **(120 Ω · tùy chọn)** | `RS485_A` | `RS485_B` | Điện trở kết thúc tùy chọn |
| R9 **(330 Ω · tùy chọn)** | `+3V3` | `RS485_A` | Bias kéo A lên |
| R10 **(330 Ω · tùy chọn)** | `RS485_B` | `GND` | Bias kéo B xuống |

| Chân J4 | Net | Phía ngoài |
|---:|---|---|
| 1 | `RS485_A` | Dây A tới bộ USB–RS485 |
| 2 | `RS485_B` | Dây B tới bộ USB–RS485 |
| 3 | `GND` | Tham chiếu `GND` giao tiếp |

RS485_DIR thấp: nhận; cao: phát. Chọn cấu hình lắp R8 và cặp R9/R10 theo tổng điện trở kết thúc/bias đã có trên toàn đường truyền. Ký hiệu A/B ở bộ chuyển đổi được đối chiếu với tài liệu của chính bộ đó.

## 6.4. Ánh xạ từ mô-đun sang PCB

| Tín hiệu | Mô-đun buổi 1 | PCB SMD |
|---|---|---|
| Dòng | MCP6002 U1 DIP-8 → PA0 Blue Pill | U3 SOIC-8 → R5/C13 → U2.10 |
| BIAS | Chân 7 MCP6002 U1 | U3.7, net BIAS_1V65 |
| Quang | BPW34 + MCP6002 U2 DIP-8 → PA1 | VBPW34S + U4 SOIC-8 → U2.11 |
| Phát UART | PA9 → RXD TTL485-V2.0 | U2.30 → U5.4 DI |
| Nhận UART | TXD TTL485-V2.0 → PA10 | U5.1 RO → U2.31 |
| Nguồn RS485 | 5 V, MAX13487EESA+ tự chuyển chiều | 3,3 V, MAX3485ESA+ |
| Điều khiển chiều | PB0/PB1 để trống | U2.18 PB0 → U5.2 /RE và U5.3 DE |

# 7. Quy ước dựng schematic Altium

- Đặt cùng tên net giữa các sheet; nếu dùng thiết kế phân cấp, khai báo Port/Sheet Entry tương ứng và chọn phạm vi net phù hợp dự án.
- U3 và U4 có đủ hai kênh op-amp cùng chân nguồn 4/8. Nếu symbol tách nguồn thành unit riêng, đặt đủ unit nguồn, tránh bỏ sót chân ẩn.
- Các chân đầu 1/2 của điện trở và tụ không phân cực trong bảng là quy ước nối. Tụ tantalum C1/C2 dùng cực +/−; ánh xạ số pad theo mã thư viện.
- Vị trí ký hiệu trên hình không quyết định số chân. Đối chiếu Pin Designator của symbol với Pad Designator của footprint cho đúng package IC.
- Các chân MCU để trống có thể dùng No ERC theo quy tắc dự án. Tất cả chân nguồn, CT và photodiode được nối theo các bảng tương ứng.
- Footprint linh kiện được dựng theo mã trong bảng: J1 PJ-102AH; J3/J4 MKDS bước 5,08 mm; Y1 ABM3B 5,0 × 3,2 mm; R2 0805; C2 case C 6032.

# 8. Thông số thiết kế đã chọn và điều kiện áp dụng

| Hạng mục | Lựa chọn để dựng schematic |
|---|---|
| Dòng sơ cấp | 5 A RMS theo yêu cầu; tỷ số tính toán CT 1000:1 |
| CT/burden | J3.1 = CURRENT_SENSE; J3.2 = BIAS_1V65; R2 song song thứ cấp |
| Photodiode | D1.A = GND; D1.K = PHOTO_SUM; đầu ra tăng khi dòng quang tăng |
| Tụ ra LDO | T491C226K016AT, 22 µF, 16 V, ±10%, case C 6032; ESR 1,5 Ω tại 100 kHz, 25°C |
| HSE | ABM3B-8.000MHZ-B2-T, CL 18 pF; C9/C10 27 pF với ký sinh giả thiết 4,5 pF |
| Jack nguồn | PJ-102AH, chân 1 dương, chân 2 GND, chân 3 để trống; nguồn 5 V tâm dương |
| Terminal CT | Phoenix Contact 1715721, hai cực, bước 5,08 mm |
| Terminal RS485 | Phoenix Contact 1715734, ba cực, bước 5,08 mm |
| R8–R10 | Có đầy đủ net/footprint; trạng thái lắp chọn theo đường truyền thực tế |

Các mã và bảng nối trên xác định phương án schematic. Đặc tính thực nghiệm như độ tuyến tính CT với burden 150 Ω, độ ổn định AFE, khởi động thạch anh và nhiệt/đáp ứng LDO được đánh giá trên bo thực. Thông số công bố của đúng CT đang sử dụng chưa được xác thực bằng tài liệu hãng; các phép tính 5 A dùng tỷ số giả thiết 1000:1, không gán thành dải đo được hãng bảo đảm.

# 9. Tài liệu đối chiếu số chân

1. [ST DS5319 — STM32F103x8/xB](https://www.st.com/resource/en/datasheet/stm32f103c8.pdf), Figure 8 và Table 5, cột LQFP48.
2. [ST LD1117](https://www.st.com/resource/en/datasheet/ld1117.pdf), Figure 2, SOT-223; tab nối OUT.
3. [Microchip DS20001733L — MCP6001/1R/1U/2/4](https://ww1.microchip.com/downloads/aemDocuments/documents/MSLD/ProductDocuments/DataSheets/MCP6001-1R-1U-2-4-1-MHz-Low-Power-Op-Amp-DS20001733L.pdf), Package Types và Pin Descriptions, MCP6002 SOIC-8.
4. [ADI MAX3483–MAX3491](https://www.analog.com/media/en/technical-documentation/data-sheets/MAX3483-MAX3491.pdf), Pin Configuration và Pin Description, MAX3485 DIP/SO.
5. [Vishay VBPW34S/VBPW34SR, Document 81128](https://www.vishay.com/docs/81128/vbpw34s.pdf), Package Dimensions cho đúng biến thể VBPW34S.

6. [KEMET T491C226K016AT](https://search.kemet.com/download/specsheet/T491C226K016AT), thông số điện và kích thước case C.
7. [Abracon ABM3B](https://abracon.com/Resonators/abm3b.pdf), đặt mã và pad 1/3 dao động, 2/4 GND.
8. [Same Sky PJ-102AH](https://www.sameskydevices.com/product/resource/pj-102ah.pdf), định mức và sơ đồ chân.
9. [Phoenix Contact 1715721](https://www.phoenixcontact.com/en-be/products/pcb-terminal-block-mkds-15-2-508-1715721) và [1715734](https://www.phoenixcontact.com/en-gb/products/printed-circuit-board-terminal-mkds-15-3-508-1715734), đầu nối bắt vít.
10. [Vishay CRCW](https://www.vishay.com/docs/20035/dcrcwe3.pdf), điện trở chip.
11. [KEMET C0805C270J5GACTU](https://search.kemet.com/download/specsheet/C0805C270J5GACTU), tụ tải 27 pF.

12. [PDF kết nối mô-đun](../Kế%20hoạch%20test%20module%20chốt%20PCB.pdf), mục 4.2 trang 4–6; chỉ sử dụng phần kết nối phần cứng.

Tài liệu đi kèm: [Thiết kế PCB SMD](01_Thiet_ke_phan_cung_PCB_SMD.md) · [Nối dây mô-đun buổi 1](03_Noi_day_module_Lab_buoi_1.md).
