> **Đề tài:** Thiết kế hệ thống nhúng phát hiện chớp hồ quang điện (arc-flash) trong hệ thống điện hạ thế và trung thế.
>
> **Ghi chú bản thảo:** Nội dung hướng tới khoảng 10–14 trang A4 khi dàn bằng Times New Roman 13, giãn dòng khoảng 1,15. Số trang thực tế phụ thuộc cách dàn trang và kích thước hình.

Chương 1 trình bày bài toán phát hiện chớp hồ quang điện, các yêu cầu kỹ thuật của hệ thống và một trường hợp ứng dụng tại Nhà máy Nhiệt điện Quảng Ninh. Bên cạnh đó, chương khảo sát thiết bị Mors Smitt 1S23 để tìm hiểu cách thu nhận tín hiệu, phát hiện và phối hợp với thiết bị bảo vệ.

# 1.1. Tổng quan bài toán phát hiện chớp hồ quang điện

## 1.1.1. Đối tượng nghiên cứu và bối cảnh ứng dụng

Trong hệ thống cung cấp điện công nghiệp, tủ điện là nơi bố trí các thiết bị đóng cắt, đo lường và bảo vệ. Các bộ phận như thanh cái, đầu cáp, tiếp điểm và lớp cách điện cùng làm việc trong không gian giới hạn của tủ. Khi xảy ra sự cố hồ quang nội bộ, nhiệt, áp suất và vật chất nóng phát sinh có thể làm hư hỏng thiết bị, gây nguy hiểm cho người ở gần và gián đoạn cấp điện. [TL1, mục 1 và 3.2, tr. in 78; tr. PDF 2.]

Đề tài tập trung vào việc phát hiện chớp hồ quang trong tủ điện hạ thế và trung thế. Những bộ phận cần quan tâm gồm:

- **Thanh cái, mối nối và tiếp điểm:** Đây là các phần tử dẫn điện trong tủ. Tình trạng mối nối, lớp cách điện và khoảng cách giữa các phần dẫn điện có liên quan đến nguy cơ phát sinh sự cố nội bộ.
- **Đầu cáp và khoang đấu nối:** Là nơi kết nối cáp với thiết bị. Tổng quan kỹ thuật của Kumpulainen và cộng sự xem đầu cáp là một vị trí điển hình cần quan tâm khi theo dõi sự cố hồ quang.
- **Khoang thiết bị đóng cắt và đo lường:** Gồm máy cắt, dao cách ly, dao tiếp địa và biến điện đo lường. Việc bố trí các bộ phận này cùng kết cấu vách ngăn quyết định không gian cần giám sát. [TL1, mục 3.2 và 4.3, tr. in 78–80; tr. PDF 2–4.]

Hình 1.1 cho thấy kết cấu của tủ trung thế KMZ_31 được sử dụng trong nghiên cứu về hồ quang nội bộ. Tủ có vách bao và đường thoát khí riêng. Khi xác định vùng giám sát, cần xét từng khoang và các vật cản trong tủ, thay vì chỉ xét khoảng cách từ cảm biến đến vị trí có thể xảy ra sự cố. [TL3, Hình 5, tr. in/PDF 7; W4, “Sensor Placement”, tr. in/PDF 25.]

{{HINH_1}}

Phạm vi giám sát được xem xét từ toàn trạm, dãy tủ đến từng khoang tủ. Trong đó, khoang tủ là đơn vị cần khảo sát cụ thể khi bố trí đầu thu quang. Hướng dẫn của hãng yêu cầu cảm biến phải bao phủ các khoang được bảo vệ; một đầu thu không tự bảo đảm khả năng quan sát mọi khoang trong dãy tủ. [W4, “Sensor Placement”, tr. in/PDF 25.]

Đối với hệ thống nhúng, nhiệm vụ nghiên cứu là thu nhận dấu hiệu sự cố, xử lý để nhận biết sự kiện và đưa ra tín hiệu phản hồi. Việc cắt nguồn còn cần đến các phần tử bảo vệ và thiết bị đóng cắt bên ngoài. Vì vậy, khi xây dựng yêu cầu, cần xác định rõ đầu vào nào được sử dụng, đầu ra cung cấp thông tin gì và phần chức năng nào thuộc bộ phát hiện. [TL1, mục 2 và 6.2, tr. in 78–79, 84; tr. PDF 2–3, 8.]

## 1.1.2. Hiện tượng hồ quang điện và chớp hồ quang điện

Hồ quang điện là hiện tượng phóng điện phát sáng, trong đó dòng điện đi qua môi trường plasma nóng giữa các điện cực. Hình dạng và sự phát triển của hồ quang phụ thuộc vào thiết bị, môi trường và nguồn năng lượng duy trì phóng điện. Trong mạch điện, cần phân biệt ba khái niệm thường gặp:

- **Hồ quang điện — electric arc:** Chỉ hiện tượng phóng điện. Hồ quang có thể xuất hiện trong một quá trình làm việc đã được thiết kế, chẳng hạn quá trình ngắt dòng của máy cắt.
- **Sự cố hồ quang — arc fault:** Chỉ sự cố có hồ quang phát sinh ngoài chức năng làm việc dự kiến của thiết bị.
- **Chớp hồ quang điện — arc flash:** Gắn với thành phần bức xạ nhiệt của hồ quang năng lượng lớn. Với đề tài này, nhiệm vụ phát hiện tập trung vào dấu hiệu của sự kiện, đặc biệt là phát sáng, để phục vụ việc nhận biết và phản hồi. [TL2, mục 1, tr. in 7; tr. PDF 1; TL1, mục 2, tr. in 78–79; tr. PDF 2–3.]

Trong thao tác đóng cắt bình thường, hồ quang được hình thành trong bộ phận có kết cấu chịu và dập hồ quang. Với sự cố nội bộ, phóng điện xảy ra tại nơi không được thiết kế cho quá trình đó, làm tác động đến những phần tử xung quanh. Sự khác nhau này có ý nghĩa đối với bộ phát hiện: tín hiệu xuất hiện trong quá trình làm việc bình thường phải được xem xét khi đánh giá tác động gây nhầm. [TL2, mục 1, tr. in 7; tr. PDF 1.]

Những yếu tố liên quan đến sự cố được tài liệu tổng quan đề cập gồm tình trạng cách điện, các điểm đấu nối, tiếp điểm và công tác bảo trì. Theo dõi các dấu hiệu suy giảm trước sự cố có thể hỗ trợ phòng ngừa. Tuy nhiên, phát hiện hồ quang đã xuất hiện là một nhiệm vụ khác, đòi hỏi nhận biết và phản hồi trong thời gian ngắn. [TL1, mục 3 và 4, tr. in 78–81; tr. PDF 2–5.]

Tác động của hồ quang đến thiết bị và con người có thể chia thành các nhóm chính:

- **Tác động nhiệt:** Bức xạ và vật chất nóng có thể gây bỏng, làm hỏng cách điện và các phần dẫn điện.
- **Tác động áp suất:** Kênh hồ quang giãn nở tạo sóng áp suất; khí trong vỏ tủ được nung nóng còn gây tăng áp trong không gian bao kín. Hai quá trình này được phân biệt trong nghiên cứu về nổ hồ quang.
- **Hư hỏng và gián đoạn hoạt động:** Hư hỏng thiết bị có thể kéo theo thời gian ngừng cấp điện, sửa chữa và khôi phục hệ thống. [TL2, tóm tắt và mục 1, tr. in 7; tr. PDF 1; TL1, mục 1, tr. in 78; tr. PDF 2.]

Hình 1.2 ghi lại tủ KMZ_31 trước, trong và sau thử nghiệm tại phòng thí nghiệm công suất lớn ICMET, Romania. Ánh sáng phát ra trong quá trình thử và hư hỏng sau thử cho thấy sự cố cần được xem xét cả về phát hiện lẫn khả năng chịu đựng của kết cấu tủ. [TL3, mục 1 và Hình 1, tr. in/PDF 1–2.]

{{HINH_2}}

Các nghiên cứu về hồ quang sử dụng nhiều loại tín hiệu khác nhau. Lezama và cộng sự nghiên cứu hồ quang nối tiếp trên mạch dân dụng 230 V AC–50 Hz bằng tương quan dòng điện giữa các chu kỳ. Lin và cộng sự nghiên cứu định vị hồ quang DC trong hệ thống quang điện từ bức xạ điện từ thu bằng anten. Đây là những bài toán có đối tượng, tín hiệu và điều kiện khác với phát hiện chớp hồ quang trong tủ điện. [TL4, tóm tắt, tr. in 227; tr. PDF 1; TL6, tóm tắt và mục 1, tr. PDF 1.]

Khi tham khảo các công trình trên, cần lựa chọn nội dung phù hợp với nhiệm vụ nghiên cứu. Kết quả nhận dạng trên một tập tải dân dụng không đại diện cho khả năng phát hiện trong tủ trung thế; độ chính xác định vị hồ quang DC cũng không thay thế cho độ nhạy đầu thu quang. Cơ chế thu nhận và xử lý từng loại tín hiệu sẽ được tìm hiểu ở Chương 2.

## 1.1.3. Số liệu minh chứng và tính cấp thiết

Mức độ nguy hiểm của sự cố thể hiện qua hư hỏng thiết bị và năng lượng tác động trong những điều kiện cụ thể. Hình 1.3 là ảnh thanh cái hạ thế sau một phép thử được công bố trong tài liệu tổng quan. Điều kiện của phép thử gồm điện áp U = 726 V, dòng ngắn mạch ký hiệu Ik = 77 kA và thời gian hồ quang 65 ms. Sau thử, thanh cái bị nóng chảy cục bộ tại ranh giới lớp cách điện. [TL1, Hình 2, tr. in 80; tr. PDF 4.]

{{HINH_3}}

Phép thử cho thấy hư hỏng có thể hình thành trong khoảng thời gian ngắn. Bên cạnh đó, năng lượng tác động còn phụ thuộc vào thời gian hồ quang tồn tại. Hình 1.4 biểu diễn quan hệ này trong trường hợp tính toán với U = 15 kV, Ik = 50 kA, khe hở 152 mm và khoảng cách làm việc 910 mm. Khi các điều kiện của trường hợp tính giữ nguyên, năng lượng trên đơn vị diện tích tăng theo thời gian hồ quang. [TL1, mục 5.2–5.5 và Hình 5, tr. in 81–83; tr. PDF 5–7.]

{{HINH_4}}

Từ những minh chứng trên, bài toán phát hiện đặt ra các nhu cầu sau:

- **Nhận biết sớm sự kiện:** Rút ngắn thời gian từ khi dấu hiệu hồ quang xuất hiện đến khi có tín hiệu phản hồi, tạo điều kiện cho khâu bảo vệ tiếp theo làm việc.
- **Phân biệt được tác động gây nhầm:** Xem xét tín hiệu sự cố cùng điều kiện làm việc bình thường, tránh đánh giá bộ phát hiện chỉ bằng một trường hợp kích thích thuận lợi.
- **Đánh giá được từng khâu:** Xác định thời gian thu nhận, xử lý và xuất tín hiệu; khi xét toàn hệ thống phải tính đến thiết bị bảo vệ và máy cắt. [TL1, mục 5.5–5.6 và 6.2, tr. in 83–84; tr. PDF 7–8; các nhu cầu trên được rút ra cho đề tài.]

Các giá trị thử nghiệm vừa nêu là điều kiện của tài liệu nguồn. Bộ tài liệu hiện có chưa cung cấp thống kê đủ phạm vi và thời gian quan sát để xác định tần suất sự cố tại Việt Nam hoặc Nhà máy Nhiệt điện Quảng Ninh. Do đó, tính cấp thiết ở đây được làm rõ từ hậu quả và nhu cầu phản hồi, thay vì ước lượng xác suất sự cố theo năm.

Với nhiệm vụ này, hệ thống nhúng cần có khả năng thu nhận tín hiệu, đưa ra quyết định và cung cấp đầu ra để kiểm tra. Những yêu cầu về điện áp, tần số, dòng điện, độ nhạy và thời gian cần được xác định trước khi lựa chọn giải pháp phần cứng.

# 1.2. Phân tích yêu cầu kỹ thuật của bài toán

## 1.2.1. Yêu cầu về điện áp

Yêu cầu điện áp liên quan đến cả hệ thống được giám sát và bản thân bộ phát hiện. Trong quá trình thiết kế, cần tách ba loại điện áp:

- **Điện áp hệ thống:** Là điện áp của thiết bị điện nằm trong phạm vi giám sát. Chẳng hạn, hồ sơ biến tần tại Quảng Ninh quy định nguồn ba pha 6,6 kV ±10%. Giá trị này mô tả bối cảnh ứng dụng trung thế.
- **Điện áp tín hiệu:** Là mức điện áp ở các giao diện đo và xử lý. Sơ đồ 1S23 cho thấy cảm biến kết nối với mô-đun, còn đầu ra mô-đun nối tới đầu vào trạng thái rơ-le; đây là đường tín hiệu cần được kiểm tra về mức điện, cực tính và cách ly.
- **Nguồn phụ trợ:** Là nguồn nuôi thiết bị phát hiện. Với 1S23, nguồn này có các mức DC danh định theo biến thể sản phẩm, được trình bày ở mục 1.4. [W1, Chương 4, tr. in 169/339; tr. PDF 252; W3, “Description”, “Auxiliary Supply” và “Connection and Wiring Diagram”, tr. PDF 2, 5, 7.]

Việc tách các loại điện áp giúp xác định đúng giao diện cần thiết kế. Điện áp trung thế của thiết bị được giám sát không phải điện áp đưa trực tiếp vào bộ xử lý nhúng. Mỗi cổng thu nhận hoặc xuất tín hiệu cần được mô tả bằng mức danh định, dải làm việc và điều kiện kết nối với thiết bị ngoài.

Đối với nguyên mẫu, dải nguồn và mức tín hiệu sẽ được xác định theo phương án thu nhận lựa chọn ở Chương 2. Nội dung đánh giá gồm kiểm tra nguồn cấp, đo mức tại đầu vào–đầu ra và đối chiếu với đặc tính các khối kết nối. Trạng thái cụ thể hóa yêu cầu được tổng hợp trong Bảng 1.1.

## 1.2.2. Yêu cầu về tần số

Tần số cần được xem xét theo từng đại lượng thay vì dùng chung một giá trị cho toàn hệ thống. Ba nội dung liên quan trực tiếp gồm:

- **Tần số nguồn điện:** Hồ sơ Quảng Ninh quy định nguồn biến tần 50 Hz ±5%, trong khi dải tần đầu ra được yêu cầu là 0–50 Hz. Hai thông số này thuộc đặc tính thiết kế của biến tần.
- **Dải tần tín hiệu cần thu nhận:** Phụ thuộc vào dấu hiệu được sử dụng. Kênh chỉ tiếp nhận trạng thái dòng có nhu cầu khác với kênh đo dạng sóng; kênh quang cần theo dõi được biến đổi ánh sáng phục vụ phát hiện.
- **Tần số lấy mẫu:** Là đặc tính của phương án số hóa tín hiệu. Trong nghiên cứu hồ quang nối tiếp của Lezama, mạch nguồn làm việc ở 50 Hz nhưng tín hiệu dòng được lấy mẫu 5 kHz. [W1, Chương 4, tr. in 169/339; tr. PDF 252; TL4, tóm tắt, tr. in 227; tr. PDF 1.]

Ví dụ trên cho thấy tần số nguồn không quyết định trực tiếp tần số thu nhận. Đối với hệ thống của đề tài, cần xác định thông tin nào phải được giữ lại trước khi chọn băng thông và tốc độ xử lý. Nếu bộ thu nhận làm mất biến đổi cần nhận biết thì việc tăng tốc xử lý ở phía sau cũng không khôi phục được thông tin đó.

Khi đánh giá, cần đối chiếu dải đáp ứng của chuỗi thu nhận với tín hiệu tham chiếu, đồng thời xem xét ảnh hưởng của các khối điều hòa và xử lý. Dải tần đo của nguyên mẫu sẽ phụ thuộc loại tín hiệu được lựa chọn, không lấy nguyên cấu hình của một nghiên cứu hồ quang nối tiếp làm yêu cầu cho kênh quang.

## 1.2.3. Yêu cầu về dòng điện

Dòng điện có thể được sử dụng để nhận biết sự cố hoặc xác nhận một dấu hiệu khác. Với bảo vệ dựa trên ánh sáng và quá dòng, tài liệu tổng quan mô tả việc phối hợp hai điều kiện để tăng tính chắc chắn của quyết định. Hình 1.5 trình bày nguyên lý này: tín hiệu tác động chỉ được hình thành theo tổ hợp ánh sáng và quá dòng của sơ đồ nguồn. [TL1, mục 5.6 và Hình 6, tr. in 83; tr. PDF 7.]

{{HINH_5}}

Khi xây dựng kênh dòng, cần phân biệt:

- **Dòng định mức:** Gắn với chế độ làm việc của tải hoặc thiết bị.
- **Dòng sự cố:** Là dòng điện trong điều kiện sự cố. Dòng hồ quang có thể thấp hơn dòng sự cố kim loại, từ đó ảnh hưởng đến thời gian tác động của bảo vệ quá dòng.
- **Tín hiệu đưa vào bộ phát hiện:** Có thể là đại lượng thứ cấp của khối đo hoặc trạng thái do phần tử bảo vệ cung cấp, tùy cấu trúc hệ thống. Với 1S23, chức năng kiểm tra dòng thuộc rơ-le ngoài trong sơ đồ ứng dụng. [TL1, mục 5.3, tr. in 81–82; tr. PDF 5–6; W4, “Example Schematic”, tr. in/PDF 13.]

Yêu cầu của kênh dòng vì vậy cần nêu rõ vị trí lấy thông tin, dạng tín hiệu và vai trò trong quyết định phát hiện. Nếu sử dụng dòng để xác nhận tín hiệu quang, phải xác định điều kiện phối hợp và quan hệ thời gian giữa hai tín hiệu. Nội dung này khác với việc chọn một ngưỡng từ dòng ngắn mạch của nguồn thử.

Cách đánh giá gồm kiểm tra riêng từng tín hiệu và kiểm tra tổ hợp được quy định hợp lệ. Ngưỡng, tỷ số biến dòng và giao diện cụ thể chưa được xác lập cho nguyên mẫu. Hồ sơ Quảng Ninh được phân tích ở mục 1.3 cung cấp yêu cầu kết hợp đo dòng, nhưng chưa quy định một phép logic cụ thể. [W1, Chương 4, tr. in 171/339; tr. PDF 254.]

## 1.2.4. Yêu cầu về độ nhạy

Độ nhạy phản ánh khả năng nhận biết tín hiệu trong điều kiện xác định. Với kênh quang, cần xem xét từ đầu thu đến quyết định của bộ phát hiện. Có ba nội dung phải được mô tả riêng:

- **Khả năng thu nhận của cảm biến:** Liên quan đến kích thích quang và tín hiệu điện thu được tại đầu ra cảm biến.
- **Ngưỡng tác động:** Là điều kiện mà mạch hoặc khối xử lý dùng để nhận biết sự kiện.
- **Khả năng phát hiện của hệ thống:** Được đánh giá bằng kết quả nhận đúng, bỏ sót và báo nhầm trên tập tình huống thử được mô tả rõ.

Vị trí đầu thu là một phần của điều kiện đánh giá. User Guide 1S23 yêu cầu bố trí cảm biến bao phủ các khoang cần bảo vệ và dùng thêm đầu thu khi vùng giám sát lớn hơn vùng thu nhận. Hướng dẫn cũng đề cập ảnh hưởng của ánh sáng môi trường kéo dài đến chức năng thiết bị. [W4, “Sensor Installation”, tr. in/PDF 23–26; W3, “Arc Sensor Continuously Picked Up”, tr. in/PDF 3.]

Từ đó, phép đánh giá độ nhạy cần ghi rõ nguồn kích thích, khoảng cách, hướng thu, vật cản và ánh sáng nền. Một lần không phát hiện có thể xuất phát từ tín hiệu bị che khuất hoặc thu nhận không đủ, bên cạnh nguyên nhân về ngưỡng. Ngược lại, đánh giá chỉ bằng việc chiếu sáng mạnh trực tiếp vào đầu thu chưa phản ánh khả năng phân biệt sự kiện trong điều kiện sử dụng.

Đối với đồ án, điều kiện cần phát hiện và tập tác động gây nhầm phải được xây dựng cùng phương án thu nhận. Chỉ sau khi có các điều kiện này mới có thể đặt ngưỡng và đánh giá tỷ lệ phát hiện có ý nghĩa. Bảng 1.1 ghi nhận phần dữ liệu cần bổ sung, thay cho việc dùng một yêu cầu chung như độ nhạy cao.

## 1.2.5. Yêu cầu về thời gian phản hồi

Thời gian phản hồi có ý nghĩa khi xác định rõ mốc bắt đầu và kết thúc. Với mô-đun phát hiện, một cách đánh giá là đo từ lúc kích thích xuất hiện đến lúc đầu ra điện làm việc. Bulletin 1S23 v01.0 sử dụng đúng cách mô tả này cho thông số dưới 2 ms: từ chớp sáng đến đầu ra tác động. [W3, “Technical Data”, tr. in 5/11; tr. PDF 5.]

Các khoảng thời gian cần tách trong quá trình đánh giá gồm:

- **Thời gian thu nhận:** Từ kích thích tham chiếu đến khi tín hiệu sẵn sàng cho khối xử lý.
- **Thời gian xử lý và xuất đầu ra:** Từ tín hiệu nhận được đến khi đầu ra đạt trạng thái tác động quy định.
- **Thời gian phối hợp bảo vệ và cắt:** Thuộc các phần tử phía sau bộ phát hiện, bao gồm rơ-le và thiết bị đóng cắt. Tài liệu tổng quan chỉ ra rằng khi phát hiện làm việc nhanh, thời gian loại trừ còn phụ thuộc đáng kể vào thiết bị sơ cấp. [TL1, mục 5.6 và 6.2, tr. in 83–84; tr. PDF 7–8.]

Ngoài độ trễ, đầu ra còn có độ rộng xung. Bulletin 1S23 ghi độ trễ dưới 2 ms và xung duy trì 110 ms ±10 ms. Độ rộng xung cho biết thời gian đầu ra ở trạng thái tác động; nó không phải khoảng thời gian chờ trước khi phát hiện. [W3, “Trip Output Circuit Operation” và “Technical Data”, tr. in/PDF 3, 5.]

Đối với nguyên mẫu, cần đo kích thích tham chiếu và đầu ra trên cùng cơ sở thời gian. Báo cáo kết quả phải nêu vị trí đặt mốc, điều kiện kích thích và cách xác định trạng thái đầu ra. Nếu sử dụng nguồn sáng thay thế, kết quả được dùng để đánh giá đáp ứng quang của bộ phát hiện trong điều kiện thử, không thay thế thời gian cắt sự cố của cả hệ thống.

## 1.2.6. Yêu cầu về chu kỳ lấy mẫu

Chu kỳ lấy mẫu là khoảng thời gian giữa hai lần thu nhận liên tiếp khi thực hiện số hóa đều. Quan hệ giữa chu kỳ và tần số lấy mẫu là \(f_s = 1/T_s\). Việc chọn chu kỳ phải dựa vào tín hiệu và thời gian dành cho quyết định phát hiện.

Tùy cách thu nhận, nội dung cần đánh giá có thể khác nhau:

- **Kênh đo tương tự bằng ADC:** Cần xác định dải thông tin giữ lại, chu kỳ lấy mẫu và ảnh hưởng của khối điều hòa tín hiệu trước ADC.
- **Kênh nhận trạng thái số:** Cần xác định khả năng nhận cạnh hoặc xung, độ trễ tiếp nhận và điều kiện để không bỏ qua sự kiện.
- **Kênh xử lý liên tục bằng mạch so sánh:** Cần xét đáp ứng của mạch và đường truyền tín hiệu tới bộ xử lý, thay vì mặc định mọi hoạt động đều được mô tả bằng chu kỳ ADC.

Trong công trình của Lezama, tín hiệu dòng trên nguồn 50 Hz được lấy mẫu 5 kHz để phục vụ phương pháp tương quan. Ví dụ này cho thấy tốc độ lấy mẫu gắn với phương pháp xử lý và đặc điểm tín hiệu. Vì vậy, chọn tần số thu nhận chỉ bằng cách lấy gấp đôi tần số điện lưới chưa đủ cho bài toán phát hiện biến đổi nhanh. [TL4, tóm tắt và mục 2, tr. in 227–229; tr. PDF 1–3.]

Yêu cầu của đề tài là xác định cơ chế thu nhận cho từng kênh trước khi chốt chu kỳ. Khi kiểm tra, cần đối chiếu thời điểm nhận sự kiện với tín hiệu tham chiếu và xem xét khả năng tiếp nhận khi bộ xử lý đang thực hiện nhiệm vụ khác. Tài liệu 1S23 được khảo sát chỉ công bố các đặc tính hoạt động liên quan, không cung cấp tần số lấy mẫu nội bộ để dùng làm thông số thiết kế của nguyên mẫu. [W3, “Technical Data”, tr. in/PDF 5.]

## 1.2.7. Tổng hợp yêu cầu kỹ thuật ban đầu

Bảng 1.1 tổng hợp yêu cầu và nội dung cần xác định trước khi thiết kế. Các thông số của hồ sơ ứng dụng và thiết bị thương mại được giữ làm giá trị đối chiếu; phần chưa định lượng được ghi rõ để tiếp tục xử lý ở bước lựa chọn giải pháp.

*Bảng 1.1. Tổng hợp yêu cầu kỹ thuật ban đầu.*

| Mã yêu cầu | Nội dung | Giá trị/tiêu chí hoặc dữ liệu cần bổ sung | Căn cứ | Cách đánh giá | Trạng thái |
|---|---|---|---|---|---|
| YC-01 | Điện áp | Tách điện áp hệ thống, tín hiệu và nguồn phụ trợ; xác định dải của từng cổng nguyên mẫu | Mục 1.2.1; W1, Ch. 4, tr. in 169/PDF 252; W3, tr. 5 | Kiểm tra nguồn và đo mức đầu vào–đầu ra | Chưa chốt dải nguyên mẫu |
| YC-02 | Tần số | Nguồn biến tần trong hồ sơ: 50 Hz ±5%; xác định riêng dải thông kênh đo | Mục 1.2.2; W1, Ch. 4, tr. in 169/PDF 252; TL4, tr. in 227/PDF 1 | Đối chiếu đáp ứng kênh thu nhận với tín hiệu tham chiếu | Có giá trị nguồn tham chiếu; cần chọn băng thông |
| YC-03 | Dòng điện | Xác định vị trí, dạng tín hiệu và điều kiện phối hợp; bổ sung ngưỡng khi chọn giải pháp | Mục 1.2.3; TL1, mục 5.3, 5.6; W1, Ch. 4, tr. in 171/PDF 254 | Kiểm tra từng tín hiệu và tổ hợp hợp lệ | Có yêu cầu chức năng; chưa chốt giao diện, ngưỡng |
| YC-04 | Độ nhạy | Mô tả nguồn kích thích, bố trí thu nhận, ánh sáng nền và tình huống gây nhầm | Mục 1.2.4; W4, tr. 23–26; W3, tr. 3 | Ghi nhận đúng, bỏ sót, báo nhầm trên tập thử xác định | Cần xây dựng điều kiện đánh giá |
| YC-05 | Thời gian phản hồi | Đo từ kích thích tham chiếu đến đầu ra; phân biệt với độ rộng xung và thời gian cắt | Mục 1.2.5; W3, tr. 5; TL1, mục 5.6, 6.2 | Đo đồng thời tham chiếu và đầu ra | Đã xác định đại lượng; chưa chốt giới hạn |
| YC-06 | Chu kỳ lấy mẫu | Xác định kênh dùng ADC, nhận trạng thái hoặc xử lý liên tục trước khi chọn chu kỳ | Mục 1.2.6; TL4, mục 2 | Đo chu kỳ hoặc độ trễ nhận sự kiện theo cơ chế lựa chọn | Phụ thuộc thiết kế thu nhận |

Việc xác lập yêu cầu còn cần xem xét tiêu chuẩn phù hợp với phạm vi thiết bị. Tài liệu tổng quan đề cập các tiêu chuẩn liên quan đến thiết bị đóng cắt, còn Bulletin 1S23 liệt kê những hạng mục kiểm tra của sản phẩm. Lựa chọn bộ tiêu chuẩn cho nguyên mẫu phải dựa trên đối tượng và điều kiện áp dụng cụ thể. [TL1, mục 3.2, tr. in 78; tr. PDF 2; W3, “Compliance”, tr. in/PDF 6.]

Để làm rõ cách các yêu cầu này xuất hiện trong một công trình, mục 1.3 xem xét hồ sơ thiết kế của Nhà máy Nhiệt điện Quảng Ninh. Phần khảo sát 1S23 sau đó bổ sung cách triển khai chức năng ở cấp thiết bị.

# 1.3. Phân tích quy trình phát hiện và phối hợp bảo vệ hồ quang theo hồ sơ thiết kế tại Nhà máy Nhiệt điện Quảng Ninh

## 1.3.1. Giới thiệu nhà máy và cơ sở lựa chọn trường hợp nghiên cứu

Nhà máy Nhiệt điện Quảng Ninh do Công ty Cổ phần Nhiệt điện Quảng Ninh quản lý, vận hành, gồm bốn tổ máy với tổng công suất 1.200 MW. Đây là thông tin giới thiệu do doanh nghiệp công bố trên website của công ty. [W2, “Giới thiệu Công ty Cổ Phần Nhiệt Điện Quảng Ninh”, đoạn về quản lý và vận hành.]

Trong dự án nâng cấp, cải tạo hệ thống xử lý khí thải, hồ sơ *Điều chỉnh Báo cáo Nghiên cứu khả thi* có yêu cầu bảo vệ hồ quang đối với biến tần. Phần hồ sơ sử dụng mang tên chủ đầu tư Công ty Cổ phần Nhiệt điện Quảng Ninh và đơn vị tư vấn Viện Năng lượng. Nội dung liên quan nằm trong Chương 4, trang in 169–171/339, tương ứng trang PDF 252–254 của bản gộp. [W1, Chương 4, tr. in 169–171/339; tr. PDF 252–254.]

Trường hợp này được lựa chọn vì hồ sơ nêu rõ mối liên hệ giữa phát hiện hồ quang, thông tin dòng điện và tín hiệu gửi tới máy cắt. Qua đó có thể phân tích yêu cầu bảo vệ theo một phạm vi thiết bị cụ thể, thay vì chỉ mô tả chung về nguy cơ hồ quang. Nội dung dưới đây được trình bày theo yêu cầu thiết kế; giới hạn về dữ liệu hiện trạng được tập hợp tại mục 1.3.5.

## 1.3.2. Phạm vi hệ thống và thiết bị được phân tích

Phạm vi khảo sát là hệ biến tần phục vụ động cơ quạt khói mới trong dự án. Hồ sơ xem xét lựa chọn giải pháp truyền động và quy định các yêu cầu liên quan đến nguồn cấp, biến áp cách ly, thiết bị đóng cắt và bảo vệ. Các bộ phận có liên quan đến bài toán gồm:

- **Nguồn cấp và biến áp cách ly:** Biến tần được yêu cầu lắp sau biến áp cách ly để giảm ảnh hưởng tới mạng điện cung cấp. Thông số nguồn được lựa chọn là ba pha 6,6 kV ±10%, tần số 50 Hz ±5%.
- **Khối biến đổi công suất:** Hồ sơ đề cập phương án HV IGBT/LV IGBT. Trong yêu cầu an toàn, Power Cell và máy biến áp được nêu là các bộ phận cần xét khi xảy ra phóng điện, ngắn mạch có hồ quang.
- **Máy cắt cấp nguồn:** Máy cắt đầu vào được yêu cầu tự động ngắt điện biến tần khi có sự cố. Hệ bảo vệ hồ quang phải có khả năng gửi tín hiệu điều khiển đến máy cắt cấp nguồn. [W1, Chương 4, tr. in 168–171/339; tr. PDF 251–254.]

Như vậy, bài toán tại đây thuộc phạm vi thiết bị trung thế 6,6 kV của hệ biến tần. Yêu cầu phát hiện phải gắn với những bộ phận được nêu trong hồ sơ và khả năng phối hợp cắt nguồn. Đối với đề tài, đây là trường hợp tham khảo phía trung thế; phạm vi hạ thế vẫn cần được xem xét theo các điều kiện ứng dụng tương ứng.

## 1.3.3. Yêu cầu phát hiện và phối hợp bảo vệ trong hồ sơ

Danh sách chức năng bảo vệ của biến tần có mục phát hiện hồ quang điện. Phần yêu cầu an toàn tiếp tục quy định thiết bị phải nhận biết, phản hồi nhanh, kết hợp đo dòng và gửi tín hiệu tới máy cắt. Bảng 1.2 tóm tắt từng nội dung và thông tin có thể sử dụng để phân tích. [W1, Chương 4, tr. in 170–171/339; tr. PDF 253–254.]

*Bảng 1.2. Yêu cầu bảo vệ hồ quang trong hồ sơ thiết kế.*

| Nội dung hồ sơ | Ý nghĩa chức năng | Trang/mục | Giới hạn thông tin |
|---|---|---|---|
| Có chức năng phát hiện hồ quang trong danh sách bảo vệ biến tần | Nhận biết sự cố có hồ quang là một yêu cầu của thiết bị | W1, Ch. 4, thông số biến tần, tr. in 170/339; PDF 253 | Chưa xác định thiết bị thực hiện |
| Phát hiện và phản hồi nhanh, kịp thời nhận biết sự cố | Có yêu cầu về thời gian trong chuỗi bảo vệ | W1, Ch. 4, “Tiêu chuẩn an toàn”, tr. in 171/339; PDF 254 | Không có giá trị thời gian định lượng trong đoạn này |
| Kết hợp công nghệ đo dòng để nâng cao tính tin cậy | Sử dụng thông tin dòng cùng chức năng phát hiện | Cùng vị trí, PDF 254 | Chưa nêu ngưỡng, vị trí đo hoặc phép logic |
| Gửi tín hiệu điều khiển tới máy cắt cấp nguồn | Liên kết khâu phát hiện với phần tử cắt nguồn | Cùng vị trí, PDF 254 | Chưa có giao diện và sơ đồ mạch chi tiết |
| Xét phóng điện, ngắn mạch tại Power Cell hoặc máy biến áp | Xác định bộ phận thuộc phạm vi sự cố cần quan tâm | Cùng vị trí, PDF 254 | Không quy định vị trí cảm biến |
| Đáp ứng yêu cầu an toàn của thiết bị 6,6 kV, gồm phản hồi, cách điện và hạn chế ảnh hưởng hồ quang | Xem bảo vệ cùng kết cấu và đặc tính thiết bị | Cùng vị trí, PDF 254 | Chưa có kết quả thử hoặc nghiệm thu trong phần hồ sơ sử dụng |

Yêu cầu của hồ sơ có thể tập hợp thành ba nhóm:

- **Phát hiện sự cố:** Thiết bị nhận biết được hiện tượng hồ quang trong phạm vi cần bảo vệ và tạo phản hồi kịp thời.
- **Phối hợp thông tin:** Đo dòng điện được sử dụng để nâng cao tính tin cậy của chức năng bảo vệ.
- **Phối hợp tác động:** Tín hiệu bảo vệ được đưa đến máy cắt cấp nguồn để thực hiện cắt mạch khi có sự cố. [W1, Chương 4, “Tiêu chuẩn an toàn”, tr. in 171/339; tr. PDF 254.]

Các nhóm trên cho thấy bộ phát hiện là một phần trong hệ bảo vệ. Chức năng nhận biết chỉ có ý nghĩa trong phối hợp hệ thống khi tín hiệu được đưa tới đúng phần tử tác động và đáp ứng giao diện yêu cầu.

## 1.3.4. Trình tự chức năng phát hiện và phối hợp tác động

Từ yêu cầu thiết kế, trình tự chức năng được diễn giải thành các bước dưới đây. Đây là quan hệ giữa các chức năng bảo vệ, không phải quy trình thao tác của nhân viên vận hành.

1. **Nhận biết sự cố có hồ quang.** Thiết bị phát hiện theo dõi dấu hiệu sự cố trong phạm vi hệ biến tần. Hồ sơ yêu cầu có chức năng này và nêu Power Cell hoặc máy biến áp trong các trường hợp phóng điện, ngắn mạch cần xét. [W1, Chương 4, tr. in 170–171/339; tr. PDF 253–254.]

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

Trường hợp này làm rõ yêu cầu phối hợp ở cấp hệ thống. Để tìm hiểu cách triển khai ở cấp thiết bị, phần tiếp theo khảo sát Mors Smitt 1S23 từ tài liệu sản phẩm và hướng dẫn của hãng. Đây là đối tượng tham khảo độc lập; chưa có bằng chứng xác nhận nhà máy sử dụng 1S23.

# 1.4. Khảo sát thiết bị phát hiện hồ quang điện Mors Smitt 1S23

## 1.4.1. Giới thiệu thiết bị và phạm vi ứng dụng

Mors Smitt 1S23 là mô-đun giao diện phát hiện hồ quang, sử dụng cảm biến quang 1S30 và đưa tín hiệu tới đầu vào trạng thái của rơ-le bảo vệ. Hãng mô tả ứng dụng của thiết bị trong tủ điện vỏ kim loại, cách điện bằng không khí. [W3, “Introduction”, tr. in/PDF 2.]

Trang sản phẩm KMET trong bộ nguồn giới thiệu thiết bị dưới tên *1S23 Arc Flash Module – 2 point sensors / 1 zone*. KMET là đơn vị giới thiệu, phân phối; các thông số được đối chiếu với tài liệu RMS Mors Smitt. Hình 1.6 trình bày ảnh sản phẩm từ bản lưu trang KMET. [TL5, tiêu đề và phần giới thiệu sản phẩm.]

{{HINH_6}}

Thiết bị được khảo sát qua hai tài liệu chính:

- **Technical Bulletin v01.0, ngày 24/03/2025:** Trình bày chức năng, đặc tính kỹ thuật, giao diện và sơ đồ đấu nối.
- **User Guide Iss C, ngày 06/06/2022:** Trình bày trạng thái chỉ thị, phối hợp với rơ-le, bố trí cảm biến và kiểm tra chức năng. [W3, chân trang PDF 1–11; W4, “About This Manual”, tr. in/PDF 2 và mục lục tr. 3–4.]

Đối với bài toán của đồ án, 1S23 là ví dụ về một thiết bị thực hiện chức năng phát hiện và xuất tín hiệu, còn quyết định kiểm tra dòng, tác động rơ-le và cắt nguồn được phối hợp với thiết bị bên ngoài. Cách phân chia này giúp xác định rõ phần chức năng cần đánh giá khi xây dựng nguyên mẫu. [W4, “Example Schematic” và “Over Current Relay Configuration”, tr. in/PDF 13–14.]

## 1.4.2. Cấu hình và giao diện chức năng

Các thành phần và giao diện chính của 1S23 gồm:

- **Đầu vào cảm biến:** Kết nối một hoặc hai cảm biến 1S30 theo biến thể đặt hàng. Hướng dẫn yêu cầu số cảm biến đấu nối phù hợp với loại mô-đun; dùng sai số lượng có thể tạo tình trạng lỗi cảm biến.
- **Nguồn phụ trợ:** Có các mức điện áp DC danh định theo biến thể. Nguồn này cấp cho mô-đun, tách với điện áp của hệ thống được giám sát.
- **Đầu ra ARC FAULT:** Đưa thông tin phát hiện sự cố tới đầu vào trạng thái rơ-le bảo vệ.
- **Đầu ra SUPERVISION:** Đưa thông tin giám sát tình trạng hệ thống và cảm biến tới thiết bị tiếp nhận. [W3, “Description”, tr. 2; “Technical Data”, tr. 5; W4, “1S23 Connection diagram”, tr. 12.]

Sản phẩm một hoặc hai cảm biến có đầu ra sự cố chung trong sơ đồ được khảo sát. Vì vậy, số đầu thu không đồng nghĩa số vùng tác động độc lập. Cấu hình giới thiệu trong TL5 được gọi là một vùng giám sát. [W4, sơ đồ đấu nối, tr. in/PDF 12; TL5, tiêu đề sản phẩm.]

Hình 1.7 cho thấy đầu nguồn, đầu cảm biến và hai dây đầu ra. Các đầu ra sử dụng khóa bán dẫn có phân cực, chuyển mạch phía âm nguồn. Khi kết nối, cần xét đúng cực tính và cấu trúc đầu vào thiết bị nhận. [W3, “Connection and Wiring Diagram”, tr. in 7/11; tr. PDF 7.]

{{HINH_7}}

Trên mặt mô-đun, trạng thái được thể hiện bằng đèn PWR và ARC:

- **PWR:** Liên quan đến nguồn và tình trạng làm việc, bao gồm giám sát cảm biến.
- **ARC:** Chỉ thị tín hiệu quang vượt điều kiện phát hiện.

Mô-đun còn có giám sát tính liên tục mạch cảm biến và watchdog cho hệ thống. Nhờ đó, thiết bị phân biệt được trạng thái làm việc bình thường với lỗi thu nhận, thay vì chỉ cung cấp thông tin có hoặc không có sự kiện. [W3, “System Supervision”, “Arc Sensor Supervision” và “Front Panel Layout and LED Indications”, tr. in/PDF 3.]

## 1.4.3. Nguyên lý phát hiện và phối hợp với rơ-le bảo vệ

Chuỗi xử lý của 1S23 bắt đầu từ tín hiệu quang. Khi cường độ sáng vượt ngưỡng tác động, khóa bán dẫn đầu ra sự cố dẫn, đưa phía âm nguồn tới đầu vào trạng thái của rơ-le. Tín hiệu SUPERVISION được đưa đến đầu vào riêng để thông báo tình trạng giám sát. [W3, “Trip Output Circuit Operation” và “System Supervision and Sensor Supervision Output Circuit Operation”, tr. in/PDF 3.]

Trong cấu hình có kiểm tra dòng, nhiệm vụ của các phần tử được phân chia như sau:

- **Cảm biến 1S30:** Thu nhận ánh sáng trong vùng được bố trí giám sát.
- **Mô-đun 1S23:** Theo dõi cảm biến, phát hiện điều kiện quang và xuất tín hiệu sự cố, giám sát.
- **Rơ-le bảo vệ ngoài:** Nhận các trạng thái từ 1S23, thực hiện phối hợp với phần tử quá dòng và đưa đầu ra tới mạch điều khiển cắt.
- **Máy cắt:** Thực hiện ngắt mạch theo tín hiệu bảo vệ. [W3, “Description” và “Application”, tr. 2; W4, “Example Schematic”, tr. 13.]

Sự phân chia này có ý nghĩa khi đánh giá thời gian. Độ trễ từ ánh sáng đến đầu ra 1S23 chỉ thuộc phần đầu chuỗi; để xác định thời gian cắt toàn hệ thống cần thêm đặc tính của rơ-le, mạch tác động và máy cắt.

Hướng dẫn hãng nêu hai yêu cầu quan trọng khi đấu nối:

- **Đúng loại đầu vào:** ARC FAULT và SUPERVISION sử dụng chuyển mạch âm, phải đưa tới đầu vào số cách ly phù hợp; các đầu vào liên quan không dùng chung cực âm với đầu vào khác theo sơ đồ mẫu.
- **Đúng chức năng đầu ra:** Đầu ra 1S23 được thiết kế cho đầu vào trạng thái rơ-le bảo vệ, không phù hợp để tác động trực tiếp rơ-le phụ hoặc cuộn cắt máy cắt. [W4, “Example Schematic” và “Over Current Relay Configuration”, tr. in/PDF 13–14.]

Như vậy, khi tham khảo 1S23, cần đọc định mức điện cùng sơ đồ ứng dụng và giới hạn đấu nối. Một trị số dòng lớn nhất trong bảng thông số không đủ để kết luận đầu ra có thể điều khiển trực tiếp mọi tải chấp hành.

## 1.4.4. Thông số kỹ thuật liên quan đến đề tài

Bảng 1.3 tập hợp những thông số của 1S23 liên quan đến yêu cầu điện áp, thời gian và giao diện. Các giá trị theo Bulletin v01.0 là thông số sản phẩm dùng để đối chiếu, chưa phải chỉ tiêu của nguyên mẫu.

*Bảng 1.3. Thông số kỹ thuật tham khảo của Mors Smitt 1S23.*

| Thông số | Giá trị | Điều kiện/biến thể/phiên bản | Ý nghĩa với bài toán | Nguồn, trang |
|---|---|---|---|---|
| Cảm biến tương thích | Một hoặc hai cảm biến 1S30 | Theo biến thể đặt hàng | Đối chiếu số đầu thu với cấu hình thiết bị | W3 v01.0, tr. 2–3; W4 Iss C, tr. 12 |
| Điện áp phụ trợ danh định | 24; 32; 48; 110; 125; 220; 240; 250 VDC | Các mức điện áp của từng biến thể | Xác định đúng nguồn cho thiết bị | W3 v01.0, tr. 5 |
| Dải làm việc của nguồn | ±20% điện áp danh định | Với mức danh định tương ứng | Không hiểu thành một dải liên tục 24–250 VDC | W3 v01.0, tr. 5 |
| Công suất tiêu thụ | Dưới 0,75 W khi giám sát; dưới 1,5 W trong 2 s ở mức lớn nhất | Tại nguồn 110 VDC | Tham khảo yêu cầu nguồn trong điều kiện công bố | W3 v01.0, tr. 5 |
| Thời gian tác động đầu ra | Dưới 2 ms | Từ chớp sáng đến đầu ra, Bulletin 24/03/2025 | Phân biệt với thời gian cắt toàn hệ | W3 v01.0, tr. 5 |
| Độ rộng xung sự cố | 110 ms ±10 ms | Xung cố định | Thời gian duy trì trạng thái đầu ra | W3 v01.0, tr. 3, 5 |
| Kiểu đầu ra | Khóa bán dẫn phân cực, chuyển mạch âm | Đầu ra giao diện trạng thái | Kiểm tra cực tính và cách ly đầu vào nhận | W3 v01.0, tr. 5; W4 Iss C, tr. 13–14 |
| Dòng lớn nhất đầu ra sự cố | 3,1 A; 1,6 A; 0,75 A | Theo nhóm nguồn 24/32/48 V; 110/125 V; 220/240/250 V | Đọc cùng giới hạn sử dụng đầu ra | W3 v01.0, tr. 5; W4 Iss C, tr. 14 |
| Đầu ra giám sát | 70 mA trong 60 ms; 30 mA liên tục | Mọi biến thể trong bảng hãng | Phân biệt khả năng ngắn hạn và liên tục | W3 v01.0, tr. 5 |
| Giám sát cảm biến | Dòng giám sát 2 mA; mất dòng thì bỏ trạng thái healthy sau 1 s | Giám sát tính liên tục | Tách thời gian báo lỗi khỏi thời gian phát hiện sự cố | W3 v01.0, tr. 3 |
| Cảm biến bị kích thích sáng kéo dài | Vô hiệu chức năng trip khi kích thích hơn 500 ms | Đồng thời bỏ trạng thái giám sát bình thường | Xét ảnh hưởng ánh sáng nền đến khả năng sẵn sàng | W3 v01.0, tr. 3 |

Khi đối chiếu tài liệu, có hai điểm cần làm rõ:

- **Thời gian tác động giữa các bản Bulletin:** Bản K ngày 13/06/2024 ghi dưới 1,5 ms, còn v01.0 ngày 24/03/2025 ghi dưới 2 ms và nêu mốc từ chớp sáng đến đầu ra. Bảng 1.3 dùng bản v01.0; nguyên nhân thay đổi thông số không được suy ra chỉ từ hai bảng dữ liệu. [W5, “Technical Data”, tr. 5; W3, “Technical Data”, tr. 5.]
- **Độ rộng xung giữa Bulletin và User Guide:** User Guide Iss C ghi 100 ms trong bảng chỉ thị và xấp xỉ 100 ms trong phần kiểm tra; Bulletin v01.0 ghi 110 ms ±10 ms. User Guide quy định ưu tiên thông tin của Technical Bulletin, nên giá trị có dung sai trong Bảng 1.3 được lấy theo Bulletin. [W4, “Documentation”, tr. 5; “Summary of Indications”, tr. 9; “Arc Trip Testing”, tr. 33; W3, tr. 3, 5.]

TL5 cũng ghi dưới 2 ms và xung 110 ms ±10 ms, phù hợp các mục tương ứng của Bulletin v01.0. Riêng nguồn phụ trợ cần đọc theo từng mức danh định, thay vì chỉ dựa vào cách viết rút gọn 24–250 VDC trên trang giới thiệu. Với thiết bị cụ thể, mã hàng và tài liệu đi kèm vẫn là thông tin cần đối chiếu trước khi áp dụng. [TL5, phần giới thiệu và bảng thông số; W3, tr. 5.]

## 1.4.5. Bố trí cảm biến và kiểm tra chức năng theo hướng dẫn hãng

Bố trí cảm biến phải bảo đảm thu nhận ánh sáng trong những khoang được bảo vệ. User Guide đưa ví dụ ở khoang máy cắt, thanh cái và đầu cáp, đồng thời yêu cầu bổ sung đầu thu nếu vùng giám sát vượt vùng bao phủ. Hình 1.8 minh họa hai vị trí trong hướng dẫn: khoang máy cắt và khoang thanh cái. [W4, “Sensor Placement” và “Example Sensor Placement”, tr. in/PDF 25–27.]

{{HINH_8}}

Với cảm biến 1S30A, hãng khuyến nghị khoảng cách bố trí xấp xỉ 5–6 m để tạo chồng lấn vùng nhận biết trong minh họa của hướng dẫn. Giá trị này cần được xem cùng hình học bố trí và điều kiện quan sát. Khi áp dụng vào tủ có vách ngăn, phải xét từng khoang và đường truyền ánh sáng thực tế. [W4, “Sensor Spacing”, tr. in/PDF 23; “Sensor Placement”, tr. in/PDF 25.]

Nội dung kiểm tra chức năng trong hướng dẫn được chia thành các nhóm:

- **Kiểm tra trước cấp nguồn:** Xem tình trạng mô-đun, thông tin định mức, số lượng cảm biến và đấu nối theo sơ đồ.
- **Kiểm tra trạng thái giám sát:** Xác nhận chỉ thị và đầu ra SUPERVISION, kiểm tra phản ứng khi mạch cảm biến bị gián đoạn hoặc có lỗi theo hướng dẫn.
- **Kiểm tra phát hiện:** Dùng nguồn chớp sáng thích hợp để kích thích cảm biến và theo dõi đầu ra sự cố. Với cấu hình có kiểm tra dòng, điều kiện dòng liên quan cần được tạo đồng thời.
- **Kiểm tra phối hợp đầu ra:** Xác nhận rơ-le nhận đúng tín hiệu và tạo đầu ra theo sơ đồ bảo vệ được kiểm tra. [W4, “Commissioning”, “Site Commissioning Verification Checklist”, “SUPERVISION Output Verification” và “Arc Trip Testing”, tr. in/PDF 30–33.]

Các nội dung trên là kiểm tra chức năng bằng kích thích thử, không phải yêu cầu tạo hồ quang trung thế. Hãng lưu ý một số đèn chớp nhỏ có thể không đủ công suất kích hoạt cảm biến. Vì vậy, điều kiện nguồn sáng phải được ghi nhận khi đánh giá; kết quả tác động hay không tác động chỉ có ý nghĩa khi biết điều kiện đã sử dụng. [W4, “ARC Trip Verification”, tr. in/PDF 30.]

Đối với đề tài, cách kiểm tra này gợi ra việc đánh giá cả sự kiện và trạng thái sẵn sàng. Một bộ phát hiện cần được theo dõi không chỉ khi có kích thích mà còn khi lỗi đầu thu hoặc đường tín hiệu có thể làm mất khả năng phát hiện.

## 1.4.6. Nội dung tham khảo cho hệ thống nhúng của đồ án

Qua khảo sát 1S23, những nội dung có thể tham khảo cho hệ thống nhúng gồm:

- **Xác định rõ giao diện:** Mô tả loại tín hiệu vào, nguồn phụ trợ, cực tính và đặc tính đầu ra. Nội dung này liên quan trực tiếp YC-01 và YC-03.
- **Đánh giá trọn chuỗi phát hiện:** Đặt mốc từ kích thích tham chiếu đến đầu ra, phân biệt thời gian phản hồi với độ rộng xung. Đây là căn cứ hoàn thiện cách đánh giá YC-05.
- **Xét vùng quan sát và tác động gây nhầm:** Bố trí đầu thu, ánh sáng nền và điều kiện kích thích phải đi cùng việc đánh giá độ nhạy của YC-04.
- **Theo dõi khả năng sẵn sàng:** Phân biệt tín hiệu sự cố với trạng thái lỗi cảm biến hoặc hệ thống. [W3, tr. 2–5; W4, tr. 12–14, 23–26, 30–33; đối chiếu các yêu cầu trong Bảng 1.1.]

Tài liệu sản phẩm không cung cấp đầy đủ thuật toán, tần số lấy mẫu và phần cứng xử lý để tái tạo thiết bị. Do đó, các yêu cầu về băng thông và chu kỳ thu nhận cần được xây dựng từ tín hiệu và phương pháp lựa chọn cho đồ án. Số cảm biến, mức nguồn và định mức đầu ra của 1S23 được dùng để tham khảo cách mô tả thiết bị, không tự trở thành cấu hình nguyên mẫu. [W3, “Technical Data”, tr. in/PDF 5; W4, “Documentation”, tr. in/PDF 5.]

Việc khảo sát đã làm rõ mối liên hệ giữa phát hiện, giao diện và phối hợp bảo vệ ở cấp mô-đun. Kết hợp với yêu cầu trong hồ sơ Quảng Ninh, các nội dung này là cơ sở để xác định phần công việc của đề tài trước khi thiết kế chi tiết.

# 1.5. Kết luận chương

Chương 1 đã trình bày đối tượng nghiên cứu, hiện tượng chớp hồ quang và các hậu quả liên quan đến thiết bị, con người. Các minh chứng thử nghiệm cho thấy ý nghĩa của việc phát hiện và phản hồi trong thời gian ngắn. Từ đó, chương xác định sáu nhóm yêu cầu về điện áp, tần số, dòng điện, độ nhạy, thời gian phản hồi và chu kỳ lấy mẫu.

Hồ sơ thiết kế tại Nhà máy Nhiệt điện Quảng Ninh đặt ra yêu cầu phát hiện hồ quang, kết hợp đo dòng và gửi tín hiệu tới máy cắt trong phạm vi hệ biến tần trung thế. Khảo sát độc lập 1S23 bổ sung cách tổ chức giao diện, giám sát cảm biến và phối hợp với rơ-le ngoài. Dữ liệu hiện có chưa xác nhận hiện trạng hệ bảo vệ tại nhà máy và chưa đủ để chốt toàn bộ thông số của nguyên mẫu.

Trên cơ sở đó, Chương 2 sẽ trình bày cơ sở lý thuyết về phát hiện, thu nhận và xử lý tín hiệu, đồng thời phân tích, lựa chọn linh kiện. Những thông số còn thiếu trong Bảng 1.1 cần được cụ thể hóa cùng phương án thiết kế và điều kiện đánh giá của hệ thống.
