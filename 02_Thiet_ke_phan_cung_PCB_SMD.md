# Thiết kế phần cứng PCB SMD phát hiện chớp hồ quang điện

## Phạm vi thiết kế

Hệ thống thu nhận tín hiệu dòng điện và ánh sáng, xử lý để phát hiện nhanh dấu hiệu chớp hồ quang, rồi gửi dữ liệu hoặc cảnh báo về laptop qua RS485. Thử nghiệm thực hiện ở hạ áp; trung áp được phân tích về khả năng ứng dụng. Hệ thống thực hiện phát hiện và cảnh báo, không điều khiển đóng cắt tải.

Thiết kế sử dụng PCB hai lớp, ưu tiên linh kiện gắn bề mặt (SMD). AFE là mạch xử lý tín hiệu tương tự trước MCU; ADC chuyển điện áp thành dữ liệu số; package là kiểu vỏ linh kiện. Hệ thống gồm năm khối được trình bày dưới đây.

Thông số hãng được dùng theo điều kiện công bố. Giá trị linh kiện được xác định theo yêu cầu chức năng, điều kiện làm việc và tính toán; các khoản dự trù và kết quả mô hình là đầu vào thiết kế. Những thông số còn để ngỏ được tổng hợp cuối tài liệu.

## Đối chiếu kết nối mô-đun với PCB SMD

Kết nối phần cứng được đối chiếu mục 4.2 của tài liệu người dùng cung cấp. Các giá trị dòng thiết kế và lựa chọn linh kiện PCB được xác định riêng trong tài liệu này.

| Phần mạch | Kết nối mô-đun | Triển khai trên PCB |
|---|---|---|
| Nguồn | Adapter 5 V cấp Blue Pill và TTL485-V2.0; 3V3 Blue Pill cấp hai MCP6002 | Adapter 5 V vào U1 LD1117S33TR; đường 3,3 V cấp MCU, hai MCP6002 và MAX3485 |
| IC dòng/BIAS | MCP6002 U1, DIP-8 | MCP6002 U3, SOIC-8; cùng chức năng và số chân op-amp |
| CT | Đỏ → chân 3 U1; đen → chân 7 U1 (BIAS); burden song song hai dây | Đỏ → J3.1 → U3.3; đen → J3.2 → U3.7; R2 song song J3 |
| Burden | 150 Ω–2 W trên mô-đun | R2 150 Ω, 0,125 W, 0805 theo tính toán thiết kế 5 A; giá trị điện trở giữ cùng mức chuyển đổi |
| Lọc dòng | U1.1 → R 1 kΩ → PA0; tụ 100 nF từ PA0 xuống GND; U1.2 hồi tiếp về U1.1 | U3.1 → R5 → U2.10; C13 xuống GND; U3.2 nối U3.1 trước R5 |
| IC quang | MCP6002 U2 DIP-8 và BPW34 chân cắm | MCP6002 U4 SOIC-8 và VBPW34S SMD |
| Photodiode | K → chân 2 IC quang; A → GND; chân 3 → BIAS | D1.K → U4.2; D1.A → GND; U4.3 → BIAS_1V65 |
| Hồi tiếp quang | Rf 10 kΩ song song Cf 100 pF giữa chân 1–2; đầu ra chân 1 → PA1 | R6 song song C15 giữa U4.1–U4.2; U4.1 → U2.11 |
| Kênh quang còn lại | Chân 5 → BIAS; chân 6–7 nối nhau; đầu ra 7 không cấp tải ngoài | U4.5 → BIAS_1V65; U4.6–U4.7; không nối U4.7 vào U3.7 |
| UART | PA9 → RXD mô-đun; TXD mô-đun → PA10 | PA9 → DI MAX3485; RO MAX3485 → PA10 |
| Chiều truyền | TTL485-V2.0 dùng MAX13487EESA+, 5 V, tự chuyển chiều; PB0/PB1 để trống | MAX3485ESA+, 3,3 V; PB0 nối chung DE và /RE |
| Nạp/debug | ST-Link V2 → PA13, PA14, GND; VTref nếu có theo đầu nạp | J2 đưa ra SWDIO, SWCLK, GND, 3V3 và NRST |

Mã U1/U2 trong sơ đồ mô-đun là hai MCP6002. Mã U1/U2 trên PCB lần lượt là LDO và MCU. Bảng nối PCB dùng tên chân DI/RO theo datasheet MAX3485, tách biệt nhãn TXD/RXD của mô-đun tự chuyển chiều.

# 1. Khối nguồn

## 1.1. Lựa chọn cấu hình nguồn

Dùng **adapter cách ly 5 VDC–2 A → jack DC cái → LD1117S33TR → 3,3 V** cấp cho STM32F103C8T6, hai MCP6002 và MAX3485. Mức 3,3 V phù hợp các IC và đơn giản hóa giao tiếp. Bộ chuyển đổi USB–RS485 lấy nguồn từ USB laptop.

Chọn jack Same Sky PJ-102AH, định mức 24 VDC–5 A, dùng adapter 5 V tâm dương với phích phù hợp trụ tâm Ø2,0 mm của jack. Chọn LD1117S33TR vì có đầu ra cố định 3,3 V và package SOT-223 phù hợp lắp SMD. Việc lựa chọn IC dựa trên hai điều kiện: đủ chênh lệch điện áp để ổn áp và tổn hao nhiệt phù hợp mức tải thiết kế.

## 1.2. Xác định mức tải để kiểm tra LD1117S33TR

Dòng thiết kế nguồn được lấy từ tổng dòng dự trù của các khối. Các khoản phân bổ thiết kế là:

| Nhóm tải | Dòng dự trù | Căn cứ phân bổ |
|---|---:|---|
| STM32F103C8T6 | 60 mA | ST DS5319 Rev 20, mục 5.3.5, Bảng 13 [1]: mốc 50 mA khi chạy Flash ở 72 MHz, bật toàn bộ ngoại vi, môi trường 85°C, chân vào/ra không tải; chọn thêm 20% dự phòng |
| Hai MCP6002 | 2 mA | Mốc dòng tĩnh bốn op-amp là 0,68 mA; dành thêm 1,32 mA cho tải đầu ra và dự phòng |
| MAX3485 và đường truyền | 70 mA | Dự toán sơ bộ 55 mA cho tải kết thúc, 2,2 mA cho IC và 10 mA dành cho bias, tổng 67,2 mA; làm tròn lên |
| Cầu chia BIAS và điện trở kéo | 10 mA | Khoản phân bổ thiết kế gồm dòng các nhánh và dự phòng; bias RS485 tính ở dòng trên |
| **Tổng** | **142 mA** | **60 + 2 + 70 + 10** |

**Căn cứ khoản 2 mA.** Mỗi MCP6002 có hai op-amp, nên hai IC có bốn op-amp được cấp nguồn. Dòng tĩnh là dòng duy trì hoạt động bên trong op-amp. Microchip DS20001733L, mục DC Electrical Characteristics [5] cho mốc tối đa tham khảo 170 µA/op-amp tại nguồn 5,5 V, điện áp đồng pha đầu vào 5 V và dòng tải đầu ra bằng 0:

$$I_{Q,\mathrm{AFE}}=2\times2\times170\ \mu\mathrm{A}=0,68\ \mathrm{mA}$$

Hai hệ số 2 là số IC và số op-amp mỗi IC. Khoản $2-0,68=1,32\ \mathrm{mA}$ dành cho dòng đầu ra cấp tải cùng dự phòng là giả thiết phân bổ thiết kế; mức chốt phụ thuộc tải đầu ra ở nguồn 3,3 V.

**Căn cứ khoản RS485.** Hai điện trở kết thúc 120 Ω tạo tải tương đương 60 Ω (vai trò tại mục 5.2). Dùng 3,3 V làm mốc dự toán được $3,3/60=55\ \mathrm{mA}$. Cộng dòng IC không tải tối đa 2,2 mA khi bật phát theo bảng DC Electrical Characteristics của ADI MAX3485 [7], và khoản bias $3,3/330=10\ \mathrm{mA}$, được 67,2 mA. Mức 70 mA dùng dự toán nguồn theo cấu hình này.

**Căn cứ khoản mạch phụ.** Cầu chia hai điện trở 10 kΩ tiêu thụ $3,3/20\,000=0,165\ \mathrm{mA}$; mỗi điện trở kéo 10 kΩ chịu đủ 3,3 V tiêu thụ 0,33 mA. Chọn khoản dự trù 10 mA có dự phòng, chốt theo tổng dòng các nhánh trong sơ đồ hoàn chỉnh.

Từ tổng 142 mA, chọn **200 mA** làm mức tải kiểm tra LDO, cao hơn dự trù khoảng 41%. Tính với đầu vào giả định **4,75–5,25 V** (5 V ±5%) và môi trường quanh PCB **40°C**, là giả thiết cho điều kiện thời tiết nóng tại Việt Nam.

**Kiểm tra dư áp.** ST LD1117, Bảng 6 [4] cho đầu ra 3,235–3,365 V tại dòng 0–800 mA, đầu vào 4,75–10 V, nhiệt độ mối nối 0–125°C và tụ ra 10 µF. Dùng mốc chênh lệch áp tối đa 1,2 V tại 800 mA để kiểm tra tải 200 mA:

$$V_{\mathrm{dư}}=4,75-3,365-1,2=0,185\ \mathrm{V}$$

Phần dư dương đáp ứng điều kiện điện áp theo các mốc tính, làm cơ sở lựa chọn phương án hạ 5 V xuống 3,3 V bằng LD1117S33TR.

**Kiểm tra nhiệt.** LDO chuyển phần công suất chênh lệch điện áp thành nhiệt. Lấy đầu vào cao nhất, đầu ra thấp nhất và cộng khoản công suất theo dòng riêng tối đa 10 mA (Bảng 6, đầu vào ≤15 V):

$$P_{\mathrm{LDO,dự\ trù}}=(5,25-3,235)\times0,2+5,25\times0,01\approx0,456\ \mathrm{W}$$

Dùng nhiệt trở mối nối–môi trường 110°C/W của SOT-223 (Bảng 2), nhiệt độ bên trong IC được ước lượng bằng nhiệt độ môi trường cộng độ tăng nhiệt do tổn hao:

$$T_J\approx40+110\times0,456\approx90^\circ\mathrm{C}$$

Kết quả thấp hơn mốc nhiệt độ mối nối hoạt động tối đa 125°C (Bảng 1), hỗ trợ lựa chọn SOT-223 ở tải thiết kế. Đây là đánh giá sơ bộ, phụ thuộc điều kiện tản nhiệt PCB. Dòng vào dự trù $200+10=210\ \mathrm{mA}$ nằm trong khả năng cấp 2 A của adapter.

## 1.3. Lựa chọn tụ đầu vào và đầu ra

**Tụ đầu vào:** chọn 10 µF để hỗ trợ nguồn gần chân IN khi tải thay đổi. Mã tham khảo KEMET T491B106K016AT, mục General Information và Electrical Characteristics [8] có quy cách 10 µF, ±10%, 16 V, tantalum SMD, package 3528. Định mức 16 V tạo dự phòng so với đầu vào 5,25 V.

**Tụ đầu ra:** phần mô tả ST LD1117 nêu điện dung tối thiểu 10 µF để ổn định. Chọn 22 µF để có dư điện dung. Với dung sai ±10%, giá trị nhỏ nhất khi xét dung sai ban đầu là:

$$C_{2,\min}=22(1-0,1)=19,8\ \mu\mathrm{F}>10\ \mu\mathrm{F}$$

Phép tính này là căn cứ chọn mức 22 µF thay vì đặt điện dung sát mức tối thiểu. Chọn KEMET T491C226K016AT, 22 µF, 16 V, ±10%, tantalum SMD case C 6032; ESR công bố 1,5 Ω tại 100 kHz, 25°C. Điện dung, ESR và điều kiện làm việc của mã này là đầu vào đánh giá ổn định LD1117 trên PCB.

## 1.4. Tổng hợp linh kiện nguồn

| Linh kiện | Thông số / package | SL | Chức năng và cơ sở chọn |
|---|---|---:|---|
| Jack DC cái | Same Sky PJ-102AH, 24 VDC–5 A, THT | 1 | Nhận nguồn 5 V tâm dương; pin 1 dương, pin 2 GND, pin 3 để trống |
| LD1117S33TR | 3,3 V, SOT-223 | 1 | Hạ áp; lựa chọn được kiểm tra dư áp và nhiệt tại mức tải 200 mA ở mục 1.2 |
| Tụ đầu vào | 10 µF, 16 V, tantalum SMD; tham khảo T491B106K016AT, ±10%, 3528 | 1 | Hỗ trợ nguồn tại IN; điện dung và mã linh kiện theo mục 1.3 |
| Tụ đầu ra | T491C226K016AT, 22 µF, 16 V, ±10%, case C 6032 | 1 | Dư điện dung so với 10 µF; ESR 1,5 Ω tại 100 kHz, 25°C |

# 2. Khối MCU và nạp/debug

## 2.1. Lựa chọn MCU và phân bổ chân

Chọn **STM32F103C8T6 LQFP-48** để tích hợp trực tiếp lên PCB. MCU đáp ứng hai đầu vào ADC để đọc điện áp cảm biến, UART để trao đổi dữ liệu với MAX3485 và SWD để nạp/debug. Căn cứ chức năng chân theo ST DS5319:

| Chân | Nhiệm vụ |
|---|---|
| PA0, PA1 | ADC nhận tín hiệu dòng và quang tương ứng |
| PA9 / USART1_TX | Phát UART tới DI của MAX3485 |
| PA10 / USART1_RX | Nhận UART từ RO của MAX3485 |
| PB0 | Điều khiển chung DE và /RE của MAX3485 |

## 2.2. Lựa chọn tụ nguồn, clock và mạch khởi động

**Tụ nguồn.** Dùng một tụ 100 nF cho mỗi chân VDD để hỗ trợ dòng tức thời tại chân nguồn; LQFP-48 có ba chân VDD nên chọn ba tụ. Chọn thêm tụ tổng 10 µF cho toàn MCU và cặp 100 nF–1 µF cho VDDA, nguồn phần tương tự phục vụ ADC. Các giá trị lấy theo phương án cấp nguồn của ST AN2586, mục Power supplies [2]. Chọn X7R, 16 V, 0805; mã tụ tổng được xét điện dung hữu dụng tại 3,3 V. VDDA và VBAT dùng chung nguồn 3,3 V.

**Thạch anh và tụ tải.** Chọn Abracon ABM3B-8.000MHZ-B2-T, HSE 8 MHz, CL = 18 pF, SMD 5,0 × 3,2 mm; bộ nhân tần PLL ×9 cho phép cấu hình clock hệ thống 72 MHz. Hai tụ tải được chọn theo điện dung tải của mã thạch anh, dựa trên ST AN2867 [3]:

$$C_L=\frac{C_{X1}C_{X2}}{C_{X1}+C_{X2}}+C_{\mathrm{ký\ sinh}}$$

$C_L$ lấy từ mã thạch anh; $C_{X1},C_{X2}$ là hai tụ ngoài; $C_{\mathrm{ký\ sinh}}$ là điện dung chân và đường mạch. Chọn hai tụ bằng nhau thì **mỗi tụ** có giá trị $C_X=2(C_L-C_{\mathrm{ký\ sinh}})$. Với CL = 18 pF và điện dung ký sinh thiết kế 4,5 pF, chọn mỗi tụ 27 pF, KEMET C0805C270J5GACTU, C0G, ±5%, 50 V, 0805. Y1 pad 1/3 là hai đầu dao động, pad 2/4 nối GND. Điện dung ký sinh là giả thiết tính; khả năng khởi động và mức kích thích được đánh giá theo AN2867 trên mạch thực.

**BOOT0 và NRST.** Chọn điện trở 10 kΩ kéo BOOT0 xuống GND để khởi động từ Flash. Giá trị 10 kΩ tạo mức kéo xuống với dòng 0,33 mA khi chịu đủ 3,3 V. Khi chịu đủ 3,3 V, công suất là $3,3^2/10\,000=1,089\ \mathrm{mW}$, thấp hơn định mức chọn 0,125 W. NRST dùng tụ 100 nF xuống GND để giảm nhiễu, kết hợp điện trở kéo lên bên trong MCU theo ST DS5319, mục NRST pin characteristics.

**Nạp/debug.** Chọn đầu nối SWD gồm 3V3, GND, SWDIO, SWCLK và NRST để dùng ST-Link V2. SWDIO và SWCLK mang tín hiệu giao tiếp; 3V3 thể hiện mức nguồn mạch đích.

## 2.3. Tổng hợp linh kiện MCU

| Linh kiện | Thông số / package | SL | Chức năng và cơ sở chọn |
|---|---|---:|---|
| STM32F103C8T6 | LQFP-48, 3,3 V | 1 | Đáp ứng hai đầu vào ADC, UART và SWD ở nguồn 3,3 V |
| Tụ VDD | 100 nF, X7R, 16 V, 0805 | 3 | Một tụ mỗi chân VDD, theo phương án nguồn AN2586 |
| Tụ nguồn tổng | 10 µF, X7R, 16 V, 0805 | 1 | Hỗ trợ nguồn toàn MCU; chọn theo AN2586 |
| Tụ VDDA | 100 nF và 1 µF, X7R, 16 V, 0805 | Mỗi loại 1 | Giảm nhiễu nguồn phần ADC theo AN2586 |
| Thạch anh HSE | ABM3B-8.000MHZ-B2-T, 8 MHz, CL 18 pF, 5,0 × 3,2 mm | 1 | Tạo clock HSE; pad 1/3 dao động, 2/4 GND |
| Tụ tải HSE | C0805C270J5GACTU, 27 pF, ±5%, C0G, 50 V, 0805 | 2 | Tính theo CL 18 pF và ký sinh giả thiết 4,5 pF |
| Điện trở BOOT0 | 10 kΩ, 1%, 0,125 W, 0805 | 1 | Chọn khởi động Flash; công suất kiểm tra tại mục 2.2 |
| Tụ NRST | 100 nF, X7R, 16 V, 0805 | 1 | Giảm nhiễu reset theo hướng dẫn hãng |
| Đầu nối SWD | 5 tín hiệu, bước chân 2,54 mm | 1 | Nạp/debug bằng ST-Link V2 |

# 3. Khối cảm biến dòng và AFE dòng

## 3.1. Lựa chọn cấu hình xử lý tín hiệu

Chọn đường tín hiệu **CT DL-CT08CL6-1000/1 ngoài PCB → điện trở tải 150 Ω → op-amp đệm → lọc 1 kΩ–100 nF → PA0**. CT là biến dòng; điện trở tải chuyển dòng thứ cấp thành điện áp. Mạch đệm giảm ảnh hưởng của tải phía ADC lên tín hiệu cảm biến.

Chọn một MCP6002-I/SN riêng cho nhánh dòng: một op-amp đệm tín hiệu, một op-amp đệm BIAS. BIAS là mức điện áp nền, chọn giữa nguồn 3,3 V để tín hiệu có khoảng dao động về hai phía. BIAS được dùng chung cho AFE dòng và AFE quang. MCP6002 dùng nguồn đơn 3,3 V, ngõ vào/ra gần hai mức nguồn và có hai op-amp trong một IC; package SOIC-8 phù hợp cấu hình PCB. Căn cứ đặc tính theo Microchip DS20001733L.

## 3.2. Xác định điện trở tải, BIAS và bộ lọc

**Điện trở tải 150 Ω.** Chọn $R_B=150\ \Omega$ làm giá trị thiết kế cho khâu chuyển dòng thứ cấp thành điện áp. Mức chuyển đổi là 150 V/A tính theo dòng thứ cấp; khả năng đáp ứng dải đo được xét theo tỷ số CT và biên điện áp AFE. Gọi $I_{P,\max}$ là dòng sơ cấp lớn nhất, $N$ là tỷ số CT và $R_B$ là điện trở tải. Công suất dùng chọn định mức điện trở là:

$$P_{B,\max}=\left(\frac{I_{P,\max}}{N}\right)^2R_B,\qquad R_B=150\ \Omega$$

Với dòng sơ cấp tính theo giá trị hiệu dụng, công thức cho công suất trung bình trên điện trở. Định mức và package được chọn có dư so với công suất này, đồng thời đáp ứng tải thứ cấp cho phép của CT và biên điện áp AFE. Với dòng sơ cấp thiết kế 5 A RMS và giả thiết $N=1000$, dòng thứ cấp 5 mA tạo công suất $0,005^2\times150=3,75\ \mathrm{mW}$. Chọn Vishay CRCW0805150RFKEA, 150 Ω, 1%, 0,125 W, 0805. Burden mắc song song thứ cấp: dây đỏ CT vào CURRENT_SENSE, dây đen CT về BIAS 1,65 V; hai đầu burden nối vào hai net này. Theo mô hình sin tuyến tính, điện áp tín hiệu nằm khoảng 0,589–2,711 V. Khả năng CT thực làm việc với burden 150 Ω được xác định từ đặc tính tải và độ tuyến tính của đúng cảm biến.

**Hai điện trở BIAS 10 kΩ.** Hai điện trở bằng nhau tạo mức giữa nguồn:

$$V_{\mathrm{BIAS}}=3,3\frac{10\,000}{10\,000+10\,000}=1,65\ \mathrm{V}$$

Chọn hai điện trở 10 kΩ để tạo tỷ lệ chia 1:1 với tổng trở 20 kΩ, dòng qua cầu chia là 0,165 mA. Đây là lựa chọn thiết kế nhằm hạn chế dòng tiêu thụ của cầu chia; op-amp phía sau đảm nhiệm cấp dòng cho tải BIAS. Mỗi điện trở chịu 1,65 V, tiêu tán $1,65^2/10\,000\approx0,272\ \mathrm{mW}$, phù hợp định mức chọn 0,125 W. Op-amp đệm BIAS cấp mức nền cho hai AFE, hạn chế tải làm thay đổi điện áp cầu chia.

**Bộ lọc 1 kΩ–100 nF.** Chọn cặp giá trị này để tạo lọc thông thấp khoảng 1,59 kHz trước ADC. Điện trở nằm trên đường tín hiệu; tụ từ phía PA0 xuống GND làm giảm thành phần tần số cao. Tần số cắt dùng mô tả giới hạn lọc của cặp linh kiện đã chọn:

$$f_c=\frac{1}{2\pi RC}=\frac{1}{2\pi\times1000\times100\times10^{-9}}\approx1,59\ \mathrm{kHz}$$

Mức 1,59 kHz là tần số cắt thiết kế của nhánh dòng. Chọn điện trở 1% để hạn chế sai lệch điện trở và tụ X7R cho chức năng lọc. Tụ nguồn IC 100 nF hỗ trợ dòng tức thời tại MCP6002; tụ lọc tín hiệu phục vụ đường vào ADC.

## 3.3. Tổng hợp linh kiện AFE dòng

| Linh kiện | Thông số / package | SL | Chức năng và cơ sở chọn |
|---|---|---:|---|
| CT DL-CT08CL6-1000/1 | Đặt ngoài PCB | 1 | Cảm nhận dòng điện; tỷ số và dải đo theo đúng model |
| Đầu nối CT | Phoenix Contact 1715721, MKDS 1,5/2-5,08, terminal bắt vít hai cực | 1 | Nhận thứ cấp CT; chân 1 CURRENT_SENSE, chân 2 BIAS |
| MCP6002-I/SN | SOIC-8, 3,3 V | 1 | Đủ hai kênh đệm dòng và BIAS |
| Điện trở tải | CRCW0805150RFKEA, 150 Ω, 1%, 0,125 W, 0805 | 1 | Chuyển dòng thành áp; công suất 3,75 mW tại 5 A theo tỷ số giả thiết 1000:1 |
| Điện trở BIAS | 10 kΩ, 1%, 0,125 W, 0805 | 2 | Tạo 1,65 V; kiểm tra công suất tại mục 3.2 |
| Tụ nguồn IC | 100 nF, X7R, 16 V, 0805 | 1 | Hỗ trợ dòng tức thời và giảm nhiễu nguồn MCP6002 |
| Điện trở lọc | 1 kΩ, 1%, 0,125 W, 0805 | 1 | Cùng tụ 100 nF tạo tần số cắt khoảng 1,59 kHz |
| Tụ lọc tín hiệu | 100 nF, X7R, 16 V, 0805 | 1 | Giảm thành phần tần số cao tại PA0 |

# 4. Khối cảm biến quang và AFE quang

## 4.1. Lựa chọn cảm biến và op-amp

Chọn cấu hình **VBPW34S → MCP6002 với hồi tiếp 10 kΩ–100 pF → PA1**. Photodiode tạo dòng điện khi nhận ánh sáng; op-amp chuyển dòng này thành điện áp để ADC đọc.

Chọn VBPW34S vì là photodiode SMD gullwing, phù hợp lắp trên PCB SMD theo Vishay Document 81128, phần mô tả và package [6]. Chọn MCP6002-I/SN riêng cho khâu chuyển dòng quang thành điện áp, dùng nguồn 3,3 V và BIAS chung từ nhánh dòng. Kênh op-amp còn lại cấu hình đệm BIAS, đầu ra để trống. Chọn cathode photodiode vào nút tổng dòng tại đầu vào đảo op-amp, anode xuống GND; đầu không đảo nhận BIAS. Cấu hình phân cực ngược này tạo điện áp đầu ra tăng khi ánh sáng tăng.

## 4.2. Lựa chọn mạng hồi tiếp và tụ nguồn

**Điện trở hồi tiếp 10 kΩ.** Điện trở $R_f$ quyết định mức chuyển dòng quang thành điện áp. Với chiều photodiode được chọn trong mạch:

$$\Delta V_{\mathrm{OUT}}=I_{\mathrm{photo}}R_f$$

$I_{\mathrm{photo}}$ là dòng quang, $\Delta V_{\mathrm{OUT}}$ là mức thay đổi điện áp so với BIAS. Chọn $R_f=10\ \mathrm{k\Omega}$, tương ứng hệ số chuyển đổi 10 mV/µA. Đây là mức chuyển đổi thiết kế; dải dòng quang tương ứng được xác định từ khoảng điện áp đầu ra hữu dụng quanh BIAS.

Chọn điện trở 1%, 0,125 W. Với mốc 3,3 V đặt trên điện trở 10 kΩ, công suất $3,3^2/10\,000=1,089\ \mathrm{mW}$, tạo dư so với định mức đã chọn trong cấu hình nguồn đơn.

**Tụ hồi tiếp 100 pF.** Tụ $C_f$ song song với $R_f$ hỗ trợ ổn định và giảm đáp ứng ở tần số cao. Chọn 100 pF, C0G/NP0, ±5% để tạo hồi tiếp có điện dung ổn định. Giá trị 100 pF là lựa chọn thiết kế; mức ổn định và đáp ứng của cặp 10 kΩ–100 pF phụ thuộc điện dung VBPW34S và đặc tính MCP6002.

**Tụ nguồn 100 nF.** Chọn tụ X7R gần chân cấp điện MCP6002 để hỗ trợ dòng tức thời và giảm nhiễu nguồn tại IC. Định mức 16 V đáp ứng nguồn 3,3 V.

## 4.3. Tổng hợp linh kiện AFE quang

| Linh kiện | Thông số / package | SL | Chức năng và cơ sở chọn |
|---|---|---:|---|
| VBPW34S | SMD gullwing theo Vishay | 1 | Thu ánh sáng; chọn dạng SMD theo yêu cầu PCB |
| MCP6002-I/SN | SOIC-8, 3,3 V | 1 | Chuyển dòng quang thành điện áp, dùng nguồn 3,3 V |
| Điện trở hồi tiếp $R_f$ | 10 kΩ, 1%, 0,125 W, 0805 | 1 | Tạo hệ số chuyển đổi 10 mV/µA; công suất theo mục 4.2 |
| Tụ hồi tiếp $C_f$ | 100 pF, ±5%, C0G/NP0, ≥16 V, 0805 | 1 | Hỗ trợ ổn định hồi tiếp, dùng điện môi ổn định |
| Tụ nguồn | 100 nF, X7R, 16 V, 0805 | 1 | Hỗ trợ nguồn cục bộ cho op-amp |

# 5. Khối truyền thông RS485

## 5.1. Lựa chọn IC và linh kiện điều khiển

Chọn **MAX3485ESA+, SOIC-8, 3,3 V** để chuyển UART mức 3,3 V của MCU thành tín hiệu chênh lệch trên A–B. IC dùng chung nguồn MCU và làm việc bán song công, tức hai chiều luân phiên dùng cùng đường truyền. PA9 nối DI; RO về PA10. Phía laptop dùng USB–RS485 CH340 lấy nguồn USB.

DE và /RE nối chung về PB0: mức cao chọn phát, mức thấp chọn nhận, theo ADI MAX3483–MAX3491, Pin Description và Function Tables [7]. Chọn điện trở kéo xuống 10 kΩ để mặc định nhận khi chân MCU ở trạng thái trở kháng cao. Chọn 0,125 W theo mốc công suất 1,089 mW tại 3,3 V. Tụ nguồn 100 nF hỗ trợ cấp điện cục bộ; đầu nối A/B/GND phù hợp các tín hiệu giao tiếp đưa ra cáp.

## 5.2. Lựa chọn điện trở kết thúc và bias

**Điện trở kết thúc 120 Ω.** Điện trở này đặt giữa A–B tại đầu cuối để giảm tín hiệu phản xạ trở lại từ đầu cáp. Giá trị được chọn phù hợp trở kháng đặc trưng của cáp; cấu hình cáp 120 Ω dùng điện trở 120 Ω theo TI SLLA272, phần Bus Termination [9]. PCB bố trí một vị trí lắp, được sử dụng khi là đầu cuối cần kết thúc đường truyền.

**Cặp bias 330 Ω.** Bias đặt mức nghỉ xác định cho A–B khi các bộ phát ngừng truyền. Chọn một điện trở kéo A lên 3,3 V và một điện trở kéo B xuống GND. Với hai điện trở kết thúc 120 Ω trên toàn đường truyền, tải tương đương là $R_T=60\ \Omega$. Dòng nghỉ đi qua hai điện trở bias và tải này; hiệu điện áp A–B bằng dòng nhân tải:

$$V_{AB,\mathrm{nghỉ}}=\frac{3,3\times60}{330+60+330}=0,275\ \mathrm{V}$$

Đối chiếu ngưỡng nhận mức cao +200 mV trong bảng DC Electrical Characteristics của ADI MAX3485. Xét nguồn thấp 3,235 V, hai điện trở bias tăng 1% và tải kết thúc giảm 1%:

$$V_{AB,\min}\approx\frac{3,235\times59,4}{333,3+59,4+333,3}\approx0,265\ \mathrm{V}$$

Kết quả cao hơn 0,2 V trong mô hình điện trở, là căn cứ chọn cặp 330 Ω cho cấu hình đã xét. Mức nghỉ thực còn phụ thuộc tải đầu thu và nhiễu. Chỉ lắp cặp bias theo cấu hình chung, có xét phần sẵn có trong USB–RS485.

**Công suất điện trở.** Dùng công thức $P=V^2/R$, lấy 3,3 V làm mốc điện áp trên từng điện trở:

$$P_{120,\mathrm{mốc}}=\frac{3,3^2}{120}\approx0,091\ \mathrm{W},\qquad P_{330,\mathrm{mốc}}=\frac{3,3^2}{330}=0,033\ \mathrm{W}$$

Từ hai mốc này, chọn điện trở kết thúc **0,25 W, 1206** và điện trở bias **0,125 W, 0805** để có dư công suất ở điện áp danh định.

## 5.3. Tổng hợp linh kiện RS485

| Linh kiện | Thông số / package | SL | Chức năng và cơ sở chọn |
|---|---|---:|---|
| MAX3485ESA+ | SOIC-8, 3,3 V | 1 | Giao tiếp RS485 bán song công, dùng chung nguồn MCU |
| Tụ nguồn | 100 nF, X7R, 16 V, 0805 | 1 | Hỗ trợ dòng tức thời và giảm nhiễu nguồn tại IC |
| Điện trở kéo DE,/RE | 10 kΩ, 1%, 0,125 W, 0805 | 1 | Mặc định nhận; công suất theo mục 5.1 |
| Đầu nối RS485 | Phoenix Contact 1715734, MKDS 1,5/3-5,08, terminal bắt vít ba cực | 1 | Chân 1 A, chân 2 B, chân 3 GND |
| Điện trở kết thúc | 120 Ω, 1%, 0,25 W, 1206 | 1 vị trí | Phù hợp cáp 120 Ω; công suất theo mục 5.2; lắp theo đường truyền |
| Điện trở bias | 330 Ω, 1%, 0,125 W, 0805 | 2 vị trí | Mức nghỉ và công suất theo mục 5.2; lắp theo cấu hình bias chung |

# Điều kiện áp dụng của phương án thiết kế

Các mã linh kiện và kết nối được xác định trong bảng của từng khối và file bảng nối chân Altium. Dòng sơ cấp thiết kế là 5 A RMS, tính theo giả thiết CT 1000:1. Tỷ số và đặc tính tải 150 Ω của cảm biến thực quyết định độ tuyến tính và dải đo đạt được. Các khoản dòng nguồn, nhiệt độ LDO và điện dung ký sinh thạch anh là giá trị dự trù hoặc mô hình, được đối chiếu bằng phép đo trên PCB.

Điện trở kết thúc và cặp bias RS485 có đủ vị trí/đường nối; trạng thái lắp tùy cấu hình cáp và phần sẵn có tại bộ USB–RS485. Cấu hình cơ bản gồm năm khối; CT đặt ngoài PCB, SS14, SM712, LED và buzzer nằm ngoài danh sách lắp.

# Tài liệu tra cứu

1. **ST DS5319 — STM32F103x8/STM32F103xB.** Bảng 13 dòng ở chế độ chạy; sơ đồ chân và NRST. [Tài liệu thông số kỹ thuật](https://www.st.com/resource/en/datasheet/stm32f103c8.pdf).
2. **ST AN2586 — Getting started with STM32F10xxx hardware development.** Nguồn, khởi động, đặt lại, xung clock và SWD. [Tài liệu](https://www.st.com/resource/en/application_note/an2586-stm32-hardware-design-guidelines-stmicroelectronics.pdf).
3. **ST AN2867 — Guidelines for oscillator design.** Tụ tải và điều kiện dao động. [Tài liệu](https://www.st.com/resource/en/application_note/an2867-oscillator-design-guide-for-stm8afals-stm32-mcus-and-mpus-stmicroelectronics.pdf).
4. **ST LD1117 — DocID2572.** Bảng 2 nhiệt trở, Bảng 6 bản 3,3 V, yêu cầu tụ. [Tài liệu thông số kỹ thuật](https://www.st.com/resource/en/datasheet/ld1117.pdf).
5. **Microchip MCP6001/1R/1U/2/4 — 1 MHz Low-Power Op Amp.** Dòng tĩnh mỗi kênh và đặc tính op-amp. [Trang hãng và tài liệu thông số kỹ thuật](https://www.microchip.com/en-us/product/MCP6002).
6. **Vishay VBPW34S/VBPW34SR — Tài liệu 81128.** Cảm biến quang SMD. [Tài liệu thông số kỹ thuật](https://www.vishay.com/docs/81128/vbpw34s.pdf).
7. **ADI MAX3483–MAX3491.** Đặc tính điện một chiều, ngưỡng nhận và sơ đồ chân. [Tài liệu thông số kỹ thuật](https://www.analog.com/media/en/technical-documentation/data-sheets/MAX3483-MAX3491.pdf).
8. **KEMET T491B106K016AT.** Tụ 10 µF, ±10%, 16 V. [Thông số linh kiện](https://search.kemet.com/download/specsheet/T491B106K016AT).

9. **TI SLLA272 — The RS-485 Design Guide.** Điện trở kết thúc và bias. [Tài liệu](https://www.ti.com/lit/an/slla272d/slla272d.pdf).

10. [KEMET T491C226K016AT](https://search.kemet.com/download/specsheet/T491C226K016AT), tụ đầu ra.
11. [Abracon ABM3B](https://abracon.com/Resonators/abm3b.pdf), thông số và pad thạch anh.
12. [Same Sky PJ-102AH](https://www.sameskydevices.com/product/resource/pj-102ah.pdf), jack nguồn.
13. [Phoenix Contact 1715721](https://www.phoenixcontact.com/en-be/products/pcb-terminal-block-mkds-15-2-508-1715721) và [1715734](https://www.phoenixcontact.com/en-gb/products/printed-circuit-board-terminal-mkds-15-3-508-1715734), terminal.
14. [KEMET C0805C270J5GACTU](https://search.kemet.com/download/specsheet/C0805C270J5GACTU), tụ tải thạch anh.
15. [Vishay CRCW](https://www.vishay.com/docs/20035/dcrcwe3.pdf), điện trở tải.

## Tài liệu kết nối liên quan

- [Bảng linh kiện và nối chân PCB Altium](02_Bang_linh_kien_va_noi_chan_PCB_Altium.md).
- [Nối dây mô-đun lab buổi 1](03_Noi_day_module_Lab_buoi_1.md).
- [Kế hoạch test module chốt PCB — chỉ tham chiếu phần kết nối](../Kế%20hoạch%20test%20module%20chốt%20PCB.pdf), mục 4.2, trang 4–6.
