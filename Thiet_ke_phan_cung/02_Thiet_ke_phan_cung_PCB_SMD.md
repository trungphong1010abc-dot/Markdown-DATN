# Giai đoạn 2 — Thiết kế phần cứng và chọn linh kiện PCB SMD

## Mục tiêu thiết kế và trạng thái hiện tại

Đồ án thiết kế hệ thống nhúng IoT phát hiện chớp hồ quang điện trong hệ thống điện hạ áp và trung áp. Cấu hình phần cứng ở giai đoạn này thu nhận dòng điện bằng CT, thu ánh sáng bằng photodiode, xử lý tại STM32 rồi truyền dữ liệu qua RS485 tới máy tính hoặc gateway. Định hướng của sản phẩm là cảnh báo; hệ thống không điều khiển máy cắt và không thực hiện ngắt điện. PCB trong tài liệu này mới đảm nhiệm thu nhận và truyền dữ liệu, chưa tích hợp đèn hoặc còi cảnh báo. Phép thử hiện tại giới hạn ở nguyên mẫu hạ áp, còn khả năng triển khai tại trung áp mới được phân tích.

File này chuyển cấu hình nguyên mẫu và số liệu thử nghiệm ở [file 1](01_Chon_linh_kien_module_va_noi_day.md) thành phương án linh kiện SMD cho PCB. Các khối được xem xét theo đường đi của tín hiệu: nguồn cung cấp các rail ổn định; MCU nhận tín hiệu ở ADC; khối CT và khối quang điều hòa hai đại lượng đo; khối RS485 đưa dữ liệu ra ngoài bo. Bảng BOM ghi cấu hình đang dự kiến, còn phần tính toán giải thích vì sao chọn giá trị đó và điều kiện nào vẫn phải kiểm tra. Cách nối từng chân trên schematic được trình bày tại [file 3](03_Huong_dan_noi_day_schematic.md).

Khi có số đo nguyên mẫu, quyết định PCB cần được đối chiếu với dòng thực, mức BIAS, biên độ trước/sau lọc và đáp ứng quang. Nếu phép đo chưa được thực hiện, lựa chọn được ghi là phương án tính toán hoặc theo datasheet, không coi là kết quả đã xác nhận. Thay đổi linh kiện so với nguyên mẫu cũng tạo thành một cấu hình mới cần đo lại trên PCB. Riêng kênh quang, PCB có hai tầng RC sau TIA; vì vậy phép đo PA1 trên module nối thẳng chỉ mô tả cấu hình module, không thay thế phép đo riêng tại `TIA_LIGHT` và `ADC_LIGHT` sau khi hàn.

Trong tài liệu, thông số nhà sản xuất, giá trị thiết kế, giả thiết và kết quả đo được phân biệt rõ. BOM hiện tại chưa xác nhận đầy đủ mã đặt hàng, ESR hay footprint của mọi linh kiện; các mục đó chỉ được khóa sau khi đối chiếu với linh kiện thực tế.

Khi vẽ schematic, các khối liên kết bằng sáu nhãn net: `ADC_CURRENT`, `ADC_LIGHT`, `BIAS_1V65`, `UART_TX`, `UART_RX` và `RS485_DIR`. Nguồn dùng Power Port `+3V3` và `GND`; đầu vào nguồn mang nhãn `+5V`. Các mối nối trong cùng một khối được vẽ bằng dây để sơ đồ dễ theo dõi.

Quy ước tụ dùng chung cho ba tài liệu: tụ gốm chọn định mức 50 V, tụ tantalum C1/C2 chọn 16 V. Mã điện dung ba chữ số được quy đổi theo pF: 27 pF (270), 47 pF (470), 100 pF (101), 10 nF (103), 100 nF (104), 1 µF (105), 10 µF (106), 22 µF (226). Đây là mã quy đổi giá trị, không có nghĩa mọi tụ SMD đều in mã trên thân. Package và footprint phải khớp mã linh kiện mua; riêng tụ gốm 10 µF–50 V kích thước 0805 trong BOM vẫn cần xác minh.

### Quy tắc đo và lấy mẫu theo cảm biến

Trước khi chọn tốc độ lấy mẫu, phải kiểm tra toàn đường tín hiệu: cảm biến → mạch khuếch đại/chuyển đổi → lọc → ADC. Điện áp tại ADC phải nằm trong khoảng 0–3,3 V, có khoảng dự phòng để tín hiệu không bị cắt đỉnh.

Trong mạch hiện tại, **nhánh CT dùng lọc thông thấp R3/C12**; **nhánh quang dùng R11/C17 và R12/C18 làm hai tầng lọc thông thấp sau TIA**. Cả hai nhánh không có lọc thông cao riêng. Cf nằm trong hồi tiếp TIA, không được xem là tầng chống alias đã xác nhận. Chống alias nghĩa là làm giảm tín hiệu quá nhanh bằng mạch analog trước ADC để ADC không đọc tín hiệu nhanh thành hình dạng chậm giả. Lọc thông thấp giảm tín hiệu nhanh; lọc thông cao giảm tín hiệu DC/chậm. Tốc độ lấy mẫu và lọc phải được chọn cùng nhau. Các giá trị dưới đây là cấu hình thiết kế và mốc khảo sát ban đầu; hiệu quả thực cần đo.

| Cảm biến | Mục tiêu đo | fs khởi đầu mỗi kênh | T_sampling = 1/fs | Điều kiện cần chốt |
|---|---|---:|---:|---|
| CT DL-CT08CL6-1000/1 | Dạng sóng dòng AC cơ bản/vùng thấp; nếu cần phân tích tới 9 kHz, tăng tốc độ và băng thông toàn nhánh | 32 ksample/s ban đầu; 50–100 ksample/s nếu giữ tới 9 kHz | 31,25 µs; 20–10 µs | RC hiện tại 1 kΩ–100 nF có fc ≈ 1,59 kHz, không phù hợp nếu cần giữ tới 9 kHz. Xác nhận tỷ số, dòng định mức và burden đúng mã CT trước khi chốt R2 = 150 Ω. |
| VBPW34S (PCB), BPW34 (nguyên mẫu) | Phát hiện biến thiên ánh sáng; độ rộng xung tối thiểu cần nhận biết còn phải định nghĩa | 50 ksample/s ban đầu | 20 µs | `fs` áp dụng cho tín hiệu tại PA1 sau lọc trên PCB. Cf = 100 pF nằm trong TIA; PCB có thêm hai tầng RC sau TIA, nhưng chúng chưa được xác nhận đủ mức chống alias. Cực tính từ R6/C15 khoảng 159 kHz không phải băng thông thực. Đánh giá đáp ứng toàn AFE; nếu cần bắt xung <100 µs, khảo sát từ 100 ksample/s (10 µs) trở lên. |

Ghi `fs` và `T_sampling` riêng cho từng kênh. Ví dụ `fs` của CT là 32 ksample/s thì khoảng cách giữa hai lần đọc là 31,25 µs; photodiode ở 50 ksample/s thì khoảng cách là 20 µs. Chu kỳ gửi UART/log không phải chu kỳ lấy mẫu. Đối với xung quang, cần xác định độ rộng nhỏ nhất $t_{p,min}$, sườn xung, mức tín hiệu so với nền, dạng lặp và tiêu chí phát hiện. Tính khởi đầu $f_s\geq N/t_{p,min}$ với $N=5$–10; ví dụ xung 100 µs tương ứng 50–100 ksample/s (20–10 µs), còn xung 10 µs tương ứng 500 ksample/s–1 Msample/s. Đây là phép tính số mẫu, chưa xác nhận khả năng ADC/firmware hoặc đáp ứng mạch analog. Dùng LED xung có điều khiển để khảo sát AFE; không tạo hồ quang và không xem thử nghiệm LED là tương đương thử nghiệm hồ quang thực. IEC 61000-4-30:2025 và IEC 61000-4-7 là tài liệu tham khảo khi đánh giá chất lượng điện/hài. IEC 60255-1:2022, IEC 60255-26:2023 và IEC 60255-27:2023 chỉ liên quan nếu hệ thống hướng tới thiết bị rơ-le/bảo vệ. IEC 60947-9-2:2021 là tham khảo cho thiết bị phát hiện/giảm thiểu hồ quang nội bộ hạ áp; tiêu chuẩn này không cung cấp một tốc độ lấy mẫu chung cho prototype. Không tuyên bố tuân thủ khi chưa thực hiện các phép thử tương ứng.

## 1. Bảng linh kiện PCB và danh sách đã đặt

Các bảng dưới đây gộp lựa chọn linh kiện và BOM **theo từng khối**; linh kiện cùng giá trị được tách theo vị trí sử dụng để dễ đọc. SL là số lượng cho một PCB; adapter, ST-Link, CT và USB–RS485 là thiết bị ngoài bo. R8–R10 là vị trí tùy chọn, không mặc định lắp toàn bộ.

Các linh kiện trong bảng đã được đặt mua. Trước khi xác định footprint, cần đối chiếu mã linh kiện, dung sai, định mức và package với linh kiện thực tế. BT1 sử dụng nút nhấn SMD hai chân, kích thước 3 × 6 × 2,5 mm, thường hở và nhấn-nhả; mã nhà sản xuất cùng kích thước/khoảng cách pad cần được xác minh theo linh kiện thực tế.

### 1.1. Khối nguồn

| Mã | Linh kiện / giá trị / mã hãng | Package | SL | Căn cứ lựa chọn / lưu ý |
|---|---|---|---:|---|
| J1 | Jack DC cái: 5,5 mm (tham khảo PJ-102AH) | THT | 1 | Phù hợp phích adapter; xác nhận lỗ tâm, chân và footprint theo jack thực |
| U1 | LDO: LD1117S33TR, 3,3 V; tới 800 mA, còn phụ thuộc nhiệt | SOT-223 | 1 | Hạ 5 V xuống 3,3 V; dòng dùng được còn phụ thuộc nhiệt |
| C1 | Tụ tantalum: 10 µF (106), 16 V | 3528 (B case), cần xác nhận mã thực | 1 | Tụ đầu vào; có phân cực |
| C2 | Tụ tantalum: 22 µF (226), 16 V | 6032 (C case) | 1 | Tụ đầu ra; có phân cực; chọn điện dung cao hơn mức tối thiểu 10 µF (106) nêu trong datasheet LD1117 |

### 1.2. Khối MCU

| Mã | Linh kiện / giá trị / mã hãng | Package | SL | Cơ sở lựa chọn / lưu ý |
|---|---|---|---:|---|
| U2 | MCU: STM32F103C8T6; 72 MHz; Flash 64 KB; SRAM 20 KB; 2,0–3,6 V | LQFP-48 | 1 | Có ADC 12 bit, UART, DMA và SWD để đọc cảm biến, xử lý và truyền dữ liệu |
| C3–C5 | Tụ gốm: 100 nF (104), X7R, 50 V | 0805 | 3 | Một tụ 100 nF (104) cho mỗi chân VDD MCU |
| C9 | Tụ gốm: 10 µF (106), X7R, 50 V | 0805 | 1 | Tụ nguồn tổng MCU |
| C6 | Tụ gốm: 100 nF (104), X7R, 50 V | 0805 | 1 | Lọc nguồn VDDA, phối hợp C10 1 µF (105) |
| C10 | Tụ gốm: 1 µF (105), X7R, 50 V | 0805 | 1 | Lọc nguồn VDDA phục vụ ADC |
| Y1 | Thạch anh: ABM3B-8.000MHZ-B2-T, 8 MHz; CL = 18 pF | 5,0 × 3,2 mm | 1 | Nguồn clock ngoài; có thể cấu hình PLL ×9 để đạt 72 MHz |
| C8, C11 | Tụ gốm: 27 pF (270), ±5 %, C0G, 50 V (C0805C270J5GACTU) | 0805 | 2 | Tụ tải cho đúng mã Y1 |
| R1 | Điện trở: 10 kΩ, 1 %, 0,125 W | 0805 | 1 | Kéo BOOT0 xuống để khởi động từ Flash |
| C7 | Tụ gốm: 100 nF (104), X7R, 50 V | 0805 | 1 | Tụ NRST theo cấu hình reset |
| BT1 | Nút nhấn RESET: 2 chân SMD 3 × 6 × 2,5 mm, thường hở, nhấn nhả; mã hãng chưa xác nhận | SMD 3 × 6 × 2,5 mm; pad cần đối chiếu nút thực | 1 | Khởi động lại MCU thuận tiện khi chạy thử; mã hãng và footprint cần xác nhận theo nút thực |
| H1 | Header SWD: 1×5, bước 2,54 mm | Header | 1 | Đưa ra 3V3, GND, SWDIO, SWCLK và NRST |

### 1.3. Khối dòng

| Mã | Linh kiện / giá trị / mã hãng | Package | SL | Cơ sở lựa chọn / lưu ý |
|---|---|---|---:|---|
| P1 | Terminal 2 cực: Bước 5,08 mm (Phoenix 1715721) | THT | 1 | Kết nối thứ cấp CT |
| U3 | Op-amp: MCP6002-I/SN; nguồn hãng 1,8–6,0 V; GBW điển hình 1 MHz | SOIC-8 | 1 | Cấp 3,3 V; một kênh đệm dòng, một kênh đệm BIAS |
| R2 | Điện trở: 150 Ω, 1 %, 0,125 W (CRCW0805150RFKEA) | 0805 | 1 | Burden PCB; đối chiếu với phép thử module và giới hạn tải CT trước khi chốt |
| R5, R4 | Điện trở: 10 kΩ, 1 %, 0,125 W | 0805 | 2 | Cầu chia tạo BIAS danh định 1,65 V |
| C13 | Tụ gốm: 100 nF (104), X7R, 50 V | 0805 | 1 | Tụ nguồn U3 |
| R3 | Điện trở: 1 kΩ, 1 %, 0,125 W | 0805 | 1 | Cùng C12 tạo lọc trước ADC |
| C12 | Tụ gốm: 100 nF (104), X7R, 50 V | 0805 | 1 | Phối hợp R3 tạo lọc trước ADC dòng |

### 1.4. Khối quang

| Mã | Linh kiện / giá trị / mã hãng | Package | SL | Cơ sở lựa chọn / lưu ý |
|---|---|---|---:|---|
| D1 | Photodiode: VBPW34S | SMD gullwing | 1 | Thu ánh sáng; phù hợp lắp SMD; dùng footprint đúng biến thể Vishay |
| U4 | Op-amp: MCP6002-I/SN; nguồn hãng 1,8–6,0 V; GBW điển hình 1 MHz | SOIC-8 | 1 | IC riêng cấp 3,3 V; chuyển dòng quang thành áp, kênh còn lại không cấp tải ngoài |
| R6 | Điện trở: 10 kΩ, 1 %, 0,125 W | 0805 | 1 | Điện trở hồi tiếp; chọn ban đầu để khảo sát độ nhạy |
| C15 | Tụ gốm: 100 pF (101), ±5 %, C0G/NP0, 50 V | 0805 | 1 | Hồi tiếp song song R6 để hỗ trợ ổn định; giá trị cần kiểm chứng |
| C14 | Tụ gốm: 100 nF (104), X7R, 50 V | 0805 | 1 | Tụ nguồn U4 |
| R11, R12 | Điện trở: 1 kΩ, 1 %, 0,125 W | 0805 | 2 | Nối tiếp tạo hai tầng lọc thông thấp sau U4A, trước ADC_LIGHT |
| C17, C18 | Tụ gốm: 10 nF (103), X7R, 50 V | 0805 | 2 | Tụ shunt lọc; C17 tại nút R11/R12 và C18 tại ADC_LIGHT, đều xuống GND |

### 1.5. Khối truyền thông

| Mã | Linh kiện / giá trị / mã hãng | Package | SL | Cơ sở lựa chọn / lưu ý |
|---|---|---|---:|---|
| U5 | RS485: MAX3485ESA+; 3,0–3,6 V; tới 10 Mbps | SOIC-8 | 1 | Chuyển UART 3,3 V sang RS485 bán song công; 10 Mbps là khả năng IC, chưa phải baudrate hệ thống |
| C16 | Tụ gốm: 100 nF (104), X7R, 50 V | 0805 | 1 | Tụ nguồn U5 |
| R7 | Điện trở: 10 kΩ, 1 %, 0,125 W | 0805 | 1 | Kéo chung DE và /RE xuống thấp, mặc định nhận |
| J2 | Terminal 3 cực A/B/GND, bước 5,08 mm; tham khảo Phoenix 1715734 | THT | 1 | Đấu dây cáp RS485; giữ thứ tự chân A/B/GND |
| R9 | Điện trở: 120 Ω, 1 %, 0,25 W | 1206 | 1 | Kết thúc đường truyền dùng cáp 120 Ω; lắp theo vị trí đầu cuối; Vị trí tùy chọn DNP, lắp theo cấu hình bus |
| R8, R10 | Điện trở: 330 Ω, 1 %, 0,125 W | 0805 | 2 | Tạo mức nghỉ; lắp theo cấu hình bias của toàn bus; Vị trí tùy chọn DNP, lắp theo cấu hình bus |

### 1.6. Thiết bị ngoài PCB

| Mã | Linh kiện / giá trị / mã hãng | Package | SL | Cơ sở lựa chọn / lưu ý |
|---|---|---|---:|---|
| — | Adapter: 5 VDC–2 A, jack 5,5/2,1 mm | Ngoài PCB | 1 | Nguồn cách ly cấp mạch; 2 A là khả năng cấp, xác nhận phích phù hợp jack thực |
| — | ST-Link V2: Nạp STM32 | Ngoài PCB | 1 | Nạp/debug qua SWD, không cấp song song nguồn adapter |
| CT1 | CT: DL-CT08CL6-1000/1 | Ngoài PCB | 1 | Thu dòng AC; tỷ số tính toán tạm lấy 1000:1, chưa xác nhận bằng tài liệu hãng |
| — | USB–RS485: CH340, lấy nguồn USB | Ngoài PCB | 1 | Giao tiếp laptop; lấy nguồn USB riêng |

**Tổng mua theo giá trị:** điện trở 10 kΩ gồm R1/R5/R4/R6/R7: 5 chiếc; điện trở 1 kΩ gồm R3/R11/R12: 3 chiếc; tụ 100 nF (104) 0805: 9 chiếc; tụ 10 nF (103) 0805: 2 chiếc cho lọc quang. Các dòng trong bảng là các vị trí riêng, không cộng lại lần nữa theo phần tính toán bên dưới. Linh kiện mua dự phòng chưa tính vào SL.

## 2. Căn cứ lựa chọn và tính toán theo từng khối

Các mục 2.1–2.6 tương ứng lần lượt với bảng linh kiện 1.1–1.6. Phép tính kiểm tra điều kiện thiết kế theo giả thiết đã ghi; chưa thay thế datasheet linh kiện thực hoặc kết quả thử nghiệm.

### 2.1. Khối nguồn

**Cơ sở lựa chọn:** adapter 5 V kết hợp LD1117S33TR tạo nguồn 3,3 V cho MCU, hai MCP6002 và MAX3485. LDO điện áp đầu ra cố định giúp đơn giản hóa cấu trúc nguồn; C1 bố trí tại đầu vào và C2 phục vụ ổn định đầu ra. Model J1 cần được xác định theo đầu nối của adapter thực tế.

#### 2.1.1. Công suất và nhiệt

**Kiểm tra chính:** tổng dòng phân bổ ban đầu khoảng **142 mA**; chọn **200 mA** làm mức kiểm tra nguồn. Cả hai là giá trị thiết kế, phải đo lại. Với đầu vào giả thiết 5,25 V, đầu ra 3,235 V và dòng riêng LDO dự toán 10 mA:

$$P_{U1}\approx(5,25-3,235)\times0,2+5,25\times0,01=0,456\ \mathrm{W}$$

Với nhiệt trở tham khảo 110°C/W và môi trường giả thiết 40°C, nhiệt độ mối nối ước lượng khoảng **90°C**; kết quả phụ thuộc tản nhiệt PCB. Cần đánh giá nhiệt thực khi có tải.

**Kết luận lựa chọn U1:** theo tính toán, LD1117S33TR dạng SOT-223 đáp ứng điều kiện nhiệt với điện áp vào 4,75–5,25 V, dòng tải thiết kế không quá 200 mA và nhiệt độ môi trường cục bộ quanh IC không quá 40°C, với điều kiện nhiệt trở hiệu dụng của PCB không vượt khoảng 142°C/W khi sử dụng mục tiêu nhiệt độ mối nối 105°C. U1 được giữ trong BOM thiết kế hiện tại. Khả năng nhiệt của PCB thực tế chưa được xác nhận do chưa có layout hoàn chỉnh và kết quả đo. Mức 105°C là mục tiêu thiết kế có dự phòng, không phải giới hạn do nhà sản xuất quy định.

Theo [ST LD1117, Rev 38, bảng 1, 2 và 6](https://www.st.com/resource/en/datasheet/ld1117.pdf), phiên bản tiêu chuẩn có nhiệt độ mối nối làm việc 0–125°C; SOT-223 có RθJA = 110°C/W và RθJC = 15°C/W; dòng riêng tối đa dùng tính toán là 10 mA. **125°C là nhiệt độ mối nối bên trong, không phải nhiệt độ không khí hoặc nhiệt độ vỏ cho phép.** Không dùng mức bảo vệ quá nhiệt làm điểm vận hành.

Mô hình tính: P ≈ (Vin − Vout) × Iout + Vin × Id; Tj ≈ Ta + P × RθJA. Dùng Vin = 5,25 V, Vout = 3,235 V, Id = 10 mA:

| Tải đầu ra | Công suất nhiệt ước tính | Tj tại Ta = 40°C, RθJA = 110°C/W | Đánh giá theo mô hình |
|---|---:|---:|---|
| 142 mA, ngân sách ban đầu | 0,339 W | 77,2°C | Dưới mục tiêu 105°C |
| 200 mA, mức kiểm tra thiết kế | 0,456 W | 90,1°C | Dưới mục tiêu 105°C; cách giới hạn 125°C khoảng 35°C |
| 500 mA, minh họa khi tăng tải | 1,060 W | 156,6°C | Vượt giới hạn; không chấp nhận với giả thiết tản nhiệt này |
| 800 mA, minh họa giới hạn dòng IC | 1,665 W | 223,1°C | Không thể vận hành liên tục với giả thiết này |

Các nhiệt độ vượt giới hạn chỉ là kết quả ngoại suy để loại phương án, không phải nhiệt độ IC sẽ duy trì khi bảo vệ tác động. Với tải 200 mA, điều kiện đạt mục tiêu 105°C tại Ta = 40°C là RθJA ≤ (105 − 40)/0,4555 ≈ **142,7°C/W**. Nếu giữ RθJA = 110°C/W thì Ta tối đa theo mục tiêu này khoảng **54,9°C**; tại Ta = 60°C, Tj đã khoảng 110,1°C. Vì vậy không mở rộng kết luận sang tủ điện nóng mà chưa tính lại.

**Yêu cầu layout và kiểm tra:** dành vùng đồng nối tab OUT của U1 với **+3V3**, không nối tab vào GND; tránh chỉ nối tab bằng đường đồng nhỏ. Diện tích đồng, số lớp, vỏ hộp và luồng khí ảnh hưởng nhiệt trở, nên không gán một diện tích đồng bảo đảm khi chưa có mô hình/layout. Kiểm tra ở đầu vào 5,25 V, tải 200 mA, môi trường cục bộ 40°C và điều kiện vỏ dự kiến đến khi nhiệt ổn định; đo điện áp ra, dòng và nhiệt. Nhiệt vỏ đo được không được coi trực tiếp là Tj; cần phương pháp suy ra Tj phù hợp hoặc mô hình nhiệt đã kiểm chứng. Đồng thời kiểm tra tụ/ESR và độ ổn định nguồn như bên dưới.

**Cần xác nhận:** mã và ESR/dung sai của C1/C2, độ ổn định đầu ra LDO, điện áp adapter dưới tải. Chưa gán ESR hoặc dung sai cho C2 khi chưa xác nhận đúng mã tụ thực. Tiếp điểm jack thực chưa xác nhận; không coi model PJ-102AH là jack đã chốt. Chi tiết nối hiện hành xem file 3.


#### 2.1.2. Ngân sách dòng thiết kế

| Nhóm tải | Phân bổ | Căn cứ / giới hạn |
|---|---:|---|
| STM32F103C8T6 | 60 mA | Mốc khoảng 50 mA trong DS5319, 72 MHz, ngoại vi bật, 85°C, I/O không tải; cộng 20% dự phòng |
| Hai MCP6002, bốn kênh | 2 mA | Iq max 170 µA/kênh × 4 = 0,68 mA; phần còn lại dành tải đầu ra/dự phòng |
| MAX3485 và tải bus | 70 mA | Ước lượng bảo thủ: 3,3 V/60 Ω = 55 mA; IC 2,2 mA; khoảng 10 mA bias; làm tròn, không phải dòng phát đã đo |
| Cầu chia BIAS và kéo | 10 mA | Phân bổ kèm dự phòng, không phải dòng riêng cầu chia |
| **Tổng / mức kiểm tra** | **142 / 200 mA** | 200 mA cao hơn tổng khoảng 41%; phải đo lại |

#### 2.1.3. Dư áp và tụ

Giả thiết đầu vào 4,75–5,25 V. Dùng đầu ra biên trên 3,365 V và dropout tối đa tham khảo 1,2 V tại 800 mA trong datasheet LD1117:

$$V_{dư}=4,75-3,365-1,2=0,185\ \mathrm{V}>0$$

Phép kiểm sơ bộ có dư áp theo các mốc tính; điện áp adapter tại tải thực vẫn phải đo. Giới hạn 800 mA của IC không đồng nghĩa PCB cấp được 800 mA liên tục.

C1 chọn tantalum 10 µF (106)–16 V, dự kiến 3528 (B case); định mức áp có dự phòng với 5,25 V. Package/footprint phải đối chiếu đúng mã tụ 16 V thực. C2 chọn tantalum 22 µF (226)–16 V, 6032; datasheet LD1117 nêu tối thiểu 10 µF (106) đầu ra. **Chưa xác nhận dung sai C2 nên chưa chốt điện dung nhỏ nhất.** Nếu *giả thiết* ±10% thì 22 × 0,9 = 19,8 µF; chỉ là kiểm tra có điều kiện. C1 trong bảng cũ ghi ±10%, nay xem là yêu cầu lựa chọn cần đối chiếu mã thực. ESR và ổn định LDO phải kiểm tra theo đúng tụ mua; không mặc định mã tụ 16 V cũ là mã đã chốt cho C2 hiện tại.

### 2.2. Khối MCU

**Tụ tải thạch anh:** với hai tụ bằng nhau và điện dung ký sinh **giả thiết** 4,5 pF:

$$C_X=2(C_L-C_s)=2(18-4,5)=27\ \mathrm{pF}$$

**Cơ sở lựa chọn:** MCU tích hợp ADC, DMA, UART và SWD, phù hợp với yêu cầu thu thập hai kênh, xử lý và truyền dữ liệu. Nguồn clock 8 MHz có thể được nhân bằng PLL với hệ số ×9; đặc tính này không tự xác định thời gian phát hiện của toàn hệ thống.

**Kiểm tra R1:** với 3,3 V và 10 kΩ, công suất 3,3²/10000 ≈ 1,1 mW, thấp hơn định mức chọn 125 mW. Tụ nguồn theo hướng dẫn AN2586: 100 nF (104) cho từng VDD, 100 nF (104) + 1 µF (105) cho VDDA, tụ tổng 10 µF (106). C7 100 nF (104) phục vụ reset; MCU có kéo lên NRST bên trong.

**BT1 RESET:** sử dụng nút nhấn SMD hai chân, kích thước 3 × 6 × 2,5 mm, thường hở và nhấn-nhả để khởi động lại MCU trong quá trình thử nghiệm; nút không ngắt nguồn toàn mạch. C7 và cấu hình kéo lên NRST bên trong MCU được duy trì; thiết kế hiện tại không bổ sung điện trở kéo ngoài. Cách kết nối được trình bày tại mục 3.6 của file 3. Mã nhà sản xuất và kích thước/khoảng cách pad cần được đối chiếu với datasheet hoặc linh kiện thực tế; hình 3D không đủ căn cứ để xác nhận footprint. Thiết kế không bổ sung nút BOOT; R1 tiếp tục kéo BOOT0 xuống GND.

**Cần xác nhận:** khởi động thạch anh, dòng tiêu thụ, cấu hình lấy mẫu và hiệu năng thuật toán. Thông số MCU chưa tự chứng minh thời gian phát hiện. Tụ C9 cần đủ điện dung hữu dụng tại 3,3 V.

### 2.3. Khối dòng

**Cơ sở lựa chọn:** CT1 thu dòng xoay chiều; P1 kết nối cuộn thứ cấp với PCB; R2 chuyển dòng thứ cấp thành điện áp; U3 đệm tín hiệu và BIAS; R3/C12 lọc tín hiệu trước ADC. MCP6002 hoạt động với nguồn thiết kế 3,3 V, tuy nhiên GBW điển hình 1 MHz không xác nhận băng thông của toàn nhánh. C13 100 nF (104) lọc nguồn tại IC. Burden PCB sử dụng **150 Ω, 1%, 0,125 W**. Phép thử module tại file 1 so sánh 47 Ω và 150 Ω nhằm ghi nhận biên độ và headroom tại cùng dòng. Điện trở 47 Ω, 5%, 0,25 W chỉ dùng trong phép thử module, không thuộc BOM hoặc footprint PCB.

**BIAS:** hai điện trở R5/R4 cùng 10 kΩ tạo mức danh định 3,3 × 10/(10 + 10) = **1,65 V**; dòng cầu chia 3,3/20 kΩ = **0,165 mA**. Kênh đệm của U3 giúp hạn chế ảnh hưởng tải lên cầu chia; mức và khả năng cấp dòng BIAS phải kiểm tra thực. U3 và U4 là hai MCP6002 riêng, cùng dùng nguồn 3,3 V.

**Kiểm tra burden:** với dòng sơ cấp thiết kế **5 A RMS**, tỷ số **giả thiết 1000:1**, mô hình CT tuyến tính và dòng hình sin:

$$I_S=5/1000=5\ \mathrm{mA};\qquad V_{B,\mathrm{RMS}}=0,005\times150=0,75\ \mathrm{V}$$

$$P_{R2}=0,005^2\times150=3,75\ \mathrm{mW}<125\ \mathrm{mW}$$

Đỉnh tín hiệu khoảng 1,061 V; quanh BIAS 1,65 V được khoảng **0,589–2,711 V**, nằm trong nguồn 3,3 V theo mô hình lý tưởng. Đây là kiểm tra biên áp/công suất, chưa chứng minh CT làm việc chính xác với burden 150 Ω.

**Bộ lọc:** R3 = 1 kΩ và C12 = 100 nF (104) cho:

$$f_c=\frac{1}{2\pi RC}\approx1,59\ \mathrm{kHz}$$

Tốc độ lấy mẫu khởi đầu của CT là 32 ksample/s (`T_sampling` = 31,25 µs) khi khảo sát dạng sóng 50/60 Hz và vùng tần số thấp. Nếu yêu cầu bảo toàn dạng sóng đến 9 kHz, cần khảo sát 50–100 ksample/s để có khoảng 5–10 mẫu mỗi chu kỳ. Khi đó phải thiết kế lại R3/C12 để tín hiệu 9 kHz không bị làm nhỏ mạnh. R3/C12 hiện tại giảm tín hiệu nhanh từ khoảng 1,59 kHz trở lên; nó có tác dụng lọc thông thấp nhưng chưa được xác nhận là bộ chống alias đầy đủ cho mọi mục tiêu. IEC 61000-4-7 không quy định trực tiếp tốc độ lấy mẫu firmware cho cấu hình này.

**Hạng mục cần xác nhận:** tỷ số biến dòng, tải thứ cấp cho phép và tính tuyến tính của CT; mức BIAS; dải tần cần bảo toàn cho thuật toán. Khi chưa xác định yêu cầu băng thông, chưa thể kết luận tần số cắt 1,59 kHz là tối ưu. Mức 5 A là giá trị thiết kế của PCB, không phải dải dòng đã thử nghiệm và không đại diện cho dòng sự cố trong tủ hạ áp/trung áp.

### 2.4. Khối quang

**Cơ sở lựa chọn:** D1 VBPW34S thu nhận ánh sáng và sử dụng biến thể SMD tương ứng với footprint. U4 MCP6002 là IC riêng, cấp nguồn 3,3 V. R6 xác định hệ số chuyển đổi dòng quang–điện áp; C15 hỗ trợ ổn định mạng hồi tiếp; C14 100 nF (104) lọc nguồn. R11/C17/R12/C18 tạo hai tầng lọc thông thấp sau đầu ra TIA, trước ADC_LIGHT. Khác với phép thử module có thể nối thẳng TIA tới ADC, PCB mặc định đưa tín hiệu qua cả hai tầng này. Do chưa có dữ liệu dòng quang, R6/C15 vẫn là giá trị khảo sát và chưa được chứng minh là tối ưu.

Nhánh quang dùng TIA tham chiếu BIAS danh định 1,65 V. Với cực tính thiết kế hiện hành, mô hình lý tưởng là:

$$V_{OUT}\approx V_{BIAS}+I_{photo}R6$$

R6 = 10 kΩ tạo hệ số lý tưởng **10 mV/µA**. Dải dòng quang hữu dụng phụ thuộc biên ra op-amp và ánh sáng nền. Cf = 100 pF nằm trong đường hồi tiếp của TIA. Sau TIA, R11/C17 và R12/C18 tạo lọc thông thấp trước ADC_LIGHT; cấu hình hiện tại không có lọc thông cao riêng.

**Hạng mục cần xác nhận:** độ nhạy, bão hòa, đáp ứng xung và ổn định của AFE với cặp 10 kΩ–100 pF (101), cùng mức giảm tín hiệu nhanh và độ suy giảm xung do tầng lọc đầu ra. Do chưa có dữ liệu dòng quang thực tế, chưa thể kết luận R6/C15 là tối ưu hoặc xác định khoảng cách phát hiện. Kênh op-amp còn lại không cấp tải ngoài; cấu hình chi tiết được trình bày tại file 3.

**Lọc đầu ra PCB:** lắp R11 = R12 = 1 kΩ mắc nối tiếp, C17 = C18 = 10 nF mắc từ mỗi nút sau điện trở xuống GND. Tần số cắt của mỗi tầng xét riêng xấp xỉ 15,9 kHz; hai tầng liên tiếp giảm khoảng 14 dB ở 25 kHz và 22 dB ở 50 kHz theo mô hình lý tưởng. Đây là cấu hình thiết kế để giảm tín hiệu nhanh trước ADC, chưa phải mức chống alias đã được chứng nhận. Nó phù hợp hơn để khảo sát xung 100 µs ở 100 ksample/s; xung 10 µs có thể bị suy giảm rõ. Sau khi hàn PCB, đo đáp ứng thực và đối chiếu với cấu hình module nối thẳng để xác nhận độ suy giảm xung.

Mốc lấy mẫu quang khởi đầu là 50 ksample/s (T_sampling = 20 µs). Với xung thử 100 µs, mốc này cho khoảng 5 mẫu/xung; 100 ksample/s (10 µs) cho khoảng 10 mẫu/xung. Nếu yêu cầu xung 10 µs, công thức 5–10 mẫu/xung cho 500 ksample/s–1 Msample/s. Đây là phép tính mục tiêu, không phải khẳng định STM32/firmware hiện đạt được; phải xác nhận tốc độ ADC thực, sampling time, trigger/DMA và thời gian thu. Chưa có độ rộng xung hồ quang tối thiểu được yêu cầu nên chưa thể tuyên bố mạch bắt được xung hồ quang cụ thể.

Khi thử PCB, dùng LED xung có độ rộng/sườn điều khiển được; ghi nguồn sáng/bước sóng, khoảng cách, góc, nền sáng, độ rộng và chu kỳ lặp, mức đầu ra TIA/ADC, clipping, số lần phát hiện/bỏ sót và độ trễ. Quan sát đồng thời tín hiệu tham chiếu LED và đầu ra TIA bằng oscilloscope. Không suy băng thông toàn TIA từ cực $R6C15$ hoặc datasheet photodiode riêng lẻ; phép thử LED chỉ đặc trưng đường điện tử/quang trong điều kiện thử đó.

### 2.5. Khối truyền thông

**Cơ sở lựa chọn:** MAX3485 sử dụng nguồn 3,3 V và tương thích với giao tiếp UART của MCU; J2 cung cấp các kết nối A/B/GND tới cáp. R7 10 kΩ thiết lập trạng thái nhận mặc định; C16 100 nF (104) lọc nguồn. R9 dùng để kết thúc bus, còn R8/R10 tạo mạch bias khi topology bus yêu cầu; việc lắp các điện trở này phụ thuộc cấu hình toàn bus. Tốc độ tối đa 10 Mbps của IC không phải baudrate đã xác định cho hệ thống.

Với hai điện trở kết thúc 120 Ω, tải tương đương 60 Ω. Một cặp bias 330 Ω tạo điện áp nghỉ lý tưởng:

$$V_{AB}=\frac{3,3\times60}{330+60+330}=0,275\ \mathrm{V}$$

Mốc này cao hơn ngưỡng nhận +0,2 V của MAX3485 trong mô hình điện trở; cần xét thêm tải đầu thu, sai số và nhiễu. Ước lượng công suất khi đặt 3,3 V trên điện trở: **120 Ω → 90,8 mW; 330 Ω → 33 mW**, thấp hơn định mức đã chọn.

**Cần xác nhận:** điện trở bias/kết thúc sẵn có trong USB–RS485, điện áp nghỉ và chất lượng truyền. R8–R10 là vị trí tùy chọn, không mặc định lắp toàn bộ. USB–RS485 CH340 lấy nguồn USB laptop; không cấp song song thêm 5 V từ adapter.

Xét nguồn thấp 3,235 V và điện trở ±1%:

$$V_{AB,min}\approx\frac{3,235\times59,4}{333,3+59,4+333,3}\approx0,265\ \mathrm{V}$$

Đây vẫn là mô hình điện trở, chưa gồm mọi ảnh hưởng tải đầu thu và nhiễu; không thay phép đo bus thực.

### 2.6. Thiết bị ngoài PCB

| Thiết bị | Căn cứ lựa chọn / kiểm tra | Giới hạn cần xác nhận |
|---|---|---|
| Adapter cách ly 5 V–2 A | Với mức kiểm tra đường 3,3 V là 0,2 A và Iq LDO giả thiết 0,01 A, dòng đầu vào LDO ước lượng 0,21 A; công suất đầu vào danh định khoảng 5 × 0,21 = 1,05 W. Adapter 5 × 2 = 10 W có dự phòng theo mô hình này | Đây là tính cho PCB hiện hành, không dùng dòng module TTL485. Nếu có tải 5 V trực tiếp phải cộng riêng. Đo điện áp dưới tải; xác nhận cách ly, cực tính và phích/jack thực |
| ST-Link V2 | Được chọn để nạp/debug SWD; header H1 đưa ra nguồn tham chiếu, GND, SWDIO, SWCLK và NRST | Kiểm chức năng chân của đầu nạp thực, đặc biệt VTref và chân cấp nguồn; không cấp song song với adapter. Không có phép tính công suất để chứng minh khả năng nạp; phải thử kết nối/nạp/debug |
| CT1 DL-CT08CL6-1000/1 | Cảm biến ngoài PCB, tính tỷ số và burden ở 2.3; bộ tải lab một/hai/ba R 50 Ω tại 12 VAC cho dòng dự kiến 0,24/0,48/0,72 A | Tỷ số 1000:1 chưa xác nhận bằng datasheet hãng. Mức 5 A ở 2.3 là mốc tính PCB, không phải dải đã thử; cần đo và đối chiếu tải thứ cấp cho phép |
| USB–RS485 CH340 | Kết nối bus A/B với USB laptop để lưu dữ liệu, lấy nguồn từ USB | Không nối nguồn 5 V USB song song adapter. Chưa chốt mã bộ chuyển đổi nên chưa gán dòng tiêu thụ, tốc độ hoặc khả năng cách ly. Kiểm bias/kết thúc có sẵn và thử truyền theo cấu hình thực |

**Kết luận lựa chọn:** thiết bị ngoài bo được chọn theo chức năng và khả năng tương thích. Chỉ adapter và mô hình CT có phép tính định lượng với dữ liệu hiện có; ST-Link/USB–RS485 phải xác nhận bằng tài liệu đúng thiết bị và thử thực tế, không tự đặt thông số để chứng minh.

## 3. Quy ước và phần cần xác nhận

- **0805, 1206:** kích thước package theo hệ inch; không phải giá trị điện trở/điện dung. Chọn để thuận tiện lắp prototype; kiểm tra định mức của mã thực.
- **X7R:** chọn cho tụ nguồn/lọc thông thường; điện dung hữu dụng có thể giảm khi có điện áp DC.
- **C0G/NP0:** chọn cho tụ tải thạch anh và tụ hồi tiếp nhỏ vì độ ổn định điện dung.
- **Điện trở 1%:** hạn chế sai lệch giá trị; không đồng nghĩa toàn hệ thống có sai số 1%.
- Chốt mã linh kiện thực trước khi hoàn thiện BOM/footprint. Ưu tiên đo: **nguồn → BIAS → dòng → quang → RS485**. Chỉ kết luận độ trễ và khả năng phát hiện sau khi có thuật toán và kết quả kiểm thử.

### 3.1. Đưa kết quả test module vào quyết định PCB

Trước khi chốt giá trị/footprint, điền số đo của cấu hình module cuối cùng từ file 1. Không thay số đo bằng mốc tính hoặc giới hạn datasheet.

| Hạng mục | Ghi từ kết quả module | Quyết định cho PCB |
|---|---|---|
| Nguồn và BIAS | Điện áp 5 V/3,3 V, BIAS không tải/có tải, điều kiện đo | Chốt nguồn vào, LDO, tụ và kiểm tra nhiệt theo đúng IC PCB |
| CT/burden | CT thực; so sánh 47 Ω với 150 Ω ở cùng dòng sơ cấp thực; ghi BIAS, min/max trước/sau lọc, dạng sóng và clipping | Giữ R2 PCB = 150 Ω, 1% nếu đáp ứng mục tiêu và còn headroom; điện trở 47 Ω, 5%/0,25 W chỉ là tải thử trên module. Nếu dữ liệu thiếu thì ghi rõ chưa xác nhận |
| RC dòng | Cấu hình R3/C12, tần số hoặc dạng sóng vào/ra, suy giảm quan sát được | Chốt lọc theo băng thông cần giữ và tốc độ lấy mẫu; không suy ra băng thông chỉ từ fs |
| Photodiode/TIA và lọc quang | BPW34, Rf/Cf, điều kiện chiếu/che; nếu có, so đầu ra TIA với PA1 khi nối thẳng và khi qua hai tầng RC; ghi suy giảm đỉnh/nhiễu/đáp ứng xung | Chốt VBPW34S, R6/C15 và giữ hai tầng RC PCB như cấu hình thiết kế ban đầu hoặc ghi lý do đánh giá lại; số đo module không thay phép đo xác nhận trên PCB |
| ADC/lấy mẫu | Kênh, fs thực, `T_sampling` thực, số mẫu, mức min/max | Xác nhận STM32/AFE PCB đáp ứng; fs và `T_sampling` phải ghi riêng cho CT và quang |
| RS485/tích hợp | Cấu hình UART, thời gian chạy, lỗi/reset/sụt nguồn | Chốt U5 và các phần bus theo topology thực, không mặc định lắp termination/bias tùy chọn |

Khi chưa có số đo, dùng giá trị trong BOM như lựa chọn thiết kế ban đầu, không ghi là đã được kiểm chứng. Sau khi đổi linh kiện trên PCB, đánh dấu đó là cấu hình mới và thử lại sau khi hàn.

### 3.2. Kiểm tra linh kiện thực tế và xác định footprint

| Hạng mục | Phải xác nhận |
|---|---|
| C1 | Tantalum 10 µF (106)–16 V, dự kiến 3528; xác nhận mã hãng, package/footprint, dung sai và ESR; phân cực/pad |
| C2 | Tantalum 22 µF (226)–16 V, 6032; mã hãng, dung sai và ESR cần xác nhận theo tụ thực |
| J1 | Jack thực nhãn 1 = +DC, 2 = −DC; xác nhận chân 3, lỗ tâm và footprint |
| U1 | LD1117S33TR SOT-223; symbol chân 4 đại diện tab OUT, cùng net +3V3 với chân 2 |
| Y1 | Đúng ABM3B-8.000MHZ-B2-T, CL 18 pF và bản vẽ pad; không chọn chỉ theo 8 MHz/5032 |
| D1 | Đúng VBPW34S và footprint gullwing; khác BPW34 chân cắm của module |
| U3/U4 | Hai IC MCP6002-I/SN SOIC-8 riêng, dùng 3,3 V; khác DIP-8 module |
| U5 | MAX3485ESA+ 3,3 V; không mua thay bằng TTL485-V2.0 5 V tự chuyển chiều |
| R8–R10 | Quyết định theo vị trí đầu cuối và bias đã có trên toàn bus/USB–RS485 |
| BT1 | Nút RESET 2 chân SMD 3 × 6 × 2,5 mm, thường hở, nhấn nhả; xác nhận mã hãng, kích thước/khoảng cách pad và ánh xạ symbol–pad theo nút thực |
| P1 | Terminal 2 cực, bước 5,08 mm; kiểm kích thước thực; Phoenix 1715721 là phương án tham khảo |
| J2 | Terminal 3 cực, bước 5,08 mm; xác nhận kích thước và footprint thực, Phoenix 1715734 là phương án tham khảo; giữ 1 = A, 2 = B, 3 = GND |

## 4. Tài liệu đối chiếu

| Linh kiện / nội dung | Nguồn hãng |
|---|---|
| STM32F103C8T6 | [ST DS5319 — thông số, sơ đồ chân, ADC và dòng tiêu thụ](https://www.st.com/resource/en/datasheet/stm32f103c8.pdf) |
| Nguồn/reset MCU | [ST AN2586 — hướng dẫn thiết kế phần cứng](https://www.st.com/resource/en/application_note/an2586-stm32-hardware-design-guidelines-stmicroelectronics.pdf) |
| Thạch anh/tụ tải | [ST AN2867](https://www.st.com/resource/en/application_note/an2867-oscillator-design-guide-for-stm8afals-stm32-mcus-and-mpus-stmicroelectronics.pdf) · [Abracon ABM3B](https://abracon.com/Resonators/abm3b.pdf) |
| LD1117S33TR | [ST LD1117 — đầu ra, tụ ổn định và nhiệt trở](https://www.st.com/resource/en/datasheet/ld1117.pdf) |
| MCP6002 | [Microchip MCP6002 — datasheet và đặc tính op-amp](https://www.microchip.com/en-us/product/MCP6002) |
| VBPW34S | [Vishay Document 81128 — đặc tính quang và package](https://www.vishay.com/docs/81128/vbpw34s.pdf) |
| MAX3485 | [ADI MAX3483–MAX3491 — nguồn, mức logic và ngưỡng nhận](https://www.analog.com/media/en/technical-documentation/data-sheets/MAX3483-MAX3491.pdf) |
| Kết thúc/bias RS485 | [TI SLLA272 — RS-485 Design Guide](https://www.ti.com/lit/an/slla272d/slla272d.pdf) |

| Phương pháp đo / yêu cầu thiết bị | Nguồn tiêu chuẩn |
|---|---|
| Chất lượng điện AC 50/60 Hz | [IEC 61000-4-30:2025](https://webstore.iec.ch/en/publication/71611) |
| Đo sóng hài/liên hài đến 9 kHz | [IEC 61000-4-7](https://webstore.iec.ch/en/publication/4226) |
| Yêu cầu chung cho thiết bị rơ-le/bảo vệ | [IEC 60255-1:2022](https://webstore.iec.ch/en/publication/59762) |
| EMC và an toàn cho thiết bị rơ-le/bảo vệ | [IEC 60255-26:2023](https://webstore.iec.ch/en/publication/62084) · [IEC 60255-27:2023](https://webstore.iec.ch/en/publication/63370) |

Nguồn đối chiếu mã điện trở/tụ và đầu nối: [Vishay CRCW](https://www.vishay.com/docs/20035/dcrcwe3.pdf), [KEMET C0805C270J5GACTU](https://search.kemet.com/download/specsheet/C0805C270J5GACTU), [Phoenix 1715721](https://www.phoenixcontact.com/en-be/products/pcb-terminal-block-mkds-15-2-508-1715721).

CT, adapter, jack và tụ mua thực chưa đủ mã/datasheet để khẳng định toàn bộ thông số hãng. Những phép tính dựa trên giả thiết đã ghi rõ tại từng khối.

**Tiến độ:** nguồn mới được kiểm tra trực quan kết nối; chưa kiểm thử thực hoặc hoàn tất ERC/footprint. Đang làm MCU và SWD theo file 3. Chưa hoàn thiện sơ đồ khối và phần giải thích chức năng/vị trí các khối cho thuyết minh. SS14, SM712, LED và buzzer không thuộc danh sách lắp hiện hành.
