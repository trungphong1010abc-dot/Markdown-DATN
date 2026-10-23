# Giai đoạn 3 — Hướng dẫn nối dây schematic Altium

**Phương pháp tra cứu và kết nối:** xác định khối chức năng trong bảng dưới đây, sau đó kết nối theo số chân và tên net/điểm nối tương ứng. Net Label chỉ được sử dụng cho các tín hiệu liên khối đã liệt kê; các kết nối nội bộ được thể hiện bằng dây. Ký hiệu `U2.30` chỉ chân 30 của IC U2. Giá trị linh kiện được quy định tại [file 2](02_Thiet_ke_phan_cung_PCB_SMD.md); cấu hình nguyên mẫu và kết quả thử nghiệm được trình bày tại [file 1](01_Chon_linh_kien_module_va_noi_day.md).

### Vị trí của file này trong pipeline

Đây là bước 3, được triển khai sau khi cấu hình PCB tại file 2 đã được xác định. Trình tự sử dụng tài liệu gồm: **(1)** kiểm tra bảng linh kiện và net tổng quan; **(2)** kết nối nguồn và mass; **(3)** kết nối MCU, clock, reset và SWD; **(4)** kết nối nhánh dòng và BIAS; **(5)** kết nối nhánh quang; **(6)** kết nối RS485 và đầu nối; **(7)** rà soát net, ánh xạ chân symbol/footprint và ERC. Trình tự này đi từ khối nguồn tới MCU, các kênh đo và cuối cùng là truyền thông.

Trước khi lập schematic, đối chiếu mã, vị trí và giá trị linh kiện với BOM tại file 2. Kết quả thử nghiệm module tại file 1 giải thích mục đích của các điểm đo; sơ đồ module không thay thế cấu hình net PCB. Mọi khác biệt giữa giá trị hoặc net trong tài liệu này với BOM hoặc phần tính toán tại file 2 phải được giải quyết trước khi hoàn tất schematic. Sau khi hoàn tất kết nối, kiểm tra ERC, ánh xạ pin-to-pad và footprint theo linh kiện thực trước khi triển khai layout PCB.

**Trạng thái cấu hình:** tài liệu mô tả cấu hình thiết kế hiện hành. Model linh kiện, số chân hoặc kết nối chỉ được thay đổi khi có căn cứ kỹ thuật và được cập nhật đồng bộ. Mã tụ thực tế, cấu trúc tiếp điểm jack và một số footprint còn cần xác nhận; BOM hiện tại chưa xác nhận việc hoàn tất mua hàng, ERC hoặc kiểm thử. Vị trí và số chân trong symbol Altium tuân theo thư viện dự án; không thay đổi cách bố trí chân bên trong symbol.

Linh kiện hai chân: đầu 1 → net thứ nhất, đầu 2 → net thứ hai.

| Tra cứu | Nội dung |
|---|---|
| Khối nguồn — U1, J1 | Mục 2 |
| Khối MCU — U2, H1 | Mục 3 |
| Khối dòng — U3, P1 | Mục 4 |
| Khối quang — U4, D1 | Mục 5 |
| Khối truyền thông — U5, J2 | Mục 6 |
| Tài liệu đối chiếu chân | Mục 8 |

---

## 1. Danh sách khối và net liên kết

| Khối | IC chính | Đầu nối | Net liên khối |
|---|---|---|---|
| Khối nguồn | U1 LD1117S33TR | J1 jack DC | `+3V3`, `GND` (nguồn chung); `+5V` ở đầu vào nguồn |
| Khối MCU | U2 STM32F103C8T6 | H1 SWD | `ADC_CURRENT`, `ADC_LIGHT`, `UART_TX`, `UART_RX`, `RS485_DIR` |
| Khối dòng | U3 MCP6002-I/SN | P1 CT | `BIAS_1V65`, `ADC_CURRENT` |
| Khối quang | U4 MCP6002-I/SN, D1 VBPW34S | — | `BIAS_1V65`, `ADC_LIGHT` |
| Khối truyền thông | U5 MAX3485ESA+ | J2 terminal 3 cực A/B/GND | `UART_TX`, `UART_RX`, `RS485_DIR` |

Adapter 5 V, ST-Link V2, CT và USB–RS485 CH340 là thiết bị ngoài PCB.

**Quy tắc đặt nhãn net:** sử dụng sáu Net Label liên kết giữa các khối: `ADC_CURRENT`, `ADC_LIGHT`, `BIAS_1V65`, `UART_TX`, `UART_RX` và `RS485_DIR`. Các đầu nối cùng một tín hiệu phải sử dụng nhãn trùng tên; nhãn được gắn trực tiếp vào dây nối tới chân linh kiện. Nguồn sử dụng Power Port `+3V3` và `GND`; ký hiệu `+5V` được sử dụng tại đầu vào theo sơ đồ nguồn. Các kết nối nội bộ được thể hiện bằng dây, không sử dụng nhãn net riêng.

H1 và mạch reset thuộc cụm MCU; P1 thuộc khối dòng; J2 thuộc khối truyền thông. Thạch anh, BOOT0, reset/SWD tới H1, cầu chia BIAS, burden/đệm dòng, hồi tiếp quang và A/B tới J2 đều nối dây trực tiếp trong khối. Tên chân vẫn dùng để tra cứu, không phải yêu cầu đặt label.

**Phân biệt nhánh quang module và PCB:** TIA (Transimpedance Amplifier, bộ khuếch đại chuyển dòng thành điện áp) nằm trong U4A. Trên PCB, đầu ra TIA `TIA_LIGHT` phải đi qua R11/C17 rồi R12/C18 trước khi tới `ADC_LIGHT`; không nối tắt hai điểm này. Cấu hình module nối TIA thẳng hoặc lắp tạm hai tầng RC chỉ dùng để so sánh trong phép thử file 1, không thay đổi đường nối mặc định của PCB.

---

## 2. Khối nguồn

## 2.1. Tra linh kiện

| Mã | Tên linh kiện / thông số cụ thể | Package | SL |
|---|---|---|---:|
| J1 | Jack DC cái: 5,5 mm (tham khảo PJ-102AH) | THT | 1 |
| U1 | LDO: LD1117S33TR, 3,3 V; tới 800 mA, còn phụ thuộc nhiệt | SOT-223 | 1 |
| C1 | Tụ tantalum: 10 µF (106), 16 V | 3528 (B case), cần xác nhận mã thực | 1 |
| C2 | Tụ tantalum: 22 µF (226), 16 V | 6032 (C case) | 1 |

Thông số được quy định tại file 2. Mã nhà sản xuất và footprint cần được xác minh theo linh kiện thực tế.

## 2.2. Nối nguồn

| Linh kiện / chân | Nối tới net | Cùng net với |
| --- | --- | --- |
| J1.1 — nhãn +DC của jack thực | `+5V` | U1.3 IN, C1 cực + |
| J1.2 — nhãn −DC của jack thực | `GND` | U1.1 GND, C1 cực −, C2 cực − |
| U1.1 GND | `GND` | Mass toàn PCB |
| U1.2 OUT | `+3V3` | C2 cực +, nguồn các IC |
| U1.3 IN | `+5V` | J1 dương, C1 cực + |
| U1.4 (tab) | `+3V3` | Cùng điện với OUT |

J1.3: schematic hiện nối GND cùng J1.2. Cấu trúc tiếp điểm của jack thực tế chưa được xác nhận; cần đo hoặc đối chiếu trước khi hoàn tất PCB. PJ-102AH chỉ là mã tham khảo, không phải model đã xác nhận. Tên nguồn được quy định là `+5V`, `+3V3` và `GND`; không bổ sung hậu tố IN.

---

## 3. Khối MCU

## 3.1. Tra linh kiện

| Mã | Tên linh kiện / thông số cụ thể | Package | SL |
|---|---|---|---:|
| U2 | MCU: STM32F103C8T6; 72 MHz; Flash 64 KB; SRAM 20 KB; 2,0–3,6 V | LQFP-48 | 1 |
| C3–C5 | Tụ gốm: 100 nF (104), X7R, 50 V | 0805 | 3 |
| C9 | Tụ gốm: 10 µF (106), X7R, 50 V | 0805 | 1 |
| C6 | Tụ gốm: 100 nF (104), X7R, 50 V | 0805 | 1 |
| C10 | Tụ gốm: 1 µF (105), X7R, 50 V | 0805 | 1 |
| Y1 | Thạch anh: ABM3B-8.000MHZ-B2-T, 8 MHz; CL = 18 pF | 5,0 × 3,2 mm | 1 |
| C8, C11 | Tụ gốm: 27 pF (270), ±5 %, C0G, 50 V (C0805C270J5GACTU) | 0805 | 2 |
| R1 | Điện trở: 10 kΩ, 1 %, 0,125 W | 0805 | 1 |
| C7 | Tụ gốm: 100 nF (104), X7R, 50 V | 0805 | 1 |
| BT1 | Nút nhấn RESET: 2 chân SMD 3 × 6 × 2,5 mm, thường hở, nhấn nhả; mã hãng chưa xác nhận | SMD 3 × 6 × 2,5 mm; pad cần đối chiếu nút thực | 1 |
| H1 | Header SWD: 1×5, bước 2,54 mm | Header | 1 |

Thông số được quy định tại file 2. Mã nhà sản xuất và footprint cần được xác minh theo linh kiện thực tế.

## 3.2. Nối chân U2 theo chức năng

### A. Nguồn và mass

| Chân U2 | Tên chân | Nguồn / label liên khối / dây trực tiếp | Điểm nối |
| ---: | --- | --- | --- |
| 1 | VBAT | `+3V3` | Nguồn chung |
| 8 | VSSA | `GND` | Mass phần tương tự |
| 9 | VDDA | `+3V3` | C6, C10 |
| 23 | VSS_1 | `GND` | Mass |
| 24 | VDD_1 | `+3V3` | C3 |
| 35 | VSS_2 | `GND` | Mass |
| 36 | VDD_2 | `+3V3` | C4 |
| 47 | VSS_3 | `GND` | Mass |
| 48 | VDD_3 | `+3V3` | C5 |

### B. ADC và RS485

| Chân U2 | Tên chân | Nguồn / label liên khối / dây trực tiếp | Điểm nối |
| ---: | --- | --- | --- |
| 10 | PA0 / ADC_IN0 | `ADC_CURRENT` | Đầu ra bộ lọc dòng |
| 11 | PA1 / ADC_IN1 | `ADC_LIGHT` | Nút sau R12/C18, đầu ra lọc thông thấp quang |
| 18 | PB0 | `RS485_DIR` | U5.2, U5.3, R7 |
| 30 | PA9 / USART1_TX | `UART_TX` | U5.4 DI |
| 31 | PA10 / USART1_RX | `UART_RX` | U5.1 RO |

### C. Clock, reset và nạp/debug

| Chân U2 | Tên chân | Nguồn / label liên khối / dây trực tiếp | Điểm nối |
| ---: | --- | --- | --- |
| 5 | PD0 / OSC_IN | nối trực tiếp U2.5–Y1.1–C8.1 | Y1, C8 |
| 6 | PD1 / OSC_OUT | nối trực tiếp U2.6–Y1.3–C11.1 | Y1, C11 |
| 7 | NRST | nối trực tiếp U2.7–C7.1–BT1.1–H1.5 | C7, H1.5, BT1.1 |
| 34 | PA13 / SWDIO | nối trực tiếp U2.34–H1.3 | H1.3 |
| 37 | PA14 / SWCLK | nối trực tiếp U2.37–H1.4 | H1.4 |
| 44 | BOOT0 | nối trực tiếp U2.44–R1.1 | R1 đầu 1 |

## 3.3. Các chân MCU không sử dụng

Các chân liệt kê dưới đây không được sử dụng trong cấu hình hiện tại. Không nối các chân này thành một net NC chung.

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
| --- | --- | --- | --- |
| C3 (100 nF (104)) | `+3V3` tại U2.24 | `GND` | Tụ VDD_1 |
| C4 (100 nF (104)) | `+3V3` tại U2.36 | `GND` | Tụ VDD_2 |
| C5 (100 nF (104)) | `+3V3` tại U2.48 | `GND` | Tụ VDD_3 |
| C9 (10 µF (106)) | `+3V3` | `GND` | Tụ nguồn tổng |
| C6, C10 (100 nF (104) / 1 µF (105)) | `+3V3` tại U2.9 | `GND` | Song song cho VDDA |
| Y1.1 | nối trực tiếp U2.5–Y1.1–C8.1 | — | Đầu dao động → U2.5 |
| Y1.3 | nối trực tiếp U2.6–Y1.3–C11.1 | — | Đầu dao động → U2.6 |
| Y1.2, Y1.4 | `GND` | — | Pad vỏ |
| C8 (27 pF (270)) | nối trực tiếp U2.5–Y1.1–C8.1 | `GND` |  |
| C11 (27 pF (270)) | nối trực tiếp U2.6–Y1.3–C11.1 | `GND` |  |
| R1 (10 kΩ) | nối trực tiếp U2.44–R1.1 | `GND` | Kéo xuống |
| C7 (100 nF (104)) | nối trực tiếp U2.7–C7.1–BT1.1–H1.5 | `GND` | Tụ reset |
| BT1 (RESET, 2 chân SMD 3 × 6 × 2,5 mm, thường hở) | nối trực tiếp U2.7–C7.1–BT1.1–H1.5 tại U2.7, H1.5, C7 | `GND` | Nhấn kéo NRST xuống thấp; nhả để MCU khởi động lại |

## 3.5. Đầu nối H1 SWD

| Chân H1 | Nguồn / dây trực tiếp | Chân MCU |
| ---: | --- | --- |
| 1 | `+3V3` | Nguồn mạch đích |
| 2 | `GND` | GND |
| 3 | nối trực tiếp U2.34–H1.3 | U2.34 |
| 4 | nối trực tiếp U2.37–H1.4 | U2.37 |
| 5 | nối trực tiếp U2.7–C7.1–BT1.1–H1.5 | U2.7 |

Khi PCB đã cấp nguồn từ adapter, không nối thêm đầu ra 3,3 V của ST-Link.

---

## 3.6. Nối nút RESET BT1

1. BT1.1 nối dây trực tiếp tới U2.7, H1.5 và C7.1 (100 nF (104)); không đặt Net Label reset.
2. BT1.2 → `GND`. Giữ C7 từ NRST xuống GND; giữ H1.5 để đầu nạp truy cập NRST.
3. Dùng nút **2 chân SMD 3 × 6 × 2,5 mm, thường hở, nhấn nhả**: bình thường hở, nhấn nối NRST với GND, nhả để MCU khởi động lại. Không nối nút RESET lên +3V3.

BT1 chọn loại “Nut Nhan 2 Chan SMD 3x6x2.5” theo thư viện người dùng cung cấp. BT1.1/2 là quy ước symbol hai chân; đối chiếu ánh xạ symbol–pad với nút thực. Kiểm tra kích thước và khoảng cách hai pad theo datasheet hoặc đo nút thực; tên kích thước và hình 3D chưa đủ xác nhận footprint. Đo thông mạch: thả nút hở, nhấn nút thông. Giữ nguyên vị trí và số chân của symbol Altium người dùng cung cấp.

Xác định mã nhà sản xuất, kích thước và footprint trước khi triển khai PCB. Cơ sở thiết kế mạch reset: ST AN2586 và DS5319 (liên kết tại mục 8). Không bổ sung nút BOOT; BOOT0/R1 và PB2/BOOT1 giữ nguyên cấu hình hiện hành. R11 ở mục 5 thuộc lọc quang, không thuộc mạch reset.

---

## 4. Khối dòng

## 4.1. Tra linh kiện

| Mã | Tên linh kiện / thông số cụ thể | Package | SL |
|---|---|---|---:|
| P1 | Terminal 2 cực: Bước 5,08 mm (Phoenix 1715721) | THT | 1 |
| U3 | Op-amp: MCP6002-I/SN; nguồn hãng 1,8–6,0 V; GBW điển hình 1 MHz | SOIC-8 | 1 |
| R2 | Điện trở: 150 Ω, 1 %, 0,125 W (CRCW0805150RFKEA) | 0805 | 1 |
| R5, R4 | Điện trở: 10 kΩ, 1 %, 0,125 W | 0805 | 2 |
| C13 | Tụ gốm: 100 nF (104), X7R, 50 V | 0805 | 1 |
| R3 | Điện trở: 1 kΩ, 1 %, 0,125 W | 0805 | 1 |
| C12 | Tụ gốm: 100 nF (104), X7R, 50 V | 0805 | 1 |
| CT1 | CT: DL-CT08CL6-1000/1; tỷ số 1000:1 còn là giả thiết | Ngoài PCB | 1 |

Thông số được quy định tại file 2. Mã nhà sản xuất và footprint cần được xác minh theo linh kiện thực tế.

## 4.2. Chân U3 và mạch BIAS

### A. U3B — đệm BIAS

| Chân | Chức năng | Label liên khối / dây trực tiếp |
| ---: | --- | --- |
| 5 | IN+ B | nối trực tiếp R5.2–R4.1–U3.5 |
| 6 | IN− B | `BIAS_1V65`; nối U3.7 |
| 7 | OUT B | `BIAS_1V65`; dùng chung hai AFE |

### B. U3A — đệm dòng

| Chân | Chức năng | Label liên khối / dây trực tiếp |
| ---: | --- | --- |
| 1 | OUT A | nối trực tiếp U3.1–U3.2–R3.1; nối U3.2 và R3.1 |
| 2 | IN− A | nối trực tiếp U3.1–U3.2–R3.1; hồi tiếp từ U3.1 |
| 3 | IN+ A | nối trực tiếp P1.1–R2.1–U3.3; nối P1.1 và R2.1 |

### C. Nguồn U3

| Chân | Chức năng | Net |
| ---: | --- | --- |
| 4 | VSS | `GND` |
| 8 | VDD | `+3V3` |

| Linh kiện | Đầu 1 | Đầu 2 |
| --- | --- | --- |
| R5 (10 kΩ) | `+3V3` | nối trực tiếp R5.2–R4.1–U3.5 |
| R4 (10 kΩ) | nối trực tiếp R5.2–R4.1–U3.5 | `GND` |
| C13 (100 nF (104)) | `+3V3` tại U3.8 | `GND` |
| R3 (1 kΩ) | nối trực tiếp U3.1–U3.2–R3.1 | `ADC_CURRENT` |
| C12 (100 nF (104)) | `ADC_CURRENT` | `GND` |

## 4.3. Nối CT và burden

| Chân / linh kiện | Nối tới net | Cùng điểm nối |
| --- | --- | --- |
| P1.1 | nối trực tiếp P1.1–R2.1–U3.3 | R2.1, U3.3 |
| P1.2 | `BIAS_1V65` | R2.2, U3.7 |
| R2.1 | nối trực tiếp P1.1–R2.1–U3.3 | Đầu thứ nhất burden |
| R2.2 | `BIAS_1V65` | Đầu thứ hai burden |
| CT1 dây đỏ | P1.1 | nối trực tiếp R2.1 và U3.3 |
| CT1 dây đen | P1.2 | BIAS_1V65 → U3.7 |

Burden song song thứ cấp CT. Không nối P1.2 xuống GND.

**Giá trị trên PCB:** R2 là burden 150 Ω, 1%, 0,125 W theo thiết kế hiện tại. Điện trở 47 Ω, 5%/0,25 W chỉ dùng thử trên module để so với 150 Ω; không lắp song song với R2 và không thay đổi schematic PCB nếu chưa có quyết định thiết kế sau lab.

---

## 5. Khối quang

## 5.1. Tra linh kiện

| Mã | Tên linh kiện / thông số cụ thể | Package | SL |
|---|---|---|---:|
| D1 | Photodiode: VBPW34S | SMD gullwing | 1 |
| U4 | Op-amp: MCP6002-I/SN; nguồn hãng 1,8–6,0 V; GBW điển hình 1 MHz | SOIC-8 | 1 |
| R6 | Điện trở: 10 kΩ, 1 %, 0,125 W | 0805 | 1 |
| C15 | Tụ gốm: 100 pF (101), ±5 %, C0G/NP0, 50 V | 0805 | 1 |
| C14 | Tụ gốm: 100 nF (104), X7R, 50 V | 0805 | 1 |

Thông số được quy định tại file 2. Mã nhà sản xuất và footprint cần được xác minh theo linh kiện thực tế.

## 5.2. Chân U4 và mạng hồi tiếp

### A. U4A — TIA, chuyển dòng quang → áp

| Chân | Chức năng | Label liên khối / dây trực tiếp |
| ---: | --- | --- |
| 1 | OUT A | Nút `TIA_LIGHT`; nối R6.1, C15.1 và đầu vào mạng lọc quang R11/C17/R12/C18. Không nối trực tiếp chân này tới `ADC_LIGHT`. |
| 2 | IN− A | nối trực tiếp U4.2–R6.2–C15.2–D1.K; nối R6.2, C15.2, D1.K |
| 3 | IN+ A | `BIAS_1V65` |

### B. U4B — đệm BIAS

| Chân | Chức năng | Label liên khối / dây trực tiếp |
| ---: | --- | --- |
| 5 | IN+ B | `BIAS_1V65` |
| 6 | IN− B | nối trực tiếp U4.6–U4.7; nối U4.7 |
| 7 | OUT B | nối trực tiếp U4.6–U4.7; chỉ hồi tiếp về U4.6 |

### C. Nguồn U4

| Chân | Chức năng | Net |
| ---: | --- | --- |
| 4 | VSS | `GND` |
| 8 | VDD | `+3V3` |

| Linh kiện | Đầu 1 | Đầu 2 | Ghi chú |
| --- | --- | --- | --- |
| R6 (10 kΩ) | `TIA_LIGHT` / U4.1 | nối trực tiếp U4.2–R6.2–C15.2–D1.K | Hồi tiếp TIA |
| C15 (100 pF (101)) | `TIA_LIGHT` / U4.1 | nối trực tiếp U4.2–R6.2–C15.2–D1.K | Mắc song song R6 |
| R11 (1 kΩ) | `TIA_LIGHT` / U4.1 | Nút X | Điện trở nối tiếp tầng lọc thứ nhất |
| C17 (10 nF (103)) | Nút X | `GND` | Tụ shunt tầng lọc thứ nhất |
| R12 (1 kΩ) | Nút X | `ADC_LIGHT` / U2.11 | Điện trở nối tiếp tầng lọc thứ hai |
| C18 (10 nF (103)) | `ADC_LIGHT` / U2.11 | `GND` | Tụ shunt tầng lọc thứ hai |
| C14 (100 nF (104)) | `+3V3` tại U4.8 | `GND` | Tụ nguồn |
| D1.A (anode) | `GND` | — |  |
| D1.K (cathode) | nối trực tiếp U4.2–R6.2–C15.2–D1.K | — |  |

Không nối điểm U4.2–R6.2–C15.2–D1.K với `BIAS_1V65`. U4.7 chỉ hồi tiếp trực tiếp về U4.6; không chập U4.7 với U3.7.

**Kết nối mặc định trên PCB:** nối `TIA_LIGHT` → R11 → nút X → R12 → `ADC_LIGHT`/U2.11. Mắc C17 từ nút X xuống GND và C18 từ `ADC_LIGHT` xuống GND. Không nối tắt `TIA_LIGHT` tới `ADC_LIGHT`, vì đường tắt sẽ bỏ qua cả hai tầng lọc.

Khi thử trên module, có thể so sánh TIA nối thẳng với TIA qua hai tầng RC để định lượng ảnh hưởng của lọc lên xung. Phép so sánh này dùng để đánh giá đáp ứng; không thay đổi cấu hình mặc định của PCB đã chọn ở trên. Sau khi lắp PCB, đo lại đáp ứng thực và xác nhận xung ngắn nhất cần phát hiện.

---

## 6. Khối truyền thông

## 6.1. Tra linh kiện

| Mã | Tên linh kiện / thông số cụ thể | Package | SL |
|---|---|---|---:|
| U5 | RS485: MAX3485ESA+; 3,0–3,6 V; tới 10 Mbps | SOIC-8 | 1 |
| C16 | Tụ gốm: 100 nF (104), X7R, 50 V | 0805 | 1 |
| R7 | Điện trở: 10 kΩ, 1 %, 0,125 W | 0805 | 1 |
| J2 | Terminal 3 cực A/B/GND, bước 5,08 mm; tham khảo Phoenix 1715734 | THT | 1 |
| R9 | Điện trở: 120 Ω, 1 %, 0,25 W | 1206 | 1 |
| R8, R10 | Điện trở: 330 Ω, 1 %, 0,125 W | 0805 | 2 |

Thông số được quy định tại file 2. Mã nhà sản xuất và footprint cần được xác minh theo linh kiện thực tế. R8–R10 là các vị trí tùy chọn; việc lắp đặt phụ thuộc topology bus.

## 6.2. Chân U5

| Chân U5 | Tên chân | Nguồn / label liên khối / dây trực tiếp | Nối tới |
| ---: | --- | --- | --- |
| 1 | RO | `UART_RX` | U2.31 PA10 |
| 2 | /RE | `RS485_DIR` | U2.18 PB0, U5.3, R7.1 |
| 3 | DE | `RS485_DIR` | U2.18 PB0, U5.2, R7.1 |
| 4 | DI | `UART_TX` | U2.30 PA9 |
| 5 | GND | `GND` | Mass |
| 6 | A | nối trực tiếp U5.6–J2.1–R9.1–R8.2 | J2.1, R9.1, R8.2 |
| 7 | B | nối trực tiếp U5.7–J2.2–R9.2–R10.1 | J2.2, R9.2, R10.1 |
| 8 | VCC | `+3V3` | C16.1 |

## 6.3. Điện trở và đầu nối

| Linh kiện | Đầu 1 | Đầu 2 | Chức năng |
| --- | --- | --- | --- |
| C16 (100 nF (104)) | `+3V3` tại U5.8 | `GND` | Tụ nguồn |
| R7 (10 kΩ) | `RS485_DIR` | `GND` | Mặc định nhận |
| R9 (120 Ω, tùy chọn) | nối trực tiếp U5.6–J2.1–R9.1–R8.2 | nối trực tiếp U5.7–J2.2–R9.2–R10.1 | Kết thúc đường truyền |
| R8 (330 Ω, tùy chọn) | `+3V3` | nối trực tiếp U5.6–J2.1–R9.1–R8.2 | Bias kéo A lên |
| R10 (330 Ω, tùy chọn) | nối trực tiếp U5.7–J2.2–R9.2–R10.1 | `GND` | Bias kéo B xuống |

| Chân J2 — terminal 3 cực | Nguồn / dây trực tiếp | Phía ngoài |
| ---: | --- | --- |
| 1 | nối trực tiếp U5.6–J2.1–R9.1–R8.2 | Dây A tới USB–RS485 |
| 2 | nối trực tiếp U5.7–J2.2–R9.2–R10.1 | Dây B tới USB–RS485 |
| 3 | `GND` | GND giao tiếp |

---

## 7. Quy ước dựng schematic Altium

**Lựa chọn giữa Net Label và chú thích:** số lượng chân trên một net không phải căn cứ duy nhất để lựa chọn cách thể hiện kết nối. Các chân trong cùng khối được nối trực tiếp bằng dây; tín hiệu liên khối sử dụng Net Label cùng tên tại các đầu kết nối. Một nhãn có thể liên kết nhiều điểm cùng điện thế, chẳng hạn BIAS cấp cho hai AFE. Text String mô tả chức năng như “cầu chia tạo mức nền 1,65 V”, “lọc trước ADC”, “hồi tiếp” hoặc “điều khiển chiều”; chú thích không tạo kết nối điện. Tên linh kiện, giá trị và tên chân được duy trì để phục vụ tra cứu. `UART_TX` và `UART_RX` là tên net của thiết kế; ngoại vi phần cứng tương ứng là USART1. Không sử dụng chung một Net Label `UART` cho cả TX và RX.

- Chỉ đặt 6 Net Label liên khối ở mục 1; dây nội bộ nối trực tiếp. Khi chia sheet, dùng Port/Sheet Entry phù hợp cấu trúc dự án và kiểm tra phạm vi kết nối; không mặc định Net Label cùng tên tự nối xuyên sheet.
- U3, U4 có đủ hai kênh + chân nguồn 4/8. Nếu symbol tách nguồn thành unit riêng, đặt đủ unit.
- Tụ tantalum C1/C2 có phân cực; ánh xạ số pad theo thư viện.
- Đối chiếu Pin Designator của symbol với Pad Designator của footprint.
- Chân MCU để trống: dùng No ERC theo quy tắc dự án.
- Footprint: xác định J1 theo jack thực tế; đối chiếu footprint của terminal P1/J2 bước 5,08 mm với linh kiện thực; Y1 ABM3B có kích thước 5,0 × 3,2 mm. J2 sử dụng thứ tự chân 1 = A, 2 = B, 3 = GND; không thay đổi số hoặc vị trí chân symbol.

---

## 7.1. Trạng thái triển khai schematic

- Khối nguồn: đã kiểm tra trực quan kết nối, chưa đồng nghĩa thử mạch thực hoặc hoàn tất ERC/footprint.
- Đang dựng MCU và nạp/debug theo mục 3; PA9 là TX, PA10 là RX; PB0 chung DE và /RE của MAX3485.
- Kiểm Pin Designator ↔ Pad Designator theo đúng symbol/footprint. Không tự di chuyển chân bên trong symbol; có thể bố trí lại cả linh kiện.
- Không bổ sung hoặc loại bỏ linh kiện nếu chưa có căn cứ kỹ thuật; mọi thay đổi cấu hình cần kèm theo giải thích và cập nhật tài liệu liên quan.

---

## 8. Tài liệu đối chiếu chân và schematic

Hướng dẫn mạch reset: [ST AN2586 — STM32 hardware design guidelines](https://www.st.com/resource/en/application_note/an2586-stm32-hardware-design-guidelines-stmicroelectronics.pdf).

1. [ST DS5319 — STM32F103x8/xB](https://www.st.com/resource/en/datasheet/stm32f103c8.pdf)
2. [ST LD1117](https://www.st.com/resource/en/datasheet/ld1117.pdf) — SOT-223, tab nối OUT
3. [Microchip DS20001733L — MCP6002](https://ww1.microchip.com/downloads/aemDocuments/documents/MSLD/ProductDocuments/DataSheets/MCP6001-1R-1U-2-4-1-MHz-Low-Power-Op-Amp-DS20001733L.pdf)
4. [ADI MAX3483–MAX3491](https://www.analog.com/media/en/technical-documentation/data-sheets/MAX3483-MAX3491.pdf)
5. [Vishay VBPW34S, Doc 81128](https://www.vishay.com/docs/81128/vbpw34s.pdf)
6. [Abracon ABM3B](https://abracon.com/Resonators/abm3b.pdf)
7. [Phoenix Contact 1715721](https://www.phoenixcontact.com/en-be/products/pcb-terminal-block-mkds-15-2-508-1715721)
