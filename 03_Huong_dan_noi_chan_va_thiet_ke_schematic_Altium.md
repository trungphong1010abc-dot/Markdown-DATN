# Hướng dẫn nối chân và thiết kế schematic Altium

Tài liệu hướng dẫn số chân, net và kiểm tra kết nối khi dựng schematic. Bảng linh kiện, BOM, mua hàng và tính toán xem [file 02](02_Lua_chon_linh_kien_BOM_va_tinh_toan_PCB.md); nguyên mẫu module xem [file 01](01_Huong_dan_kiem_thu_phan_cung_nguyen_mau_module_cho_lab.md).

**Trạng thái:** giữ cấu hình thiết kế hiện hành, không tự đổi model/chân. Mã tụ thực, tiếp điểm jack và một số footprint còn phải xác nhận; “chốt bảng” chưa có nghĩa hoàn tất mua hàng/ERC/kiểm thử. Giữ vị trí và số chân trong symbol Altium người dùng cung cấp, không tự bố trí lại chân bên trong symbol.

**Cách đọc:** `U2.30` = IC U2, chân 30. Cùng tên **net** = nối điện. Linh kiện hai chân: đầu 1 → net thứ nhất, đầu 2 → net thứ hai.

| Tra cứu | Nội dung |
|---|---|
| Khối nguồn — U1, J1 | Mục 2 |
| Khối MCU — U2, J2 | Mục 3 |
| Khối dòng — U3, J3 | Mục 4 |
| Khối quang — U4, D1 | Mục 5 |
| Khối truyền thông — U5, J4 | Mục 6 |
| Tài liệu đối chiếu chân | Mục 8 |

---

# 1. Danh sách khối và net liên kết

| Khối | IC chính | Đầu nối | Net liên khối |
|---|---|---|---|
| Khối nguồn | U1 LD1117S33TR | J1 jack DC | `+5V`, `+3V3`, `GND` |
| Khối MCU | U2 STM32F103C8T6 | J2 SWD | `ADC_CURRENT`, `ADC_LIGHT`, `UART1_TX`, `UART1_RX`, `RS485_DIR`, `SWDIO`, `SWCLK`, `NRST` |
| Khối dòng | U3 MCP6002-I/SN | J3 CT | `BIAS_1V65`, `ADC_CURRENT` |
| Khối quang | U4 MCP6002-I/SN, D1 VBPW34S | — | `BIAS_1V65`, `ADC_LIGHT` |
| Khối truyền thông | U5 MAX3485ESA+ | J4 terminal 3 cực A/B/GND | `UART1_TX`, `UART1_RX`, `RS485_DIR`, `RS485_A`, `RS485_B` |

Adapter 5 V, ST-Link V2, CT và USB–RS485 CH340 là thiết bị ngoài PCB.

---

# 2. Khối nguồn

## 2.1. Tra linh kiện

Mã, giá trị, package, số lượng và thông tin mua xem mục 1 [file 02](02_Lua_chon_linh_kien_BOM_va_tinh_toan_PCB.md). Các bảng dưới đây chỉ hướng dẫn nối chân/net.

## 2.2. Nối nguồn

| Linh kiện / chân | Nối tới net | Cùng net với |
|---|---|---|
| J1.1 — nhãn +DC của jack thực | `+5V` | U1.3 IN, C1 cực + |
| J1.2 — nhãn −DC của jack thực | `GND` | U1.1 GND, C1 cực −, C2 cực − |
| U1.1 GND | `GND` | Mass toàn PCB |
| U1.2 OUT | `+3V3` | C2 cực +, nguồn các IC |
| U1.3 IN | `+5V` | J1 dương, C1 cực + |
| U1.4 (tab) | `+3V3` | Cùng điện với OUT |

J1.3: schematic hiện nối GND cùng J1.2. Chưa xác nhận cấu trúc tiếp điểm của jack thực; phải đo/đối chiếu trước khi chốt PCB. PJ-102AH chỉ là tham khảo, không coi là model thực. Giữ tên nguồn `+5V`, `+3V3`, `GND`, không thêm hậu tố IN.

---

# 3. Khối MCU

## 3.1. Tra linh kiện

Mã, giá trị, package, số lượng và thông tin mua xem mục 1 [file 02](02_Lua_chon_linh_kien_BOM_va_tinh_toan_PCB.md). Các bảng dưới đây chỉ hướng dẫn nối chân/net.

## 3.2. Nối chân U2 theo chức năng

### A. Nguồn và mass

| Chân U2 | Tên chân | Net | Điểm nối |
|---:|---|---|---|
| 1 | VBAT | `+3V3` | Nguồn chung |
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
| 18 | PB0 | `RS485_DIR` | U5.2, U5.3, R7 |
| 30 | PA9 / USART1_TX | `UART1_TX` | U5.4 DI |
| 31 | PA10 / USART1_RX | `UART1_RX` | U5.1 RO |

### C. Clock, reset và nạp/debug

| Chân U2 | Tên chân | Net | Điểm nối |
|---:|---|---|---|
| 5 | PD0 / OSC_IN | `HSE_IN` | Y1, C9 |
| 6 | PD1 / OSC_OUT | `HSE_OUT` | Y1, C10 |
| 7 | NRST | `NRST` | C11, J2.5, SW1.1 |
| 34 | PA13 / SWDIO | `SWDIO` | J2.3 |
| 37 | PA14 / SWCLK | `SWCLK` | J2.4 |
| 44 | BOOT0 | `BOOT0` | R1 đầu 1 |

## 3.3. Chân MCU để trống

Các chân dưới đây để trống, không nối chúng thành cùng một net NC.

| Số chân | Tên chân |
|---|---|
| 2, 3, 4 | PC13, PC14, PC15 |
| 12–17 | PA2, PA3, PA4, PA5, PA6, PA7 |
| 19–22 | PB1, PB2/BOOT1, PB10, PB11 |
| 25–29 | PB12, PB13, PB14, PB15, PA8 |
| 32, 33 | PA11, PA12 |
| 38–43 | PA15, PB3, PB4, PB5, PB6, PB7 |
| 45, 46 | PB8, PB9 |

## 3.4. Nối tụ, thạch anh, BOOT0 và reset

| Linh kiện | Đầu 1 | Đầu 2 | Ghi chú |
|---|---|---|---|
| C3 (100 nF) | `+3V3` tại U2.24 | `GND` | Tụ VDD_1 |
| C4 (100 nF) | `+3V3` tại U2.36 | `GND` | Tụ VDD_2 |
| C5 (100 nF) | `+3V3` tại U2.48 | `GND` | Tụ VDD_3 |
| C6 (10 µF) | `+3V3` | `GND` | Tụ nguồn tổng |
| C7, C8 (100 nF / 1 µF) | `+3V3` tại U2.9 | `GND` | Song song cho VDDA |
| Y1.1 | `HSE_IN` | — | Đầu dao động → U2.5 |
| Y1.3 | `HSE_OUT` | — | Đầu dao động → U2.6 |
| Y1.2, Y1.4 | `GND` | — | Pad vỏ |
| C9 (27 pF) | `HSE_IN` | `GND` | |
| C10 (27 pF) | `HSE_OUT` | `GND` | |
| R1 (10 kΩ) | `BOOT0` | `GND` | Kéo xuống |
| C11 (100 nF) | `NRST` | `GND` | Tụ reset |
| SW1 (RESET, thường hở) | `NRST` tại U2.7, J2.5, C11 | `GND` | Nhấn kéo NRST xuống thấp; nhả để MCU khởi động lại |

## 3.5. Đầu nối J2 SWD

| Chân J2 | Net | Chân MCU |
|---:|---|---|
| 1 | `+3V3` | Nguồn mạch đích |
| 2 | `GND` | GND |
| 3 | `SWDIO` | U2.34 |
| 4 | `SWCLK` | U2.37 |
| 5 | `NRST` | U2.7 |

Khi PCB đã cấp nguồn từ adapter, không nối thêm đầu ra 3,3 V của ST-Link.

---

## 3.6. Nối nút RESET SW1

1. SW1.1 → net `NRST`, cùng U2.7, J2.5 và đầu NRST của C11 100 nF.
2. SW1.2 → `GND`. Giữ C11 từ NRST xuống GND; giữ J2.5 để đầu nạp truy cập NRST.
3. Dùng nút nhấn nhả **thường hở**: bình thường hở, nhấn nối NRST với GND, nhả để MCU khởi động lại. Không nối nút RESET lên +3V3.

SW1.1/2 là quy ước cho symbol hai tiếp điểm đề xuất, chưa phải số chân hãng đã xác nhận. Nếu nút thực có bốn chân, đối chiếu datasheet để nhận diện các cặp chân nối sẵn và ánh xạ symbol–pad; không suy đoán theo vị trí chân. Giữ nguyên vị trí và số chân của symbol Altium người dùng cung cấp.

Chốt mã hãng, kích thước và footprint trước khi làm PCB. Cơ sở mạch reset: ST AN2586 và DS5319 (liên kết ở mục 8). Không thêm nút BOOT hoặc R11; BOOT0/R1 và PB2/BOOT1 giữ nguyên cấu hình hiện hành.

---

# 4. Khối dòng

## 4.1. Tra linh kiện

Mã, giá trị, package, số lượng và thông tin mua xem mục 1 [file 02](02_Lua_chon_linh_kien_BOM_va_tinh_toan_PCB.md). Các bảng dưới đây chỉ hướng dẫn nối chân/net.

## 4.2. Chân U3 và mạch BIAS

### A. U3B — đệm BIAS

| Chân | Chức năng | Net và điểm nối |
|---:|---|---|
| 5 | IN+ B | `BIAS_DIV` |
| 6 | IN− B | `BIAS_1V65`; nối U3.7 |
| 7 | OUT B | `BIAS_1V65`; dùng chung hai AFE |

### B. U3A — đệm dòng

| Chân | Chức năng | Net và điểm nối |
|---:|---|---|
| 1 | OUT A | `CURRENT_BUF`; nối U3.2 và R5.1 |
| 2 | IN− A | `CURRENT_BUF`; hồi tiếp từ U3.1 |
| 3 | IN+ A | `CURRENT_SENSE`; nối J3.1 và R2.1 |

### C. Nguồn U3

| Chân | Chức năng | Net |
|---:|---|---|
| 4 | VSS | `GND` |
| 8 | VDD | `+3V3` |

| Linh kiện | Đầu 1 | Đầu 2 |
|---|---|---|
| R3 (10 kΩ) | `+3V3` | `BIAS_DIV` |
| R4 (10 kΩ) | `BIAS_DIV` | `GND` |
| C12 (100 nF) | `+3V3` tại U3.8 | `GND` |
| R5 (1 kΩ) | `CURRENT_BUF` | `ADC_CURRENT` |
| C13 (100 nF) | `ADC_CURRENT` | `GND` |

## 4.3. Nối CT và burden

| Chân / linh kiện | Nối tới net | Cùng điểm nối |
|---|---|---|
| J3.1 | `CURRENT_SENSE` | R2.1, U3.3 |
| J3.2 | `BIAS_1V65` | R2.2, U3.7 |
| R2.1 | `CURRENT_SENSE` | Đầu thứ nhất burden |
| R2.2 | `BIAS_1V65` | Đầu thứ hai burden |
| CT1 dây đỏ | J3.1 | CURRENT_SENSE → U3.3 |
| CT1 dây đen | J3.2 | BIAS_1V65 → U3.7 |

Burden song song thứ cấp CT. Không nối J3.2 xuống GND.

---

# 5. Khối quang

## 5.1. Tra linh kiện

Mã, giá trị, package, số lượng và thông tin mua xem mục 1 [file 02](02_Lua_chon_linh_kien_BOM_va_tinh_toan_PCB.md). Các bảng dưới đây chỉ hướng dẫn nối chân/net.

## 5.2. Chân U4 và mạng hồi tiếp

### A. U4A — chuyển dòng quang → áp

| Chân | Chức năng | Net và điểm nối |
|---:|---|---|
| 1 | OUT A | `ADC_LIGHT`; nối U2.11, R6.1, C15.1 |
| 2 | IN− A | `PHOTO_SUM`; nối R6.2, C15.2, D1.K |
| 3 | IN+ A | `BIAS_1V65` |

### B. U4B — đệm BIAS

| Chân | Chức năng | Net và điểm nối |
|---:|---|---|
| 5 | IN+ B | `BIAS_1V65` |
| 6 | IN− B | `OPT_BIAS_BUF`; nối U4.7 |
| 7 | OUT B | `OPT_BIAS_BUF`; chỉ hồi tiếp về U4.6 |

### C. Nguồn U4

| Chân | Chức năng | Net |
|---:|---|---|
| 4 | VSS | `GND` |
| 8 | VDD | `+3V3` |

| Linh kiện | Đầu 1 | Đầu 2 | Ghi chú |
|---|---|---|---|
| R6 (10 kΩ) | `ADC_LIGHT` | `PHOTO_SUM` | Hồi tiếp |
| C15 (100 pF) | `ADC_LIGHT` | `PHOTO_SUM` | Song song R6 |
| C14 (100 nF) | `+3V3` tại U4.8 | `GND` | Tụ nguồn |
| D1.A (anode) | `GND` | — | |
| D1.K (cathode) | `PHOTO_SUM` | — | |

**PHOTO_SUM ≠ BIAS_1V65.** Không nối tắt. OPT_BIAS_BUF cũng riêng, không chập U4.7 với U3.7.

---

# 6. Khối truyền thông

## 6.1. Tra linh kiện

Mã, giá trị, package, số lượng và thông tin mua xem mục 1 [file 02](02_Lua_chon_linh_kien_BOM_va_tinh_toan_PCB.md). Các bảng dưới đây chỉ hướng dẫn nối chân/net.

## 6.2. Chân U5

| Chân U5 | Tên chân | Net | Nối tới |
|---:|---|---|---|
| 1 | RO | `UART1_RX` | U2.31 PA10 |
| 2 | /RE | `RS485_DIR` | U2.18 PB0, U5.3, R7.1 |
| 3 | DE | `RS485_DIR` | U2.18 PB0, U5.2, R7.1 |
| 4 | DI | `UART1_TX` | U2.30 PA9 |
| 5 | GND | `GND` | Mass |
| 6 | A | `RS485_A` | J4.1, R8.1, R9.2 |
| 7 | B | `RS485_B` | J4.2, R8.2, R10.1 |
| 8 | VCC | `+3V3` | C16.1 |

## 6.3. Điện trở và đầu nối

| Linh kiện | Đầu 1 | Đầu 2 | Chức năng |
|---|---|---|---|
| C16 (100 nF) | `+3V3` tại U5.8 | `GND` | Tụ nguồn |
| R7 (10 kΩ) | `RS485_DIR` | `GND` | Mặc định nhận |
| R8 (120 Ω, tùy chọn) | `RS485_A` | `RS485_B` | Kết thúc đường truyền |
| R9 (330 Ω, tùy chọn) | `+3V3` | `RS485_A` | Bias kéo A lên |
| R10 (330 Ω, tùy chọn) | `RS485_B` | `GND` | Bias kéo B xuống |

| Chân J4 — terminal 3 cực | Net | Phía ngoài |
|---:|---|---|
| 1 | `RS485_A` | Dây A tới USB–RS485 |
| 2 | `RS485_B` | Dây B tới USB–RS485 |
| 3 | `GND` | GND giao tiếp |

---

# 7. Quy ước dựng schematic Altium

- Đặt cùng tên net giữa các sheet; khai báo Port/Sheet Entry nếu dùng thiết kế phân cấp.
- U3, U4 có đủ hai kênh + chân nguồn 4/8. Nếu symbol tách nguồn thành unit riêng, đặt đủ unit.
- Tụ tantalum C1/C2 có phân cực; ánh xạ số pad theo thư viện.
- Đối chiếu Pin Designator của symbol với Pad Designator của footprint.
- Chân MCU để trống: dùng No ERC theo quy tắc dự án.
- Footprint: J1 theo jack thực; J3/J4 terminal bước 5,08 mm, đối chiếu footprint theo linh kiện thực; Y1 ABM3B 5,0×3,2 mm. J4 giữ 1 = A, 2 = B, 3 = GND; không tự đổi số/vị trí chân symbol.

---

## 7.1. Trạng thái triển khai schematic

- Khối nguồn: đã kiểm tra trực quan kết nối, chưa đồng nghĩa thử mạch thực hoặc hoàn tất ERC/footprint.
- Đang dựng MCU và nạp/debug theo mục 3; PA9 là TX, PA10 là RX; PB0 chung DE và /RE của MAX3485.
- Kiểm Pin Designator ↔ Pad Designator theo đúng symbol/footprint. Không tự di chuyển chân bên trong symbol; có thể bố trí lại cả linh kiện.
- Không tự thêm/bớt linh kiện; khi phát hiện vấn đề kỹ thuật, giải thích trước khi thay đổi cấu hình.

---

# 8. Tài liệu đối chiếu chân và schematic

Hướng dẫn mạch reset: [ST AN2586 — STM32 hardware design guidelines](https://www.st.com/resource/en/application_note/an2586-stm32-hardware-design-guidelines-stmicroelectronics.pdf).

1. [ST DS5319 — STM32F103x8/xB](https://www.st.com/resource/en/datasheet/stm32f103c8.pdf)
2. [ST LD1117](https://www.st.com/resource/en/datasheet/ld1117.pdf) — SOT-223, tab nối OUT
3. [Microchip DS20001733L — MCP6002](https://ww1.microchip.com/downloads/aemDocuments/documents/MSLD/ProductDocuments/DataSheets/MCP6001-1R-1U-2-4-1-MHz-Low-Power-Op-Amp-DS20001733L.pdf)
4. [ADI MAX3483–MAX3491](https://www.analog.com/media/en/technical-documentation/data-sheets/MAX3483-MAX3491.pdf)
5. [Vishay VBPW34S, Doc 81128](https://www.vishay.com/docs/81128/vbpw34s.pdf)
6. [Abracon ABM3B](https://abracon.com/Resonators/abm3b.pdf)
7. [Phoenix Contact 1715721](https://www.phoenixcontact.com/en-be/products/pcb-terminal-block-mkds-15-2-508-1715721)
