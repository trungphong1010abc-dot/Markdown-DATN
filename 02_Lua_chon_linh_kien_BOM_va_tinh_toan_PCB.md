# Lựa chọn linh kiện, BOM mua hàng và tính toán PCB

**Đề tài:** Thiết kế hệ thống nhúng IoT phát hiện sớm chớp hồ quang điện trong hệ thống điện hạ áp và trung áp.

Thu dòng và ánh sáng → STM32 → RS485 → laptop/gateway. Phát hiện nhanh khi dấu hiệu xuất hiện, không dự báo. Hạ áp có thử nghiệm; trung áp chỉ phân tích ứng dụng. Không có mạch ngắt tải, LED hoặc buzzer.

Tài liệu dùng chung cho lựa chọn linh kiện, BOM mua hàng và tính toán. Bảng mua chia theo khối ở mục 1; lý do và phép tính chi tiết ở các mục sau. Cách nối chân và net xem [file 03](03_Huong_dan_noi_chan_va_thiet_ke_schematic_Altium.md).

**Quy ước:** thông số hãng = theo datasheet; giá trị chọn = thiết kế; giả thiết/ước lượng = chưa xác nhận; kết quả đo = chỉ ghi sau kiểm thử. “Chốt bảng linh kiện” không có nghĩa mọi mã mua/ESR/footprint đã được xác nhận.

## 1. Bảng linh kiện và danh sách mua dùng chung

Các bảng dưới đây gộp lựa chọn linh kiện và BOM **theo từng khối**; linh kiện cùng giá trị được tách theo vị trí sử dụng để dễ đọc. SL là số lượng cho một PCB; adapter, ST-Link, CT và USB–RS485 là thiết bị ngoài bo. R8–R10 là vị trí tùy chọn, không mặc định lắp toàn bộ.

Các link Shopee là **link tìm kiếm**, chưa xác minh shop, giá hoặc tồn kho. Đối chiếu đúng mã, dung sai, định mức và package trước khi mua. Mã nút RESET SW1 và footprint còn phải chốt theo nút thực.

### 1.1. Khối nguồn

| Mã | Linh kiện / giá trị / mã hãng | Package | SL | Lý do chọn / lưu ý | Tên tìm Shopee | Link Shopee |
|---|---|---|---:|---|---|---|
| J1 | Jack DC cái: 5,5 mm (tham khảo PJ-102AH) | THT | 1 | Phù hợp phích adapter; xác nhận lỗ tâm, chân và footprint theo jack thực | jack dc 5.5mm cái hàn PCB | [Tìm trên Shopee](https://shopee.vn/search?keyword=jack%20dc%205.5mm%20c%C3%A1i%20h%C3%A0n%20PCB) |
| U1 | LDO: LD1117S33TR, 3,3 V; tới 800 mA, còn phụ thuộc nhiệt | SOT-223 | 1 | Hạ 5 V xuống 3,3 V; dòng dùng được còn phụ thuộc nhiệt | LD1117S33TR SOT-223 | [Tìm trên Shopee](https://shopee.vn/search?keyword=LD1117S33TR%20SOT-223) |
| C1 | Tụ tantalum: 10 µF, 16 V | 3528 (B case) | 1 | Tụ đầu vào; có phân cực | tụ tantalum 10uF 16V 3528 SMD | [Tìm trên Shopee](https://shopee.vn/search?keyword=t%E1%BB%A5%20tantalum%2010uF%2016V%203528) |
| C2 | Tụ tantalum: 22 µF, 16 V | 6032 (C case) | 1 | Tụ đầu ra; có phân cực; chọn điện dung cao hơn mức tối thiểu 10 µF nêu trong datasheet LD1117 | tụ tantalum 22uF 16V 6032 SMD | [Tìm trên Shopee](https://shopee.vn/search?keyword=t%E1%BB%A5%20tantalum%2022uF%2016V%206032) |

### 1.2. Khối MCU

| Mã | Linh kiện / giá trị / mã hãng | Package | SL | Lý do chọn / lưu ý | Tên tìm Shopee | Link Shopee |
|---|---|---|---:|---|---|---|
| U2 | MCU: STM32F103C8T6; 72 MHz; Flash 64 KB; SRAM 20 KB; 2,0–3,6 V | LQFP-48 | 1 | Có ADC 12 bit, UART, DMA và SWD để đọc cảm biến, xử lý và truyền dữ liệu | STM32F103C8T6 LQFP48 | [Tìm trên Shopee](https://shopee.vn/search?keyword=STM32F103C8T6%20LQFP48) |
| C3–C5 | Tụ gốm: 100 nF (104), X7R, 16 V | 0805 | 3 | Một tụ 100 nF cho mỗi chân VDD MCU | tụ gốm 100nF 0805 X7R 16V | [Tìm trên Shopee](https://shopee.vn/search?keyword=t%E1%BB%A5%20g%E1%BB%91m%20100nF%200805%20X7R) |
| C6 | Tụ gốm: 10 µF, X7R, 16 V | 0805 | 1 | Tụ nguồn tổng MCU | tụ gốm 10uF 0805 X7R 16V | [Tìm trên Shopee](https://shopee.vn/search?keyword=t%E1%BB%A5%20g%E1%BB%91m%2010uF%200805%20X7R) |
| C7 | Tụ gốm: 100 nF (104), X7R, 16 V | 0805 | 1 | Lọc nguồn VDDA, phối hợp C8 1 µF | tụ gốm 100nF 0805 X7R 16V | [Tìm trên Shopee](https://shopee.vn/search?keyword=t%E1%BB%A5%20g%E1%BB%91m%20100nF%200805%20X7R) |
| C8 | Tụ gốm: 1 µF, X7R, 16 V | 0805 | 1 | Lọc nguồn VDDA phục vụ ADC | tụ gốm 1uF 0805 X7R 16V | [Tìm trên Shopee](https://shopee.vn/search?keyword=t%E1%BB%A5%20g%E1%BB%91m%201uF%200805%20X7R) |
| Y1 | Thạch anh: ABM3B-8.000MHZ-B2-T, 8 MHz; CL = 18 pF | 5,0 × 3,2 mm | 1 | Nguồn clock ngoài; có thể cấu hình PLL ×9 để đạt 72 MHz | thạch anh 8MHz 5032 SMD | [Tìm trên Shopee](https://shopee.vn/search?keyword=th%E1%BA%A1ch%20anh%208MHz%205032%20SMD) |
| C9, C10 | Tụ gốm: 27 pF, ±5 %, C0G, 50 V (C0805C270J5GACTU) | 0805 | 2 | Tụ tải cho đúng mã Y1 | tụ gốm 27pF 0805 C0G NPO | [Tìm trên Shopee](https://shopee.vn/search?keyword=t%E1%BB%A5%20g%E1%BB%91m%2027pF%200805%20C0G) |
| R1 | Điện trở: 10 kΩ, 1 %, 0,125 W | 0805 | 1 | Kéo BOOT0 xuống để khởi động từ Flash | điện trở 10K 0805 1% | [Tìm trên Shopee](https://shopee.vn/search?keyword=%C4%91i%E1%BB%87n%20tr%E1%BB%9F%2010K%200805%201%25) |
| C11 | Tụ gốm: 100 nF (104), X7R, 16 V | 0805 | 1 | Tụ NRST theo cấu hình reset | tụ gốm 100nF 0805 X7R 16V | [Tìm trên Shopee](https://shopee.vn/search?keyword=t%E1%BB%A5%20g%E1%BB%91m%20100nF%200805%20X7R) |
| SW1 | Nút nhấn RESET: Thường hở, nhấn nhả, 2 tiếp điểm; mã hãng chưa chốt | SMD, footprint cần xác nhận | 1 | Khởi động lại MCU thuận tiện khi chạy thử; mã hãng và footprint cần xác nhận theo nút thực | nút nhấn reset SMD thường hở | [Tìm trên Shopee](https://shopee.vn/search?keyword=nut%20nhan%20reset%20SMD%20thuong%20ho) |
| J2 | Header SWD: 1×5, bước 2,54 mm | Header | 1 | Đưa ra 3V3, GND, SWDIO, SWCLK và NRST | header đực 1x5 2.54mm | [Tìm trên Shopee](https://shopee.vn/search?keyword=header%20%C4%91%E1%BB%B1c%201x5%202.54mm) |

### 1.3. Khối dòng

| Mã | Linh kiện / giá trị / mã hãng | Package | SL | Lý do chọn / lưu ý | Tên tìm Shopee | Link Shopee |
|---|---|---|---:|---|---|---|
| J3 | Terminal 2 cực: Bước 5,08 mm (Phoenix 1715721) | THT | 1 | Kết nối thứ cấp CT | terminal 2 chân 5.08mm hàn PCB | [Tìm trên Shopee](https://shopee.vn/search?keyword=terminal%202%20ch%C3%A2n%205.08mm%20h%C3%A0n%20PCB) |
| U3 | Op-amp: MCP6002-I/SN; nguồn hãng 1,8–6,0 V; GBW điển hình 1 MHz | SOIC-8 | 1 | Cấp 3,3 V; một kênh đệm dòng, một kênh đệm BIAS | MCP6002 SOIC-8 | [Tìm trên Shopee](https://shopee.vn/search?keyword=MCP6002%20SOIC-8) |
| R2 | Điện trở: 150 Ω, 1 %, 0,125 W (CRCW0805150RFKEA) | 0805 | 1 | Burden chuyển dòng thành áp; 150 Ω là giá trị ban đầu để kiểm thử | điện trở 150R 0805 1% | [Tìm trên Shopee](https://shopee.vn/search?keyword=%C4%91i%E1%BB%87n%20tr%E1%BB%9F%20150R%200805%201%25) |
| R3, R4 | Điện trở: 10 kΩ, 1 %, 0,125 W | 0805 | 2 | Cầu chia tạo BIAS danh định 1,65 V | điện trở 10K 0805 1% | [Tìm trên Shopee](https://shopee.vn/search?keyword=%C4%91i%E1%BB%87n%20tr%E1%BB%9F%2010K%200805%201%25) |
| C12 | Tụ gốm: 100 nF (104), X7R, 16 V | 0805 | 1 | Tụ nguồn U3 | tụ gốm 100nF 0805 X7R 16V | [Tìm trên Shopee](https://shopee.vn/search?keyword=t%E1%BB%A5%20g%E1%BB%91m%20100nF%200805%20X7R) |
| R5 | Điện trở: 1 kΩ, 1 %, 0,125 W | 0805 | 1 | Cùng C13 tạo lọc trước ADC | điện trở 1K 0805 1% | [Tìm trên Shopee](https://shopee.vn/search?keyword=%C4%91i%E1%BB%87n%20tr%E1%BB%9F%201K%200805%201%25) |
| C13 | Tụ gốm: 100 nF (104), X7R, 16 V | 0805 | 1 | Phối hợp R5 tạo lọc trước ADC dòng | tụ gốm 100nF 0805 X7R 16V | [Tìm trên Shopee](https://shopee.vn/search?keyword=t%E1%BB%A5%20g%E1%BB%91m%20100nF%200805%20X7R) |

### 1.4. Khối quang

| Mã | Linh kiện / giá trị / mã hãng | Package | SL | Lý do chọn / lưu ý | Tên tìm Shopee | Link Shopee |
|---|---|---|---:|---|---|---|
| D1 | Photodiode: VBPW34S | SMD gullwing | 1 | Thu ánh sáng; phù hợp lắp SMD; dùng footprint đúng biến thể Vishay | VBPW34S photodiode SMD | [Tìm trên Shopee](https://shopee.vn/search?keyword=VBPW34S%20photodiode%20SMD) |
| U4 | Op-amp: MCP6002-I/SN; nguồn hãng 1,8–6,0 V; GBW điển hình 1 MHz | SOIC-8 | 1 | IC riêng cấp 3,3 V; chuyển dòng quang thành áp, kênh còn lại không cấp tải ngoài | MCP6002 SOIC-8 | [Tìm trên Shopee](https://shopee.vn/search?keyword=MCP6002%20SOIC-8) |
| R6 | Điện trở: 10 kΩ, 1 %, 0,125 W | 0805 | 1 | Điện trở hồi tiếp; chọn ban đầu để khảo sát độ nhạy | điện trở 10K 0805 1% (gộp tổng 5 chiếc) | [Tìm trên Shopee](https://shopee.vn/search?keyword=dien%20tro%2010K%200805%201%25) |
| C15 | Tụ gốm: 100 pF, ±5 %, C0G/NP0, ≥ 16 V | 0805 | 1 | Hồi tiếp song song R6 để hỗ trợ ổn định; giá trị cần kiểm chứng | tụ gốm 100pF 0805 C0G NPO | [Tìm trên Shopee](https://shopee.vn/search?keyword=t%E1%BB%A5%20g%E1%BB%91m%20100pF%200805%20C0G) |
| C14 | Tụ gốm: 100 nF (104), X7R, 16 V | 0805 | 1 | Tụ nguồn U4 | tụ gốm 100nF 0805 X7R 16V | [Tìm trên Shopee](https://shopee.vn/search?keyword=t%E1%BB%A5%20g%E1%BB%91m%20100nF%200805%20X7R) |

### 1.5. Khối truyền thông

| Mã | Linh kiện / giá trị / mã hãng | Package | SL | Lý do chọn / lưu ý | Tên tìm Shopee | Link Shopee |
|---|---|---|---:|---|---|---|
| U5 | RS485: MAX3485ESA+; 3,0–3,6 V; tới 10 Mbps | SOIC-8 | 1 | Chuyển UART 3,3 V sang RS485 bán song công; 10 Mbps là khả năng IC, chưa phải baudrate hệ thống | MAX3485 SOIC-8 | [Tìm trên Shopee](https://shopee.vn/search?keyword=MAX3485%20SOIC-8) |
| C16 | Tụ gốm: 100 nF (104), X7R, 16 V | 0805 | 1 | Tụ nguồn U5 | tụ gốm 100nF 0805 X7R 16V | [Tìm trên Shopee](https://shopee.vn/search?keyword=t%E1%BB%A5%20g%E1%BB%91m%20100nF%200805%20X7R) |
| R7 | Điện trở: 10 kΩ, 1 %, 0,125 W | 0805 | 1 | Kéo chung DE và /RE xuống thấp, mặc định nhận | điện trở 10K 0805 1% | [Tìm trên Shopee](https://shopee.vn/search?keyword=%C4%91i%E1%BB%87n%20tr%E1%BB%9F%2010K%200805%201%25) |
| J4 | Terminal 3 cực A/B/GND, bước 5,08 mm; tham khảo Phoenix 1715734 | THT | 1 | Đấu dây cáp RS485; giữ thứ tự chân A/B/GND | terminal 3 chân 5.08mm hàn PCB | [Tìm trên Shopee](https://shopee.vn/search?keyword=terminal%203%20chan%205.08mm%20han%20PCB) |
| R8 | Điện trở: 120 Ω, 1 %, 0,25 W | 1206 | 1 | Kết thúc đường truyền dùng cáp 120 Ω; lắp theo vị trí đầu cuối; Vị trí tùy chọn DNP, lắp theo cấu hình bus | điện trở 120R 1206 1% | [Tìm trên Shopee](https://shopee.vn/search?keyword=%C4%91i%E1%BB%87n%20tr%E1%BB%9F%20120R%201206%201%25) |
| R9, R10 | Điện trở: 330 Ω, 1 %, 0,125 W | 0805 | 2 | Tạo mức nghỉ; lắp theo cấu hình bias của toàn bus; Vị trí tùy chọn DNP, lắp theo cấu hình bus | điện trở 330R 0805 1% | [Tìm trên Shopee](https://shopee.vn/search?keyword=%C4%91i%E1%BB%87n%20tr%E1%BB%9F%20330R%200805%201%25) |

### 1.6. Thiết bị ngoài PCB

| Mã | Linh kiện / giá trị / mã hãng | Package | SL | Lý do chọn / lưu ý | Tên tìm Shopee | Link Shopee |
|---|---|---|---:|---|---|---|
| — | Adapter: 5 VDC–2 A, jack 5,5/2,1 mm | Ngoài PCB | 1 | Nguồn cách ly cấp mạch; 2 A là khả năng cấp, xác nhận phích phù hợp jack thực | adapter 5V 2A jack 5.5mm | [Tìm trên Shopee](https://shopee.vn/search?keyword=adapter%205V%202A%20jack%205.5mm) |
| — | ST-Link V2: Nạp STM32 | Ngoài PCB | 1 | Nạp/debug qua SWD, không cấp song song nguồn adapter | ST-Link V2 STM32 | [Tìm trên Shopee](https://shopee.vn/search?keyword=ST-Link%20V2%20STM32) |
| CT1 | CT: DL-CT08CL6-1000/1 | Ngoài PCB | 1 | Thu dòng AC; tỷ số tính toán tạm lấy 1000:1, chưa xác nhận bằng tài liệu hãng | biến dòng CT DL-CT08CL6 | [Tìm trên Shopee](https://shopee.vn/search?keyword=bi%E1%BA%BFn%20d%C3%B2ng%20CT%20DL-CT08CL6) |
| — | USB–RS485: CH340, lấy nguồn USB | Ngoài PCB | 1 | Giao tiếp laptop; lấy nguồn USB riêng | USB RS485 CH340 | [Tìm trên Shopee](https://shopee.vn/search?keyword=USB%20RS485%20CH340) |

**Tổng mua theo giá trị:** điện trở 10 kΩ gồm R1/R3/R4/R6/R7: 5 chiếc; tụ 100 nF 0805: 9 chiếc. Các dòng trong bảng là các vị trí riêng, không cộng lại lần nữa theo phần tính toán bên dưới. Linh kiện mua dự phòng chưa tính vào SL.

## 2. Căn cứ lựa chọn và tính toán theo từng khối

Các mục 2.1–2.6 tương ứng lần lượt với bảng linh kiện 1.1–1.6. Phép tính kiểm tra điều kiện thiết kế theo giả thiết đã ghi; chưa thay thế datasheet linh kiện thực hoặc kết quả thử nghiệm.

### 2.1. Khối nguồn

**Lý do chọn:** adapter 5 V kết hợp LD1117S33TR tạo nguồn 3,3 V chung cho MCU, hai MCP6002 và MAX3485. LDO đầu ra cố định giúp mạch đơn giản; C1 hỗ trợ đầu vào, C2 phục vụ ổn định đầu ra. J1 chọn theo phích adapter thực, chưa chốt model jack.

#### 2.1.1. Công suất và nhiệt

**Kiểm tra chính:** tổng dòng phân bổ ban đầu khoảng **142 mA**; chọn **200 mA** làm mức kiểm tra nguồn. Cả hai là giá trị thiết kế, phải đo lại. Với đầu vào giả thiết 5,25 V, đầu ra 3,235 V và dòng riêng LDO dự toán 10 mA:

$$P_{U1}\approx(5,25-3,235)\times0,2+5,25\times0,01=0,456\ \mathrm{W}$$

Với nhiệt trở tham khảo 110°C/W và môi trường giả thiết 40°C, nhiệt độ mối nối ước lượng khoảng **90°C**; kết quả phụ thuộc tản nhiệt PCB. Cần đánh giá nhiệt thực khi có tải.

**Cần xác nhận:** mã và ESR/dung sai của C1/C2, độ ổn định đầu ra LDO, điện áp adapter dưới tải. Chưa gán ESR hoặc dung sai cho C2 khi chưa xác nhận đúng mã tụ thực. Tiếp điểm jack thực chưa xác nhận; không coi model PJ-102AH là jack đã chốt. Chi tiết nối hiện hành xem file 03.


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

C1 chọn tantalum 10 µF–16 V, 3528; định mức áp có dự phòng với 5,25 V. C2 chọn tantalum 22 µF–16 V, 6032; datasheet LD1117 nêu tối thiểu 10 µF đầu ra. **Chưa xác nhận dung sai C2 nên chưa chốt điện dung nhỏ nhất.** Nếu *giả thiết* ±10% thì 22 × 0,9 = 19,8 µF; chỉ là kiểm tra có điều kiện. C1 trong bảng cũ ghi ±10%, nay xem là yêu cầu lựa chọn cần đối chiếu mã thực. ESR và ổn định LDO phải kiểm tra theo đúng tụ mua; không mặc định mã tụ 16 V cũ là mã đã chốt cho C2 hiện tại.

### 2.2. Khối MCU

**Tụ tải thạch anh:** với hai tụ bằng nhau và điện dung ký sinh **giả thiết** 4,5 pF:

$$C_X=2(C_L-C_s)=2(18-4,5)=27\ \mathrm{pF}$$

**Lý do chọn:** MCU có ADC, DMA, UART và SWD phù hợp thu hai kênh, xử lý và truyền dữ liệu. Nguồn clock 8 MHz có thể nhân PLL ×9; chưa tự chứng minh thời gian phát hiện của hệ thống.

**Kiểm tra R1:** với 3,3 V và 10 kΩ, công suất 3,3²/10000 ≈ 1,1 mW, thấp hơn định mức chọn 125 mW. Tụ nguồn theo hướng dẫn AN2586: 100 nF cho từng VDD, 100 nF + 1 µF cho VDDA, tụ tổng 10 µF. C11 100 nF phục vụ reset; MCU có kéo lên NRST bên trong.

**SW1 RESET:** nút nhấn thường hở để chủ động reset MCU khi chạy thử, không phải ngắt nguồn toàn mạch. Giữ C11 và cấu hình kéo lên NRST bên trong MCU; không bổ sung điện trở kéo ngoài trong lần cập nhật này. Cách nối xem mục 3.6 file 03; chốt mã nút, kích thước và footprint theo datasheet linh kiện thực. Không thêm nút BOOT; R1 kéo BOOT0 xuống GND giữ nguyên.

**Cần xác nhận:** khởi động thạch anh, dòng tiêu thụ, cấu hình lấy mẫu và hiệu năng thuật toán. Thông số MCU chưa tự chứng minh thời gian phát hiện. Tụ C6 cần đủ điện dung hữu dụng tại 3,3 V.

### 2.3. Khối dòng

**Lý do chọn:** CT1 thu dòng AC, J3 đưa thứ cấp vào PCB, R2 chuyển dòng thành áp; U3 đệm tín hiệu và BIAS; R5/C13 lọc trước ADC. MCP6002 làm việc được ở nguồn thiết kế 3,3 V, nhưng GBW điển hình 1 MHz không tự chứng minh băng thông của cả nhánh. C12 100 nF lọc nguồn tại IC. Burden 150 Ω là phương án ban đầu cần đối chiếu đúng CT.

**BIAS:** hai điện trở R3/R4 cùng 10 kΩ tạo mức danh định 3,3 × 10/(10 + 10) = **1,65 V**; dòng cầu chia 3,3/20 kΩ = **0,165 mA**. Kênh đệm của U3 giúp hạn chế ảnh hưởng tải lên cầu chia; mức và khả năng cấp dòng BIAS phải kiểm tra thực. U3 và U4 là hai MCP6002 riêng, cùng dùng nguồn 3,3 V.

**Kiểm tra burden:** với dòng sơ cấp thiết kế **5 A RMS**, tỷ số **giả thiết 1000:1**, mô hình CT tuyến tính và dòng hình sin:

$$I_S=5/1000=5\ \mathrm{mA};\qquad V_{B,\mathrm{RMS}}=0,005\times150=0,75\ \mathrm{V}$$

$$P_{R2}=0,005^2\times150=3,75\ \mathrm{mW}<125\ \mathrm{mW}$$

Đỉnh tín hiệu khoảng 1,061 V; quanh BIAS 1,65 V được khoảng **0,589–2,711 V**, nằm trong nguồn 3,3 V theo mô hình lý tưởng. Đây là kiểm tra biên áp/công suất, chưa chứng minh CT làm việc chính xác với burden 150 Ω.

**Bộ lọc:** R5 = 1 kΩ và C13 = 100 nF cho:

$$f_c=\frac{1}{2\pi RC}\approx1,59\ \mathrm{kHz}$$

**Cần xác nhận:** tỷ số, tải thứ cấp cho phép và tuyến tính CT; BIAS; dải tần cần giữ cho thuật toán. Chưa có yêu cầu băng thông thì chưa khẳng định 1,59 kHz là tối ưu. Mức 5 A là mốc tính thiết kế PCB, không phải dải đã thử ở lab và không đại diện dòng sự cố trong tủ LV/MV.

### 2.4. Khối quang

**Lý do chọn:** D1 VBPW34S thu ánh sáng, dùng biến thể SMD đúng footprint; U4 MCP6002 là IC riêng cấp 3,3 V. R6 xác định hệ số chuyển dòng–áp, C15 hỗ trợ ổn định hồi tiếp; C14 100 nF lọc nguồn. Chưa có dữ liệu dòng quang nên R6/C15 là lựa chọn khảo sát, chưa chứng minh tối ưu.

Nhánh quang dùng TIA tham chiếu BIAS danh định 1,65 V. Với cực tính thiết kế hiện hành, mô hình lý tưởng là:

$$V_{OUT}\approx V_{BIAS}+I_{photo}R6$$

R6 = 10 kΩ tạo hệ số lý tưởng **10 mV/µA**. Dải dòng quang hữu dụng phụ thuộc biên ra op-amp và ánh sáng nền.

**Cần xác nhận:** độ nhạy, bão hòa, đáp ứng xung và dao động AFE với cặp 10 kΩ–100 pF. Chưa có dữ liệu dòng quang thực nên chưa thể chứng minh R6/C15 tối ưu hoặc xác định khoảng cách phát hiện. Kênh op-amp còn lại không cấp tải ngoài; chi tiết cấu hình xem file 03.

### 2.5. Khối truyền thông

**Lý do chọn:** MAX3485 dùng nguồn 3,3 V, phù hợp giao tiếp UART MCU; J4 đưa A/B/GND ra cáp. R7 10 kΩ đặt trạng thái mặc định nhận, C16 100 nF lọc nguồn. R8 kết thúc bus, R9/R10 tạo bias khi toàn bus cần; không mặc định lắp cả ba. Khả năng 10 Mbps của IC chưa phải baudrate được chọn cho hệ thống.

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
| ST-Link V2 | Được chọn để nạp/debug SWD; header J2 đưa ra nguồn tham chiếu, GND, SWDIO, SWCLK và NRST | Kiểm chức năng chân của đầu nạp thực, đặc biệt VTref và chân cấp nguồn; không cấp song song với adapter. Không có phép tính công suất để chứng minh khả năng nạp; phải thử kết nối/nạp/debug |
| CT1 DL-CT08CL6-1000/1 | Cảm biến ngoài PCB, tính tỷ số và burden ở 2.3; bộ tải lab một/hai/ba R 50 Ω tại 12 VAC cho dòng dự kiến 0,24/0,48/0,72 A | Tỷ số 1000:1 chưa xác nhận bằng datasheet hãng. Mức 5 A ở 2.3 là mốc tính PCB, không phải dải đã thử; cần đo và đối chiếu tải thứ cấp cho phép |
| USB–RS485 CH340 | Kết nối bus A/B với USB laptop để lưu dữ liệu, lấy nguồn từ USB | Không nối nguồn 5 V USB song song adapter. Chưa chốt mã bộ chuyển đổi nên chưa gán dòng tiêu thụ, tốc độ hoặc khả năng cách ly. Kiểm bias/kết thúc có sẵn và thử truyền theo cấu hình thực |

**Kết luận lựa chọn:** thiết bị ngoài bo được chọn theo chức năng và khả năng tương thích. Chỉ adapter và mô hình CT có phép tính định lượng với dữ liệu hiện có; ST-Link/USB–RS485 phải xác nhận bằng tài liệu đúng thiết bị và thử thực tế, không tự đặt thông số để chứng minh.

## 3. Quy ước và phần cần xác nhận

- **0805, 1206:** kích thước package theo hệ inch; không phải giá trị điện trở/điện dung. Chọn để thuận tiện lắp prototype; kiểm tra định mức của mã thực.
- **X7R:** chọn cho tụ nguồn/lọc thông thường; điện dung hữu dụng có thể giảm khi có điện áp DC.
- **C0G/NP0:** chọn cho tụ tải thạch anh và tụ hồi tiếp nhỏ vì độ ổn định điện dung.
- **Điện trở 1%:** hạn chế sai lệch giá trị; không đồng nghĩa toàn hệ thống có sai số 1%.
- Chốt mã linh kiện thực trước khi hoàn thiện BOM/footprint. Ưu tiên đo: **nguồn → BIAS → dòng → quang → RS485**. Chỉ kết luận độ trễ và khả năng phát hiện sau khi có thuật toán và kết quả kiểm thử.

### 3.1. Kiểm trước khi đặt mua/chốt footprint

| Hạng mục | Phải xác nhận |
|---|---|
| C1 | Tantalum 10 µF–16 V, 3528; mã hãng, dung sai và ESR; phân cực/pad |
| C2 | Tantalum 22 µF–16 V, 6032; mã hãng, dung sai và ESR cần xác nhận theo tụ thực |
| J1 | Jack thực nhãn 1 = +DC, 2 = −DC; xác nhận chân 3, lỗ tâm và footprint |
| U1 | LD1117S33TR SOT-223; symbol chân 4 đại diện tab OUT, cùng net +3V3 với chân 2 |
| Y1 | Đúng ABM3B-8.000MHZ-B2-T, CL 18 pF và bản vẽ pad; không chọn chỉ theo 8 MHz/5032 |
| D1 | Đúng VBPW34S và footprint gullwing; khác BPW34 chân cắm của module |
| U3/U4 | Hai IC MCP6002-I/SN SOIC-8 riêng, dùng 3,3 V; khác DIP-8 module |
| U5 | MAX3485ESA+ 3,3 V; không mua thay bằng TTL485-V2.0 5 V tự chuyển chiều |
| R8–R10 | Quyết định theo vị trí đầu cuối và bias đã có trên toàn bus/USB–RS485 |
| SW1 | Nút RESET thường hở, mã hãng/kích thước/footprint và ánh xạ tiếp điểm theo datasheet nút thực |
| J3 | Terminal 2 cực, bước 5,08 mm; kiểm kích thước thực; Phoenix 1715721 là phương án tham khảo |
| J4 | Terminal 3 cực, bước 5,08 mm; xác nhận kích thước và footprint thực, Phoenix 1715734 là phương án tham khảo; giữ 1 = A, 2 = B, 3 = GND |

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

Nguồn đối chiếu mã điện trở/tụ và đầu nối: [Vishay CRCW](https://www.vishay.com/docs/20035/dcrcwe3.pdf), [KEMET C0805C270J5GACTU](https://search.kemet.com/download/specsheet/C0805C270J5GACTU), [Phoenix 1715721](https://www.phoenixcontact.com/en-be/products/pcb-terminal-block-mkds-15-2-508-1715721).

CT, adapter, jack và tụ mua thực chưa đủ mã/datasheet để khẳng định toàn bộ thông số hãng. Những phép tính dựa trên giả thiết đã ghi rõ tại từng khối.

**Tiến độ:** nguồn mới được kiểm tra trực quan kết nối; chưa kiểm thử thực hoặc hoàn tất ERC/footprint. Đang làm MCU và SWD theo file 03. Chưa hoàn thiện sơ đồ khối và phần giải thích chức năng/vị trí các khối cho thuyết minh. SS14, SM712, LED và buzzer không thuộc danh sách lắp hiện hành.
