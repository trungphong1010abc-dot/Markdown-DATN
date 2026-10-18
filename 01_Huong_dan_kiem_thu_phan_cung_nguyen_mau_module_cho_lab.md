# Hướng dẫn kiểm thử phần cứng nguyên mẫu module cho lab

**Quy ước tụ dùng chung cho 4 file:** tụ gốm chọn 50 V; tụ tantalum C1/C2 chọn 16 V. Mã điện dung 3 chữ số tính theo pF: 27 pF (270), 47 pF (470), 100 pF (101), 10 nF (103), 100 nF (104), 1 µF (105), 10 µF (106), 22 µF (226). Đây là mã quy đổi điện dung, không khẳng định mọi tụ SMD đều in mã trên thân. Package/footprint phải đối chiếu đúng mã mua, đặc biệt tụ gốm 10 µF (106)–50 V; kích thước 0805 trong bảng là dự kiến cho đến khi xác nhận mã đáp ứng.

**Đề tài:** Thiết kế hệ thống nhúng IoT phát hiện sớm chớp hồ quang điện trong hệ thống điện hạ áp và trung áp.

Tài liệu hướng dẫn chuẩn bị ở nhà, nối phần cứng module, kiểm thử tại lab và xử lý số liệu sau đo. Cấu hình và ví dụ tính được phân biệt với thông số hãng và kết quả phải đo; nguồn kỹ thuật chính thống liệt kê ở F.

> **Phạm vi:** “phát hiện sớm” là phát hiện nhanh khi dấu hiệu xuất hiện, không dự báo. Hạ áp có thử nghiệm; trung áp chỉ phân tích khả năng ứng dụng. Phiên thử bằng **12 VAC và đèn pin** kiểm tra đường đo, chưa chứng minh phát hiện hồ quang thực. Cấu hình thiết bị không có mạch ngắt tải, LED hay buzzer.

**Tra cứu nhanh**

| Cần làm | Xem phần |
|---|---|
| Hiểu luồng tín hiệu và kế hoạch | A |
| Kiểm đủ đồ, nối module và dụng cụ | B |
| Chuẩn bị firmware, kiểm tra ở nhà | C |
| Thực hiện ba nhóm kiểm thử tại lab | D.I dòng → D.II quang → D.III tích hợp |
| Phân tích, lựa chọn phần cứng và chuyển sang PCB | E |
| Xử lý số liệu nhánh dòng và RMS từ CSV | D.I.3 |
| Tra tài liệu hãng chính thống | F |

## A. Kiến trúc và kế hoạch

```text
CT → burden 150 Ω → MCP6002 dòng → RC 1 kΩ–100 nF (104) → PA0 ┐
                                                       ├→ Blue Pill → module MAX3485 → USB–RS485 → laptop
BPW34 → MCP6002 quang, Rf 10 kΩ // Cf 100 pF (101) → PA1       ┘                         ↓
                                                                    gateway/dashboard (làm sau)

Adapter 5 VDC → chân 5V Blue Pill
3V3 Blue Pill → hai MCP6002 + VCC module MAX3485
PB0 Blue Pill → DE và /RE module MAX3485 (điều khiển chiều)
Nguồn cách ly 12 VAC → dây qua CT → tải điện trở → về nguồn AC (đường tải riêng)
```

| Giai đoạn | Việc làm | Nơi làm | Kết quả cần có |
|---|---|---|---|
| GĐ1: module | Nguồn, BIAS, AFE, ADC, RS485, CT, quang và tích hợp | Nhà + lab buổi 1 | Nguyên mẫu phản ứng, lưu được dữ liệu |
| GĐ2: thiết kế phần cứng | Đối chiếu burden/RC/Rf/Cf, tính nguồn, schematic/BOM | Chuẩn bị trước lab, phân tích sau lab | Lựa chọn có căn cứ và danh sách còn phải xác nhận |
| GĐ3: PCB | Thiết kế, chế tạo, hàn, kiểm tra | Kế hoạch riêng | PCB hoạt động |
| GĐ4: hoàn thiện | Thuật toán, IoT, gá lắp, thử xung, đánh giá | Sau khi PCB chạy | Hệ thống và hồ sơ đánh giá |

GĐ1 và GĐ2 dùng chung số liệu lab buổi 1. Một lượt đo hai kênh có thể dùng cho cả kiểm tra CT và so sánh lọc. **Lọc dòng lắp cố định từ nhà; “trước lọc” là điểm đo, không phải phiên tháo lọc.**

## B. Linh kiện và kết nối nguyên mẫu

Mã **U1/U2 ở file này là hai MCP6002 DIP-8 của module**, không phải mã U1/U2 trên PCB. Bảng chân PCB nằm ở [file 03](03_Huong_dan_noi_chan_va_thiet_ke_schematic_Altium.md).

### B.1. Quy ước linh kiện và đường tín hiệu

**U1 = MCP6002-I/P DIP-8 nhánh dòng/BIAS. U2 = MCP6002-I/P DIP-8 nhánh quang.** Mã U1/U2 trong file này dùng cho mô-đun; xem bảng nối PCB riêng khi chuyển sang SMD.

| Đường | Kết nối chính |
|---|---|
| Nguồn | Adapter cách ly 5 V → chân 5V Blue Pill; 3V3 Blue Pill → U1/U2 và module MAX3485 |
| Dòng | CT → burden 150 Ω → U1 → R lọc 1 kΩ → PA0 |
| Quang | BPW34 → U2 với Rf 10 kΩ/Cf 100 pF (101) → PA1 |
| Dữ liệu | Blue Pill ↔ module MAX3485 (PB0 điều khiển chiều) ↔ USB–RS485 CH340 ↔ laptop |
| Tải CT | Nguồn 12 VAC riêng → dây xuyên CT → tải điện trở → về nguồn AC |

### B.2. Linh kiện dùng để nối mô-đun

| Khối | Linh kiện | SL | Đặc điểm |
|---|---|---:|---|
| Nguồn | Adapter cách ly 5 VDC, jack phù hợp | 1 bộ | Theo thiết bị hiện có; cấu hình nguồn đề tài 5 V–2 A |
| MCU | STM32F103C8T6 Blue Pill | 1 | Có nguồn 3V3 trên bo |
| Nạp | ST-Link V2 và dây | 1 bộ | Dùng các tín hiệu SWD |
| Dòng | CT DL-CT08CL6-1000/1 | 1 | Hai dây đỏ/đen |
| Dòng/BIAS | MCP6002-I/P | 1 | U1, DIP-8, cấp 3,3 V |
| Dòng | Burden 150 Ω–2 W | 1 | Song song thứ cấp CT |
| BIAS | Điện trở 10 kΩ | 2 | Cầu chia 3,3 V |
| Lọc dòng | Điện trở 1 kΩ | 1 | Giữa U1.1 và PA0 |
| Lọc dòng | Tụ gốm 100 nF (104), 50 V | 1 | PA0 xuống GND |
| Quang | BPW34 chân cắm | 1 | Dùng một cảm biến trong mạch |
| Quang | MCP6002-I/P | 1 | U2, DIP-8, cấp 3,3 V |
| Quang | Rf 10 kΩ | 1 | Hồi tiếp giữa U2.1–U2.2 |
| Quang | Cf: tụ gốm 100 pF (101), 50 V | 1 | Song song Rf |
| Nguồn AFE | Tụ gốm 100 nF (104), 50 V | 2 | Mỗi IC U1/U2 một tụ |
| RS485 | Module MAX3485, có DI/RO/DE và /RE | 1 | Cấp 3,3 V; PB0 điều khiển chung DE và /RE; hậu tố IC cần xác nhận theo module thực |
| RS485 laptop | USB–RS485 CH340 | 1 | Cấp nguồn USB laptop |
| Đấu nối | Breadboard, jumper, dây/header | 1 bộ | Nối theo nhãn chân thực tế |
| Tải ngoài | Nguồn cách ly 12 VAC–1,5 A | 1 | Cấp riêng tải điện trở |
| Tải ngoài | Điện trở sứ 50 Ω–25 W | 3 | Có thể mắc 1, 2 hoặc 3 nhánh song song |
| Tải ngoài | Dây silicone 20 AWG, jack AC ra cọc vít, đầu nối | 1 bộ | Dùng cho dòng tải, tách khỏi jumper tín hiệu |

**Tổng ba tụ 104:** một tụ nguồn U1, một tụ nguồn U2 và một tụ lọc PA0. Tụ nguồn và tụ lọc là ba linh kiện riêng.

### B.3. Xác định chân MCP6002 DIP-8

| Chân | Chức năng | Chân | Chức năng |
|---:|---|---:|---|
| 1 | OUT A | 8 | VDD |
| 2 | IN− A | 7 | OUT B |
| 3 | IN+ A | 6 | IN− B |
| 4 | VSS/GND | 5 | IN+ B |

Nhìn từ trên IC, xác định chân 1 bằng dấu chấm hoặc rãnh định hướng rồi đếm theo datasheet. Tên U1.7 nghĩa là chân 7 của U1.

### B.4. Nối nguồn

| Từ | Nối đến |
|---|---|
| Adapter 5 V cực dương | Qua jack → chân 5V Blue Pill; không cấp trực tiếp 5 V vào VCC module MAX3485 |
| Adapter cực âm | GND Blue Pill và thanh GND breadboard |
| 3V3 Blue Pill | Thanh 3,3 V → U1.8, U2.8 và VCC module MAX3485 |
| GND chung | U1.4, U2.4, GND module MAX3485 |
| Tụ nguồn 104 thứ nhất | Giữa U1.8 và U1.4, gần U1 |
| Tụ nguồn 104 thứ hai | Giữa U2.8 và U2.4, gần U2 |

Hai MCP6002 và module MAX3485 cùng lấy 3,3 V từ Blue Pill. Adapter 5 V chỉ cấp vào chân 5V Blue Pill. USB–RS485 lấy nguồn USB laptop; không nối chân 5 V USB–RS485 song song với adapter.

**Cần xác nhận nguồn 3V3 Blue Pill:** nhận diện bộ ổn áp trên bo thực, tra khả năng cấp dòng/dropout và điều kiện nhiệt; tính cả tải sẵn trên Blue Pill, hai MCP6002, BIAS và module MAX3485 khi nhận/phát với tải bus thực. Dòng IC không thay cho dòng toàn module nếu có LED, bias hoặc linh kiện khác trên module. Đo 3V3 tại bo và VCC module khi nghỉ/phát, kiểm tra sụt áp và nhiệt. Chưa đủ mã ổn áp/module hoặc số đo thì chưa kết luận nguồn chắc chắn đủ; adapter 2 A không chứng minh đường 3V3 đủ dòng. Không áp ngân sách 142/200 mA của PCB sang Blue Pill.

### B.5. Nối cầu chia và đệm BIAS

| Phần tử / chân | Nối đến |
|---|---|
| Điện trở 10 kΩ thứ nhất | 3V3 → điện trở → điểm M |
| Điện trở 10 kΩ thứ hai | Điểm M → điện trở → GND |
| Điểm M | U1.5 |
| U1.6 | U1.7 |
| U1.7 | Net BIAS, danh định khoảng 1,65 V |

BIAS được đưa tới nhánh dòng và quang. Điểm M trước đệm và BIAS sau đệm là hai net riêng.

### B.6. Nối khối dòng

| Từ / linh kiện | Nối đến |
|---|---|
| CT dây đỏ | U1.3 |
| CT dây đen | BIAS, U1.7 |
| Burden 150 Ω–2 W | Giữa U1.3 và U1.7, song song hai dây CT |
| U1.2 | U1.1, hồi tiếp trực tiếp |
| U1.1 | Đầu thứ nhất R lọc 1 kΩ |
| Đầu còn lại R lọc | PA0 Blue Pill |
| Tụ lọc 100 nF (104) thứ ba | PA0 → tụ → GND, đặt gần PA0 |

**Hồi tiếp U1.2 lấy tại U1.1, trước R lọc.** Dây CT đen về BIAS. Tín hiệu từ U1.1 đi qua R 1 kΩ trước khi tới PA0; tránh dây nối tắt điện trở này. Burden được mắc sẵn trước khi cho dòng qua CT.

### B.7. Nối khối quang

| Từ / linh kiện | Nối đến |
|---|---|
| U2.3 | BIAS, U1.7 |
| BPW34 cathode K | U2.2 |
| BPW34 anode A | GND |
| Rf 10 kΩ | Giữa U2.1 và U2.2 |
| Cf: tụ gốm 100 pF (101), 50 V | Giữa U2.1 và U2.2, song song Rf |
| U2.1 | PA1 Blue Pill; nối ADC sau khi xác nhận điện áp phù hợp 0–3,3 V |
| U2.5 | BIAS |
| U2.6 | U2.7 |
| U2.7 | Chỉ hồi tiếp về U2.6, đầu ra không cấp tải ngoài |

U2.7 và U1.7 là hai đầu ra op-amp riêng. Giữ BPW34, Rf, Cf và các dây đầu vào gần U2; nhận diện A/K theo dấu và bản vẽ đúng BPW34 đang dùng.

### B.8. Nối khối truyền thông

| Từ | Nối đến |
|---|---|
| VCC module MAX3485 | 3V3 Blue Pill |
| GND module | GND chung |
| PA9 Blue Pill — USART1_TX | DI module |
| RO module | PA10 Blue Pill — USART1_RX |
| PB0 Blue Pill | Nối chung DE và /RE module |
| PB1 Blue Pill | Để trống |
| A module | A USB–RS485; đối chiếu quy ước nhãn hai thiết bị thực |
| B module | B USB–RS485; đối chiếu quy ước nhãn hai thiết bị thực |
| GND tín hiệu USB–RS485, nếu có và là loại không cách ly | GND tín hiệu mạch |
| Cổng USB bộ chuyển đổi | USB laptop; không nối nguồn 5 V USB–RS485 song song adapter |

Đấu theo **nhãn DI, RO, DE, /RE, VCC, GND, A, B** của module thực; không suy ra số chân header từ pinout IC. Nguyên mẫu dùng module MAX3485, chưa xác nhận hậu tố IC; PCB dùng IC MAX3485ESA+ rời. Hai cấu hình thống nhất nguyên tắc UART và PB0 điều khiển chiều, không đồng nghĩa có cùng mạch phụ trợ.

**Điều khiển theo datasheet MAX3485:** PB0 thấp → DE = 0, /RE = 0: tắt bộ phát, bật bộ nhận. PB0 cao → DE = 1, /RE = 1: bật bộ phát, tắt bộ nhận. Khởi tạo PB0 ở mức thấp để mặc định nhận; mức trong thời gian MCU reset còn phụ thuộc điện trở có sẵn trên module, không mặc định firmware đã giữ thấp trước khi chạy.

Kiểm tra mạch kéo DE,/RE, bias A/B và kết thúc bus trên cả module lẫn USB–RS485 trước khi thay đổi. Ghi giá trị và trạng thái jumper nếu có; không mặc định có R7/R8–R10 giống PCB hoặc lắp thêm điện trở trùng. Nếu phát hiện thiếu mạch cần thiết, ghi vấn đề để xử lý riêng, chưa tự thêm linh kiện.

### B.9. Nối ST-Link V2

| ST-Link | Blue Pill |
|---|---|
| SWDIO | PA13 |
| SWCLK | PA14 |
| GND | GND |
| VTref, nếu đầu nạp có | 3V3 theo hướng dẫn chính đầu nạp |

Blue Pill được cấp nguồn adapter. Đầu ra cấp nguồn 3,3 V của ST-Link clone được để tách khỏi nguồn Blue Pill; VTref chỉ dùng theo chức năng tham chiếu của đúng đầu nạp.

### B.10. Nối tải AC và dụng cụ ở lab

Nguồn tải 12 VAC và nguồn mạch đo 5 VDC là hai nguồn riêng. Phần dưới chỉ mô tả đường dây nguồn/tải và vị trí nối dụng cụ.

#### B.10.1. Mạch tải qua CT

| Đường dây | Cách nối |
|---|---|
| Đầu X của nguồn 12 VAC | Dây chung luồn một lượt qua cửa sổ CT → đầu thứ nhất bộ tải |
| Đầu còn lại bộ tải | Về đầu Y của nguồn 12 VAC |
| Một tải 50 Ω | Một điện trở giữa hai đầu bộ tải |
| Hai hoặc ba tải 50 Ω | Các điện trở mắc song song giữa cùng hai đầu bộ tải |
| Vị trí CT | Trên một dây chung trước điểm chia nhánh |
| Hai dây thứ cấp CT | Đỏ → U1.3; đen → U1.7; burden luôn song song hai đầu |

Chỉ luồn một dây tải qua CT. Tắt nguồn tải trước khi đổi dây hoặc đổi số nhánh điện trở. Đặt điện trở công suất trên bề mặt chịu nhiệt, tách khỏi breadboard.

#### B.10.2. Đồng hồ và oscilloscope

| Dụng cụ | Điểm nối |
|---|---|
| Đồng hồ V~ | Song song hai đầu bộ tải |
| Đồng hồ A~ | Nối tiếp trên dây tải chung |
| Ampe kìm phù hợp dòng nhỏ, nếu dùng thay đồng hồ A~ | Kẹp một dây tải chung |
| Oscilloscope CH1 | Đầu probe vào U1.1, trước R lọc |
| Oscilloscope CH2 | Đầu probe vào PA0, sau R lọc |
| Mass hai probe | Cùng GND mạch đo |
| Khi quan sát quang | Đầu probe vào U2.1, mass vào GND |

Nhờ người phụ trách lab xác nhận nguồn AC cách ly và cách nối mass oscilloscope trước khi cấp tải. Mass probe đặt tại GND mạch, không tại BIAS. Đồng hồ ở thang dòng chỉ nối tiếp; burden luôn nối kín khi có dòng qua CT.


### B.11. Đồ chuẩn bị thêm và linh kiện dự phòng

| Đồ dùng | Số lượng | Mục đích / lưu ý |
|---|---:|---|
| BPW34 dự phòng | 1 ngoài chiếc đang lắp | Tổng chuẩn bị 2 chiếc, chỉ lắp một |
| Tụ gốm 10 nF (103)–50 V; tụ 10 µF (106): gốm 50 V hoặc tantalum 16 V theo loại thực | Mỗi loại 1 | Dự phòng, không tự lắp thêm |
| Rf 100 kΩ; Cf 47 pF (470) | Mỗi loại 1 | Chỉ thay khi có phương án và lý do, ghi cấu hình mới |
| Burden/R/C thay thử | Theo phương án tính trước | Không tháo lọc chỉ để so sánh trước/sau |
| Laptop, sạc, cáp; PlatformIO; firmware và script log | 1 bộ | Thử build/nạp và mở log trước khi đi |
| Đồng hồ số, đồng hồ AC/ampe kìm dòng nhỏ | Có hoặc mượn | Kiểm tra nguồn và dòng tham chiếu |
| Oscilloscope hai kênh + hai probe; USB lưu dữ liệu nếu cần | Mượn tại lab | Biết cách lưu ảnh/CSV |
| Đèn pin | 1 | Chiếu/che tĩnh |
| LED trắng 5 mm + R 330 Ω; bộ tạo xung chọn sau | 1 bộ ở GĐ4 | Nguồn kích quang **ngoài thiết bị**, chưa dùng thử xung ở lab buổi 1 |

Nguồn mạch được chọn là adapter cách ly **5 V–2 A**. Đây là khả năng cấp dòng của nguồn, không phải dòng tiêu thụ mạch. Ba tải 50 Ω–25 W là tải sơ cấp, khác burden 150 Ω–2 W ở thứ cấp CT.

## C. Chuẩn bị và kiểm tra tại nhà

1. Kiểm tra cực tính jack và điện áp 5 V/3,3 V trước khi nối AFE.
2. Kiểm tra U1/U2 cấp 3,3 V; BIAS gần 1,65 V. Điểm M trước đệm khác net BIAS sau đệm.
3. Đo U1.1, PA0 và U2.1 so với GND; xác nhận phù hợp dải ADC 0–3,3 V trước khi nối ADC.
4. Kiểm tra U1.2 hồi tiếp về U1.1 trước R lọc; R 1 kΩ không bị nối tắt; C 100 nF (104) từ PA0 xuống GND.
5. Build/nạp ST-Link; kiểm tra ADC hai kênh và RS485 theo B.8: **PA9 TX → DI; RO → PA10 RX; PB0 → chung DE và /RE; PB1 để trống.** Khởi tạo PB0 thấp; thử gửi/nhận và thời điểm trả về nhận theo hướng dẫn dưới đây, chưa coi cấu hình mới đã được kiểm thử.
6. Lưu kết quả CHE–PHONG–DEN (che / ánh sáng phòng / đèn pin), xác nhận nhánh quang phản ứng. Không cần làm lại toàn bộ ở lab nếu cấu hình không đổi.
7. Lưu ảnh mạch, giá trị linh kiện, tên/phiên bản firmware và thử mở file log/CSV.

**Firmware RS485 khi thử:**

1. Đặt giá trị đầu ra PB0 thấp trước khi cho chân hoạt động ở chế độ output; cấu hình USART1 và thông số bản tin khớp phía laptop.
2. Trước mỗi bản tin, đưa PB0 cao. Chỉ bắt đầu phát UART sau khi đáp ứng thời gian cho phép bộ phát hoạt động theo datasheet đúng IC và mạch module thực.
3. Gửi toàn bộ bản tin; xử lý/xóa cờ TC cũ đúng trình tự RM0008 để kiểm tra hoàn thành của **lần gửi hiện tại**. Sau dữ liệu cuối, chờ UART **TC = 1**, rồi đưa PB0 thấp để nhận. TXE chỉ báo thanh ghi dữ liệu trống; DMA hoàn thành chỉ báo đã chuyển dữ liệu, không chứng minh đã gửi hết bit cuối trên dây.
4. Thời gian enable/disable bộ phát/bộ nhận và thời điểm phía laptop được phản hồi phải căn cứ bảng switching characteristics của MAX3485, mạch module và điều kiện bus; không tự chèn một độ trễ cố định chưa có căn cứ. Nguồn hãng ở F: ADI MAX3485 và ST RM0008.

**Kiểm tra RS485 trước lab:** đo 3V3 tại VCC module cả khi nhận/phát; kiểm PA9/DI khi PB0 cao, RO/PA10 khi PB0 thấp. Với oscilloscope nếu có, đối chiếu cạnh PB0 với byte cuối/TC, xác nhận không cắt cuối bản tin và có trả về nhận. Khi phía laptop gửi thử, bảo đảm hai phía không cùng phát. Ghi bản tin gửi/nhận, SEQ, baudrate/định dạng và cấu hình điện trở trên hai bộ chuyển đổi; lưu kết quả thực, chưa ghi đạt trước khi thử.

| Hiện tượng | Kiểm tra liên quan RS485 |
|---|---|
| Không có dữ liệu | VCC 3V3/GND, nhãn DI/RO, PA9/PA10, cấu hình UART, PB0 và nhãn A/B thực |
| Mất/ký tự lỗi ở cuối bản tin | Có hạ PB0 trước TC của bản tin hiện tại không; có dùng nhầm TXE hoặc DMA hoàn thành không |
| Gửi được nhưng không nhận lại | PB0 có về thấp; /RE có nối đúng; RO → PA10; thời điểm phản hồi có trùng lúc bộ phát chưa nhả bus không |
| Reset/sụt nền khi phát | Sụt 3V3 tại bo/module, tải và nhiệt ổn áp Blue Pill; bias/kết thúc lắp trùng hoặc tranh chấp bus |
| Lỗi lúc khởi động hoặc bus nghỉ | Mạch kéo DE,/RE và trạng thái reset; bias/kết thúc sẵn có ở hai đầu; không tự thêm điện trở khi chưa kiểm |

### C.1. Phân biệt các cách thu dữ liệu

| Cách thu | Chuẩn bị | Dùng để làm gì | Không được suy ra |
|---|---|---|---|
| Log chậm khoảng 500 ms/bản tin | Ghi chu kỳ thực, SEQ và định dạng; firmware điều khiển PB0 đúng trình tự ở C | Theo dõi nền/quang, liên tục truyền, reset | Không tính RMS AC từ các giá trị dòng tức thời cách 500 ms |
| ADC nhanh nếu đã có firmware | Dự kiến 20.000 mẫu/s; thu đều vào bộ đệm, gửi sau | Giữ dạng sóng để hiệu chuẩn/phân tích | Tốc độ dự kiến chưa phải tốc độ lấy mẫu đã đo |
| CSV oscilloscope | Ghi kênh, đơn vị V, thời gian và cài đặt máy | Phân tích điện áp trước/sau lọc | Không gọi là ADC count |

Ví dụ lựa chọn thu nhanh: **4000 mẫu / 20.000 mẫu/s = 0,2 s**, tương ứng 10 chu kỳ nếu đúng 50 Hz. Không gửi từng mẫu ASCII ở 9600 baud khi đang thu nhanh. Chưa cần chốt hệ số ADC → ampere để chọn linh kiện; phải giữ dữ liệu gốc và điều kiện thu: dòng tham chiếu, burden/RC, firmware, số mẫu N, tốc độ lấy mẫu fs thực, đơn vị và tên file.

## D. Thực hiện tại lab buổi 1

**Trình tự:** I kiểm thử nhánh dòng (dòng tải thực + CT/burden + RC) → II kiểm thử nhánh quang → III kiểm thử tích hợp 10 phút.

Trước cấp tải: nhờ người phụ trách xác nhận nguồn AC cách ly, bảo vệ và mass oscilloscope; kiểm lại phần B.10. Burden luôn nối kín khi có dòng qua CT. Tắt nguồn trước khi sửa dây/đổi số tải. Không tự tạo hồ quang trong kế hoạch này.

### I. Kiểm thử khối dòng

**Mục tiêu:** kiểm tra tín hiệu theo dòng tải, biên áp phù hợp ADC và tác dụng của bộ lọc. Đo dòng tham chiếu, trước lọc và sau lọc trong **cùng một lượt thử**.

**Giữ nguyên cấu hình:** một lượt dây sơ cấp qua CT; burden 150 Ω–2 W; U1 MCP6002 cấp 3,3 V; RC 1 kΩ–100 nF (104) lắp cố định. Sau khi ghi bảng đo, xử lý và tính toán ngay tại I.3.

#### I.1. Chuẩn bị và nối dụng cụ

1. Nối tải theo B.10: nguồn 12 VAC cách ly → một dây qua CT → tải → về nguồn AC; CT ở dây chung trước điểm chia nhánh. Mạch đo dùng nguồn 5 VDC riêng.
2. Đồng hồ V~ song song tải; đồng hồ A~ nối tiếp dây chung hoặc ampe kìm phù hợp dòng nhỏ kẹp một dây. Không mắc thang dòng vào hai đầu nguồn.
3. CH1 tại **U1.1 trước lọc**, CH2 tại **PA0 sau lọc**; hai mass cùng GND, không tại BIAS. Kiểm hồi tiếp U1.2 về U1.1 trước R, không có dây nối tắt R lọc.
4. Đo nguồn 3,3 V tại U1 và BIAS tại U1.7; xử lý nguồn/nền sai trước khi đánh giá CT. Oscilloscope bắt đầu DC coupling, 5 ms/div; chỉnh V/div để thấy sóng quanh BIAS, hệ số probe trên máy khớp probe thực.

Burden luôn nối kín khi có dòng qua CT. Tắt nguồn tải trước khi đổi số điện trở; không tháo, nối tắt hoặc thay RC để so sánh trước/sau. Đặt tải công suất trên bề mặt chịu nhiệt, xa breadboard.

#### I.2. Đo bốn mức tải và ghi chung một bảng

Với nguồn danh định 12 VAC và các điện trở 50 Ω mắc song song:

| Điều kiện | Dòng dự kiến | Tổng công suất tải dự kiến |
|---|---:|---:|
| Không dòng | 0 A | 0 W |
| Một R | 0,24 A | 2,88 W |
| Hai R | 0,48 A | 5,76 W |
| Ba R | 0,72 A | 8,64 W |

Đây là **số tính trước, không phải số đo**. Nguồn định mức 1,5 A không làm tải tự lấy 1,5 A.

1. Thử lần lượt không dòng → một R → hai R → ba R; tắt nguồn trước mỗi lần đổi tải.
2. Mỗi mức đo V tải và I RMS thực, ghi BIAS rồi lưu đồng thời CH1/CH2. Không lấy dòng dự kiến thay dòng tham chiếu.
3. Ghi min/max hai kênh, tần số, bẹt đỉnh/méo/dao động và nhiễu trước–sau vào bảng. Khi so nhiễu phải giữ cùng thang đo, hệ số probe và cài đặt máy.
4. Lưu ảnh có thang thời gian/điện áp/hệ số probe, CSV nếu có, ảnh cách luồn CT và thông tin dụng cụ. Nếu thu ADC nhanh, ghi điều kiện theo C.1.

| Tải | V tải thực (V RMS) | I thực (A RMS) | BIAS (V) | U1.1 trước lọc min/max (V) | PA0 sau lọc min/max (V) | Nhận xét / file |
|---|---|---|---|---|---|---|
| Không dòng | — | … | … | … / … | … / … | … |
| Một R | … | … | … | … / … | … / … | … |
| Hai R | … | … | … | … / … | … / … | … |
| Ba R | … | … | … | … / … | … / … | … |

“Không dòng” là tải thực sự không có dòng; nếu dụng cụ không đọc 0, ghi giá trị và điều kiện. Nếu I khác dự kiến, kiểm điện áp, giá trị R và cách mắc trước khi kết luận CT sai. Nếu dạng sóng bất thường, kiểm dây qua CT → burden → nguồn/BIAS → chân U1 rồi mới xem xét đổi linh kiện.

#### I.3. Xử lý và tính toán sau khi có số liệu

Phần tính trước dùng đúng ba mức tải ở I.2. Sau khi đo, thay bằng số liệu thực của từng hàng để đối chiếu; các bảng kết quả thực để trống đến khi có dữ liệu.

##### a. Đối chiếu bộ tải 12 VAC

Với mỗi R = 50 Ω và n = 1, 2, 3 tải song song:

$$R_{eq}=R/n;\qquad I_{load}=V_{RMS}/R_{eq};\qquad P_{total}=V_{RMS}^2/R_{eq}$$

R tương đương lần lượt 50 Ω, 25 Ω và khoảng 16,67 Ω. Ở 12 V, mỗi R nhận 12²/50 = **2,88 W**; tổng dòng/công suất dự kiến xem D.I.2. Khi phân tích phải dùng điện áp và dòng đo thực. Bộ thử dự kiến khoảng 0,72 A, không bắt buộc đạt định mức nguồn 1,5 A.

##### b. Đối chiếu CT, burden và biên độ trước/sau lọc

Điều kiện mô hình: một lượt dây sơ cấp; tỷ số CT **giả thiết 1000:1**, chưa có datasheet hãng đúng CT; Rb = 150 Ω; U1 đệm gain 1; dòng gần hình sin. BIAS lấy từ số đo U1.7.

$$I_s=I_p/1000;\quad V_{b,RMS}=I_sR_b;\quad V_{b,peak}=\sqrt{2}V_{b,RMS}$$
$$V_{out,min/max}=V_{BIAS}\mp V_{b,peak};\qquad P_b=I_s^2R_b$$

Hệ số √2 chỉ dùng cho hình sin. Từ min/max thực:

$$V_{peak,đo}=(V_{max}-V_{min})/2;\qquad V_{tâm}=(V_{max}+V_{min})/2$$
$$V_{pp}=V_{max}-V_{min};\qquad G_{đo}(\%)=100\times V_{pp,sau}/V_{pp,trước}$$

**Bảng tính trước theo đúng các mức tải ở I.2:** giả thiết nguồn tải đúng 12 VAC, tải đúng 50 Ω mỗi nhánh, tỷ số CT 1000:1, dòng hình sin, BIAS = 1,650 V và op-amp lý tưởng. Đây là kết quả tính từ giả thiết, **không phải min/max đã đo**.

| Tải | Ip dự kiến (A RMS) | Is tính (mA RMS) | Vb,RMS tính (V) | Vb,peak tính (V) | U1.1 min/max lý thuyết (V) | Pb tính (mW) |
|---|---:|---:|---:|---:|---|---:|
| Không dòng | 0,00 | 0,00 | 0,000 | 0,0000 | 1,6500 / 1,6500 | 0,00000 |
| Một R | 0,24 | 0,24 | 0,036 | 0,0509 | 1,5991 / 1,7009 | 0,00864 |
| Hai R | 0,48 | 0,48 | 0,072 | 0,1018 | 1,5482 / 1,7518 | 0,03456 |
| Ba R | 0,72 | 0,72 | 0,108 | 0,1527 | 1,4973 / 1,8027 | 0,07776 |

**Khi có số đo:** làm lần lượt cho đúng từng hàng không dòng / một R / hai R / ba R ở I.2. Thay Ip bằng dòng RMS thực và BIAS bằng điện áp U1.7 thực để tính lại biên áp dự kiến; không dùng bảng danh định thay số đo. Lấy min/max CH1 thực để tính Vpeak,đo và Vtâm; lấy min/max CH1/CH2 thực để tính Gđo. Không tự điền min/max, nhiễu hoặc phần trăm sai lệch khi chưa đo.

| Tải | Vpeak trước lọc tính từ Ip thực (V) | Vpeak trước lọc từ CH1 thực (V) | Vtâm CH1 thực (V) | Gđo từ CH1/CH2 thực (%) | Nhiễu trước/sau thực (mVpp) |
|---|---|---|---|---|---|
| Không dòng | … | … | … | Không dùng tỷ số khi biên độ gần 0 | … / … |
| Một R | … | … | … | … | … / … |
| Hai R | … | … | … | … | … / … |
| Ba R | … | … | … | … | … / … |

Không dùng tỷ số biên độ khi tín hiệu trước gần 0. Đối chiếu đúng CT về tỷ số, dòng/tần số, tải thứ cấp cho phép và điều kiện sai số; đối chiếu biên ra MCP6002 theo tải. Tín hiệu nằm trong dải ADC chưa chứng minh CT chính xác với burden 150 Ω. Chênh giữa tính và đo gồm cả ảnh hưởng mô hình, dụng cụ và linh kiện, không phải độ chính xác riêng CT.

**Dải thử:** ghi theo dòng thực lớn nhất đo được; khoảng 0,72 A chỉ là dự kiến. Nguồn 1,5 A là định mức nguồn, không phải một mức thử. Mốc 5 A ở file 02 chỉ phục vụ tính thiết kế PCB, không phải dòng đã thử tại lab và không đại diện dòng sự cố LV/MV.

##### c. Đối chiếu RC 1 kΩ–100 nF (104)

$$f_c=\frac{1}{2\pi RC}\approx1592\ \mathrm{Hz};\qquad |H(f)|=\frac{1}{\sqrt{1+(f/f_c)^2}}$$

Tại 50 Hz, mô hình RC bậc một giữ khoảng **99,95%** biên độ. Phép so sánh ở D.I chưa kiểm chứng đáp ứng tại 1592 Hz, lọc chống alias hoặc giữ đặc trưng nhanh của dòng hồ quang. Phải xét trở kháng nguồn, thời gian lấy mẫu ADC và băng thông cần giữ; tham khảo ST AN2834 ở F. Nếu điều chỉnh R/C sau này phải ghi cấu hình mới và đo lại.

##### d. Tính RMS phần AC từ CSV (khi có dữ liệu dạng sóng)

Cơ sở: [Tektronix, Waveform Measurement Definitions](https://download.tek.com/manual/070928301.pdf), bảng 3–25, định nghĩa AC/SDEviation là RMS độ lệch so với trung bình bản ghi. Công thức dưới đây áp dụng định nghĩa đó cho các mẫu CSV, không lấy tài liệu nội bộ làm nguồn.

1. Chọn đoạn ổn định, lấy mẫu cách đều, chứa nhiều chu kỳ; ưu tiên số chu kỳ nguyên để giảm ảnh hưởng cửa sổ đo.
2. Với CSV oscilloscope, dùng cột điện áp V và thời gian tương ứng. Với ADC count, đổi đúng sang V theo cấu hình ADC/điện áp tham chiếu nếu muốn kết quả đơn vị V.
3. Tính trung bình rồi RMS sau khi trừ trung bình:

$$\bar V=\frac{1}{N}\sum_{k=1}^{N}V_k;\qquad V_{AC,RMS}=\sqrt{\frac{1}{N}\sum_{k=1}^{N}(V_k-\bar V)^2}$$

Đối chiếu với Vb,RMS = IsRb ở mục b phía trên cho điểm trước lọc. Nếu file là ADC count, kết quả ban đầu vẫn là count; chỉ gọi volt sau khi đổi đúng đơn vị. Cách thu và thông tin cần lưu xem C.1; log chậm 500 ms không dùng tính RMS AC. Việc bỏ trung bình không tự loại mọi nhiễu/sai số hoặc chứng minh độ chính xác CT.

#### I.4. Đánh giá và hồ sơ mang về

- **CT/burden:** dòng tăng thì biên độ trước lọc có tăng không; tâm sóng có gần BIAS đo được không; tắt tải có về nền không; có cắt đỉnh/méo/dao động bất thường không?
- **RC:** so biên độ và nhiễu trước/sau cùng mức tải, cùng cài đặt. Khi tín hiệu trước lọc gần 0, so nền/nhiễu riêng, không dùng tỷ số biên độ.
- **ADC:** kiểm min/max và khoảng dự phòng thực. Nằm trong 0–3,3 V chưa đủ chứng minh burden phù hợp CT.
- **Lựa chọn:** có thể giữ RC ban đầu nếu gần giữ biên độ 50 Hz, không méo/dao động bất thường và giảm nhiễu quan sát. Chưa xác nhận chống alias, đáp ứng tần số cao hoặc giữ đặc trưng nhanh hồ quang. Burden 150 Ω còn phải đối chiếu đúng datasheet CT và biên ra MCP6002; chưa đủ căn cứ thì giữ là phương án thử.

**Mang về:** bảng đo, ảnh/CSV hai kênh, cài đặt/dụng cụ, ảnh mạch và cấu hình cuối; nếu thu ADC thì kèm thông tin firmware và lấy mẫu ở C.1. Ghi dải theo **dòng thực lớn nhất đã đo**; định mức nguồn 1,5 A và mốc thiết kế PCB 5 A không phải dải đã thử.

Mẫu kết luận: “Nhánh dòng được thử đến … A RMS; burden … Ω cho biên độ trước lọc …, tâm sóng …; RC … cho tỷ lệ biên độ … và nhiễu … trong điều kiện … . Giữ cấu hình ban đầu / cần kiểm tra …; tải CT cho phép và băng thông cho thuật toán còn phải xác nhận.”

### II. Kiểm thử khối quang

**Mục tiêu:** kiểm tra chuyển ánh sáng thành điện áp, quan sát dao động dưới ánh sáng cố định, tạo căn cứ chọn Rf/Cf.

1. Giữ U2 cấp 3,3 V, Rf = 10 kΩ, Cf = 100 pF (101). Dùng lại dữ liệu CHE–PHONG–DEN ở nhà nếu cấu hình không đổi.
2. Đo 5 V, 3,3 V tại AFE, BIAS và dao động nền.
3. Probe U2.1, mass GND. Giữ sáng cố định, quan sát và lưu ảnh; chiếu/che xác nhận phản ứng.
4. Ghi mức đèn, khoảng cách và cách che. Không quy đổi đèn pin thành lux/năng lượng hồ quang khi chưa đo.
5. Nếu phải thay Rf/Cf, ghi lý do và cấu hình mới, đo lại; không trộn số liệu hai cấu hình.

| Đại lượng/điều kiện | Kết quả | Ảnh/dữ liệu gốc |
|---|---|---|
| 5 V so với GND | … V | … |
| 3,3 V tại U2.8–U2.4 | … V | … |
| BIAS | … V; … mVpp | … |
| U2.1, ánh sáng cố định | … V; dao động … | … |
| U2.1 khi che / chiếu | … / … V | … |
| Rf / Cf thực | … Ω / … pF | … |
| Đèn / khoảng cách / cài đặt máy | … | … |

$$\Delta V=V_{sáng}-V_{che};\qquad \Delta I_{photo}=\Delta V/R_f$$

Thay Vsáng và Vche bằng **số đo ở hàng U2.1 khi che / chiếu** trong bảng trên, Rf bằng giá trị thực đang lắp. Với Rf danh định 10 kΩ, ΔIphoto (µA) = 100 × ΔV (V). Chưa có số đo thì để trống ΔV và ΔIphoto; không tự gán điện áp che/sáng hoặc giới hạn đầu ra.

$$f_{RfCf}=\frac{1}{2\pi R_fC_f}\approx159\ \mathrm{kHz}$$

Mốc này là cực của mạng hồi tiếp, **không phải băng thông thực toàn TIA**. Chọn Cf còn phụ thuộc điện dung photodiode, đầu vào op-amp và ký sinh; xem nguồn F.

**Quyết định:** phản ứng sáng/che rõ, đầu ra không sát biên, không thấy dao động bất thường ở cài đặt đã ghi → có cơ sở giữ 10 kΩ/100 pF (101) ban đầu. Thang thời gian chậm chưa loại trừ mọi dao động nhanh; nhờ người phụ trách hỗ trợ mở rộng quan sát khi cần.

**Hồ sơ:** ảnh sáng cố định, số che/sáng/nền, nguồn và cấu hình. Mẫu kết luận: “Nhánh quang Rf …, Cf … phản ứng … trong điều kiện …; chưa thấy dao động ở cài đặt …; đáp ứng xung, bão hòa dưới ánh sáng hồ quang và khoảng cách phát hiện chưa kiểm chứng.”

### III. Kiểm thử tích hợp 10 phút

**Mục tiêu:** phát hiện lỗi nguồn, truyền dữ liệu và reset khi các khối cùng chạy; không phải thử độ bền dài hạn.

#### III.1. Ghi cấu hình trước chạy

| Hạng mục | Cấu hình thực |
|---|---|
| Burden | … Ω; … W |
| Lọc dòng cố định | 1 kΩ; 100 nF (104) |
| Quang | Rf … Ω; Cf … pF |
| Firmware / chu kỳ log thực | … / … ms |
| RS485 | Module MAX3485; VCC đo … V; PB0 chung DE và /RE; baudrate/định dạng … |
| Mạch phụ trợ bus thực | Kéo DE,/RE …; bias …; kết thúc/jumper trên module và USB–RS485 … |
| Tải | Ba R 50 Ω–25 W song song; dòng thực … A |
| Ngày giờ / dụng cụ / cài đặt / tên log | … |

Giữ adapter 5 VDC cấp Blue Pill suốt phiên; module MAX3485 lấy 3V3 Blue Pill, không lấy 5 V trực tiếp. Không đổi dây tải. Trước chạy, kiểm gửi/nhận, DI/RO, PB0 và TC theo C; nếu chưa xác nhận nguồn/chiều truyền thì ghi vấn đề và xử lý trước phiên tích hợp. Bắt đầu log và đếm giờ cùng lúc. Oscilloscope quan sát PA0.

#### III.2. Lịch thao tác

| Thời điểm | Việc làm | Ghi nhận |
|---|---|---|
| Phút 0 | Nguồn AC tải tắt | PA0 nền … V; log có/không |
| Phút 2 | Bật nguồn tải AC | Sóng AC …; log tiếp tục … |
| Phút 4 | Tắt nguồn tải AC | PA0 về nền …; log tiếp tục … |
| Phút 6 | Bật lại nguồn tải AC | Sóng trở lại …; log tiếp tục … |
| Phút 8 | Đèn pin mức 1, cách 20 cm; chiếu 10 s, che 10 s | L trước …; sáng …; che … |
| Phút 10 | Kết thúc | Lưu log, đo nguồn cuối |

Bật/tắt nguồn tải theo cách người phụ trách xác nhận. Đọc nhánh dòng từ dạng sóng PA0, không tính RMS từ giá trị I của log chậm. Đọc L sau giữ trạng thái vài giây. “Log tiếp tục” là bản tin mới và SEQ tăng; ghi thời điểm dừng hoặc SEQ quay đầu.

#### III.3. Bảng nguồn và kiểm tra log

Đo DC so với GND sau khi trạng thái ổn định:

| Thời điểm | Tải | 5 V thực (V) | 3V3 Blue Pill (V) | VCC module nhận/phát (V) | BIAS U1 (V) |
|---|---|---|---|---|---|
| Phút 0 | Tắt | … | … | … / … | … |
| Phút 5 | Tắt | … | … | … / … | … |
| Gần phút 10 | Bật | … | … | … / … | … |

Các số DC là số đo tại điều kiện đã ghi; để kiểm sụt áp ngắn khi phát, dùng oscilloscope nếu có và ghi min/max/cài đặt. Đo điện áp trung bình không tự loại trừ xung sụt nguồn.

| Nội dung log | Kết quả |
|---|---|
| Bắt đầu / kết thúc | … / … |
| Bản tin hợp lệ / sai định dạng | … / … |
| SEQ thiếu / trùng / giảm | … / … / … |
| Reset ngoài ý muốn | … |
| Chiều RS485 | PB0 thấp khi nhận …; cao khi phát …; về thấp sau TC …; bản tin phản hồi … |
| Tên file | … |

$$N_{kỳ\ vọng}\approx T_{phiên}/T_{gửi}$$

10 phút / 0,5 s ≈ **1200 bản tin**. Đối chiếu timestamp và SEQ; vị trí bắt đầu/kết thúc hay gửi tức thời có thể làm lệch một bản tin. Khoảng cách giữa hai phiên riêng không tự coi là mất gói.

**Đánh giá:** hai nhánh còn phản ứng, truyền liên tục, không reset ngoài ý muốn; nguồn 3V3 tại module phù hợp giới hạn IC/mạch thực ở cả nhận/phát; kiểm tra PB0/TC và chiều truyền không cho thấy cắt bản tin hoặc tranh chấp bus, không còn lỗi chưa giải thích. Kế hoạch chưa quy định ngưỡng sai lệch nguồn bằng số; ghi thay đổi thực và đối chiếu giới hạn linh kiện, không tự ghi “±…% đạt chuẩn”. Số đo module không thay tính nguồn PCB.

Mẫu kết luận: “Cấu hình … chạy … phút; hai nhánh …; log …; reset …; nguồn thay đổi … . Xác nhận hoạt động tích hợp ban đầu, chưa đánh giá độ bền dài hạn.”

## E. Sau lab: từ số đo đến thiết kế PCB

### E.1. Kiểm đủ hồ sơ trước khi rời lab

- [ ] Mở được ảnh/CSV trước và sau lọc; khớp từng dòng thực.
- [ ] Có nguồn, BIAS, ảnh quang và điều kiện chiếu.
- [ ] Có log 10 phút, lịch thao tác và bảng nguồn.
- [ ] Có ảnh mạch, giá trị linh kiện cấu hình cuối, tên firmware và chu kỳ log.
- [ ] Nếu thu ADC nhanh: có N, fs thực, đơn vị và tên file.
- [ ] Ghi dòng thực lớn nhất; không lấy định mức nguồn 1,5 A làm dải đã thử.
- [ ] Ghi rõ phép chưa làm, file thiếu, lỗi chưa giải thích.

### E.2. Chọn linh kiện bằng dữ liệu nào?

| Phần cần quyết định | Dữ liệu lab | Còn phải đối chiếu |
|---|---|---|
| Burden | Ip, BIAS, biên độ/dạng sóng trước lọc (D.I) | Tải cho phép của đúng CT, biên AFE/ADC |
| RC dòng | Trước/sau lọc, nhiễu (D.I) | Băng thông thuật toán, lấy mẫu ADC |
| Rf/Cf | Sáng/che, dao động (D.II) | Ổn định TIA, điện dung, biên đầu ra |
| Nguồn PCB | Nguồn module khi tích hợp (D.III), chỉ tham khảo | Dòng IC rời, tải đồng thời, LDO/tụ/nhiệt |
| Hiệu chuẩn firmware | ADC sau lọc và dòng tham chiếu | Hiệu chuẩn lại khi PCB chạy |
| Schematic/BOM | Cấu hình được chọn và giới hạn | Mã, định mức, SL, chân, footprint |

Thiếu bằng chứng thì quyết định có thể là “giữ phương án thử, cần kiểm chứng tiếp”; không buộc mọi lựa chọn thành chốt cuối ngay sau một buổi lab.

### E.3. Tính nguồn PCB tại nhà

Tra dòng theo **linh kiện sẽ hàn** và chế độ hoạt động, kể cả RS485 khi phát. Không dùng dòng Blue Pill/module thay dòng MCU rời.

$$I_{3V3}=I_{STM32}+I_{AFE\ dòng}+I_{AFE\ quang}+I_{RS485}+I_{khác}$$
$$P_{LDO}\approx(V_{in}-V_{out})I_{out}+V_{in}I_q;\qquad T_j\approx T_a+\theta_{JA}P_{LDO}$$

Phương án PCB hiện hành ở [file 02](02_Lua_chon_linh_kien_BOM_va_tinh_toan_PCB.md) dự trù 142 mA, kiểm tra ở 200 mA và có xét Iq. Đây không phải ngân sách hay khả năng cấp dòng 3V3 của Blue Pill; nguyên mẫu phải kiểm tra riêng theo B.4. Nhiệt trở phụ thuộc package/PCB thực; kiểm ổn định tụ, dòng và nhiệt theo đúng LD1117S33TR. Tải 5 V trực tiếp nếu có phải cộng riêng khi chọn nguồn đầu vào, không dồn vào dòng 3,3 V.

### E.4. Hoàn thiện schematic, BOM và báo cáo

Mỗi linh kiện ghi **mã – giá trị – định mức – số lượng – footprint**. Kiểm burden về biên áp/công suất/tải CT; ghi RC/Rf/Cf là ban đầu hay đã kiểm chứng; nguồn tính theo IC PCB. PA0 dòng, PA1 quang, PA9 TX, PA10 RX. Nguyên mẫu dùng module MAX3485 3,3 V; PCB dùng IC MAX3485ESA+ rời 3,3 V. Cả hai dùng PB0 chung DE và /RE; module phải đối chiếu hậu tố IC, header và mạch phụ trợ thực, không mặc định giống PCB.

Phân biệt cấu hình: module dùng burden 150 Ω–2 W và BPW34 chân cắm; PCB dùng R2 150 Ω–0,125 W và VBPW34S SMD. PCB có SW1 RESET dùng nút nhấn 2 chân SMD 3 × 6 × 2,5 mm, thường hở, nhấn nhả, nối NRST–GND, giữ C11 100 nF (104) và J2.5 theo file 02–03; không thêm nút BOOT. Không đưa mã linh kiện PCB sang bảng module.

Kiểm SWD, khả năng tiếp cận điểm đo nguồn/BIAS/AFE và footprint đúng mã mua. Việc cần điểm đo là yêu cầu bố trí/kiểm tra, không tự bổ sung linh kiện ngoài BOM. Ba tụ 100 nF (104) ở module là ba vị trí riêng, chưa bao gồm các tụ MCU/IC khác trên PCB.

| Phần trong quyển đồ án | Nội dung đưa vào |
|---|---|
| Thiết kế phần cứng | CT/burden, BIAS, RC, TIA; công thức; datasheet; lý do và giới hạn chọn |
| Kiểm thử | Bộ thử, dụng cụ/cài đặt, cấu hình, bảng đo, ảnh/CSV, đối chiếu tính–đo, lỗi và xử lý |
| Giới hạn | Dải dòng đã đo; quang tĩnh; tích hợp 10 phút; xung sáng/đặc trưng nhanh/hồ quang thực chưa thử; MV chỉ phân tích |

Mẫu tổng hợp: “Nguyên mẫu đã kiểm tra dòng trong dải … A, quang dưới điều kiện …, tích hợp … phút. Dữ liệu dùng để … . Lựa chọn … còn cần … trước khi chốt PCB. Phiên thử chưa xác nhận phát hiện chớp hồ quang thực.”

### E.5. Điều kiện chuyển sang PCB

- [ ] Có cấu hình cuối và dữ liệu tương ứng, phân biệt số tính/số đo.
- [ ] Burden/RC/Rf/Cf có căn cứ; thiếu tài liệu hoặc phép đo phải ghi rõ.
- [ ] Nguồn tính theo IC sẽ hàn, không lấy dòng Blue Pill thay MCU.
- [ ] Schematic/BOM đủ mã, giá trị, định mức, SL, chân và footprint.
- [ ] Không đổi R/C sau lab rồi ghi cấu hình mới đã được kiểm chứng.
- [ ] Giữ danh sách vấn đề chưa giải quyết và việc phải kiểm tra sau hàn.

**Tiến độ ghi nhận:** nguồn PCB đã kiểm tra trực quan kết nối, chưa kiểm thử thực hoặc hoàn tất ERC/footprint; đang làm MCU và SWD theo mục 3 file 03. Sơ đồ khối tổng thể và giải thích chức năng/vị trí cho thuyết minh vẫn cần hoàn thiện; sơ đồ luồng ở A chỉ phục vụ hướng dẫn nguyên mẫu.

## F. Tài liệu kỹ thuật chính thống

Chỉ dùng tài liệu công khai của nhà sản xuất làm nguồn kỹ thuật. Cấu hình, trình tự lab và ví dụ số là lựa chọn của kế hoạch thử; không coi là quy trình được hãng chứng nhận.

1. [Microchip MCP6002](https://www.microchip.com/en-us/product/MCP6002): nguồn, biên ra, tải, đặc tính op-amp; không dùng để chứng nhận CT.
2. [ST AN2834](https://www.st.com/resource/en/application_note/an2834-how-to-get-the-best-adc-accuracy-in-stm32-microcontrollers-stmicroelectronics.pdf): ảnh hưởng mạch ngoài và điều kiện lấy mẫu ADC.
3. [TI – Transimpedance Considerations for High-Speed Amplifiers](https://www.ti.com/lit/an/sboa122/sboa122.pdf): ổn định, băng thông và điện dung TIA; không phải datasheet MCP6002.
4. [Vishay BPW34/BPW34S](https://www.vishay.com/docs/81521/bpw34.pdf): cảm biến module, thông số theo phân cực. PCB dùng VBPW34S theo file 02–03, không tự đồng nhất footprint.
5. [Tektronix – Programmer Manual, bảng 3–25](https://download.tek.com/manual/070928301.pdf): định nghĩa RMS toàn tín hiệu và AC/SDEviation; làm cơ sở tính RMS phần AC từ CSV ở D.I.3.d.
6. [ST LD1117](https://www.st.com/resource/en/datasheet/ld1117.pdf): ổn áp, tụ và nhiệt theo đúng mã/package PCB; không mặc định đây là ổn áp trên Blue Pill thực.
7. [ADI MAX3483–MAX3491](https://www.analog.com/media/en/technical-documentation/data-sheets/MAX3483-MAX3491.pdf): phần MAX3485, nguồn IC 3,0–3,6 V, chức năng DI/RO/DE và /RE, bảng driver/receiver switching characteristics. Thông số IC không tự xác nhận cấu hình toàn module.
8. [ST RM0008](https://www.st.com/resource/en/reference_manual/cd00171190.pdf): phần USART, truyền dữ liệu và USART_SR (TC/TXE), căn cứ chờ UART gửi xong trước khi trả chiều nhận.

Chưa có datasheet hãng đúng **DL-CT08CL6-1000/1** để xác nhận tỷ số và burden. Giữ 1000:1 là giả thiết tính toán. Mọi ngưỡng đạt chưa có trong kế hoạch phải được thống nhất bằng căn cứ kỹ thuật; không tự thêm ngưỡng rồi coi là tiêu chuẩn.
