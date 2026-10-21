# Giai đoạn 1 — Chọn module, tính toán và kiểm thử tại lab buổi 1

**Mục tiêu:** xây dựng nguyên mẫu sử dụng module, đánh giá các kênh đo dòng và ánh sáng, xác định thông số thiết kế và thu thập dữ liệu làm căn cứ cho thiết kế PCB SMD.

**Phạm vi:** hệ thống đo dòng xoay chiều bằng biến dòng (CT) và ánh sáng bằng photodiode. Nguồn 12 VAC cách ly chỉ cấp cho tải thử nghiệm, không cấu thành kênh đo điện áp. Thử nghiệm với tải 12 VAC và nguồn sáng cầm tay chỉ đánh giá hoạt động của các kênh đo, chưa chứng minh khả năng phát hiện hồ quang thực tế. Hệ thống hiện chưa tích hợp cơ cấu ngắt tải, đèn báo hoặc còi báo. Khả năng ứng dụng ở cấp điện áp trung áp chỉ được phân tích, chưa thử nghiệm.

**Pipeline của ba giai đoạn:**

| Bước | Làm gì | Đầu ra để qua bước sau |
|---|---|---|
| 1. Xác định yêu cầu và tính sơ bộ | Đọc phần B trước khi đấu mạch: dải dòng/áp, BIAS, lọc, băng thông, xung, tiêu chuẩn tham khảo và `T_sampling` từng kênh | Giá trị tính ban đầu và các giới hạn cần kiểm tra |
| 2. Lắp nguyên mẫu | Dùng phần A làm sơ đồ nối module; đối chiếu linh kiện, chân và tải thử thực tế | Cấu hình module có thể cấp nguồn và đo an toàn |
| 3. Đo tại lab | Làm phần C theo thứ tự: kiểm tra trước cấp nguồn → đo nhánh dòng → nhánh quang → tích hợp | Số đo, dạng sóng, cấu hình, điều kiện và phần chưa xác nhận |
| 4. Chuyển sang thiết kế PCB | Sử dụng mục E.2–E.5 và bảng bàn giao; đối chiếu lựa chọn tại file 2 theo linh kiện SMD | Quyết định lựa chọn có căn cứ và danh sách hạng mục cần xác nhận trên PCB |

**Cách đọc:** phần A mô tả cấu hình nguyên mẫu ban đầu; phần B nêu cơ sở tính toán và lựa chọn thông số; phần C quy định các phép kiểm tra và ghi nhận kết quả. Sai lệch giữa giá trị tính toán và kết quả đo cần được ghi nhận và đánh giá trong giai đoạn thiết kế PCB; dữ liệu đo gốc phải được bảo toàn.

**Quy ước tụ dùng chung:** tụ gốm chọn 50 V; tụ tantalum C1/C2 chọn 16 V. Mã điện dung ba chữ số quy đổi theo pF: 27 pF (270), 47 pF (470), 100 pF (101), 10 nF (103), 100 nF (104), 1 µF (105), 10 µF (106), 22 µF (226). Package phải đối chiếu theo đúng mã mua; 0805 cho tụ gốm 10 µF–50 V vẫn cần xác minh.
## A. Chọn linh kiện và nối module

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
| GĐ1: module và lab buổi 1 | Tính sơ bộ → lắp → đo → ghi dữ liệu | Nhà + lab buổi 1 | Cấu hình và kết quả thử để làm đầu vào file 2 |
| GĐ2: thiết kế phần cứng PCB SMD | Đối chiếu số đo với tính toán/datasheet → chọn giá trị và footprint | Sau khi có dữ liệu module | BOM/schematic PCB cùng các mục còn phải kiểm chứng |
| GĐ3: nối schematic | Vẽ đúng net, chân và giá trị đã chốt ở file 2 | Trong lúc thiết kế PCB | Schematic để kiểm tra ERC, footprint và chuyển layout |

GĐ2 phụ thuộc dữ liệu GĐ1; GĐ3 phụ thuộc bảng linh kiện/giá trị/net của GĐ2. Nếu chưa có phép đo nào đó, ghi rõ giả định trong file 2 thay vì coi số tính là kết quả thử. Một lượt thu hai kênh có thể dùng cho kiểm tra CT và so sánh lọc. **Lọc dòng lắp cố định từ nhà; “trước lọc” là điểm đo, không phải phiên tháo lọc.**

### A.1. Linh kiện và kết nối nguyên mẫu

Trong file này, hai IC MCP6002 DIP-8 của module được gọi theo chức năng là **MCP6002 dòng** và **MCP6002 quang**. Ký hiệu linh kiện trên PCB có thể khác; xem bảng chân PCB ở [file 3](03_Huong_dan_noi_day_schematic.md).

#### A.1.1. Quy ước linh kiện và đường tín hiệu

**MCP6002 dòng:** MCP6002-I/P DIP-8 dùng cho nhánh dòng và BIAS. **MCP6002 quang:** MCP6002-I/P DIP-8 dùng cho nhánh quang. Các tên này áp dụng cho mô-đun; xem bảng nối PCB riêng khi chuyển sang SMD.

| Đường | Kết nối chính |
|---|---|
| Nguồn | Adapter cách ly 5 V → chân 5V Blue Pill; 3V3 Blue Pill → MCP6002 dòng/MCP6002 quang và module MAX3485 |
| Dòng | CT → burden 150 Ω → MCP6002 dòng → R lọc 1 kΩ → PA0 |
| Quang | BPW34 → MCP6002 quang với Rf 10 kΩ/Cf 100 pF (101) → PA1 |
| Dữ liệu | Blue Pill ↔ module MAX3485 (PB0 điều khiển chiều) ↔ USB–RS485 CH340 ↔ laptop |
| Tải CT | Nguồn 12 VAC riêng → dây xuyên CT → tải điện trở → về nguồn AC |

#### A.1.2. Linh kiện dùng để nối mô-đun

| Khối | Linh kiện | SL | Đặc điểm |
|---|---|---:|---|
| Nguồn | Adapter cách ly 5 VDC, jack phù hợp | 1 bộ | Theo thiết bị hiện có; cấu hình nguồn đề tài 5 V–2 A |
| MCU | STM32F103C8T6 Blue Pill | 1 | Có nguồn 3V3 trên bo |
| Nạp | ST-Link V2 và dây | 1 bộ | Dùng các tín hiệu SWD |
| Dòng | CT DL-CT08CL6-1000/1 | 1 | Hai dây đỏ/đen |
| Dòng/BIAS | MCP6002-I/P | 1 | MCP6002 dòng, DIP-8, cấp 3,3 V |
| Dòng | Burden 150 Ω–2 W | 1 | Song song thứ cấp CT |
| BIAS | Điện trở 10 kΩ | 2 | Cầu chia 3,3 V |
| Lọc dòng | Điện trở 1 kΩ | 1 | Giữa MCP6002 dòng chân 1 và PA0 |
| Lọc dòng | Tụ gốm 100 nF (104), 50 V | 1 | PA0 xuống GND |
| Quang | BPW34 chân cắm | 1 | Dùng một cảm biến trong mạch |
| Quang | MCP6002-I/P | 1 | MCP6002 quang, DIP-8, cấp 3,3 V |
| Quang | Rf 10 kΩ | 1 | Hồi tiếp giữa MCP6002 quang chân 1–MCP6002 quang chân 2 |
| Quang | Cf: tụ gốm 100 pF (101), 50 V | 1 | Song song Rf |
| Quang, lọc thử | Điện trở 1 kΩ, 1% | 2 | R11/R12; nối tiếp sau đầu ra TIA khi thử cấu hình có lọc |
| Quang, lọc thử | Tụ gốm 10 nF (103), 50 V | 2 | C17/C18; từ từng nút sau R11/R12 xuống GND |
| Nguồn AFE | Tụ gốm 100 nF (104), 50 V | 2 | Mỗi IC MCP6002 dòng/MCP6002 quang một tụ |
| RS485 | Module MAX3485, có DI/RO/DE và /RE | 1 | Cấp 3,3 V; PB0 điều khiển chung DE và /RE; hậu tố IC cần xác nhận theo module thực |
| RS485 laptop | USB–RS485 CH340 | 1 | Cấp nguồn USB laptop |
| Đấu nối | Breadboard, jumper, dây/header | 1 bộ | Nối theo nhãn chân thực tế |
| Tải ngoài | Nguồn cách ly 12 VAC–1,5 A | 1 | Cấp riêng tải điện trở |
| Tải ngoài | Điện trở sứ 50 Ω–25 W | 3 | Có thể mắc 1, 2 hoặc 3 nhánh song song |
| Tải ngoài | Dây silicone 20 AWG, jack AC ra cọc vít, đầu nối | 1 bộ | Dùng cho dòng tải, tách khỏi jumper tín hiệu |

**Tổng ba tụ 104:** một tụ nguồn MCP6002 dòng, một tụ nguồn MCP6002 quang và một tụ lọc PA0. Tụ nguồn và tụ lọc là ba linh kiện riêng.

#### A.1.3. Xác định chân MCP6002 DIP-8

| Chân | Chức năng | Chân | Chức năng |
|---:|---|---:|---|
| 1 | OUT A | 8 | VDD |
| 2 | IN− A | 7 | OUT B |
| 3 | IN+ A | 6 | IN− B |
| 4 | VSS/GND | 5 | IN+ B |

Nhìn từ trên IC, xác định chân 1 bằng dấu chấm hoặc rãnh định hướng rồi đếm theo datasheet. Ví dụ, “MCP6002 dòng chân 7” là chân 7 của IC dùng cho nhánh dòng.

#### A.1.4. Nối nguồn

| Từ | Nối đến |
|---|---|
| Adapter 5 V cực dương | Qua jack → chân 5V Blue Pill; không cấp trực tiếp 5 V vào VCC module MAX3485 |
| Adapter cực âm | GND Blue Pill và thanh GND breadboard |
| 3V3 Blue Pill | Thanh 3,3 V → MCP6002 dòng chân 8, MCP6002 quang chân 8 và VCC module MAX3485 |
| GND chung | MCP6002 dòng chân 4, MCP6002 quang chân 4, GND module MAX3485 |
| Tụ nguồn 104 thứ nhất | Giữa MCP6002 dòng chân 8 và MCP6002 dòng chân 4, gần MCP6002 dòng |
| Tụ nguồn 104 thứ hai | Giữa MCP6002 quang chân 8 và MCP6002 quang chân 4, gần MCP6002 quang |

Hai MCP6002 và module MAX3485 cùng lấy 3,3 V từ Blue Pill. Adapter 5 V chỉ cấp vào chân 5V Blue Pill. USB–RS485 lấy nguồn USB laptop; không nối chân 5 V USB–RS485 song song với adapter.

**Cần xác nhận nguồn 3V3 Blue Pill:** nhận diện bộ ổn áp trên bo thực, tra khả năng cấp dòng/dropout và điều kiện nhiệt; tính cả tải sẵn trên Blue Pill, hai MCP6002, BIAS và module MAX3485 khi nhận/phát với tải bus thực. Dòng IC không thay cho dòng toàn module nếu có LED, bias hoặc linh kiện khác trên module. Đo 3V3 tại bo và VCC module khi nghỉ/phát, kiểm tra sụt áp và nhiệt. Chưa đủ mã ổn áp/module hoặc số đo thì chưa kết luận nguồn chắc chắn đủ; adapter 2 A không chứng minh đường 3V3 đủ dòng. Không áp ngân sách 142/200 mA của PCB sang Blue Pill.

#### A.1.5. Nối cầu chia và đệm BIAS

| Phần tử / chân | Nối đến |
|---|---|
| Điện trở 10 kΩ thứ nhất | 3V3 → điện trở → điểm M |
| Điện trở 10 kΩ thứ hai | Điểm M → điện trở → GND |
| Điểm M | MCP6002 dòng chân 5 |
| MCP6002 dòng chân 6 | MCP6002 dòng chân 7 |
| MCP6002 dòng chân 7 | Net BIAS, danh định khoảng 1,65 V |

BIAS được đưa tới nhánh dòng và quang. Điểm M trước đệm và BIAS sau đệm là hai net riêng.

#### A.1.6. Nối khối dòng

| Từ / linh kiện | Nối đến |
|---|---|
| CT dây đỏ | MCP6002 dòng chân 3 |
| CT dây đen | BIAS, MCP6002 dòng chân 7 |
| Burden 150 Ω–2 W | Giữa MCP6002 dòng chân 3 và MCP6002 dòng chân 7, song song hai dây CT |
| MCP6002 dòng chân 2 | MCP6002 dòng chân 1, hồi tiếp trực tiếp |
| MCP6002 dòng chân 1 | Đầu thứ nhất R lọc 1 kΩ |
| Đầu còn lại R lọc | PA0 Blue Pill |
| Tụ lọc 100 nF (104) thứ ba | PA0 → tụ → GND, đặt gần PA0 |

**Hồi tiếp MCP6002 dòng chân 2 lấy tại MCP6002 dòng chân 1, trước R lọc.** Dây CT đen về BIAS. Tín hiệu từ MCP6002 dòng chân 1 đi qua R 1 kΩ trước khi tới PA0; tránh dây nối tắt điện trở này. Burden được mắc sẵn trước khi cho dòng qua CT.

#### A.1.7. Nối khối quang

| Từ / linh kiện | Nối đến |
|---|---|
| MCP6002 quang chân 3 | BIAS, MCP6002 dòng chân 7 |
| BPW34 cathode K | MCP6002 quang chân 2 |
| BPW34 anode A | GND |
| Rf 10 kΩ | Giữa MCP6002 quang chân 1 và MCP6002 quang chân 2 |
| Cf: tụ gốm 100 pF (101), 50 V | Giữa MCP6002 quang chân 1 và MCP6002 quang chân 2, song song Rf |
| MCP6002 quang chân 1 | PA1 Blue Pill; nối ADC sau khi xác nhận điện áp phù hợp 0–3,3 V |
| MCP6002 quang chân 5 | BIAS |
| MCP6002 quang chân 6 | MCP6002 quang chân 7 |
| MCP6002 quang chân 7 | Chỉ hồi tiếp về MCP6002 quang chân 6, đầu ra không cấp tải ngoài |

MCP6002 quang chân 7 và MCP6002 dòng chân 7 là hai đầu ra op-amp riêng. Giữ BPW34, Rf, Cf và các dây đầu vào gần MCP6002 quang; nhận diện A/K theo dấu và bản vẽ đúng BPW34 đang dùng.

#### A.1.8. Nối khối truyền thông

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

#### A.1.9. Nối ST-Link V2

| ST-Link | Blue Pill |
|---|---|
| SWDIO | PA13 |
| SWCLK | PA14 |
| GND | GND |
| VTref, nếu đầu nạp có | 3V3 theo hướng dẫn chính đầu nạp |

Blue Pill được cấp nguồn adapter. Đầu ra cấp nguồn 3,3 V của ST-Link clone được để tách khỏi nguồn Blue Pill; VTref chỉ dùng theo chức năng tham chiếu của đúng đầu nạp.

#### A.1.10. Nối tải AC và dụng cụ ở lab

Nguồn tải 12 VAC và nguồn mạch đo 5 VDC là hai nguồn riêng. Phần dưới chỉ mô tả đường dây nguồn/tải và vị trí nối dụng cụ.

##### A.1.10.1. Mạch tải qua CT

| Đường dây | Cách nối |
|---|---|
| Đầu X của nguồn 12 VAC | Dây chung luồn một lượt qua cửa sổ CT → đầu thứ nhất bộ tải |
| Đầu còn lại bộ tải | Về đầu Y của nguồn 12 VAC |
| Một tải 50 Ω | Một điện trở giữa hai đầu bộ tải |
| Hai hoặc ba tải 50 Ω | Các điện trở mắc song song giữa cùng hai đầu bộ tải |
| Vị trí CT | Trên một dây chung trước điểm chia nhánh |
| Hai dây thứ cấp CT | Đỏ → MCP6002 dòng chân 3; đen → MCP6002 dòng chân 7; burden luôn song song hai đầu |

Chỉ luồn một dây tải qua CT. Tắt nguồn tải trước khi đổi dây hoặc đổi số nhánh điện trở. Đặt điện trở công suất trên bề mặt chịu nhiệt, tách khỏi breadboard.

##### A.1.10.2. Đồng hồ và oscilloscope

| Dụng cụ | Điểm nối |
|---|---|
| Đồng hồ V~ | Song song hai đầu bộ tải |
| Đồng hồ A~ | Nối tiếp trên dây tải chung |
| Ampe kìm phù hợp dòng nhỏ, nếu dùng thay đồng hồ A~ | Kẹp một dây tải chung |
| Oscilloscope CH1 | Đầu probe vào MCP6002 dòng chân 1, trước R lọc |
| Oscilloscope CH2 | Đầu probe vào PA0, sau R lọc |
| Mass hai probe | Cùng GND mạch đo |
| Khi quan sát quang | Đầu probe vào MCP6002 quang chân 1, mass vào GND |

Nhờ người phụ trách lab xác nhận nguồn AC cách ly và cách nối mass oscilloscope trước khi cấp tải. Mass probe đặt tại GND mạch, không tại BIAS. Đồng hồ ở thang dòng chỉ nối tiếp; burden luôn nối kín khi có dòng qua CT.


#### A.1.11. Dụng cụ bổ sung và linh kiện dự phòng

| Đồ dùng | Số lượng | Mục đích / lưu ý |
|---|---:|---|
| BPW34 dự phòng | 1 ngoài chiếc đang lắp | Tổng chuẩn bị 2 chiếc, chỉ lắp một |
| Tụ gốm 10 nF (103)–50 V; tụ 10 µF (106): gốm 50 V hoặc tantalum 16 V theo loại thực | Mỗi loại 1 | Dự phòng, không tự lắp thêm |
| Rf 100 kΩ; Cf 47 pF (470) | Mỗi loại 1 | Chỉ thay khi có phương án và lý do, ghi cấu hình mới |
| R burden module 47 Ω, 0,25 W, 5% | 1 | So sánh với burden 150 Ω–2 W đang có; chỉ lắp một burden mỗi lượt, không mắc song song |
| RC thay thử | Theo phương án tính trước | Không tháo lọc chỉ để so sánh trước/sau |
| Laptop, sạc, cáp; PlatformIO; firmware và script log | 1 bộ | Thử build/nạp và mở log trước khi đi |
| Đồng hồ số, đồng hồ AC/ampe kìm dòng nhỏ | Có hoặc mượn | Kiểm tra nguồn và dòng tham chiếu |
| Oscilloscope hai kênh + hai probe; USB lưu dữ liệu nếu cần | Mượn tại lab | Biết cách lưu ảnh/CSV |
| Đèn pin | 1 | Chiếu/che tĩnh |
| LED trắng 5 mm + R 330 Ω; bộ tạo xung chọn sau | 1 bộ ở GĐ4 | Nguồn kích quang **ngoài thiết bị**, chưa dùng thử xung ở lab buổi 1 |

Nguồn mạch được chọn là adapter cách ly **5 V–2 A**. Đây là khả năng cấp dòng của nguồn, không phải dòng tiêu thụ mạch. Ba tải 50 Ω–25 W là tải sơ cấp, khác burden 150 Ω–2 W ở thứ cấp CT.

## B. Cơ sở tính toán và thông số đo

### 1. Phạm vi và đường tín hiệu

Hệ thống hiện đo **dòng AC bằng CT** và **ánh sáng bằng photodiode**. Không có kênh đo điện áp lưới: 12 VAC chỉ là nguồn cách ly cấp cho tải thử; ADC không được nối trực tiếp vào điện áp tải. Nguồn adapter 5 VDC cấp MCU/AFE; các tín hiệu analog được đặt quanh BIAS để nằm trong dải ADC 0–3,3 V.

```text
Dây tải sơ cấp, 12 VAC cách ly → tải điện trở → CT
CT thứ cấp → burden 150 Ω → MCP6002 đệm quanh BIAS 1,65 V → RC → PA0/ADC
BPW34 (module) hoặc VBPW34S (PCB) → MCP6002 làm TIA (Transimpedance Amplifier, mạch khuếch đại chuyển dòng thành điện áp) → PA1/ADC
STM32F103 → UART/RS485 → laptop
```

| Đại lượng | Giá trị hiện tại | Ý nghĩa/giới hạn |
|---|---:|---|
| Nguồn thử dòng | 12 VAC cách ly | Cấp tải sơ cấp; không phải điện áp đo của ADC |
| Nguồn mạch module | Adapter 5 VDC; Blue Pill tạo 3,3 V | Đo 3,3 V thực khi hai MCP6002 và MAX3485 hoạt động |
| Nguồn PCB | 5 VDC vào LD1117S33TR; rail danh định 3,3 V | Kiểm tra dòng/nhiệt LDO theo file 2 |
| BIAS analog | 1,65 V danh định | Tâm tín hiệu AC để ADC một nguồn đọc được cả hai bán kỳ |
| Dải đầu vào ADC | Xấp xỉ 0–3,3 V khi VDDA = 3,3 V | Không để tín hiệu chạm hai rail; cần chừa dự phòng cho sai số, nhiễu và quá độ |
| Điện áp lưới | Không đo trong cấu hình hiện tại | Muốn đo cần cảm biến điện áp/cách ly, AFE và kênh ADC riêng được thiết kế phù hợp |

### 2. Dòng sơ cấp, CT và burden

**Phân biệt hai điện trở:** ba điện trở sứ 50 Ω–25 W là tải sơ cấp, mắc song song để tạo dòng chạy qua dây luồn CT. Burden 150 Ω là điện trở riêng mắc song song với thứ cấp CT để đổi dòng thứ cấp thành điện áp. Không thay thế chức năng của nhau.

Với nguồn 12 VAC lý tưởng và tải sứ 50 Ω:

| Số nhánh tải 50 Ω song song | Điện trở tương đương | Dòng sơ cấp ước tính |
|---:|---:|---:|
| 1 | 50 Ω | 12/50 = 0,24 A RMS |
| 2 | 25 Ω | 12/25 = 0,48 A RMS |
| 3 | 16,67 Ω | 12/16,67 ≈ 0,72 A RMS |

Đây là giá trị tính theo 12 VAC tại tải. Điện áp thứ cấp nguồn có thể sụt; dùng ampe kế/ampe kìm phù hợp để ghi dòng thực. Tải ba nhánh ở 0,72 A tiêu thụ xấp xỉ 8,64 W tổng, tức khoảng 2,88 W mỗi điện trở nếu chia đều; điện trở có thể nóng.

CT DL-CT08CL6-1000/1 được giả định có tỷ số 1000:1. PDF thông số tìm được ghi dòng định mức 5 A vào/5 mA ra, tải lấy mẫu định mức 50 Ω và 0,25 VAC tại điểm định mức; cùng bảng ghi dải đo 0–10 A với RL ≤30 Ω. Đây là tài liệu PDF do bên bán lưu trữ, chưa xác nhận là datasheet chính thức của nhà sản xuất. Vì vậy tỷ số và giới hạn tải cần được đối chiếu với nhà cung cấp/đo thực tế. Burden 150 Ω hiện là cấu hình lắp ban đầu cho module và PCB; module chỉ so sánh thêm 47 Ω (gần mức 50 Ω trong tài liệu), còn PCB giữ R2 = 150 Ω cho tới khi quyết định lại sau lab. Độ chính xác CT ở burden ngoài điều kiện hãng chưa được bảo đảm.

Với tỷ số giả định 1000:1, tải hình sin và burden thuần trở:

$$I_s=I_p/1000,\qquad V_{b,RMS}=I_sR_b,\qquad V_{b,peak}=\sqrt{2}V_{b,RMS}$$

Với BIAS danh định 1,65 V và burden 150 Ω, các mức ADC lý tưởng là:

| Dòng sơ cấp RMS | Dòng thứ cấp RMS | Điện áp burden RMS | ADC min–max quanh BIAS | Biên độ xấp xỉ ADC 12-bit* |
|---:|---:|---:|---:|---:|
| 0,24 A | 0,24 mA | 36 mV | 1,599–1,701 V | ±63 counts |
| 0,48 A | 0,48 mA | 72 mV | 1,548–1,752 V | ±126 counts |
| 0,72 A | 0,72 mA | 108 mV | 1,497–1,803 V | ±189 counts |
| 5 A | 5 mA | 750 mV | 0,589–2,711 V | ±1.316 counts |

*Giả thiết VDDA/VREF = 3,3 V, 12-bit, 4096 mức, tín hiệu hình sin, BIAS đúng 1,65 V, CT tuyến tính đúng tỷ số, không tính sai số/độ méo và mạch theo dõi được toàn biên độ. Đây là kiểm tra headroom ADC, không phải kiểm tra độ chính xác CT.

**Ví dụ ở 0,72 A:** $I_s=0,72/1000=0,72\,mA$. $V_{b,RMS}=0,72\,mA\times150\,Ω=108\,mV$. Đổi sang đỉnh: $108\,mV\times\sqrt2=153\,mV$. Cộng/trừ quanh BIAS: $1,65\pm0,153\,V=1,497\ldots1,803\,V$. Bước lượng tử ADC xấp xỉ $3,3/4096=0,806\,mV/count$, nên độ lệch đỉnh khoảng $153/0,806=190$ counts.

Burden 50 Ω tạo điện áp xấp xỉ một phần ba mức của 150 Ω (ví dụ 36 mV RMS thay vì 108 mV RMS ở 0,72 A). Vì vậy phép thử module chỉ so sánh **47 Ω với 150 Ω** ở cùng dòng: 47 Ω gần mức 50 Ω ghi trong tài liệu CT, còn 150 Ω là giá trị đang dùng và được dự kiến cho PCB. Mục đích là xem mức tín hiệu/nhiễu thay đổi thế nào; đây không phải phép kiểm độ chính xác CT.

| Burden Rb | Vb,RMS tính ở 0,72 A sơ cấp | Đỉnh quanh BIAS 1,65 V | Min–max ADC lý tưởng ở 0,72 A | Vb,RMS ở 5 A sơ cấp | Công suất burden ở 5 A |
|---:|---:|---:|---:|---:|---:|
| 47 Ω | 33,8 mV | ±47,9 mV | 1,602–1,698 V | 0,235 V | 1,18 mW |
| 150 Ω | 108,0 mV | ±152,7 mV | 1,497–1,803 V | 0,750 V | 3,75 mW |

Các số là **tính toán**, giả sử tỷ số CT 1000:1, tín hiệu hình sin, BIAS đúng 1,65 V và CT/AFE tuyến tính. Ở dòng thiết kế 5 A, mức 47 Ω cho biên lý tưởng khoảng 1,318–1,982 V; mức 150 Ω cho khoảng 0,589–2,711 V. Burden 47 Ω loại 0,25 W đủ công suất theo mô hình 5 mA; con 150 Ω–2 W đang có cũng dùng được, chỉ dư định mức công suất. Các giá trị này là kiểm tra headroom lý tưởng, không thay thế giới hạn burden của datasheet CT.

### 3. Băng thông và lọc analog

### 3.1. Loại lọc đang dùng trên từng nhánh

| Nhánh | Mạch hiện tại | Loại mạch/lọc | Chức năng và giới hạn |
|---|---|---|---|
| Dòng CT → PA0 | R3 = 1 kΩ nối tiếp tín hiệu; C12 = 100 nF từ PA0 xuống GND | **Lọc thông thấp RC** | Cho tín hiệu chậm như 50/60 Hz đi qua; làm nhỏ dần tín hiệu nhanh và nhiễu cao tần. Không có lọc thông cao riêng. |
| Photodiode → PA1 | MCP6002 chuyển dòng quang thành áp; Rf = 10 kΩ và Cf = 100 pF mắc hồi tiếp song song | **TIA có tụ hồi tiếp** | Cấu hình module nối thẳng chưa có tầng lọc riêng sau TIA; Cf không phải lọc thông cao. PCB bổ sung R11/C17 và R12/C18 làm hai tầng thông thấp trước ADC. |

Vì vậy, cấu hình hiện tại **không dùng lọc thông cao cho cả hai nhánh**. Nhánh dòng có một bộ lọc thông thấp RC rõ ràng. Nhánh quang trên module có Cf trong mạch TIA nhưng chưa có tầng lọc riêng; PCB theo file 2/file 3 bổ sung hai tầng thông thấp sau TIA. Không nên coi Cf hoặc các tầng RC chưa đo kiểm là bằng chứng chống alias đã đạt yêu cầu.

### 3.2. Nhánh dòng: lọc thông thấp RC

R3 = 1 kΩ và C12 = 100 nF tạo thành mạch thông thấp. Có thể hiểu đơn giản: tín hiệu dòng chậm đi qua, còn phần thay đổi rất nhanh bị C12 dẫn bớt xuống GND trước khi tới PA0.

Tần số tại đó mạch bắt đầu làm tín hiệu giảm đáng kể được ước tính bằng:

$$f_c=\frac{1}{2\pi RC}\approx1,59\,kHz$$

Ở 50 Hz, mạch giữ khoảng 99,95% biên độ nên gần như không làm đổi tín hiệu. Ở 9 kHz, biên độ chỉ còn khoảng 17,4%. Do đó, cấu hình này phù hợp để khảo sát dòng AC 50/60 Hz và vùng tần số thấp; nó làm suy giảm mạnh thành phần 9 kHz và các cạnh xung nhanh. Muốn giữ các thành phần nhanh hơn phải thiết kế lại bộ lọc và đo lại toàn nhánh.

**Lọc thông cao** là loại khác: nó giảm tín hiệu DC/thay đổi rất chậm và cho tín hiệu nhanh hơn đi qua. Trong sơ đồ hiện tại không có tầng thông cao riêng. CT cũng không đo được dòng DC ổn định, vì vậy chưa có lý do để thêm tầng này. Nếu thuật toán sau này cần bỏ trôi nền, phải xác định tần số cần giữ trước khi chọn lọc thông cao; đặt tần số cắt quá cao sẽ làm giảm cả tín hiệu 50/60 Hz.

### 3.3. Nhánh quang: TIA, không phải mạch lọc thông cao

Photodiode BPW34 (module) hoặc VBPW34S (PCB) tạo dòng điện khi nhận ánh sáng. TIA là viết tắt của **Transimpedance Amplifier**, nghĩa là **bộ khuếch đại chuyển dòng điện thành điện áp**. Trong mạch này, MCP6002 cùng điện trở hồi tiếp Rf làm nhiệm vụ đó để ADC đọc được tín hiệu quang. Với Rf = 10 kΩ, mức chuyển đổi lý tưởng là khoảng 10 mV cho mỗi 1 µA dòng quang. Cf = 100 pF mắc song song Rf là tụ hồi tiếp: tụ này giúp mạch ổn định và hạn chế đáp ứng ở tần số rất cao.

Tính riêng Rf và Cf cho ra mốc khoảng 159 kHz:

$$f_{RfCf}=\frac{1}{2\pi R_fC_f}\approx159\,kHz$$

Đây **không phải** cam kết rằng toàn nhánh quang đo chính xác tới 159 kHz. Đáp ứng thực còn phụ thuộc photodiode, MCP6002, dây nối và tải. Cấu hình PCB được chọn bổ sung hai tầng lọc thông thấp sau TIA (R11/C17 và R12/C18) trước PA1 để giảm thành phần nhanh. Mức lọc này chưa được xác nhận là đủ chống alias cho mọi mục tiêu; cần đo toàn nhánh và kiểm tra xung cần phát hiện.

### 3.4. Chống alias: tránh để ADC đọc nhầm tín hiệu nhanh

ADC không nhìn tín hiệu liên tục; nó chỉ đo điện áp tại từng thời điểm lấy mẫu. Nếu có tín hiệu nhanh hơn tốc độ lấy mẫu, các điểm đo có thể tạo ra một hình dạng chậm giả. Hiện tượng đó gọi là **alias**. Khi mẫu giả đã được tạo ra, lọc bằng phần mềm sau ADC không thể khôi phục tín hiệu gốc.

Cách hạn chế là làm nhỏ tín hiệu quá nhanh bằng **lọc thông thấp đặt trước ADC**, đồng thời chọn tốc độ lấy mẫu phù hợp. Với CT, R3/C12 đã là một lọc thông thấp và có tác dụng giảm một phần tín hiệu nhanh, nhưng chưa chắc đã giảm đủ cho mọi mục tiêu. Với photodiode, Cf thuộc mạng hồi tiếp TIA; chưa có tầng chống alias riêng được xác nhận. Vì thế không thể kết luận cả hai kênh đã chống alias đầy đủ.

Ví dụ: lấy mẫu CT ở 32 ksample/s nghĩa là ADC đọc cách nhau 31,25 µs; giới hạn lý thuyết để phân biệt tần số là 16 kHz. Với photodiode ở 50 ksample/s, giới hạn lý thuyết là 25 kHz. Tín hiệu cao hơn các giới hạn này có thể hiện thành tín hiệu chậm giả, nên phải giảm chúng bằng lọc analog trước ADC. R3/C12 của CT đã làm giảm tín hiệu cao tần, nhưng chưa được kiểm chứng cho mọi mục tiêu. Tụ Cf của TIA quang không được mặc định là đủ để làm việc đó; nhánh quang cần được đo và đánh giá bộ lọc trước ADC riêng.

#### Phương án thử lọc sau TIA quang

Để đánh giá ảnh hưởng của lọc mà chưa đổi mạch TIA, có thể thử một lọc thông thấp thụ động hai tầng sau đầu ra MCP6002 quang:

```text
MCP6002 quang OUT → R11 1 kΩ → điểm X → R12 1 kΩ → PA1/ADC
                                  |                         |
                               C17 10 nF                 C18 10 nF
                                  |                         |
                                 GND                       GND
```

Mỗi tầng 1 kΩ/10 nF có tần số cắt riêng khoảng 15,9 kHz. Khi mắc nối tiếp, hai tầng làm giảm tín hiệu nhanh hơn một tầng: mô hình lý tưởng giảm khoảng 14 dB tại 25 kHz và 22 dB tại 50 kHz. Đây là mức giảm có thể đo được, **không mặc nhiên đủ để tuyên bố chống alias đạt yêu cầu**. Tầng lọc cũng làm chậm cạnh xung. Mô hình lý tưởng dự kiến giữ gần nguyên đỉnh xung 100 µs, nhưng chỉ còn khoảng một phần năm đỉnh của xung 10 µs; cần đo bằng LED xung để xác nhận với mạch thực.

Trên module, thử lần lượt **TIA nối thẳng tới PA1** và **TIA qua hai tầng RC** để thấy rõ ảnh hưởng của lọc. Giữ nguyên LED, khoảng cách, độ rộng xung, mức sáng, `fs` và cài đặt oscilloscope. Dùng `fs = 100 ksample/s` (`T_sampling = 10 µs`) cho phép thử xung 100 µs; ghi độ rộng, đỉnh, thời gian lên/xuống, trễ, số xung nhận/bỏ sót và nhiễu. Nếu ứng dụng cần bắt xung ngắn hơn 100 µs, số đo phải được dùng để đánh giá lại cấu hình lọc. Hai tầng RC là cấu hình PCB đã chọn và được liệt kê trong BOM file 2; phép so sánh trên module nhằm đánh giá đáp ứng, không phải để xác định chúng có thuộc BOM hay không.

### 4. Tốc độ lấy mẫu riêng cho từng cảm biến

Tốc độ lấy mẫu cho biết ADC đọc một kênh bao nhiêu lần mỗi giây. Chu kỳ lấy mẫu là thời gian giữa hai lần đọc liên tiếp của cùng kênh:

$$T_{sampling}=1/f_s$$

Ví dụ, 50 ksample/s nghĩa là đọc 50.000 lần mỗi giây, cách nhau 20 µs. Quy tắc tối thiểu về lý thuyết là lấy mẫu nhanh hơn hai lần tần số cao nhất cần đo. Nhưng chỉ vừa đủ hai mẫu thường không cho thấy rõ hình dạng sóng. Để khảo sát ban đầu, dùng khoảng 5–10 mẫu cho mỗi chu kỳ nhanh nhất cần giữ; với xung thì dùng khoảng 5–10 mẫu trong xung ngắn nhất cần phát hiện. Các con số này là điểm bắt đầu để thử, không thay cho việc kiểm tra mạch analog.

| Kênh/cảm biến | Mục tiêu hiện tại | fs khởi đầu mỗi kênh | T_sampling | Điều kiện/giới hạn |
|---|---|---:|---:|---|
| CT dòng | Dạng sóng 50/60 Hz và vùng thấp; hiện RC giới hạn khoảng 1,59 kHz | 32 ksample/s | 31,25 µs | Mốc khảo sát; phải xác nhận timer/ADC DMA và RC. Không thể tuyên bố đo hài 9 kHz với RC hiện tại. |
| CT dòng, phương án băng thông cao hơn | Nếu yêu cầu giữ dạng sóng đến 9 kHz | 50–100 ksample/s | 20–10 µs | Tương ứng khoảng 5,6–11 mẫu/chu kỳ tại 9 kHz; yêu cầu thay/thiết kế lại AFE và anti-alias trước. |
| Photodiode | Phát hiện biến thiên ánh sáng; độ rộng xung tối thiểu chưa được chốt | 50 ksample/s | 20 µs | Mốc thử ban đầu, khoảng 5 mẫu trên xung 100 µs. Kiểm tra băng thông/ổn định toàn TIA. |
| Photodiode, xung ngắn | Nếu yêu cầu phát hiện xung cỡ 100 µs hoặc ngắn hơn | Từ 100 ksample/s | 10 µs hoặc thấp hơn | 100 ksample/s cho khoảng 10 mẫu trên xung 100 µs; xung ngắn hơn cần fs cao hơn và xác nhận giới hạn MCP6002/AFE/ADC. |

Các mốc này là giá trị thiết kế để thử, **chưa phải cấu hình firmware hoặc kết quả đã đo**. Ghi riêng fs và T_sampling của CT và photodiode. Khi quét tuần tự hai kênh, tổng tốc độ chuyển đổi ADC phải đủ cho tổng số mẫu; cấu hình ADC sampling time cần phù hợp trở kháng nguồn. Dùng timer/trigger và DMA/buffer cho thu nhanh. Chu kỳ log/RS485 500 ms không phải chu kỳ lấy mẫu và không dùng để tính RMS 50/60 Hz hoặc bắt xung.

### 4.1. Đặc tả xung và lựa chọn tốc độ lấy mẫu

Muốn nói cảm biến “bắt được xung”, trước hết cần quy định xung ngắn nhất phải phát hiện và mức tín hiệu cần nhận ra. Chưa có số đo hồ quang hoặc yêu cầu cụ thể thì chưa biết xung hồ quang ngắn nhất là bao lâu. Thử bằng LED chỉ cho biết mạch phản ứng thế nào với LED đó, không chứng minh đã phát hiện được mọi hồ quang.

Trước khi chốt, ghi rõ các đại lượng sau:

| Đại lượng của phép thử xung | Cần ghi |
|---|---|
| Độ rộng xung nhỏ nhất $t_{p,min}$ | Thời gian sáng của từng xung; đây là đầu vào để tính fs |
| Sườn lên/xuống | Thời gian chuyển mức của nguồn sáng; cạnh nhanh hơn cần băng thông analog cao hơn |
| Mức tín hiệu | Mức nền và đỉnh tại đầu ra TIA/ADC, độ tương phản so với nền và ngưỡng phát hiện; không dùng mức lux nếu không có thiết bị đo lux phù hợp |
| Dạng lặp | Một xung hay chuỗi xung, chu kỳ lặp/khoảng cách giữa xung và thời gian quan sát |
| Điều kiện quang | Loại LED/bước sóng, khoảng cách, góc chiếu, che chắn, ánh sáng nền và vị trí cảm biến; giữ cố định khi so sánh |
| Tiêu chí đạt | Có/không phát hiện, trễ phát hiện, xung bị bỏ sót/báo giả và có clipping/bão hòa hay không |

Muốn có $N$ lần đọc trong xung ngắn nhất, có thể ước lượng tốc độ lấy mẫu như sau:

$$f_s\geq\frac{N}{t_{p,min}},\qquad T_{sampling}\leq\frac{t_{p,min}}{N}$$

Ví dụ, xung dài 100 µs có khoảng 5 mẫu nếu lấy mẫu ở 50 ksample/s (mỗi 20 µs), hoặc khoảng 10 mẫu ở 100 ksample/s (mỗi 10 µs). Xung dài 10 µs cần khoảng 500 ksample/s để có 5 mẫu, hoặc 1 Msample/s để có 10 mẫu. Đây mới là phép tính số mẫu; cần kiểm tra ADC, firmware và mạch cảm biến có chạy/đáp ứng được tốc độ ấy không.

Lấy mẫu nhanh không làm cho mạch analog phản ứng nhanh hơn. Nếu photodiode/TIA/lọc phản ứng chậm, xung vẫn bị tù và thấp trước khi tới ADC. Vì vậy cần thử cả chuỗi bằng xung LED có độ rộng và cạnh đã biết; so sánh xung điều khiển, điện áp đầu ra TIA và số ADC để xem có trễ, mất đỉnh, dao động hoặc chạm giới hạn điện áp không. Không thể xác định tốc độ thật chỉ bằng phép tính RfCf hoặc thông số riêng của photodiode.

**Phép thử xung an toàn cho module/PCB:** dùng LED nhìn thấy được điều khiển bởi bộ phát xung hoặc vi điều khiển, với mức sáng và khoảng cách cố định; không tự tạo hồ quang. Bắt đầu bằng xung rộng, giảm dần độ rộng; lưu xung điều khiển tham chiếu cùng dạng sóng MCP6002 quang chân 1/ADC, $f_s$, $T_{sampling}$ thực, min/max, số xung phát hiện/bỏ sót, độ trễ và điều kiện quang. Dùng oscilloscope có tốc độ lấy mẫu phù hợp để xác nhận độ rộng và sườn LED; phép thử LED không xác nhận độ nhạy với hồ quang thực.

### 5. Tiêu chuẩn và tài liệu tham khảo

Không có một tiêu chuẩn duy nhất quy định mọi giá trị dòng, điện áp, tần số lọc và fs cho mạch này. Chọn tài liệu theo câu hỏi kỹ thuật; datasheet đúng mã CT/photodiode/op-amp/MCU quyết định giới hạn linh kiện. Tiêu chuẩn cho phương pháp đo hoặc thiết bị hoàn chỉnh không tự động chứng minh prototype tuân thủ.

| Cần xác định/đánh giá | Tài liệu tham khảo | Áp dụng cho dự án |
|---|---|---|
| Phương pháp đo thông số chất lượng điện AC 50/60 Hz, gồm dòng/hài | [IEC 61000-4-30:2025](https://webstore.iec.ch/en/publication/71611) | Tham khảo khi định nghĩa phép đo và cách diễn giải; tiêu chuẩn có lớp phương pháp đo A/S, không đưa một fs chung cho mọi đại lượng. |
| Thiết bị/phương pháp đo hài và liên hài nguồn điện | [IEC 61000-4-7](https://webstore.iec.ch/en/publication/4226) | Tham khảo nếu cần phân tích hài; xem giới hạn băng thông và phương pháp, không chọn fs chỉ từ nhãn “9 kHz”. |
| Dùng CT trong đo chất lượng điện và ảnh hưởng biến dòng | [IEC TR 61869-103:2012](https://webstore.iec.ch/en/publication/6049) | Hướng dẫn cách xét biến dòng/biến áp đo trong hệ thống đo power quality. |
| Đánh giá độ chính xác biến dòng đo | [IEC/IEEE 61869-21:2025](https://webstore.iec.ch/en/publication/84093) | Tham khảo quy trình/độ không đảm bảo khi kiểm thử độ chính xác instrument transformer; không thay datasheet CT. |
| Thiết bị phát hiện/bảo vệ hồ quang dân dụng, mạch AC | [IEC 62606:2013+A1:2017+A2:2022](https://webstore.iec.ch/en/publication/80273) | Phạm vi AFDD cho hộ gia đình và mục đích tương tự; chỉ tham khảo nếu phạm vi sản phẩm phù hợp. Prototype này chưa có chức năng ngắt/bảo vệ nên không được coi là AFDD đạt chuẩn. |
| Phát hiện/giảm thiểu hồ quang nội bộ trong tủ đóng cắt hạ áp bằng cảm biến quang | [IEC 60947-9-2:2021](https://webstore.iec.ch/en/publication/60114) | Tham khảo đúng hướng hơn nếu xét hệ thống bảo vệ hồ quang trong switchgear; thiết bị hiện tại chưa có cơ cấu mitigation/trip. |
| Định nghĩa kiểm thử đáp ứng xung của mạch quang | Không có một tiêu chuẩn trong danh sách này chỉ định độ rộng xung quang hoặc $T_{sampling}$ cho prototype | Xác định $t_{p,min}$ từ yêu cầu ứng dụng, tính fs theo số mẫu/xung, rồi đo cả đáp ứng AFE và ADC. IEC 60947-9-2 là tham chiếu cấp thiết bị bảo vệ, không cung cấp ngưỡng xung tùy ý cho prototype này. |
| Yêu cầu chung, EMC và an toàn cho rơ-le/bảo vệ | [IEC 60255-1:2022](https://webstore.iec.ch/en/publication/59762), [IEC 60255-26:2023](https://webstore.iec.ch/en/publication/62084), [IEC 60255-27:2023](https://webstore.iec.ch/en/publication/63370) | Chỉ đi sâu nếu hướng tới thiết bị bảo vệ công nghiệp; không phải chuẩn chọn burden hoặc tần số lấy mẫu riêng cho từng cảm biến. |

### 6. Quy trình chốt thông số cho mỗi kênh

1. Xác định đại lượng và dải cần đo: dòng sơ cấp 0–5 A thiết kế; dòng lab đã thử hiện tới khoảng 0,72 A; ánh sáng/xung cần phát hiện phải định nghĩa bằng khoảng cách, nguồn sáng và độ rộng xung tối thiểu.
2. Chốt đúng sensor và datasheet; ghi tỷ số CT, tải thứ cấp, dòng tối đa/tuyến tính, đáp ứng tần số; với photodiode ghi độ nhạy phổ, dòng quang, điện dung và đáp ứng.
3. Tính burden/TIA và bias; kiểm tra giá trị RMS/peak, đầu ra op-amp, min/max ADC cùng dự phòng trước khi gắn ADC.
4. Xác định phần tín hiệu cần giữ, rồi chọn lọc thông thấp để giảm tín hiệu quá nhanh trước ADC. Chọn bộ lọc cùng tốc độ lấy mẫu để hạn chế alias (mẫu giả do ADC lấy quá thưa); chỉ thêm lọc thông cao nếu cần bỏ thành phần chậm/DC và tần số cắt không làm mất tín hiệu hữu ích.
5. Chọn fs và tính $T_{sampling}=1/f_s$ riêng cho từng kênh; kiểm năng lực ADC, thời gian sample/convert, DMA và dung lượng buffer.
6. Kiểm thử bằng nguồn/dụng cụ tham chiếu; lưu cấu hình, fs/T thực, min/max, dạng sóng, sai số và điều kiện thử. Chỉ gọi là kết quả đã xác nhận sau khi đo.

Các phép tính nguồn, nhiệt LDO, thạch anh, linh kiện và footprint riêng cho PCB nằm ở [file 2](02_Thiet_ke_phan_cung_PCB_SMD.md).


## C. Chuẩn bị và kiểm thử tại lab buổi 1

### 1. Chuẩn bị và kiểm tra tại nhà

1. Kiểm tra cực tính jack và điện áp 5 V/3,3 V trước khi nối AFE.
2. Kiểm tra MCP6002 dòng/MCP6002 quang cấp 3,3 V; BIAS gần 1,65 V. Điểm M trước đệm khác net BIAS sau đệm.
3. Đo MCP6002 dòng chân 1, PA0 và MCP6002 quang chân 1 so với GND; xác nhận phù hợp dải ADC 0–3,3 V trước khi nối ADC.
4. Kiểm tra MCP6002 dòng chân 2 hồi tiếp về MCP6002 dòng chân 1 trước R lọc; R 1 kΩ không bị nối tắt; C 100 nF (104) từ PA0 xuống GND.
5. Build/nạp ST-Link; kiểm tra ADC hai kênh và RS485 theo sơ đồ nối ở file 3 và trình tự firmware RS485 bên dưới: **PA9 TX → DI; RO → PA10 RX; PB0 → chung DE và /RE; PB1 để trống.** Khởi tạo PB0 thấp; thử gửi/nhận và thời điểm trả về nhận theo hướng dẫn dưới đây, chưa coi cấu hình mới đã được kiểm thử.
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

Phần B cho biết tín hiệu nào cần giữ, bộ lọc đang có và tốc độ lấy mẫu cần khảo sát. Phần C kiểm tra các ý đó bằng cách đo cùng tín hiệu ở hai điểm: với CT, so đầu ra trước RC với PA0 sau RC; với quang, so đầu ra TIA với PA1 sau lọc. Trên module có thể nối PA1 thẳng hoặc lắp tạm hai tầng RC; PCB mặc định dùng hai tầng RC theo file 2 và file 3. Do đó, kết quả đo trên module chỉ mô tả cấu hình đã thử, không phải kết quả đo PCB. Xem [phần B](#b-cơ-sở-tính-toán-và-thông-số-đo) để đối chiếu tần số cắt và tốc độ lấy mẫu.

Khi thu nhanh, dùng timer/trigger và ADC DMA/buffer; ghi N, fs thực, `T_sampling`, đơn vị và firmware riêng cho từng kênh. Không suy ra fs từ chu kỳ UART/log. Log chậm khoảng 500 ms/bản tin chỉ theo dõi xu hướng, không tính RMS 50/60 Hz hay bắt xung ngắn; lưu buffer rồi truyền sau thay vì gửi từng mẫu ASCII. So sánh trước/sau lọc chỉ có ý nghĩa khi cùng tín hiệu vào, cùng tốc độ lấy mẫu và cùng cài đặt đo; phép so sánh đó cho biết bộ lọc làm tín hiệu đổi thế nào, chưa tự chứng minh lọc chống alias đã đủ.

| Cách thu | Chuẩn bị | Dùng để làm gì | Không được suy ra |
|---|---|---|---|
| Log chậm khoảng 500 ms/bản tin | Ghi chu kỳ thực, SEQ và định dạng; firmware điều khiển PB0 đúng trình tự ở C | Theo dõi nền/quang, liên tục truyền, reset | Không tính RMS AC từ các giá trị dòng tức thời cách 500 ms |
| ADC nhanh nếu đã có firmware | Dùng fs và `T_sampling` theo từng kênh như phần B; thu đều vào bộ đệm, gửi sau | Giữ dạng sóng để hiệu chuẩn/phân tích | Mốc thiết kế chưa phải tốc độ lấy mẫu đã đo; phải kiểm tra băng thông AFE và thời điểm trigger thực |
| CSV oscilloscope | Ghi kênh, đơn vị V, thời gian và cài đặt máy | Phân tích điện áp trước/sau lọc | Không gọi là ADC count |

Ví dụ lựa chọn thu nhanh cho nhánh dòng: **6400 mẫu / 32.000 mẫu/s = 0,2 s**, tương ứng 10 chu kỳ nếu đúng 50 Hz. Không gửi từng mẫu ASCII ở 9600 baud khi đang thu nhanh. Chưa cần chốt hệ số ADC → ampere để chọn linh kiện; phải giữ dữ liệu gốc và điều kiện thu: dòng tham chiếu, burden/RC, firmware, số mẫu N, fs và T_sampling thực của từng kênh, đơn vị và tên file.

### 2. Thực hiện tại lab buổi 1

**Trình tự:** I kiểm thử nhánh dòng (dòng tải thực + CT/burden + RC) → II kiểm thử nhánh quang → III kiểm thử tích hợp 10 phút.

Trước khi cấp tải, người phụ trách phòng thí nghiệm cần xác nhận nguồn AC cách ly, thiết bị bảo vệ và cách nối mass oscilloscope; đối chiếu các yêu cầu tại mục A.1.10. Burden phải luôn được mắc kín khi có dòng qua CT. Ngắt nguồn trước khi thay đổi dây dẫn hoặc cấu hình tải. Phạm vi thử nghiệm không bao gồm việc tạo hồ quang.

### I. Kiểm thử khối dòng

**Mục tiêu:** kiểm tra tín hiệu theo dòng tải, biên áp phù hợp ADC và tác dụng của bộ lọc. Đo dòng tham chiếu, trước lọc và sau lọc trong **cùng một lượt thử**.

**Cấu hình nền:** một lượt dây sơ cấp qua CT; burden 150 Ω–2 W; MCP6002 dòng cấp 3,3 V; RC 1 kΩ–100 nF (104) lắp cố định. Đo bốn mức tải với 150 Ω trước, sau đó so sánh riêng 47 Ω với 150 Ω; chỉ thay burden, giữ nguyên CT, AFE, RC, dây và cài đặt oscilloscope.

#### I.1. Chuẩn bị và nối dụng cụ

1. Nối tải theo A.1.10: nguồn 12 VAC cách ly → một dây qua CT → tải → về nguồn AC; CT ở dây chung trước điểm chia nhánh. Mạch đo dùng nguồn 5 VDC riêng.
2. Đồng hồ V~ song song tải; đồng hồ A~ nối tiếp dây chung hoặc ampe kìm phù hợp dòng nhỏ kẹp một dây. Không mắc thang dòng vào hai đầu nguồn.
3. CH1 tại **MCP6002 dòng chân 1 trước lọc**, CH2 tại **PA0 sau lọc**; hai mass cùng GND, không tại BIAS. Kiểm hồi tiếp MCP6002 dòng chân 2 về MCP6002 dòng chân 1 trước R, không có dây nối tắt R lọc.
4. Đo nguồn 3,3 V tại MCP6002 dòng và BIAS tại MCP6002 dòng chân 7; xử lý nguồn/nền sai trước khi đánh giá CT. Oscilloscope bắt đầu DC coupling, 5 ms/div; chỉnh V/div để thấy sóng quanh BIAS, hệ số probe trên máy khớp probe thực.

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

| Tải | V tải thực (V RMS) | I thực (A RMS) | BIAS (V) | MCP6002 dòng chân 1 trước lọc min/max (V) | PA0 sau lọc min/max (V) | Nhận xét / file |
|---|---|---|---|---|---|---|
| Không dòng | — | … | … | … / … | … / … | … |
| Một R | … | … | … | … / … | … / … | … |
| Hai R | … | … | … | … / … | … / … | … |
| Ba R | … | … | … | … / … | … / … | … |

“Không dòng” là tải thực sự không có dòng; nếu dụng cụ không đọc 0, ghi giá trị và điều kiện. Nếu I khác dự kiến, kiểm điện áp, giá trị R và cách mắc trước khi kết luận CT sai. Nếu dạng sóng bất thường, kiểm dây qua CT → burden → nguồn/BIAS → chân MCP6002 dòng rồi mới xem xét đổi linh kiện.

**Lượt so sánh burden:** so **47 Ω (0,25 W, 5%) với 150 Ω (2 W đang có)** ở cùng dòng sơ cấp thực. Dùng ít nhất một mức thấp và mức cao nhất đã đo được (dự kiến tối đa khoảng 0,72 A); giữ nguyên CT, AFE, RC, dây, BIAS, vị trí probe và cài đặt oscilloscope. Mỗi lần: ngắt nguồn tải, xác nhận dòng sơ cấp đã về 0, thay burden, kiểm tra điện trở mắc kín song song thứ cấp CT rồi mới cấp lại tải. Không chuyển mạch khi đang có dòng và không để thứ cấp CT hở. Đọc CH1 ở đầu ra đệm trước R lọc để so biên độ, CH2 tại PA0 sau lọc. Không kẹp mass oscilloscope vào hai đầu burden để đo vi sai. Đây chỉ là so mức tín hiệu/nhiễu trong dải lab, không xác nhận độ chính xác CT hay vận hành ở 5 A.

| Rb danh định | Dung sai / công suất | I sơ cấp thực (A RMS) | BIAS (V) | CH1 trước lọc min/max (V) | PA0 sau lọc min/max (V) | Dạng sóng / clipping / nhiễu / file |
|---:|---|---:|---:|---|---|---|
| 47 Ω | 5% / 0,25 W | … | … | … / … | … / … | … |
| 150 Ω | 2 W, đo/ghi dung sai thực nếu cần | … | … | … / … | … / … | … |

Lặp lại bảng cho mỗi mức tải muốn so. Nếu điện trở 5% làm kết quả biên độ không khớp trị số danh định, đo Rb thực bằng đồng hồ khi đã tháo nguồn; ghi trị số thực, không tự hiệu chỉnh số đo để khớp lý thuyết.

#### I.3. Xử lý và tính toán sau khi có số liệu

Phần tính trước dùng đúng ba mức tải ở I.2. Sau khi đo, thay bằng số liệu thực của từng hàng để đối chiếu; các bảng kết quả thực để trống đến khi có dữ liệu.

##### a. Đối chiếu bộ tải 12 VAC

Với mỗi R = 50 Ω và n = 1, 2, 3 tải song song:

$$R_{eq}=R/n;\qquad I_{load}=V_{RMS}/R_{eq};\qquad P_{total}=V_{RMS}^2/R_{eq}$$

R tương đương lần lượt 50 Ω, 25 Ω và khoảng 16,67 Ω. Ở 12 V, mỗi R nhận 12²/50 = **2,88 W**; tổng dòng/công suất dự kiến xem D.I.2. Khi phân tích phải dùng điện áp và dòng đo thực. Bộ thử dự kiến khoảng 0,72 A, không bắt buộc đạt định mức nguồn 1,5 A.

##### b. Đối chiếu CT, burden và biên độ trước/sau lọc

Điều kiện mô hình: một lượt dây sơ cấp; tỷ số CT **giả thiết 1000:1**, chưa có datasheet hãng đúng CT; so Rb = 47 Ω và 150 Ω; MCP6002 dòng đệm gain 1; dòng gần hình sin. BIAS lấy từ số đo MCP6002 dòng chân 7.

$$I_s=I_p/1000;\quad V_{b,RMS}=I_sR_b;\quad V_{b,peak}=\sqrt{2}V_{b,RMS}$$
$$V_{out,min/max}=V_{BIAS}\mp V_{b,peak};\qquad P_b=I_s^2R_b$$

Hệ số √2 chỉ dùng cho hình sin. Từ min/max thực:

$$V_{peak,đo}=(V_{max}-V_{min})/2;\qquad V_{tâm}=(V_{max}+V_{min})/2$$
$$V_{pp}=V_{max}-V_{min};\qquad G_{đo}(\%)=100\times V_{pp,sau}/V_{pp,trước}$$

**Bảng tính trước theo đúng các mức tải ở I.2:** bảng gốc dưới đây dùng burden 150 Ω; so sánh năm giá trị có bảng lý thuyết ở phần B.2 và bảng ghi số đo ở I.2. Giả thiết nguồn tải đúng 12 VAC, tải đúng 50 Ω mỗi nhánh, tỷ số CT 1000:1, dòng hình sin, BIAS = 1,650 V và op-amp lý tưởng. Đây là kết quả tính từ giả thiết, **không phải min/max đã đo**.

| Tải | Ip dự kiến (A RMS) | Is tính (mA RMS) | Vb,RMS tính (V) | Vb,peak tính (V) | MCP6002 dòng chân 1 min/max lý thuyết (V) | Pb tính (mW) |
|---|---:|---:|---:|---:|---|---:|
| Không dòng | 0,00 | 0,00 | 0,000 | 0,0000 | 1,6500 / 1,6500 | 0,00000 |
| Một R | 0,24 | 0,24 | 0,036 | 0,0509 | 1,5991 / 1,7009 | 0,00864 |
| Hai R | 0,48 | 0,48 | 0,072 | 0,1018 | 1,5482 / 1,7518 | 0,03456 |
| Ba R | 0,72 | 0,72 | 0,108 | 0,1527 | 1,4973 / 1,8027 | 0,07776 |

**Khi có số đo:** với lượt nền dùng 150 Ω, làm lần lượt từng hàng không dòng / một R / hai R / ba R ở I.2. Với lượt so sánh, dùng Rb thực của 47 Ω và 150 Ω cùng I sơ cấp thực ở một mức tải giống nhau để tính lại $V_{b,RMS}=(I_p/1000)R_b$ và $V_{b,peak}=\sqrt2V_{b,RMS}$. Dùng BIAS thực từ chân 7 để tính biên áp dự kiến; không dùng bảng danh định thay số đo. Lấy min/max CH1 thực để tính Vpeak,đo và Vtâm; lấy min/max CH1/CH2 thực để tính Gđo. So sánh tăng biên độ với nhiễu, méo/clipping và headroom ADC. Không tự điền min/max, nhiễu hoặc phần trăm sai lệch khi chưa đo.

| Tải | Vpeak trước lọc tính từ Ip thực (V) | Vpeak trước lọc từ CH1 thực (V) | Vtâm CH1 thực (V) | Gđo từ CH1/CH2 thực (%) | Nhiễu trước/sau thực (mVpp) |
|---|---|---|---|---|---|
| Không dòng | … | … | … | Không dùng tỷ số khi biên độ gần 0 | … / … |
| Một R | … | … | … | … | … / … |
| Hai R | … | … | … | … | … / … |
| Ba R | … | … | … | … | … / … |

Không dùng tỷ số biên độ khi tín hiệu trước gần 0. Đối chiếu đúng CT về tỷ số, dòng/tần số, tải thứ cấp cho phép và điều kiện sai số; đối chiếu biên ra MCP6002 theo tải. Tín hiệu nằm trong dải ADC chưa chứng minh CT chính xác với burden 150 Ω. Chênh giữa tính và đo gồm cả ảnh hưởng mô hình, dụng cụ và linh kiện, không phải độ chính xác riêng CT.

**Dải thử:** ghi theo dòng thực lớn nhất đo được; khoảng 0,72 A chỉ là dự kiến. Nguồn 1,5 A là định mức nguồn, không phải một mức thử. Mốc 5 A ở phần B chỉ phục vụ tính thiết kế, không phải dòng đã thử tại lab và không đại diện dòng sự cố LV/MV.

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

#### I.4. Đánh giá và hồ sơ kết quả

- **CT/burden:** dòng tăng thì biên độ trước lọc có tăng không; tâm sóng có gần BIAS đo được không; tắt tải có về nền không; có cắt đỉnh/méo/dao động bất thường không?
- **RC:** so biên độ và nhiễu trước/sau cùng mức tải, cùng cài đặt. Khi tín hiệu trước lọc gần 0, so nền/nhiễu riêng, không dùng tỷ số biên độ.
- **ADC:** kiểm min/max và khoảng dự phòng thực. Nằm trong 0–3,3 V chưa đủ chứng minh burden phù hợp CT.
- **Lựa chọn:** có thể giữ RC ban đầu nếu gần giữ biên độ 50 Hz, không méo/dao động bất thường và giảm nhiễu quan sát. Chưa xác nhận chống alias, đáp ứng tần số cao hoặc giữ đặc trưng nhanh hồ quang. Burden 150 Ω còn phải đối chiếu đúng datasheet CT và biên ra MCP6002; chưa đủ căn cứ thì giữ là phương án thử.

**Hồ sơ cần lưu:** bảng đo, ảnh/CSV của hai kênh, cài đặt thiết bị đo, ảnh mạch và cấu hình cuối. Nếu thu ADC, lưu kèm phiên bản firmware và thông số lấy mẫu tại mục C.1. Dải thử nghiệm được xác định theo **dòng thực lớn nhất đã đo**; định mức nguồn 1,5 A và mốc thiết kế PCB 5 A không đại diện cho dải đã thử.

Mẫu kết luận: “Nhánh dòng được thử đến … A RMS; burden … Ω cho biên độ trước lọc …, tâm sóng …; RC … cho tỷ lệ biên độ … và nhiễu … trong điều kiện … . Giữ cấu hình ban đầu / cần kiểm tra …; tải CT cho phép và băng thông cho thuật toán còn phải xác nhận.”

### II. Kiểm thử khối quang

**Mục tiêu:** kiểm tra chuyển ánh sáng thành điện áp, quan sát dao động dưới ánh sáng cố định và đo ảnh hưởng của mạng lọc thông thấp đã chọn cho PCB tới đáp ứng xung quang.

1. Cấp nguồn 3,3 V cho MCP6002 quang; sử dụng Rf = 10 kΩ và Cf = 100 pF (101). Có thể sử dụng lại dữ liệu CHE–PHONG–DEN đã thu trước đó nếu cấu hình mạch không thay đổi.
2. Đo 5 V, 3,3 V tại AFE, BIAS và dao động nền.
3. Probe MCP6002 quang chân 1, mass GND. Giữ sáng cố định, quan sát và lưu ảnh; chiếu/che xác nhận phản ứng.
4. Ghi mức đèn, khoảng cách và cách che. Không quy đổi đèn pin thành lux/năng lượng hồ quang khi chưa đo.
5. Sau phép đo sáng/che tĩnh, trên module thử cấu hình PA1 nối thẳng và cấu hình hai tầng RC R11/C17/R12/C18 nêu tại phần B.3.4. Dùng cùng LED xung 100 µs và cùng `fs`; ghi riêng dữ liệu của hai cấu hình. PCB theo file 2 và file 3 sử dụng mặc định hai tầng RC.
6. Nếu thay Rf/Cf, ghi cấu hình mới và đo lại; không gộp dữ liệu của các cấu hình khác nhau.

| Đại lượng/điều kiện | Kết quả | Ảnh/dữ liệu gốc |
|---|---|---|
| 5 V so với GND | … V | … |
| 3,3 V tại MCP6002 quang chân 8–MCP6002 quang chân 4 | … V | … |
| BIAS | … V; … mVpp | … |
| MCP6002 quang chân 1, ánh sáng cố định | … V; dao động … | … |
| MCP6002 quang chân 1 khi che / chiếu | … / … V | … |
| Rf / Cf thực | … Ω / … pF | … |
| Lọc PA1 | Nối thẳng / hai tầng RC 1 kΩ–10 nF | … |
| Xung LED tham chiếu | Độ rộng … µs; `fs` … ksample/s | … |
| Đầu ra TIA / PA1 sau lọc | Đỉnh … / … V; trễ … µs | … |
| Đèn / khoảng cách / cài đặt máy | … | … |

$$\Delta V=V_{sáng}-V_{che};\qquad \Delta I_{photo}=\Delta V/R_f$$

Thay Vsáng và Vche bằng **số đo ở hàng MCP6002 quang chân 1 khi che / chiếu** trong bảng trên, Rf bằng giá trị thực đang lắp. Với Rf danh định 10 kΩ, ΔIphoto (µA) = 100 × ΔV (V). Chưa có số đo thì để trống ΔV và ΔIphoto; không tự gán điện áp che/sáng hoặc giới hạn đầu ra.

$$f_{RfCf}=\frac{1}{2\pi R_fC_f}\approx159\ \mathrm{kHz}$$

Mốc này là cực của mạng hồi tiếp, **không phải băng thông thực toàn TIA**. Chọn Cf còn phụ thuộc điện dung photodiode, đầu vào op-amp và ký sinh; xem nguồn F.

**Tiêu chí đánh giá:** nếu đầu ra phân biệt được giữa điều kiện chiếu sáng và che, không tiến sát biên hoạt động, đồng thời không xuất hiện dao động bất thường trong điều kiện quan sát đã ghi nhận, cấu hình 10 kΩ/100 pF (101) có thể được giữ làm phương án ban đầu. Phép quan sát ở thang thời gian chậm không loại trừ dao động nhanh; cần thiết bị có băng thông phù hợp để đánh giá bổ sung khi cần.

**Hồ sơ kết quả:** lưu ảnh dạng sóng ở điều kiện chiếu sáng cố định, số liệu che/sáng/nền, nguồn cấp và cấu hình đo. Mẫu kết luận: “Nhánh quang với Rf … và Cf … có phản ứng … trong điều kiện …; không ghi nhận dao động tại cài đặt …; đáp ứng xung, mức bão hòa dưới ánh sáng hồ quang và khoảng cách phát hiện chưa được kiểm chứng.”

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

| Thời điểm | Tải | 5 V thực (V) | 3V3 Blue Pill (V) | VCC module nhận/phát (V) | BIAS MCP6002 dòng (V) |
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

### 3. Sau lab: chuyển số đo sang lựa chọn PCB

### E.1. Kiểm đủ hồ sơ trước khi rời lab

- [ ] Mở được ảnh/CSV trước và sau lọc; khớp từng dòng thực.
- [ ] Có nguồn, BIAS, ảnh quang và điều kiện chiếu.
- [ ] Có log 10 phút, lịch thao tác và bảng nguồn.
- [ ] Có ảnh mạch, giá trị linh kiện cấu hình cuối, tên firmware và chu kỳ log.
- [ ] Nếu thu ADC nhanh: có N, fs thực, đơn vị và tên file.
- [ ] Ghi dòng thực lớn nhất; không lấy định mức nguồn 1,5 A làm dải đã thử.
- [ ] Ghi rõ phép chưa làm, file thiếu, lỗi chưa giải thích.

### E.2. Căn cứ lựa chọn linh kiện

| Phần cần quyết định | Dữ liệu lab | Còn phải đối chiếu |
|---|---|---|
| Burden | Ip, BIAS, biên độ/dạng sóng trước lọc (D.I) | Tải cho phép của đúng CT, biên AFE/ADC |
| RC dòng | Trước/sau lọc, nhiễu (D.I) | Băng thông thuật toán, lấy mẫu ADC |
| Rf/Cf | Sáng/che, dao động (D.II) | Ổn định TIA, điện dung, biên đầu ra |
| Lọc quang sau TIA | So đầu ra TIA với PA1 khi nối thẳng và khi qua hai tầng RC; ghi min/max, suy giảm đỉnh, nhiễu và đáp ứng xung | Chọn VBPW34S, R6/C15; giữ hai tầng RC PCB như cấu hình ban đầu hoặc ghi lý do đánh giá lại. Số đo module chỉ là căn cứ chọn, phải đo xác nhận trên PCB |
| Nguồn PCB | Nguồn module khi tích hợp (D.III), chỉ tham khảo | Dòng IC rời, tải đồng thời, LDO/tụ/nhiệt |
| Hiệu chuẩn firmware | ADC sau lọc và dòng tham chiếu | Hiệu chuẩn lại khi PCB chạy |
| Schematic/BOM | Cấu hình được chọn và giới hạn | Mã, định mức, SL, chân, footprint |

Khi chưa đủ bằng chứng, trạng thái lựa chọn được ghi là “phương án thử, cần kiểm chứng bổ sung”. Không xác định lựa chọn cuối cùng chỉ dựa trên một buổi thử nghiệm.

### E.3. Chuyển kết quả đo sang thiết kế

Tách số tính, giới hạn datasheet và số đo. Dùng bảng ở E.2 để chốt hoặc ghi rõ quyết định còn chờ xác nhận. Kết quả so sánh TIA nối thẳng với TIA qua hai tầng RC giúp đánh giá mức suy giảm tín hiệu/xung để chọn cấu hình PCB; vì PCB có đường mạch và tải ADC riêng, phải đo lại tại `TIA_LIGHT` và `ADC_LIGHT` sau khi hàn. Phần tính nguồn, nhiệt, footprint và BOM PCB xem [file 2](02_Thiet_ke_phan_cung_PCB_SMD.md); thông số cảm biến, lọc và lấy mẫu xem [phần B](#b-cơ-sở-tính-toán-và-thông-số-đo). Không dùng dòng tiêu thụ Blue Pill/module để thay ngân sách cho MCU rời trên PCB.

### E.4. Hoàn thiện schematic, BOM và báo cáo

Mỗi linh kiện ghi **mã – giá trị – định mức – số lượng – footprint**. Kiểm burden về biên áp/công suất/tải CT; ghi RC/Rf/Cf là ban đầu hay đã kiểm chứng; nguồn tính theo IC PCB. PA0 dòng, PA1 quang, PA9 TX, PA10 RX. Ở PCB, nhánh quang đi từ đầu ra TIA qua R11/C17 rồi R12/C18 tới `ADC_LIGHT`; đây là hai tầng thông thấp sau TIA, khác với cấu hình module nối thẳng có thể dùng khi thử. Nguyên mẫu dùng module MAX3485 3,3 V; PCB dùng IC MAX3485ESA+ rời 3,3 V. Cả hai dùng PB0 chung DE và /RE; module phải đối chiếu hậu tố IC, header và mạch phụ trợ thực, không mặc định giống PCB.

Phân biệt cấu hình: module dùng burden 150 Ω–2 W và BPW34 chân cắm; PCB dùng R2 150 Ω–0,125 W và VBPW34S SMD. PCB có SW1 RESET dùng nút nhấn 2 chân SMD 3 × 6 × 2,5 mm, thường hở, nhấn nhả, nối NRST–GND, giữ C11 100 nF (104) và J2.5 theo file 2 và 3; không thêm nút BOOT. Không đưa mã linh kiện PCB sang bảng module.

Kiểm SWD, khả năng tiếp cận điểm đo nguồn/BIAS/AFE và footprint đúng mã mua. Việc cần điểm đo là yêu cầu bố trí/kiểm tra, không tự bổ sung linh kiện ngoài BOM. Ba tụ 100 nF (104) ở module là ba vị trí riêng, chưa bao gồm các tụ MCU/IC khác trên PCB.

| Phần trong quyển đồ án | Nội dung đưa vào |
|---|---|
| Thiết kế phần cứng | CT/burden, BIAS, RC, TIA; công thức; datasheet; lý do và giới hạn chọn |
| Kiểm thử | Bộ thử, dụng cụ/cài đặt, cấu hình, bảng đo, ảnh/CSV, đối chiếu tính–đo, lỗi và xử lý |
| Giới hạn | Dải dòng đã đo; quang tĩnh; tích hợp 10 phút; xung sáng/đặc trưng nhanh/hồ quang thực chưa thử; MV chỉ phân tích |

Mẫu tổng hợp: “Nguyên mẫu đã kiểm tra dòng trong dải … A, quang dưới điều kiện …, tích hợp … phút. Dữ liệu dùng để … . Lựa chọn … còn cần … trước khi chốt PCB. Phiên thử chưa xác nhận phát hiện chớp hồ quang thực.”

### E.5. Điều kiện chuyển sang thiết kế PCB

- [ ] Có cấu hình cuối và dữ liệu tương ứng, phân biệt số tính/số đo.
- [ ] Burden/RC/Rf/Cf có căn cứ; thiếu tài liệu hoặc phép đo phải ghi rõ.
- [ ] Nguồn tính theo IC sẽ hàn, không lấy dòng Blue Pill thay MCU.
- [ ] Schematic/BOM đủ mã, giá trị, định mức, SL, chân và footprint.
- [ ] Không đổi R/C sau lab rồi ghi cấu hình mới đã được kiểm chứng.
- [ ] Giữ danh sách vấn đề chưa giải quyết và việc phải kiểm tra sau hàn.

**Trạng thái triển khai:** kết nối khối nguồn PCB đã được kiểm tra trực quan; thử nghiệm phần cứng, ERC và xác nhận footprint chưa hoàn tất. Khối MCU và giao diện SWD đang được triển khai theo file 3. Sơ đồ luồng tại phần A minh họa cấu hình nguyên mẫu.

### 4. Tài liệu kỹ thuật chính thống

Chỉ dùng tài liệu công khai của nhà sản xuất làm nguồn kỹ thuật. Cấu hình, trình tự lab và ví dụ số là lựa chọn của kế hoạch thử; không coi là quy trình được hãng chứng nhận.

1. [Microchip MCP6002](https://www.microchip.com/en-us/product/MCP6002): nguồn, biên ra, tải, đặc tính op-amp; không dùng để chứng nhận CT.
2. [ST AN2834](https://www.st.com/resource/en/application_note/an2834-how-to-get-the-best-adc-accuracy-in-stm32-microcontrollers-stmicroelectronics.pdf): ảnh hưởng mạch ngoài và điều kiện lấy mẫu ADC.
3. [TI – Transimpedance Considerations for High-Speed Amplifiers](https://www.ti.com/lit/an/sboa122/sboa122.pdf): ổn định, băng thông và điện dung TIA; không phải datasheet MCP6002.
4. [Vishay BPW34/BPW34S](https://www.vishay.com/docs/81521/bpw34.pdf): cảm biến module, thông số theo phân cực. PCB dùng VBPW34S theo file 2–3, không tự đồng nhất footprint.
5. [Tektronix – Programmer Manual, bảng 3–25](https://download.tek.com/manual/070928301.pdf): định nghĩa RMS toàn tín hiệu và AC/SDEviation; làm cơ sở tính RMS phần AC từ CSV ở D.I.3.d.
6. [ST LD1117](https://www.st.com/resource/en/datasheet/ld1117.pdf): ổn áp, tụ và nhiệt theo đúng mã/package PCB; không mặc định đây là ổn áp trên Blue Pill thực.
7. [ADI MAX3483–MAX3491](https://www.analog.com/media/en/technical-documentation/data-sheets/MAX3483-MAX3491.pdf): phần MAX3485, nguồn IC 3,0–3,6 V, chức năng DI/RO/DE và /RE, bảng driver/receiver switching characteristics. Thông số IC không tự xác nhận cấu hình toàn module.
8. [ST RM0008](https://www.st.com/resource/en/reference_manual/cd00171190.pdf): phần USART, truyền dữ liệu và USART_SR (TC/TXE), căn cứ chờ UART gửi xong trước khi trả chiều nhận.
9. [IEC 61000-4-30:2025](https://webstore.iec.ch/en/publication/71611): phương pháp đo và diễn giải thông số chất lượng điện AC 50/60 Hz; tài liệu tham khảo phương pháp, không chứng nhận nguyên mẫu.
10. [IEC 61000-4-7](https://webstore.iec.ch/en/publication/4226): hướng dẫn thiết bị/phương pháp đo sóng hài và liên hài đến 9 kHz.
11. [IEC 60255-1:2022](https://webstore.iec.ch/en/publication/59762), [IEC 60255-26:2023](https://webstore.iec.ch/en/publication/62084), [IEC 60255-27:2023](https://webstore.iec.ch/en/publication/63370): tham khảo nếu định hướng thiết bị rơ-le/bảo vệ; lần lượt về yêu cầu chung, EMC và an toàn.

Chưa có datasheet hãng đúng **DL-CT08CL6-1000/1** để xác nhận tỷ số và burden. Giữ 1000:1 là giả thiết tính toán. Mọi ngưỡng đạt chưa có trong kế hoạch phải được thống nhất bằng căn cứ kỹ thuật; không tự thêm ngưỡng rồi coi là tiêu chuẩn.
