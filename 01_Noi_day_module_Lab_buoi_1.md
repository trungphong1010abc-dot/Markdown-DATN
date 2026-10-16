# Nối phần cứng mô-đun — lab buổi 1

Tài liệu chỉ trình bày linh kiện và cách nối phần cứng cho nguyên mẫu mang lên lab buổi 1, theo mục 4.2 và phần đấu tải/dụng cụ của PDF người dùng cung cấp. Các phần quy trình thử, firmware, thu log, tính toán, tiêu chí đánh giá và kết luận nằm ngoài tài liệu này.

## 1. Quy ước linh kiện và đường tín hiệu

**U1 = MCP6002-I/P DIP-8 nhánh dòng/BIAS. U2 = MCP6002-I/P DIP-8 nhánh quang.** Mã U1/U2 trong file này dùng cho mô-đun; xem bảng nối PCB riêng khi chuyển sang SMD.

| Đường | Kết nối chính |
|---|---|
| Nguồn | Adapter cách ly 5 V → Blue Pill và TTL485-V2.0; 3V3 Blue Pill → U1/U2 |
| Dòng | CT → burden 150 Ω → U1 → R lọc 1 kΩ → PA0 |
| Quang | BPW34 → U2 với Rf 10 kΩ/Cf 100 pF → PA1 |
| Dữ liệu | Blue Pill ↔ TTL485-V2.0 ↔ USB–RS485 CH340 ↔ laptop |
| Tải CT | Nguồn 12 VAC riêng → dây xuyên CT → tải điện trở → về nguồn AC |

## 2. Linh kiện dùng để nối mô-đun

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
| Lọc dòng | Tụ 100 nF, mã 104 | 1 | PA0 xuống GND |
| Quang | BPW34 chân cắm | 1 | Dùng một cảm biến trong mạch |
| Quang | MCP6002-I/P | 1 | U2, DIP-8, cấp 3,3 V |
| Quang | Rf 10 kΩ | 1 | Hồi tiếp giữa U2.1–U2.2 |
| Quang | Cf 100 pF, mã 101 | 1 | Song song Rf |
| Nguồn AFE | Tụ 100 nF, mã 104 | 2 | Mỗi IC U1/U2 một tụ |
| RS485 | TTL485-V2.0, MAX13487EESA+ | 1 | Cấp 5 V, tự chuyển chiều |
| RS485 laptop | USB–RS485 CH340 | 1 | Cấp nguồn USB laptop |
| Đấu nối | Breadboard, jumper, dây/header | 1 bộ | Nối theo nhãn chân thực tế |
| Tải ngoài | Nguồn cách ly 12 VAC–1,5 A | 1 | Cấp riêng tải điện trở |
| Tải ngoài | Điện trở sứ 50 Ω–25 W | 3 | Có thể mắc 1, 2 hoặc 3 nhánh song song |
| Tải ngoài | Dây silicone 20 AWG, jack AC ra cọc vít, đầu nối | 1 bộ | Dùng cho dòng tải, tách khỏi jumper tín hiệu |

**Tổng ba tụ 104:** một tụ nguồn U1, một tụ nguồn U2 và một tụ lọc PA0. Tụ nguồn và tụ lọc là ba linh kiện riêng.

## 3. Xác định chân MCP6002 DIP-8

| Chân | Chức năng | Chân | Chức năng |
|---:|---|---:|---|
| 1 | OUT A | 8 | VDD |
| 2 | IN− A | 7 | OUT B |
| 3 | IN+ A | 6 | IN− B |
| 4 | VSS/GND | 5 | IN+ B |

Nhìn từ trên IC, xác định chân 1 bằng dấu chấm hoặc rãnh định hướng rồi đếm theo datasheet. Tên U1.7 nghĩa là chân 7 của U1.

## 4. Nối nguồn

| Từ | Nối đến |
|---|---|
| Adapter 5 V cực dương | Qua jack → chân 5V Blue Pill và VCC TTL485-V2.0 |
| Adapter cực âm | GND Blue Pill và thanh GND breadboard |
| 3V3 Blue Pill | Thanh 3,3 V → U1.8 và U2.8 |
| GND chung | U1.4, U2.4, GND TTL485-V2.0 |
| Tụ nguồn 104 thứ nhất | Giữa U1.8 và U1.4, gần U1 |
| Tụ nguồn 104 thứ hai | Giữa U2.8 và U2.4, gần U2 |

Hai MCP6002 dùng 3,3 V. Module TTL485-V2.0 trong tài liệu dùng 5 V. Nguồn USB–RS485 lấy riêng từ USB laptop; chân 5 V của bộ này để tách khỏi đường 5 V adapter.

## 5. Nối cầu chia và đệm BIAS

| Phần tử / chân | Nối đến |
|---|---|
| Điện trở 10 kΩ thứ nhất | 3V3 → điện trở → điểm M |
| Điện trở 10 kΩ thứ hai | Điểm M → điện trở → GND |
| Điểm M | U1.5 |
| U1.6 | U1.7 |
| U1.7 | Net BIAS, danh định khoảng 1,65 V |

BIAS được đưa tới nhánh dòng và quang. Điểm M trước đệm và BIAS sau đệm là hai net riêng.

## 6. Nối CT, burden và lọc PA0

| Từ / linh kiện | Nối đến |
|---|---|
| CT dây đỏ | U1.3 |
| CT dây đen | BIAS, U1.7 |
| Burden 150 Ω–2 W | Giữa U1.3 và U1.7, song song hai dây CT |
| U1.2 | U1.1, hồi tiếp trực tiếp |
| U1.1 | Đầu thứ nhất R lọc 1 kΩ |
| Đầu còn lại R lọc | PA0 Blue Pill |
| Tụ lọc 100 nF — 104 thứ ba | PA0 → tụ → GND, đặt gần PA0 |

**Hồi tiếp U1.2 lấy tại U1.1, trước R lọc.** Dây CT đen về BIAS. Tín hiệu từ U1.1 đi qua R 1 kΩ trước khi tới PA0; tránh dây nối tắt điện trở này. Burden được mắc sẵn trước khi cho dòng qua CT.

## 7. Nối BPW34 và mạch quang

| Từ / linh kiện | Nối đến |
|---|---|
| U2.3 | BIAS, U1.7 |
| BPW34 cathode K | U2.2 |
| BPW34 anode A | GND |
| Rf 10 kΩ | Giữa U2.1 và U2.2 |
| Cf 100 pF, mã 101 | Giữa U2.1 và U2.2, song song Rf |
| U2.1 | PA1 Blue Pill; nối ADC sau khi xác nhận điện áp phù hợp 0–3,3 V |
| U2.5 | BIAS |
| U2.6 | U2.7 |
| U2.7 | Chỉ hồi tiếp về U2.6, đầu ra không cấp tải ngoài |

U2.7 và U1.7 là hai đầu ra op-amp riêng. Giữ BPW34, Rf, Cf và các dây đầu vào gần U2; nhận diện A/K theo dấu và bản vẽ đúng BPW34 đang dùng.

## 8. Nối TTL485-V2.0 và laptop

| Từ | Nối đến |
|---|---|
| PA9 Blue Pill — USART1_TX | RXD TTL485-V2.0 |
| TXD TTL485-V2.0 | PA10 Blue Pill — USART1_RX |
| VCC TTL485-V2.0 | +5 V adapter |
| GND TTL485-V2.0 | GND chung |
| D+ TTL485-V2.0 | A/D+ USB–RS485, theo quy ước hai thiết bị |
| D− TTL485-V2.0 | B/D− USB–RS485, theo quy ước hai thiết bị |
| GND tín hiệu USB–RS485, nếu có và là loại không cách ly | GND tín hiệu mạch |
| Cổng USB bộ chuyển đổi | USB laptop |
| PB0, PB1 Blue Pill | Để trống đối với module tự chuyển chiều |

Nhãn TXD/RXD ở bảng thuộc module TTL485-V2.0 được chỉ định trong PDF. Module tự chuyển chiều dùng nguồn 5 V; cách đấu này tách biệt với IC MAX3485 rời trên PCB dùng 3,3 V và điều khiển DE,/RE.

## 9. Nối ST-Link V2

| ST-Link | Blue Pill |
|---|---|
| SWDIO | PA13 |
| SWCLK | PA14 |
| GND | GND |
| VTref, nếu đầu nạp có | 3V3 theo hướng dẫn chính đầu nạp |

Blue Pill được cấp nguồn adapter. Đầu ra cấp nguồn 3,3 V của ST-Link clone được để tách khỏi nguồn Blue Pill; VTref chỉ dùng theo chức năng tham chiếu của đúng đầu nạp.

## 10. Nối tải AC và dụng cụ ở lab

Nguồn tải 12 VAC và nguồn mạch đo 5 VDC là hai nguồn riêng. Phần dưới chỉ mô tả đường dây nguồn/tải và vị trí nối dụng cụ.

### 10.1. Mạch tải qua CT

| Đường dây | Cách nối |
|---|---|
| Đầu X của nguồn 12 VAC | Dây chung luồn một lượt qua cửa sổ CT → đầu thứ nhất bộ tải |
| Đầu còn lại bộ tải | Về đầu Y của nguồn 12 VAC |
| Một tải 50 Ω | Một điện trở giữa hai đầu bộ tải |
| Hai hoặc ba tải 50 Ω | Các điện trở mắc song song giữa cùng hai đầu bộ tải |
| Vị trí CT | Trên một dây chung trước điểm chia nhánh |
| Hai dây thứ cấp CT | Đỏ → U1.3; đen → U1.7; burden luôn song song hai đầu |

Chỉ luồn một dây tải qua CT. Tắt nguồn tải trước khi đổi dây hoặc đổi số nhánh điện trở. Đặt điện trở công suất trên bề mặt chịu nhiệt, tách khỏi breadboard.

### 10.2. Đồng hồ và oscilloscope

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

## 11. Tài liệu liên quan

- [Kế hoạch test module chốt PCB.pdf](../Kế%20hoạch%20test%20module%20chốt%20PCB.pdf): mục 4.2 trang 4–6 và phần đấu tải/dụng cụ mục I.4 trang 8. Chỉ tham chiếu kết nối phần cứng.
- [Thiết kế phần cứng PCB SMD](01_Thiet_ke_phan_cung_PCB_SMD.md).
- [Bảng linh kiện và nối chân PCB Altium](02_Bang_linh_kien_va_noi_chan_PCB_Altium.md).
