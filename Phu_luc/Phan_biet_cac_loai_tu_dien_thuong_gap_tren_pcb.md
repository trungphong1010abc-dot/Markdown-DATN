# 1. Tụ tantalum

| Dạng chân cắm (THT) | Dạng dán bề mặt (SMD) |
|---|---|
| <img src="hinh_minh_hoa/08_tantalum_tht.png" alt="Tụ tantalum chân cắm Vishay 199D" height="220"> | <img src="hinh_minh_hoa/07_tantalum_smd.png" alt="Tụ tantalum SMD Vishay 293D" height="180"> |
| Vishay 199D, thân dạng giọt. | Vishay 293D, thân dạng khối. |

Nguồn ảnh: [Vishay 199D](https://www.vishay.com/en/product/40020/), [Vishay 293D](https://www.vishay.com/en/product/40002/). Ảnh minh họa hình dáng sản phẩm, không đại diện đúng mã và trị số tụ đã mua cho node.

## 1.1. Khái niệm

Tụ tantalum là tụ điện phân dùng kim loại tantalum làm cực dương và lớp oxit tantalum làm điện môi. [1]

## 1.2. Cấu tạo và đặc điểm

Kim loại tantalum tạo cực dương; lớp oxit tantalum Ta₂O₅ cách điện giữa hai cực. Tụ tantalum rắn thông dụng dùng MnO₂ làm chất điện phân phía cực âm; loại polymer dùng polymer dẫn điện. Điện dung ít thay đổi theo điện áp DC hơn tụ gốm X7R. [1], [7]

Tụ có phân cực. Dòng TAJ và 293D đánh dấu phía cực dương bằng vạch; một số kiểu vỏ có dấu “+”. Điện dung và điện áp được in trực tiếp hoặc mã hóa tùy dòng, nên không áp dụng một vị trí đọc chung cho mọi tụ tantalum. [1], [2]

## 1.3. Ưu và nhược điểm

- **Ưu điểm:** điện dung lớn trong thân nhỏ, ổn định theo điện áp DC, phù hợp dự trữ nguồn.
- **Nhược điểm:** nhạy với điện áp ngược, quá áp và dòng nạp đột ngột; ESR và dòng gợn cho phép phải phù hợp mạch. Khả năng lọc cao tần phụ thuộc trở kháng theo tần số, không thể kết luận chỉ từ điện cảm thấp. [1], [3]

## 1.4. Ứng dụng

**Dùng trên PCB node:** C1 10 µF–16 V, vỏ 3528; C2 22 µF–16 V, vỏ 6032. C1 dự trữ điện tích ở đầu vào 5 V; C2 lọc và tham gia ổn định đầu ra 3,3 V của U1.

Lọc và dự trữ điện tích trên đường nguồn DC của thiết bị điện tử. Trên node, C1 đặt ở đầu vào nguồn và C2 ở đầu ra bộ ổn áp.

# 2. Tụ gốm X7R/X5R

| Dạng chân cắm (THT) | Dạng dán bề mặt (SMD) |
|---|---|
| <img src="hinh_minh_hoa/10_tu_gom_tht.png" alt="Tụ gốm chân cắm Vishay K series" height="220"> | <img src="hinh_minh_hoa/09_tu_gom_smd.png" alt="Tụ gốm MLCC SMD Vishay VJ" height="180"> |
| Vishay K series. | Vishay VJ Commercial. |

Nguồn ảnh: [K series](https://www.vishay.com/en/product/45171/), [VJ Commercial](https://www.vishay.com/en/product/45199/). Hai dòng có nhiều loại điện môi; hình dáng không đủ để phân biệt X7R với C0G.

## 2.1. Khái niệm

Tụ gốm X7R/X5R là tụ điện dùng điện môi gốm Class 2, có điện dung lớn trong kích thước nhỏ và thường dùng để lọc nguồn. [4], [5], [7]

## 2.2. Cấu tạo và đặc điểm

Tụ gồm các lớp điện cực xen kẽ điện môi gốm; dạng nhiều lớp gọi là MLCC. Dạng SMD nhỏ, đường nối ngắn giúp giảm điện cảm ký sinh, phù hợp lọc nhiễu cao tần sát chân IC. [3], [7]

X7R/X5R dùng điện môi gốm có khả năng phân cực mạnh để đạt điện dung lớn trong thân nhỏ. Điện áp DC làm giảm khả năng đáp ứng thêm của điện môi, nên **điện dung thực giảm khi đặt điện áp lên tụ**; mức giảm phụ thuộc mã tụ. Vì vậy, tụ ghi 10 µF không mặc nhiên giữ đủ 10 µF khi đang hoạt động. [4]

Tụ không phân cực. Tụ SMD nhỏ thường không in trị số; loại điện môi, điện dung và điện áp được xác định từ mã hàng trên nhãn túi/cuộn. Không phân biệt X7R và C0G chỉ bằng màu thân. [5]

## 2.3. Ưu và nhược điểm

- **Ưu điểm:** nhỏ gọn, điện dung lớn so với kích thước, thích hợp lọc nguồn và nhiễu cao tần.
- **Nhược điểm:** điện dung thay đổi theo điện áp DC, nhiệt độ và thời gian; thân gốm dễ nứt khi PCB bị uốn. [4], [5]

## 2.4. Ứng dụng

**Dùng trên PCB node:** tụ X7R 100 nF lọc nguồn IC và reset; C9 10 µF bổ sung điện dung nguồn MCU; C10 1 µF lọc VDDA; C12 100 nF lọc tín hiệu dòng; C17/C18 10 nF tạo hai tầng lọc quang.

Lọc nguồn sát IC, bổ sung điện dung nguồn và tạo mạch lọc RC. Trên node, nhóm này dùng ở nguồn, reset, lọc dòng và hai tầng lọc quang.

# 3. Tụ gốm C0G/NP0

| Dạng chân cắm (THT) | Dạng dán bề mặt (SMD) |
|---|---|
| <img src="hinh_minh_hoa/10_tu_gom_tht.png" alt="Hình dáng tụ gốm chân cắm dòng K" height="220"> | <img src="hinh_minh_hoa/09_tu_gom_smd.png" alt="Hình dáng tụ gốm SMD dòng VJ" height="180"> |
| K series có các mã điện môi Class 1. | VJ Commercial có các mã C0G. |

Nguồn ảnh: [K series](https://www.vishay.com/docs/45171/kseries.pdf), [VJ Commercial](https://www.vishay.com/docs/45199/vjcommercialseries.pdf). Dùng lại ảnh hai dòng sản phẩm vì mỗi dòng có nhiều điện môi; xác định C0G bằng mã hàng trên túi và datasheet.

## 3.1. Khái niệm

Tụ gốm C0G/NP0 là tụ điện dùng điện môi gốm Class 1, có điện dung ổn định theo nhiệt độ và điện áp. [4], [5]

## 3.2. Cấu tạo và đặc điểm

C0G/NP0 dùng điện môi gốm Class 1. Điện dung ổn định theo nhiệt độ và gần như không giảm do điện áp DC như X7R; tổn hao thấp. [4], [5]

Tụ không phân cực. Dạng SMD có thể giống hệt X7R; xác định C0G/NP0 và trị số bằng mã hàng. Loại có in mã điện dung được đọc theo quy ước của hãng. [5]

## 3.3. Ưu và nhược điểm

- **Ưu điểm:** điện dung ổn định, tổn hao thấp, phù hợp mạch cần độ chính xác.
- **Nhược điểm:** dải điện dung nhỏ hơn X7R trong cùng dòng và kích thước vỏ; không phù hợp thay tụ dự trữ nguồn nhiều µF. [5]

## 3.4. Ứng dụng

**Dùng trên PCB node:** C8/C11 27 pF tạo tải thạch anh; C15 100 pF mắc song song điện trở hồi tiếp của TIA.

Tạo tải thạch anh, mạch định thời, lọc chính xác và hồi tiếp. Trên node, C8/C11 tạo tải thạch anh; C15 nằm trong hồi tiếp TIA.

# 4. Tụ hóa nhôm

| Dạng chân cắm (THT) | Dạng dán bề mặt (SMD) |
|---|---|
| <img src="hinh_minh_hoa/11_tu_hoa_nhom_tht.png" alt="Tụ hóa nhôm THT Vishay 136 RVI" height="220"> | <img src="hinh_minh_hoa/12_tu_hoa_nhom_smd.png" alt="Tụ hóa nhôm SMD Vishay 142 CVZ" height="220"> |
| Vishay 136 RVI. | Vishay 142 CVZ. |

Nguồn ảnh: [136 RVI](https://www.vishay.com/en/product/28321/), [142 CVZ](https://www.vishay.com/en/product/28577/).

## 4.1. Khái niệm

Tụ hóa nhôm là tụ điện phân dùng lớp oxit nhôm làm điện môi và chất điện phân để tiếp xúc điện với lớp oxit. [6]

## 4.2. Cấu tạo và đặc điểm

Lá nhôm làm cực dương, lớp oxit nhôm làm điện môi; giấy thấm chất điện phân nằm giữa các lá điện cực. Cấu tạo cuộn giúp đạt điện dung lớn; thân thường hình trụ, có cả THT và SMD. [6]

Tụ hóa nhôm thông dụng có phân cực; vạch mang dấu “−” chỉ cực âm. Trị số µF và điện áp thường in trực tiếp trên thân; tụ SMD còn dùng mã theo hãng. Dòng lưỡng cực được đánh dấu riêng. [6]

## 4.3. Ưu và nhược điểm

- **Ưu điểm:** điện dung lớn, nhiều lựa chọn điện áp, phù hợp lọc nguồn.
- **Nhược điểm:** chất điện phân suy giảm theo thời gian; nhiệt độ cao và dòng gợn làm giảm tuổi thọ. ESR/ESL hạn chế hiệu quả lọc cao tần nên thường phối hợp tụ gốm sát IC. [3], [6]

## 4.4. Ứng dụng

**Không dùng trong BOM PCB node hiện tại.**

Lọc gợn sau chỉnh lưu, dự trữ nguồn và ghép tín hiệu ở các dòng tụ phù hợp. [6], [7]

# 5. Tụ polymer

| Dạng chân cắm (THT) | Dạng dán bề mặt (SMD) |
|---|---|
| <img src="hinh_minh_hoa/16_polymer_tht.png" alt="Ảnh chụp tụ polymer nhôm Panasonic SEPC" height="220"> | <img src="hinh_minh_hoa/13_polymer_smd.png" alt="Tụ polymer nhôm Vishay 180 CPS" height="220"> |
| Panasonic OS-CON SEPC. | Vishay 180 CPS. |

Nguồn ảnh: [Akizuki – SEPC](https://akizukidenshi.com/catalog/g/g108292/), [Vishay 180 CPS](https://www.vishay.com/en/product/28415/).

## 5.1. Khái niệm

Tụ polymer là tụ điện phân dùng polymer dẫn điện làm chất điện phân, gồm các loại nền nhôm hoặc tantalum. [7]

## 5.2. Cấu tạo và đặc điểm

Tụ dùng polymer dẫn điện làm chất điện phân; điện môi vẫn là lớp oxit nhôm hoặc oxit tantalum tùy loại. Nhóm này thường có ESR thấp, giúp giảm tổn hao khi có dòng gợn. [7]

Tụ có phân cực. Dấu cực phụ thuộc công nghệ và dòng sản phẩm: không áp dụng vạch cực dương của tantalum cho mọi tụ polymer dạng trụ. Đọc bản vẽ hãng để xác định dấu cực và mã điện dung/điện áp. [1], [7]

## 5.3. Ưu và nhược điểm

- **Ưu điểm:** ESR thấp, khả năng chịu dòng gợn tốt ở các dòng thiết kế cho nguồn chuyển mạch.
- **Nhược điểm:** có giới hạn điện áp ngược, nhiệt độ và dòng rò riêng; không thay trực tiếp tụ đầu ra bộ ổn áp chỉ vì ESR thấp hơn. [3], [7]

## 5.4. Ứng dụng

**Không dùng trong BOM PCB node hiện tại.**

Lọc đầu ra nguồn DC–DC và cấp nguồn cho tải số có dòng biến thiên nhanh. ESR của tụ phải nằm trong phạm vi bộ ổn áp cho phép. [3], [7]

# 6. Tụ màng (film)

| Dạng chân cắm (THT) | Dạng dán bề mặt (SMD) |
|---|---|
| <img src="hinh_minh_hoa/14_tu_mang_tht.png" alt="Ảnh chụp tụ màng WIMA dạng chân cắm" height="220"> | <img src="hinh_minh_hoa/15_tu_mang_smd.png" alt="Ảnh chụp tụ màng SMD Rubycon PMLCAP" height="220"> |
| WIMA, dạng hộp. | Rubycon PMLCAP 25MU106MD15750. |

Nguồn ảnh: [Reichelt – WIMA](https://vendor.reichelt.de/de/en/mks2_pet_capacitor_100_nf_10_63_vdc_rm_5-p12349.html), [Akizuki – PMLCAP](https://akizukidenshi.com/catalog/g/g107398/). PMLCAP dùng màng polymer làm điện môi, khác với nhóm tụ điện phân polymer ở mục 5.

## 6.1. Khái niệm

Tụ màng là tụ điện dùng màng nhựa cách điện giữa hai điện cực kim loại. [7], [8]

## 6.2. Cấu tạo và đặc điểm

Màng nhựa như polyester hoặc polypropylene làm điện môi; điện cực là lá kim loại hoặc lớp kim loại phủ trên màng. Có dạng cuộn, xếp lớp, chân cắm và SMD. Đặc tính tổn hao và chịu xung phụ thuộc loại màng, cấu tạo và dòng sản phẩm. [7], [8]

Tụ màng thông dụng không phân cực. Trên thân thường ghi điện dung hoặc mã ba số, chữ dung sai và điện áp; tụ an toàn còn ghi cấp X/Y và dấu chứng nhận. [8]

## 6.3. Ưu và nhược điểm

- **Ưu điểm:** không phân cực, nhiều dòng có tổn hao thấp và khả năng chịu xung tốt.
- **Nhược điểm:** thường lớn hơn tụ gốm khi cần điện dung lớn; khả năng chịu nhiệt hàn và xung phải theo đúng dòng sản phẩm. [7], [8]

## 6.4. Ứng dụng

**Không dùng trong BOM PCB node hiện tại.**

Ghép tín hiệu, lọc, định thời và mạch dập xung. Tụ nối trực tiếp với điện lưới ở vị trí yêu cầu an toàn phải thuộc đúng cấp X/Y, không chỉ đạt điện áp DC định mức. [8]

# 7. Bảng so sánh các loại tụ

| Loại tụ | Phân cực | Ưu điểm chính | Hạn chế chính | Công dụng điển hình | Trên PCB node |
|---|---|---|---|---|---|
| Tantalum rắn | Có | Điện dung lớn trong thân nhỏ, ít phụ thuộc điện áp DC | Nhạy với ngược cực, quá áp và dòng nạp | Dự trữ và lọc nguồn DC | C1, C2 |
| Gốm X7R/X5R | Không | Nhỏ, phù hợp lọc cao tần | Điện dung giảm do điện áp DC, thay đổi theo nhiệt độ | Lọc nguồn sát IC, lọc RC | Dùng X7R ở nguồn, reset và lọc tín hiệu |
| Gốm C0G/NP0 | Không | Điện dung ổn định, tổn hao thấp | Điện dung khả dụng nhỏ hơn X7R trong cùng vỏ | Thạch anh, hồi tiếp, lọc chính xác | C8, C11, C15 |
| Hóa nhôm | Có với loại thông dụng | Điện dung lớn, nhiều mức điện áp | Tuổi thọ phụ thuộc nhiệt độ và dòng gợn | Lọc sau chỉnh lưu, dự trữ nguồn | Không dùng |
| Điện phân polymer | Có | ESR thấp, phù hợp dòng gợn | Phải xét dòng rò và tương thích bộ ổn áp | Lọc nguồn DC–DC, nguồn tải số | Không dùng |
| Màng | Không với loại thông dụng | Nhiều dòng tổn hao thấp, chịu xung tốt | Kích thước lớn khi điện dung tăng | Ghép tín hiệu, lọc, dập xung | Không dùng |

# 8. Ý nghĩa các thông số thường gặp

| Thông số | Ý nghĩa | Ví dụ hoặc tác dụng |
|---|---|---|
| Điện dung | Khả năng tích trữ điện tích khi điện áp thay đổi | 1 µF = 1.000 nF = 1.000.000 pF |
| Điện áp định mức | Giới hạn điện áp cho phép trong điều kiện hãng quy định | Tụ 16 V dùng trên nguồn 5 V vẫn chịu điện áp thực tế 5 V |
| Dung sai | Sai lệch cho phép so với điện dung danh định ở điều kiện đo quy định | 10 µF ±20% tương ứng 8–12 µF |
| Điện môi | Vật liệu cách điện giữa các điện cực, quyết định nhiều đặc tính của tụ | X7R giảm điện dung do DC; C0G ổn định hơn |
| ESR | Điện trở tổn hao tương đương bên trong tụ. [3] | Gây sụt áp và sinh nhiệt khi có dòng qua tụ |
| ESL | Điện cảm ký sinh của tụ và kết nối. [3] | Hạn chế hiệu quả lọc ở tần số cao |
| Dòng gợn cho phép | Giới hạn thành phần dòng xoay chiều qua tụ ở điều kiện quy định. [6], [7] | Vượt giới hạn làm tăng nhiệt và giảm tuổi thọ |
| Dòng rò | Dòng DC nhỏ vẫn đi qua tụ khi đã nạp. [1], [6], [7] | Đáng chú ý trong mạch tiêu thụ thấp hoặc đo trở kháng cao |
| Dải nhiệt độ | Khoảng nhiệt độ được phép vận hành | Điện áp, tuổi thọ và đặc tính còn phụ thuộc điều kiện hãng quy định |
| Kiểu vỏ | Hình dáng, kích thước và cách lắp | THT hàn xuyên lỗ; SMD hàn trên bề mặt PCB |

# Tài liệu tham khảo

[1] Vishay, [293D Solid Tantalum Chip Capacitors](https://www.vishay.com/en/product/40002/) và KYOCERA AVX, [Technical Summary and Application Guidelines](https://www.kyocera-avx.com/docs/techinfo/TechSumAppGuide.pdf).

[2] KYOCERA AVX, [TAJ Series](https://datasheets.kyocera-avx.com/TAJ.pdf): kích thước, trị số, mã đặt hàng và cực tính.

[3] Analog Devices, [MT-101: Decoupling Techniques](https://www.analog.com/media/en/training-seminars/tutorials/MT-101.pdf): tụ dự trữ nguồn, tụ lọc sát IC và ESR/ESL.

[4] Murata, [DC voltage and capacitance](https://www.murata.com/support/faqs/capacitor/ceramiccapacitor/char/0005) và [Voltage characteristics of electrostatic capacitance](https://article.murata.com/en-eu/article/voltage-characteristics-of-electrostatic-capacitance).

[5] KYOCERA AVX, [C0G (NP0) Dielectric](https://datasheets.kyocera-avx.com/C0GNP0-Dielectric.pdf); Vishay, [VJ Commercial Series](https://www.vishay.com/docs/45199/vjcommercialseries.pdf).

[6] Nichicon, [General Descriptions of Aluminum Electrolytic Capacitors](https://www.nichicon.co.jp/english/products/pdf/aluminum-e.pdf).

[7] Panasonic Industry, [Basic Knowledge of Capacitors (2)](https://industrial.panasonic.com/ww/ds/ss/technical/b3); Vishay, [180 CPS Polymer Capacitors](https://www.vishay.com/en/product/28415/).

[8] Vishay, [Film Capacitors](https://www.vishay.com/en/capacitors/film/).

