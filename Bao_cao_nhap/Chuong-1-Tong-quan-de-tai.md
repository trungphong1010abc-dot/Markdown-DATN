> **Đề tài:** Thiết kế hệ thống nhúng phát hiện chớp hồ quang điện (arc-flash) trong hệ thống điện hạ thế và trung thế.
>
> **Ghi chú bản thảo:** Nội dung hướng tới khoảng 10–14 trang A4 khi dàn bằng Times New Roman 13, giãn dòng khoảng 1,15. Số trang thực tế phụ thuộc cách dàn trang và kích thước hình.

Chương 1 trình bày bài toán phát hiện chớp hồ quang điện, phân tích các yêu cầu kỹ thuật và quy trình phát hiện, phối hợp bảo vệ theo hồ sơ thiết kế tại Nhà máy Nhiệt điện Quảng Ninh. Kết quả phân tích là cơ sở cho phần lý thuyết và thiết kế hệ thống ở Chương 2.

# 1.1. Tổng quan bài toán phát hiện chớp hồ quang điện

## 1.1.1. Đối tượng nghiên cứu và bối cảnh ứng dụng

Trong hệ thống cung cấp điện công nghiệp, tủ điện là nơi bố trí các thiết bị đóng cắt, đo lường và bảo vệ. Các bộ phận như thanh cái, đầu cáp, tiếp điểm và lớp cách điện cùng làm việc trong không gian giới hạn của tủ. Khi xảy ra sự cố hồ quang nội bộ, nhiệt, áp suất và vật chất nóng phát sinh có thể làm hư hỏng thiết bị, gây nguy hiểm cho người ở gần và gián đoạn cấp điện. [TL1, mục 1 và 3.2, tr. in 78; tr. PDF 2.]

Đề tài tập trung vào việc phát hiện chớp hồ quang trong tủ điện hạ thế và trung thế. Các bộ phận được xem xét gồm:

- **Thanh cái, mối nối và tiếp điểm:** Đây là các phần tử dẫn điện trong tủ. Tình trạng mối nối, lớp cách điện và khoảng cách giữa các phần dẫn điện có liên quan đến nguy cơ phát sinh sự cố nội bộ.
- **Đầu cáp và khoang đấu nối:** Là nơi kết nối cáp với thiết bị. Tổng quan kỹ thuật của Kumpulainen và cộng sự xem đầu cáp là một vị trí điển hình trong theo dõi sự cố hồ quang.
- **Khoang thiết bị đóng cắt và đo lường:** Gồm máy cắt, dao cách ly, dao tiếp địa và biến điện đo lường. Việc bố trí các bộ phận này cùng kết cấu vách ngăn quyết định không gian giám sát. [TL1, mục 3.2 và 4.3, tr. in 78–80; tr. PDF 2–4.]

Hình 1.1 cho thấy kết cấu của tủ trung thế KMZ_31 được sử dụng trong nghiên cứu về hồ quang nội bộ. Tủ có vách bao và đường thoát khí riêng. Khi phân tích vùng giám sát, đồ án xem xét không gian từng khoang và kết cấu ngăn chia bên trong tủ. [TL3, Hình 5, tr. in/PDF 7.]

![Kết cấu tủ KMZ_31 với vách tủ và đường thoát khí](hinh_minh_hoa/Hinh_1_1_Cau_truc_tu_trung_the_KMZ_31.jpg)

*Hình 1.1. Kết cấu tủ trung thế KMZ_31 trong nghiên cứu nguồn; Exhaust Duct là đường thoát khí, Wall là vách tủ.*

*Nguồn: TL3, Hình 5, tr. in 7, tr. PDF 7. Trích ảnh từ tài liệu, giữ nguyên nhãn; bài báo phát hành theo CC BY 4.0.*

Phạm vi giám sát được xem xét từ toàn trạm, dãy tủ đến từng khoang tủ. Trong đó, vị trí thu nhận ánh sáng được phân tích theo vùng sự cố và kết cấu khoang. Tài liệu tổng quan minh họa một hệ bảo vệ có các cảm biến quang kết hợp với đo dòng; hình học và vùng đặt đầu thu là dữ liệu của phương án bố trí, không chỉ là số lượng cảm biến. [TL1, mục 5.6 và Hình 7, tr. in 83; tr. PDF 7.]

Đối với hệ thống nhúng, nhiệm vụ nghiên cứu là thu nhận dấu hiệu sự cố, xử lý để nhận biết sự kiện và đưa ra tín hiệu phản hồi. Việc cắt nguồn được thực hiện qua các phần tử bảo vệ và thiết bị đóng cắt bên ngoài. Trong phạm vi bộ phát hiện, đồ án phân tích tín hiệu đầu vào, thông tin đầu ra và quan hệ giữa các khối xử lý. [TL1, mục 2 và 6.2, tr. in 78–79, 84; tr. PDF 2–3, 8.]

Trong phạm vi nghiên cứu, bài toán phát hiện tập trung vào các nội dung sau:

- **Nhận biết sớm sự kiện:** Rút ngắn thời gian từ khi dấu hiệu hồ quang xuất hiện đến khi có tín hiệu phản hồi, tạo điều kiện cho khâu bảo vệ tiếp theo làm việc.
- **Phân biệt được tác động gây nhầm:** Xem xét tín hiệu sự cố cùng điều kiện làm việc bình thường, tránh đánh giá bộ phát hiện chỉ bằng một trường hợp kích thích thuận lợi.
- **Đánh giá được từng khâu:** Xác định thời gian thu nhận, xử lý và xuất tín hiệu; ở cấp toàn hệ thống, thời gian phản hồi còn bao gồm hoạt động của thiết bị bảo vệ và máy cắt. [TL1, mục 5.5–5.6 và 6.2, tr. in 83–84; tr. PDF 7–8; các nhu cầu trên được rút ra cho đề tài.]

## 1.1.2. Hiện tượng hồ quang điện và chớp hồ quang điện

Hồ quang điện là hiện tượng phóng điện phát sáng, trong đó dòng điện đi qua môi trường plasma nóng giữa các điện cực. Hình dạng và sự phát triển của hồ quang phụ thuộc vào thiết bị, môi trường và nguồn năng lượng duy trì phóng điện. Ba khái niệm được sử dụng trong chương gồm:

- **Hồ quang điện — electric arc:** Chỉ hiện tượng phóng điện. Hồ quang có thể xuất hiện trong một quá trình làm việc đã được thiết kế, chẳng hạn quá trình ngắt dòng của máy cắt.
- **Sự cố hồ quang — arc fault:** Chỉ sự cố có hồ quang phát sinh ngoài chức năng làm việc dự kiến của thiết bị.
- **Chớp hồ quang điện — arc flash:** Gắn với thành phần bức xạ nhiệt của hồ quang năng lượng lớn. Với đề tài này, nhiệm vụ phát hiện tập trung vào dấu hiệu của sự kiện, đặc biệt là phát sáng, để phục vụ việc nhận biết và phản hồi. [TL2, mục 1, tr. in 7; tr. PDF 1; TL1, mục 2, tr. in 78–79; tr. PDF 2–3.]

Trong thao tác đóng cắt bình thường, hồ quang được hình thành trong bộ phận có kết cấu chịu và dập hồ quang. Với sự cố nội bộ, phóng điện xảy ra tại nơi không được thiết kế cho quá trình đó, làm tác động đến những phần tử xung quanh. Sự khác nhau này có ý nghĩa đối với bộ phát hiện: tín hiệu xuất hiện trong quá trình làm việc bình thường là một nhóm tác động gây nhầm trong đánh giá bộ phát hiện. [TL2, mục 1, tr. in 7; tr. PDF 1.]

Những yếu tố liên quan đến sự cố được tài liệu tổng quan đề cập gồm tình trạng cách điện, các điểm đấu nối, tiếp điểm và công tác bảo trì. Theo dõi các dấu hiệu suy giảm trước sự cố có thể hỗ trợ phòng ngừa. Tuy nhiên, phát hiện hồ quang đã xuất hiện là một nhiệm vụ khác, đòi hỏi nhận biết và phản hồi trong thời gian ngắn. [TL1, mục 3 và 4, tr. in 78–81; tr. PDF 2–5.]

Tác động của hồ quang đến thiết bị và con người có thể chia thành các nhóm chính:

- **Tác động nhiệt:** Bức xạ và vật chất nóng có thể gây bỏng, làm hỏng cách điện và các phần dẫn điện.
- **Tác động áp suất:** Kênh hồ quang giãn nở tạo sóng áp suất; khí trong vỏ tủ được nung nóng còn gây tăng áp trong không gian bao kín. Hai quá trình này được phân biệt trong nghiên cứu về nổ hồ quang.
- **Hư hỏng và gián đoạn hoạt động:** Hư hỏng thiết bị có thể kéo theo thời gian ngừng cấp điện, sửa chữa và khôi phục hệ thống. [TL2, tóm tắt và mục 1, tr. in 7; tr. PDF 1; TL1, mục 1, tr. in 78; tr. PDF 2.]

Hình 1.2 ghi lại tủ KMZ_31 trước, trong và sau thử nghiệm tại phòng thí nghiệm công suất lớn ICMET, Romania. Ánh sáng phát ra trong quá trình thử và hư hỏng sau thử thể hiện hai khía cạnh của sự cố: dấu hiệu phục vụ phát hiện và tác động lên kết cấu tủ. [TL3, mục 1 và Hình 1, tr. in/PDF 1–2.]

![Tủ KMZ_31 trước, trong và sau thử nghiệm hồ quang nội bộ tại ICMET](hinh_minh_hoa/Hinh_1_2_Thu_nghiem_ho_quang_noi_bo_tu_KMZ_31.jpg)

*Hình 1.2. Thử nghiệm hồ quang nội bộ tủ KMZ_31 tại ICMET, Romania, gồm trạng thái trước thử và trạng thái hư hỏng sau thử.*

*Nguồn: TL3, Hình 1, tr. in 2, tr. PDF 2. Trích nguyên cụm ảnh và nhãn trong nguồn, CC BY 4.0; không phải ảnh tại nhà máy ở mục 1.3.*

Mức độ nguy hiểm của sự cố thể hiện qua hư hỏng thiết bị và năng lượng tác động trong những điều kiện cụ thể. Hình 1.3 là ảnh thanh cái hạ thế sau một phép thử được công bố trong tài liệu tổng quan. Điều kiện của phép thử gồm điện áp U = 726 V, dòng ngắn mạch ký hiệu Ik = 77 kA và thời gian hồ quang 65 ms. Sau thử, thanh cái bị nóng chảy cục bộ tại ranh giới lớp cách điện. [TL1, Hình 2, tr. in 80; tr. PDF 4.]

![Thanh cái hạ thế nóng chảy cục bộ sau thử hồ quang](hinh_minh_hoa/Hinh_1_3_Thanh_cai_ha_the_nong_chay_do_ho_quang.jpg)

*Hình 1.3. Thanh cái hạ thế nóng chảy cục bộ sau thử hồ quang tại ranh giới lớp cách điện.*

*Nguồn: TL1, Hình 2, tr. in 80, tr. PDF 4. Trích ảnh gốc; điều kiện nguồn: U = 726 V, Ik = 77 kA, thời gian hồ quang 65 ms.*

Phép thử cho thấy hư hỏng có thể hình thành trong khoảng thời gian ngắn. Bên cạnh đó, năng lượng tác động còn phụ thuộc vào thời gian hồ quang tồn tại. Hình 1.4 biểu diễn quan hệ này trong trường hợp tính toán với U = 15 kV, Ik = 50 kA, khe hở 152 mm và khoảng cách làm việc 910 mm. Khi các điều kiện của trường hợp tính giữ nguyên, năng lượng trên đơn vị diện tích tăng theo thời gian hồ quang. [TL1, mục 5.2–5.5 và Hình 5, tr. in 81–83; tr. PDF 5–7.]

![Năng lượng tác động theo thời gian hồ quang trong điều kiện của nguồn](hinh_minh_hoa/Hinh_1_4_Nang_luong_tac_dong_theo_thoi_gian_ho_quang.png)

*Hình 1.4. Năng lượng tác động theo thời gian hồ quang trong một trường hợp tính toán; trục tung là J/cm², trục hoành là ms.*

*Nguồn: TL1, Hình 5, tr. in 82, tr. PDF 6. Trích nguyên hình; điều kiện: U = 15 kV, Ik = 50 kA, khe hở 152 mm, khoảng cách làm việc 910 mm. Không phải đường đặc tính của nguyên mẫu.*

Các giá trị thử nghiệm vừa nêu là điều kiện của tài liệu nguồn. Bộ tài liệu hiện có chưa cung cấp thống kê đủ phạm vi và thời gian quan sát để xác định tần suất sự cố tại Việt Nam. Do đó, tính cấp thiết ở đây được làm rõ từ hậu quả và nhu cầu phản hồi, thay vì ước lượng xác suất sự cố theo năm.

Các nghiên cứu về hồ quang sử dụng nhiều loại tín hiệu khác nhau. Lezama và cộng sự nghiên cứu hồ quang nối tiếp trên mạch dân dụng 230 V AC–50 Hz bằng tương quan dòng điện giữa các chu kỳ. Lin và cộng sự nghiên cứu định vị hồ quang DC trong hệ thống quang điện từ bức xạ điện từ thu bằng anten. Đây là những bài toán có đối tượng, tín hiệu và điều kiện khác với phát hiện chớp hồ quang trong tủ điện. [TL4, tóm tắt, tr. in 227; tr. PDF 1; TL6, tóm tắt và mục 1, tr. PDF 1.]

Các công trình trên được sử dụng để phân biệt phạm vi và loại tín hiệu nghiên cứu. Kết quả nhận dạng trên một tập tải dân dụng không đại diện cho khả năng phát hiện trong tủ trung thế; độ chính xác định vị hồ quang DC cũng không thay thế cho độ nhạy đầu thu quang. Cơ chế thu nhận và xử lý từng loại tín hiệu sẽ được tìm hiểu ở Chương 2.

Từ đặc điểm hiện tượng và hậu quả của sự cố, đồ án phân tích các yêu cầu kỹ thuật làm cơ sở lựa chọn phương án thu nhận và xử lý tín hiệu trong phần 1.2.

# 1.2. Phân tích yêu cầu kỹ thuật của bài toán

## 1.2.1. Yêu cầu về điện áp

Yêu cầu điện áp liên quan đến cả hệ thống được giám sát và bản thân bộ phát hiện. Trong phân tích thiết kế, điện áp được chia thành ba nhóm để làm rõ điều kiện làm việc và giao diện của từng khối:

- **Điện áp hệ thống:** Là điện áp của thiết bị điện nằm trong phạm vi giám sát, gắn với bối cảnh ứng dụng hạ thế hoặc trung thế. Đại lượng này được phân biệt với mức điện áp tại giao diện bộ phát hiện.
- **Điện áp tín hiệu:** Là mức điện áp tại các giao diện thu nhận và xử lý, mô tả điều kiện kết nối giữa đầu thu, khối điều hòa và khối xử lý. Đại lượng này được phân tích theo chức năng từng khối, không đồng nhất với điện áp hệ thống.
- **Nguồn phụ trợ:** Là nguồn nuôi bộ phát hiện và các khối liên quan. Trong phân tích thiết kế, nguồn nuôi được mô tả riêng với tín hiệu đo và điện áp thiết bị giám sát. Sự phân chia giữa cảm biến, khối vào/ra và rơ-le được minh họa trong cấu trúc hệ bảo vệ của tài liệu tổng quan. [TL1, mục 5.6 và Hình 7, tr. in 83; tr. PDF 7.]

Việc phân chia điện áp làm rõ giao diện giữa các khối trong thiết kế. Điện áp trung thế của thiết bị được giám sát không phải điện áp đưa trực tiếp vào bộ xử lý nhúng. Đặc tính mỗi cổng thu nhận hoặc xuất tín hiệu được mô tả bằng mức danh định, dải làm việc và điều kiện kết nối với thiết bị ngoài.

Đối với nguyên mẫu, dải nguồn và mức tín hiệu sẽ được xác định theo phương án thu nhận lựa chọn ở Chương 2. Nội dung đánh giá gồm kiểm tra nguồn cấp, đo mức tại đầu vào–đầu ra và đối chiếu với đặc tính các khối kết nối. Trạng thái cụ thể hóa yêu cầu được tổng hợp trong Bảng 1.1.

## 1.2.2. Yêu cầu về tần số

Đồ án phân tích tần số theo từng đại lượng vì tần số nguồn, băng thông và tốc độ lấy mẫu mô tả các đặc tính khác nhau. Ba nội dung liên quan trực tiếp gồm:

- **Tần số nguồn điện:** Là tần số của nguồn AC trong phạm vi nghiên cứu. Trong công trình của Lezama, nguồn làm việc ở 50 Hz; giá trị này mô tả điều kiện nguồn của nghiên cứu tham khảo, không phải tần số lấy mẫu.
- **Dải tần tín hiệu thu nhận:** Phụ thuộc vào dấu hiệu được sử dụng. Kênh chỉ tiếp nhận trạng thái dòng có nhu cầu khác với kênh đo dạng sóng; kênh quang theo dõi biến đổi ánh sáng phục vụ phát hiện.
- **Tần số lấy mẫu:** Là đặc tính của phương án số hóa tín hiệu. Trong nghiên cứu hồ quang nối tiếp của Lezama, mạch nguồn làm việc ở 50 Hz nhưng tín hiệu dòng được lấy mẫu 5 kHz. [TL4, tóm tắt, tr. in 227; tr. PDF 1.]

Ví dụ trên cho thấy tần số nguồn không quyết định trực tiếp tần số thu nhận. Việc lựa chọn băng thông và tốc độ xử lý dựa trên đặc điểm tín hiệu mà đồ án sử dụng. Nếu biến đổi mang dấu hiệu sự cố bị mất ở khâu thu nhận, việc tăng tốc xử lý phía sau không khôi phục được thông tin đó.

Phương pháp đánh giá đối chiếu dải đáp ứng của chuỗi thu nhận với tín hiệu tham chiếu và xét ảnh hưởng của các khối điều hòa, xử lý. Dải tần đo của nguyên mẫu sẽ phụ thuộc loại tín hiệu được lựa chọn, không lấy nguyên cấu hình của một nghiên cứu hồ quang nối tiếp làm yêu cầu cho kênh quang.

## 1.2.3. Yêu cầu về dòng điện

Dòng điện có thể được sử dụng để nhận biết sự cố hoặc xác nhận một dấu hiệu khác. Với bảo vệ dựa trên ánh sáng và quá dòng, tài liệu tổng quan mô tả việc phối hợp hai điều kiện để tăng tính chắc chắn của quyết định. Hình 1.5 trình bày nguyên lý này: tín hiệu tác động chỉ được hình thành theo tổ hợp ánh sáng và quá dòng của sơ đồ nguồn. [TL1, mục 5.6 và Hình 6, tr. in 83; tr. PDF 7.]

![Nguyên lý phối hợp ánh sáng và quá dòng trong nghiên cứu nguồn](hinh_minh_hoa/Hinh_1_5_Nguyen_ly_phoi_hop_anh_sang_va_qua_dong.png)

*Hình 1.5. Ví dụ phối hợp ánh sáng và quá dòng bằng phép AND; Trip signal là tín hiệu tác động của hệ thống bảo vệ trong nguồn.*

*Nguồn: TL1, Hình 6, tr. in 83, tr. PDF 7. Trích nguyên hình minh họa nguyên lý trong nghiên cứu nguồn.*

Đối với kênh dòng, đồ án phân biệt ba đại lượng:

- **Dòng định mức:** Gắn với chế độ làm việc của tải hoặc thiết bị.
- **Dòng sự cố:** Là dòng điện trong điều kiện sự cố. Dòng hồ quang có thể thấp hơn dòng sự cố kim loại, từ đó ảnh hưởng đến thời gian tác động của bảo vệ quá dòng.
- **Tín hiệu đưa vào bộ phát hiện:** Là thông tin dòng do khối đo hoặc phần tử bảo vệ cung cấp cho quá trình xử lý. Trong cấu trúc bảo vệ quang–dòng được tổng quan, đo dòng và cảm biến ánh sáng cung cấp hai nhóm thông tin phối hợp. [TL1, mục 5.3, 5.6 và Hình 7, tr. in 81–83; tr. PDF 5–7.]

Kênh dòng được phân tích theo vị trí lấy thông tin, dạng tín hiệu và vai trò trong quyết định phát hiện. Với phương án dùng dòng xác nhận tín hiệu quang, điều kiện phối hợp và quan hệ thời gian giữa hai tín hiệu là cơ sở xây dựng logic xử lý. Nội dung này khác với việc chọn một ngưỡng từ dòng ngắn mạch của nguồn thử.

Cách đánh giá gồm kiểm tra riêng từng tín hiệu và kiểm tra tổ hợp được quy định hợp lệ. Ngưỡng, tỷ số biến dòng và giao diện cụ thể chưa được xác lập cho nguyên mẫu; các thông số này được xem xét cùng phương án thu nhận và logic xử lý của đồ án.

## 1.2.4. Yêu cầu về độ nhạy

Độ nhạy phản ánh khả năng nhận biết tín hiệu trong điều kiện xác định. Với kênh quang, độ nhạy được phân tích trên chuỗi từ đầu thu đến quyết định phát hiện, gồm ba nội dung:

- **Khả năng thu nhận của cảm biến:** Liên quan đến kích thích quang và tín hiệu điện thu được tại đầu ra cảm biến.
- **Ngưỡng tác động:** Là điều kiện mà mạch hoặc khối xử lý dùng để nhận biết sự kiện.
- **Khả năng phát hiện của hệ thống:** Được đánh giá bằng kết quả nhận đúng, bỏ sót và báo nhầm trên tập tình huống thử được mô tả rõ.

Vị trí đầu thu là một phần của điều kiện đánh giá. Tài liệu tổng quan trình bày cảm biến điểm và cảm biến dạng vòng, đồng thời mô tả việc phân vùng phát hiện bằng các đầu thu quang. Vì vậy, độ nhạy được phân tích cùng vùng quan sát và đặc điểm bố trí. [TL1, mục 5.6, tr. in 83; tr. PDF 7.]

Từ đó, điều kiện đánh giá độ nhạy gồm nguồn kích thích, khoảng cách, hướng thu, vật cản và ánh sáng nền. Một lần không phát hiện có thể xuất phát từ tín hiệu bị che khuất hoặc thu nhận không đủ, bên cạnh nguyên nhân về ngưỡng. Ngược lại, đánh giá chỉ bằng việc chiếu sáng mạnh trực tiếp vào đầu thu chưa phản ánh khả năng phân biệt sự kiện trong điều kiện sử dụng.

Trong đồ án, tình huống sự cố và tập tác động gây nhầm được xem xét cùng phương án thu nhận. Chỉ sau khi có các điều kiện này mới có thể đặt ngưỡng và đánh giá tỷ lệ phát hiện có ý nghĩa. Bảng 1.1 ghi nhận những thông số chưa xác lập, thay cho việc dùng một yêu cầu chung như độ nhạy cao.

## 1.2.5. Yêu cầu về thời gian phản hồi

Thời gian phản hồi được mô tả bằng hai mốc: thời điểm kích thích tham chiếu xuất hiện và thời điểm đầu ra điện đạt trạng thái tác động. Cách mô tả này giữ nguyên phần thu nhận trong phạm vi đánh giá, thay vì chỉ tính thời gian thực thi chương trình. Ở cấp hệ bảo vệ, tài liệu tổng quan phân biệt khâu phát hiện với phần tử thực hiện loại trừ hồ quang. [TL1, mục 5.6 và 6.2, tr. in 83–84; tr. PDF 7–8.]

Đồ án phân tích thời gian phản hồi theo các khoảng sau:

- **Thời gian thu nhận:** Từ kích thích tham chiếu đến khi tín hiệu sẵn sàng cho khối xử lý.
- **Thời gian xử lý và xuất đầu ra:** Từ tín hiệu nhận được đến khi đầu ra đạt trạng thái tác động quy định.
- **Thời gian phối hợp bảo vệ và cắt:** Thuộc các phần tử phía sau bộ phát hiện, bao gồm rơ-le và thiết bị đóng cắt. Tài liệu tổng quan chỉ ra rằng khi phát hiện làm việc nhanh, thời gian loại trừ còn phụ thuộc đáng kể vào thiết bị sơ cấp. [TL1, mục 5.6 và 6.2, tr. in 83–84; tr. PDF 7–8.]

Ngoài độ trễ xuất hiện đầu ra, một đầu ra dạng xung còn có thời gian duy trì trạng thái tác động. Độ rộng xung mô tả khoảng duy trì đó, còn độ trễ phản hồi mô tả khoảng từ kích thích đến tác động. Trong phép đánh giá, hai đại lượng được ghi nhận riêng; chúng không thay thế cho nhau hoặc cho thời gian máy cắt ngắt mạch.

Phương pháp đánh giá nguyên mẫu sử dụng kích thích tham chiếu và đầu ra trên cùng cơ sở thời gian. Vị trí đặt mốc, điều kiện kích thích và cách xác định trạng thái đầu ra là các điều kiện của phép đánh giá. Nếu sử dụng nguồn sáng thay thế, kết quả được dùng để đánh giá đáp ứng quang của bộ phát hiện trong điều kiện thử, không thay thế thời gian cắt sự cố của cả hệ thống.

## 1.2.6. Yêu cầu về chu kỳ lấy mẫu

Chu kỳ lấy mẫu là khoảng thời gian giữa hai lần thu nhận liên tiếp khi thực hiện số hóa đều. Quan hệ giữa chu kỳ và tần số lấy mẫu là $f_s = 1/T_s$. Việc lựa chọn chu kỳ dựa trên đặc điểm tín hiệu và thời gian dành cho quyết định phát hiện.

Nội dung đánh giá tương ứng với từng cách thu nhận như sau:

- **Kênh đo tương tự bằng ADC:** Các đại lượng được phân tích gồm dải thông tin giữ lại, chu kỳ lấy mẫu và ảnh hưởng của khối điều hòa tín hiệu trước ADC.
- **Kênh nhận trạng thái số:** Các đặc tính được đánh giá gồm khả năng nhận cạnh hoặc xung, độ trễ tiếp nhận và khả năng bắt sự kiện.
- **Kênh xử lý liên tục bằng mạch so sánh:** Đáp ứng của mạch và đường truyền tín hiệu tới bộ xử lý là các đặc tính được phân tích; chu kỳ ADC không mô tả cơ chế thu nhận này.

Trong công trình của Lezama, tín hiệu dòng trên nguồn 50 Hz được lấy mẫu 5 kHz để phục vụ phương pháp tương quan. Ví dụ này cho thấy tốc độ lấy mẫu gắn với phương pháp xử lý và đặc điểm tín hiệu. Vì vậy, chọn tần số thu nhận chỉ bằng cách lấy gấp đôi tần số điện lưới chưa đủ cho bài toán phát hiện biến đổi nhanh. [TL4, tóm tắt và mục 2, tr. in 227–229; tr. PDF 1–3.]

Đồ án phân tích cơ chế thu nhận của từng kênh làm cơ sở lựa chọn chu kỳ. Phương pháp kiểm tra đối chiếu thời điểm nhận sự kiện với tín hiệu tham chiếu và xem xét khả năng tiếp nhận khi bộ xử lý thực hiện nhiệm vụ khác. Giá trị chu kỳ của nguyên mẫu chưa được xác lập trong chương này; việc lựa chọn được thực hiện cùng phương án thu nhận và xử lý tín hiệu ở Chương 2.

## 1.2.7. Tổng hợp yêu cầu kỹ thuật ban đầu

Bảng 1.1 tổng hợp yêu cầu và các thông số làm cơ sở thiết kế. Các nghiên cứu về hiện tượng và bảo vệ hồ quang cung cấp căn cứ phân tích; giá trị chưa xác lập được trình bày theo trạng thái của phương án thiết kế.

*Bảng 1.1. Tổng hợp yêu cầu kỹ thuật ban đầu.*

| Mã yêu cầu | Nội dung | Giá trị/tiêu chí hoặc thông số chưa xác lập | Căn cứ | Cách đánh giá | Trạng thái |
|---|---|---|---|---|---|
| YC-01 | Điện áp | Ba nhóm: điện áp hệ thống, điện áp tín hiệu, nguồn phụ trợ; dải từng cổng theo phương án nguyên mẫu | Mục 1.2.1; TL1, mục 5.6, Hình 7, tr. in 83/PDF 7 | Kiểm tra nguồn và đo mức đầu vào–đầu ra | Chưa chốt dải nguyên mẫu |
| YC-02 | Tần số | Phân biệt tần số nguồn, băng thông và lấy mẫu; nghiên cứu tham khảo dùng nguồn 50 Hz | Mục 1.2.2; TL4, tr. in 227/PDF 1 | Đối chiếu đáp ứng kênh thu nhận với tín hiệu tham chiếu | Có giá trị nguồn tham chiếu; chưa chốt băng thông |
| YC-03 | Dòng điện | Phân tích vị trí, dạng tín hiệu và điều kiện phối hợp; ngưỡng theo phương án thu nhận | Mục 1.2.3; TL1, mục 5.3, 5.6 | Kiểm tra từng tín hiệu và tổ hợp hợp lệ | Chưa chốt giao diện, ngưỡng |
| YC-04 | Độ nhạy | Mô tả nguồn kích thích, bố trí thu nhận, ánh sáng nền và tình huống gây nhầm | Mục 1.2.4; TL1, mục 5.6, tr. in 83/PDF 7 | Ghi nhận đúng, bỏ sót, báo nhầm trên tập thử xác định | Chưa xác lập điều kiện đánh giá |
| YC-05 | Thời gian phản hồi | Đo từ kích thích tham chiếu đến đầu ra; phân biệt với độ rộng xung và thời gian cắt | Mục 1.2.5; TL1, mục 5.6, 6.2 | Đo đồng thời tham chiếu và đầu ra | Đã xác định đại lượng; chưa chốt giới hạn |
| YC-06 | Chu kỳ lấy mẫu | Xác định kênh dùng ADC, nhận trạng thái hoặc xử lý liên tục trước khi chọn chu kỳ | Mục 1.2.6; TL4, mục 2 | Đo chu kỳ hoặc độ trễ nhận sự kiện theo cơ chế lựa chọn | Phụ thuộc thiết kế thu nhận |

Phạm vi thiết bị là cơ sở xem xét tiêu chuẩn áp dụng trong quá trình xác lập yêu cầu. Tài liệu tổng quan đề cập các tiêu chuẩn liên quan đến thiết bị đóng cắt. Việc lựa chọn bộ tiêu chuẩn cho nguyên mẫu dựa trên đối tượng và điều kiện áp dụng cụ thể, không suy ra khả năng tuân thủ chỉ từ chức năng phát hiện. [TL1, mục 3.2, tr. in 78; tr. PDF 2.]

Sau phần phân tích yêu cầu kỹ thuật, mục 1.3 trình bày một trường hợp nghiên cứu riêng ở cấp hệ thống. Kết luận chương tổng hợp phạm vi và các yêu cầu làm cơ sở cho Chương 2.

# 1.3. Phân tích quy trình phát hiện và phối hợp bảo vệ hồ quang theo hồ sơ thiết kế tại Nhà máy Nhiệt điện Quảng Ninh

## 1.3.1. Giới thiệu nhà máy và cơ sở lựa chọn trường hợp nghiên cứu

Nhà máy Nhiệt điện Quảng Ninh do Công ty Cổ phần Nhiệt điện Quảng Ninh quản lý, vận hành, gồm bốn tổ máy với tổng công suất 1.200 MW. Đây là thông tin giới thiệu do doanh nghiệp công bố trên website của công ty. [W2, “Giới thiệu Công ty Cổ Phần Nhiệt Điện Quảng Ninh”, đoạn về quản lý và vận hành.]

Trong dự án nâng cấp, cải tạo hệ thống xử lý khí thải, hồ sơ *Điều chỉnh Báo cáo Nghiên cứu khả thi* có yêu cầu bảo vệ hồ quang đối với biến tần. Phần hồ sơ sử dụng mang tên chủ đầu tư Công ty Cổ phần Nhiệt điện Quảng Ninh và đơn vị tư vấn Viện Năng lượng. Nội dung liên quan nằm trong Chương 4, trang in 169–171/339, tương ứng trang PDF 252–254 của bản gộp. [W1, Chương 4, tr. in 169–171/339; tr. PDF 252–254.]

Trường hợp này được lựa chọn vì hồ sơ nêu rõ mối liên hệ giữa phát hiện hồ quang, thông tin dòng điện và tín hiệu gửi tới máy cắt. Qua đó có thể phân tích yêu cầu bảo vệ theo một phạm vi thiết bị cụ thể, thay vì chỉ mô tả chung về nguy cơ hồ quang. Nội dung dưới đây được trình bày theo yêu cầu thiết kế; giới hạn về dữ liệu hiện trạng được tập hợp tại mục 1.3.5.

## 1.3.2. Phạm vi hệ thống và thiết bị được phân tích

Phạm vi khảo sát là hệ biến tần phục vụ động cơ quạt khói mới trong dự án. Hồ sơ xem xét lựa chọn giải pháp truyền động và quy định các yêu cầu liên quan đến nguồn cấp, biến áp cách ly, thiết bị đóng cắt và bảo vệ. Các bộ phận có liên quan đến bài toán gồm:

- **Nguồn cấp và biến áp cách ly:** Biến tần được yêu cầu lắp sau biến áp cách ly để giảm ảnh hưởng tới mạng điện cung cấp. Thông số nguồn được lựa chọn là ba pha 6,6 kV ±10%, tần số 50 Hz ±5%.
- **Khối biến đổi công suất:** Hồ sơ đề cập phương án HV IGBT/LV IGBT. Trong yêu cầu an toàn, Power Cell và máy biến áp được nêu là các bộ phận thuộc phạm vi xem xét khi xảy ra phóng điện, ngắn mạch có hồ quang.
- **Máy cắt cấp nguồn:** Máy cắt đầu vào được yêu cầu tự động ngắt điện biến tần khi có sự cố. Hệ bảo vệ hồ quang phải có khả năng gửi tín hiệu điều khiển đến máy cắt cấp nguồn. [W1, Chương 4, tr. in 168–171/339; tr. PDF 251–254.]

Như vậy, bài toán tại đây thuộc phạm vi thiết bị trung thế 6,6 kV của hệ biến tần. Phạm vi phát hiện trong hồ sơ gắn với các bộ phận nêu trên và khả năng phối hợp cắt nguồn. Đối với đề tài, đây là trường hợp tham khảo phía trung thế; phạm vi hạ thế được phân tích theo các điều kiện ứng dụng tương ứng.

## 1.3.3. Yêu cầu phát hiện và phối hợp bảo vệ trong hồ sơ

Danh sách chức năng bảo vệ của biến tần có mục phát hiện hồ quang điện. Phần yêu cầu an toàn tiếp tục quy định thiết bị phải nhận biết, phản hồi nhanh, kết hợp đo dòng và gửi tín hiệu tới máy cắt. Bảng 1.2 tóm tắt từng nội dung và thông tin có thể sử dụng để phân tích. [W1, Chương 4, tr. in 170–171/339; tr. PDF 253–254.]

*Bảng 1.2. Yêu cầu bảo vệ hồ quang trong hồ sơ thiết kế.*

| Nội dung hồ sơ | Ý nghĩa chức năng | Trang/mục | Giới hạn thông tin |
|---|---|---|---|
| Có chức năng phát hiện hồ quang trong danh sách bảo vệ biến tần | Nhận biết sự cố có hồ quang là một yêu cầu của thiết bị | W1, Ch. 4, thông số biến tần, tr. in 170/339; PDF 253 | Chưa xác định thiết bị thực hiện |
| Phát hiện và phản hồi nhanh, kịp thời nhận biết sự cố | Có yêu cầu về thời gian trong chuỗi bảo vệ | W1, Ch. 4, “Tiêu chuẩn an toàn”, tr. in 171/339; PDF 254 | Không có giá trị thời gian định lượng trong đoạn này |
| Kết hợp công nghệ đo dòng để nâng cao tính tin cậy | Sử dụng thông tin dòng cùng chức năng phát hiện | Cùng vị trí, PDF 254 | Chưa nêu ngưỡng, vị trí đo hoặc phép logic |
| Gửi tín hiệu điều khiển tới máy cắt cấp nguồn | Liên kết khâu phát hiện với phần tử cắt nguồn | Cùng vị trí, PDF 254 | Chưa có giao diện và sơ đồ mạch chi tiết |
| Xét phóng điện, ngắn mạch tại Power Cell hoặc máy biến áp | Xác định bộ phận thuộc phạm vi sự cố | Cùng vị trí, PDF 254 | Không quy định vị trí cảm biến |
| Đáp ứng yêu cầu an toàn của thiết bị 6,6 kV, gồm phản hồi, cách điện và hạn chế ảnh hưởng hồ quang | Xem bảo vệ cùng kết cấu và đặc tính thiết bị | Cùng vị trí, PDF 254 | Chưa có kết quả thử hoặc nghiệm thu trong phần hồ sơ sử dụng |

Yêu cầu của hồ sơ có thể tập hợp thành ba nhóm:

- **Phát hiện sự cố:** Thiết bị nhận biết được hiện tượng hồ quang trong phạm vi bảo vệ và tạo phản hồi kịp thời.
- **Phối hợp thông tin:** Đo dòng điện được sử dụng để nâng cao tính tin cậy của chức năng bảo vệ.
- **Phối hợp tác động:** Tín hiệu bảo vệ được đưa đến máy cắt cấp nguồn để thực hiện cắt mạch khi có sự cố. [W1, Chương 4, “Tiêu chuẩn an toàn”, tr. in 171/339; tr. PDF 254.]

Các nhóm trên cho thấy bộ phát hiện là một phần trong hệ bảo vệ. Chức năng nhận biết chỉ có ý nghĩa trong phối hợp hệ thống khi tín hiệu được đưa tới đúng phần tử tác động và đáp ứng giao diện yêu cầu.

## 1.3.4. Trình tự chức năng phát hiện và phối hợp tác động

Từ yêu cầu thiết kế, trình tự chức năng được diễn giải thành các bước dưới đây. Đây là quan hệ giữa các chức năng bảo vệ, không phải quy trình thao tác của nhân viên vận hành.

1. **Nhận biết sự cố có hồ quang.** Thiết bị phát hiện theo dõi dấu hiệu sự cố trong phạm vi hệ biến tần. Hồ sơ yêu cầu có chức năng này và nêu Power Cell hoặc máy biến áp trong các trường hợp phóng điện, ngắn mạch được xét. [W1, Chương 4, tr. in 170–171/339; tr. PDF 253–254.]

2. **Kết hợp thông tin dòng điện.** Thông tin dòng tham gia quá trình bảo vệ để nâng cao tính tin cậy. Hồ sơ chưa xác định đây là phép AND, điều kiện ngưỡng hay một cách xử lý khác, nên bước này được giữ ở mức phối hợp chức năng. [W1, Chương 4, tr. in 171/339; tr. PDF 254.]

3. **Gửi tín hiệu điều khiển tới máy cắt.** Khi xử lý sự cố thuộc phạm vi bảo vệ, hệ thống phải có khả năng tạo tín hiệu đến máy cắt cấp nguồn. Khả năng này đòi hỏi xem xét giao diện giữa khối bảo vệ và mạch điều khiển máy cắt. [W1, Chương 4, tr. in 171/339; tr. PDF 254.]

4. **Cắt nguồn cấp cho phần thiết bị sự cố.** Máy cắt thực hiện chức năng ngắt mạch theo yêu cầu bảo vệ. Kết quả ở bước này còn phụ thuộc thiết bị đóng cắt và mạch phối hợp; thời gian phát hiện không đại diện cho toàn bộ thời gian cắt. [W1, Chương 4, tr. in 169 và 171/339; tr. PDF 252, 254; TL1, mục 6.2, tr. in 84; tr. PDF 8.]

Hồ sơ có mô tả tích hợp điều khiển biến tần với DCS ở phần trước. Tuy nhiên, đoạn yêu cầu bảo vệ hồ quang chỉ xác định tín hiệu gửi tới máy cắt cấp nguồn. Vì vậy, chưa thể xác định đường truyền của tín hiệu này qua DCS hoặc bổ sung các bước xác nhận, ghi sự kiện và khôi phục từ phần mô tả điều khiển chung. [W1, Chương 4, tr. in 168–169 và 171/339; tr. PDF 251–252, 254.]

## 1.3.5. Đối chiếu với yêu cầu của đề tài và giới hạn thông tin

Trường hợp Quảng Ninh bổ sung những dữ liệu liên quan trực tiếp đến các yêu cầu trong Bảng 1.1:

- **Điện áp và tần số:** Nguồn biến tần được quy định ba pha 6,6 kV ±10%, 50 Hz ±5%, cung cấp bối cảnh để phân tích ứng dụng trung thế.
- **Dòng điện:** Có yêu cầu kết hợp đo dòng với chức năng bảo vệ hồ quang.
- **Thời gian phản hồi:** Có yêu cầu phản hồi nhanh và phối hợp máy cắt, nhưng chưa có giới hạn mili giây trong đoạn được sử dụng. [W1, Chương 4, tr. in 169–171/339; tr. PDF 252–254.]

Những thông tin còn thiếu để xác định hệ thống thực tế gồm:

- Danh mục, mã và số lượng thiết bị phát hiện được cung cấp; loại cảm biến và vị trí lắp.
- Sơ đồ đấu dây, giao diện gửi tín hiệu đến máy cắt, ngưỡng và logic phối hợp dòng.
- Biên bản thử, bản vẽ hoàn công, tài liệu nghiệm thu và dữ liệu vận hành.

Tài liệu sử dụng là bản hồ sơ lưu công khai, chưa được đối chiếu với cùng tệp tải từ doanh nghiệp hoặc HNX. Vì vậy, kết quả khảo sát xác lập được yêu cầu thiết kế, chưa xác nhận hệ bảo vệ đã được lắp đặt và vận hành như thế nào. Xuất xứ bản đọc được ghi tại W1 trong danh mục tài liệu.

Trường hợp nhà máy làm rõ quan hệ giữa phát hiện sự cố, thông tin dòng điện và tác động cắt nguồn trong hồ sơ thiết kế. Phần kết luận tổng hợp các yêu cầu kỹ thuật và giới hạn thông tin của chương.

# 1.4. Kết luận chương

Chương 1 đã trình bày đối tượng nghiên cứu, hiện tượng chớp hồ quang và các hậu quả liên quan đến thiết bị, con người. Các minh chứng thử nghiệm cho thấy ý nghĩa của việc phát hiện và phản hồi trong thời gian ngắn. Từ đó, chương xác định sáu nhóm yêu cầu về điện áp, tần số, dòng điện, độ nhạy, thời gian phản hồi và chu kỳ lấy mẫu.

Hồ sơ thiết kế tại Nhà máy Nhiệt điện Quảng Ninh đặt ra yêu cầu phát hiện hồ quang, kết hợp đo dòng và gửi tín hiệu tới máy cắt trong phạm vi hệ biến tần trung thế. Dữ liệu hiện có xác lập được yêu cầu của hồ sơ, chưa xác nhận hiện trạng lắp đặt và vận hành của hệ bảo vệ. Các thông số chưa xác lập của nguyên mẫu được tiếp tục phân tích cùng phương án thiết kế.

Trên cơ sở đó, Chương 2 trình bày cơ sở lý thuyết về phát hiện, thu nhận và xử lý tín hiệu, khảo sát thiết bị thương mại và phân tích lựa chọn linh kiện. Những thông số chưa xác lập trong Bảng 1.1 được xem xét cùng phương án thiết kế và điều kiện đánh giá của hệ thống.

# Tài liệu tham khảo của Chương 1

**TL1 —** Lauri Kumpulainen, G. Amjad Hussain, Marc Rival, Matti Lehtonen, Kimmo Kauhaniemi, *Aspects of arc-flash protection and prediction*, Electric Power Systems Research 116, 2014, tr. 77–86. DOI: 10.1016/j.epsr.2014.05.011. Tệp: [Aspects of arc-flash protection and prediction.pdf](<Tham khảo/Aspects of arc-flash protection and prediction.pdf>).

**TL2 —** Vytenis Babrauskas, *Electric arc explosions—A review*, Fire Safety Journal 89, 2017, tr. 7–15. DOI: 10.1016/j.firesaf.2017.02.006. Tệp: [Electric arc explosions—A review.pdf](<Tham khảo/Electric arc explosions—A review.pdf>).

**TL3 —** Mahmood Matin, Amir Dehghanian, Mohammad Dastranj, Hossein Darijani, *Explainable artificial intelligence modeling of internal arc in a medium voltage switchgear based on different CFD simulations*, Heliyon 10, 2024, e29594. DOI: 10.1016/j.heliyon.2024.e29594. Tệp: [Explainable artificial intelligence modeling of internal arc in a medium voltage switchgear based on different CFD simulations.pdf](<Tham khảo/Explainable artificial intelligence modeling of internal arc in a medium voltage switchgear based on different CFD simulations.pdf>). CC BY 4.0 ghi tại trang PDF 1.

**TL4 —** Jinmi Lezama, Patrick Schweitzer, Etienne Tisserand, Jean-Baptiste Humbert, Serge Weber, Patrice Joyeux, *An embedded system for AC series arc detection by inter-period correlations of current*, Electric Power Systems Research 129, 2015, tr. 227–234. Tệp: [An embedded system for AC series arc detection by inter-period correlations of current.pdf](<Tham khảo/An embedded system for AC series arc detection by inter-period correlations of current.pdf>).

**TL6 —** Liangshi Lin, Wei Gao, Gengjie Yang, *A DC arc fault location method for PV systems based on redundant antenna array and ellipse algorithm*, Solar Energy 274, 2024, 112588. DOI: 10.1016/j.solener.2024.112588. Tệp: [A DC arc fault location method for PV systems based on redundant antenna array and ellipse algorithm.pdf](<Tham khảo/A DC arc fault location method for PV systems based on redundant antenna array and ellipse algorithm.pdf>).

**W1 —** Công ty Cổ phần Nhiệt điện Quảng Ninh; Viện Năng lượng (tư vấn), *Dự án nâng cấp, cải tạo hệ thống xử lý khí thải Nhà máy Nhiệt điện Quảng Ninh — Điều chỉnh Báo cáo Nghiên cứu khả thi*, Chương 4 trong tệp gộp công khai có thông tin hiển thị ký số 11/06/2026 tại trang PDF 1. [Bản sao đã đọc tại CafeF](https://cafef1.mediacdn.vn/download/110626/qtp-tai-lieu-hop-ai-hoi-dong-co-dong-3-619481.pdf); [bản lưu kiểm chứng](nguon_web/qtp-full.pdf). Tệp có 688 trang; trang in 167–171/339 của Chương 4 tương ứng PDF 250–254. Truy cập 24/10/2026. Chưa đối chiếu được cùng tệp tại doanh nghiệp/HNX; CafeF là nơi lưu bản sao, không phải tác giả hồ sơ.

**W2 —** Công ty Cổ phần Nhiệt điện Quảng Ninh, *Giới thiệu Công ty Cổ Phần Nhiệt Điện Quảng Ninh*, trang “Giới thiệu chung”, hiển thị ngày 23/03/2017. [Trang doanh nghiệp đã đọc](https://quangninhtpc.com.vn/c3/gioi-thieu-f/Gioi-thieu-chung-2-204). Truy cập 24/10/2026. Dùng cho bối cảnh doanh nghiệp, không xác nhận hiện trạng bảo vệ hồ quang.
