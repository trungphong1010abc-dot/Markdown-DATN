> **Đề tài:** Thiết kế hệ thống nhúng phát hiện chớp hồ quang điện (arc-flash) trong hệ thống điện hạ thế và trung thế.
>
> **Ghi chú bản thảo:** Chương này hướng tới khoảng 10–14 trang A4 khi dàn bằng Times New Roman 13, giãn dòng khoảng 1,15; số trang thực tế phụ thuộc lề, bảng và kích thước hình. Markdown không quy định trực tiếp phông chữ hoặc số trang.

Chương này trình bày bối cảnh và nhu cầu phát hiện chớp hồ quang điện trong hệ thống điện hạ thế và trung thế. Trên cơ sở xác định đối tượng nghiên cứu, chương phân tích các yêu cầu kỹ thuật ban đầu, xem xét hồ sơ thiết kế của Nhà máy Nhiệt điện Quảng Ninh và khảo sát độc lập thiết bị thương mại Mors Smitt 1S23. Các nội dung này tạo căn cứ cho việc nghiên cứu cơ sở lý thuyết, thu nhận tín hiệu và lựa chọn linh kiện ở Chương 2.

# 1.1. Tổng quan bài toán phát hiện chớp hồ quang điện

## 1.1.1. Đối tượng nghiên cứu và bối cảnh ứng dụng

Trong hệ thống cung cấp điện công nghiệp, thiết bị đóng cắt thực hiện việc đóng nối, phân đoạn và cô lập phần tử theo yêu cầu bảo vệ. Đối với bài toán hồ quang nội bộ, phạm vi quan tâm tập trung vào phần dẫn điện, cách điện và các khoang của tủ điện. Tổng quan của Kumpulainen và cộng sự xác định những nhóm vị trí cần chú ý gồm khoang đấu nối, dao cách ly và dao tiếp địa, mối nối bắt bu-lông, tiếp điểm, biến điện đo lường và máy cắt. Đây là căn cứ khoanh vùng nghiên cứu, chưa phải danh sách vị trí lắp cảm biến cho một công trình cụ thể. [TL1, mục 3.2, tr. in 78; tr. PDF 2.]

Cần phân biệt đơn vị không gian ở các mức toàn trạm, dãy tủ và khoang tủ. Toàn trạm là bối cảnh cấp điện; dãy tủ thể hiện sự phân chia các ngăn lộ; khoang tủ là không gian mà đường truyền ánh sáng, khí nóng và áp suất sự cố chịu ảnh hưởng của kết cấu bao che. Từ nghiên cứu về tủ trung thế, đề tài nhận thấy một đầu thu quan sát được một khoang không đồng nghĩa toàn bộ dãy tủ đã được bao phủ. Phạm vi phát hiện phải được mô tả theo vùng có thể thu nhận tín hiệu, thay vì chỉ ghi chung là giám sát trạm điện. [TL3, mục 2 và Hình 5, tr. PDF 7; phần liên hệ là phân tích của đề tài.]

Hình 1.1 minh họa kết cấu tủ KMZ_31 trong một nghiên cứu về hồ quang nội bộ. Vách tủ và đường thoát khí cho thấy kết cấu cơ khí là một điều kiện của hiện tượng, đồng thời là dữ liệu cần xét khi đánh giá vùng quan sát. Hình không mô tả tủ điện tại Nhà máy Nhiệt điện Quảng Ninh.

![Kết cấu tủ KMZ_31 với vách tủ và đường thoát khí](hinh_minh_hoa/Hinh_1_1_Cau_truc_tu_trung_the_KMZ_31.jpg)

*Hình 1.1. Kết cấu tủ trung thế KMZ_31 trong nghiên cứu nguồn; Exhaust Duct là đường thoát khí, Wall là vách tủ.*

*Nguồn: TL3, Hình 5, tr. in 7, tr. PDF 7. Trích ảnh từ tài liệu, giữ nguyên nhãn; bài báo phát hành theo CC BY 4.0.*

Đối tượng trực tiếp của đề tài là dấu hiệu phục vụ phát hiện chớp hồ quang và chuỗi chức năng của hệ thống nhúng thực hiện nhiệm vụ đó. Đối tượng chịu tác động của sự cố gồm thiết bị điện và con người trong vùng ảnh hưởng; mức ảnh hưởng phụ thuộc cấu trúc thiết bị và điều kiện sự cố. Phát hiện cần được đặt trong quan hệ với bảo vệ điện, nhưng không đồng nhất với toàn bộ quá trình cắt nguồn và dập tắt hồ quang. Tổng quan kỹ thuật phân biệt phát hiện, xử lý bằng rơ-le và các phần tử loại trừ hồ quang như máy cắt hoặc thiết bị chuyên dụng. [TL1, mục 2, Hình 1, tr. in 78–79; tr. PDF 2–3.]

Theo phạm vi này, một bộ phát hiện cần được mô tả bằng tín hiệu vào, điều kiện quyết định và trạng thái đầu ra. Khi chưa có khảo sát lắp đặt, đề tài chưa xác định số vùng, số kênh hoặc vị trí đầu thu. Cách giới hạn đó giữ cho yêu cầu nghiên cứu gắn với dữ liệu có thể kiểm tra và tránh suy rộng từ một tủ mẫu sang mọi hệ thống hạ thế, trung thế. Các yêu cầu lựa chọn linh kiện chỉ có thể cụ thể hóa sau khi xác định những ranh giới này.

## 1.1.2. Hiện tượng hồ quang điện và chớp hồ quang điện

Hồ quang điện (*electric arc*) là hiện tượng phóng điện phát sáng có dòng điện đi qua môi trường plasma nóng. Trong phạm vi sự cố thiết bị, *arc fault* chỉ sự cố có hồ quang phát sinh ngoài chức năng làm việc dự kiến. Thuật ngữ *arc flash* gắn với thành phần bức xạ nhiệt của hồ quang năng lượng lớn. Trong đề tài, “phát hiện chớp hồ quang điện” được dùng cho nhiệm vụ nhận biết dấu hiệu sự kiện hồ quang nguy hiểm, không hàm ý hệ thống đo đầy đủ năng lượng tác động lên con người. [TL2, mục 1, tr. in 7; tr. PDF 1.]

Không phải mọi hồ quang đều là sự cố ngoài kiểm soát. Khi máy cắt ngắt dòng, hồ quang có thể xuất hiện trong bộ phận được thiết kế để chịu và dập hồ quang. Trái lại, hồ quang nội bộ ngoài vùng chức năng dự kiến làm phát sinh nguy cơ đối với các bộ phận bao quanh. Babrauskas lưu ý thiết bị đóng cắt được thiết kế chịu những tác động áp suất do hồ quang trong thao tác bình thường. Vì vậy, không thể lấy riêng việc có ánh sáng làm kết luận rằng mọi hoạt động đóng cắt đều là sự cố. [TL2, mục 1, tr. in 7; tr. PDF 1.]

Những nguyên nhân và điều kiện liên quan được tài liệu xem xét gồm suy giảm cách điện, sự cố tại đấu nối và tiếp điểm, cùng các yếu tố thiết kế, lắp đặt và bảo trì. Đầu cáp là một vị trí điển hình được tổng quan kỹ thuật đề cập khi theo dõi sự cố đang phát triển. Tuy nhiên, dấu hiệu trước sự cố và dấu hiệu khi hồ quang đã xuất hiện phục vụ hai nhiệm vụ khác nhau: theo dõi tình trạng hỗ trợ phòng ngừa, còn phát hiện chớp hồ quang là phản ứng với hiện tượng đã xảy ra. [TL1, mục 3.2–3.5 và 4.3–4.4, tr. in 78–80; tr. PDF 2–4.]

Hồ quang nội bộ có thể đồng thời tạo bức xạ nhiệt, phát sáng, gia tăng áp suất và phát tán vật chất nóng. Tổng quan về nổ hồ quang phân biệt sóng áp suất lan truyền từ kênh hồ quang với sự tăng áp của khí trong không gian bao kín. Do đó, *arc blast* không nên được dùng thay hoàn toàn cho *arc flash*: hai thuật ngữ nhấn mạnh những thành phần tác động khác nhau của sự kiện. [TL2, tóm tắt và mục 1, tr. in 7; tr. PDF 1.]

Hình 1.2 cho thấy tủ KMZ_31 trước, trong và sau thử nghiệm tại phòng thí nghiệm công suất lớn ICMET, Romania. Hình giúp liên hệ hiện tượng phát sáng với hư hỏng kết cấu sau thử; nó không cung cấp tỷ lệ tai nạn hoặc mức chịu đựng chung của mọi tủ điện. Nghiên cứu nguồn sử dụng trường hợp này để đặt vấn đề về áp suất bên trong tủ. [TL3, mục 1 và Hình 1, tr. PDF 1–2.]

![Tủ KMZ_31 trước, trong và sau thử nghiệm hồ quang nội bộ tại ICMET](hinh_minh_hoa/Hinh_1_2_Thu_nghiem_ho_quang_noi_bo_tu_KMZ_31.jpg)

*Hình 1.2. Thử nghiệm hồ quang nội bộ tủ KMZ_31 tại ICMET, Romania, gồm trạng thái trước thử và trạng thái hư hỏng sau thử.*

*Nguồn: TL3, Hình 1, tr. in 2, tr. PDF 2. Trích nguyên cụm ảnh và nhãn trong nguồn, CC BY 4.0; không phải ảnh tại nhà máy ở mục 1.3.*

Về phạm vi nghiên cứu, hồ quang nối tiếp trên mạch tải dân dụng, hồ quang DC trong hệ quang điện và hồ quang nội bộ tủ phân phối cần được phân biệt. Lezama và cộng sự nghiên cứu hồ quang nối tiếp trên hệ dân dụng 230 V AC–50 Hz, nhận dạng bằng tương quan dòng giữa các chu kỳ. Lin và cộng sự nghiên cứu định vị hồ quang DC trong hệ PV từ bức xạ điện từ thu bằng anten. Hai công trình cho thấy sự đa dạng của tín hiệu và phương pháp, nhưng không trực tiếp xác lập chỉ tiêu phát hiện quang cho tủ trung thế. [TL4, tóm tắt, tr. in 227; tr. PDF 1; TL6, tóm tắt và mục 1, tr. PDF 1.]

Từ sự khác biệt đó, đề tài chỉ sử dụng các nghiên cứu ngoài phạm vi chính để làm rõ ranh giới áp dụng. Kết quả nhận dạng dòng điện với một tập tải xác định không được chuyển thành xác suất phát hiện chớp hồ quang trong khoang tủ. Độ chính xác định vị trong hệ PV cũng không phải độ nhạy của đầu thu quang. Cơ chế và phương pháp xử lý chi tiết được dành cho Chương 2 sau khi xác định loại tín hiệu cần khai thác.

## 1.1.3. Số liệu minh chứng và tính cấp thiết

Tính cấp thiết của đề tài được xem xét từ hậu quả có điều kiện kiểm chứng. Bộ tài liệu sử dụng chưa cung cấp một thống kê có mẫu số, thời gian quan sát và phạm vi thiết bị đủ rõ để tính tần suất sự cố tại Việt Nam hoặc riêng Nhà máy Nhiệt điện Quảng Ninh. Vì vậy, chương không ước lượng xác suất sự cố theo năm và không dùng số lượng ảnh hư hỏng làm bằng chứng cho mức độ thường xuyên.

Minh chứng trực tiếp là thử nghiệm thanh cái hạ thế trong Hình 1.3. Nguồn ghi điện áp U = 726 V, dòng ngắn mạch ký hiệu Ik = 77 kA và thời gian hồ quang 65 ms; sau thử đã xuất hiện nóng chảy cục bộ tại ranh giới lớp cách điện. Các giá trị này thuộc điều kiện thử của tài liệu, không phải dòng định mức thanh cái, thông số nhà máy hoặc kết quả thực nghiệm của đồ án. [TL1, Hình 2, tr. in 80; tr. PDF 4.]

![Thanh cái hạ thế nóng chảy cục bộ sau thử hồ quang](hinh_minh_hoa/Hinh_1_3_Thanh_cai_ha_the_nong_chay_do_ho_quang.jpg)

*Hình 1.3. Thanh cái hạ thế nóng chảy cục bộ sau thử hồ quang tại ranh giới lớp cách điện.*

*Nguồn: TL1, Hình 2, tr. in 80, tr. PDF 4. Trích ảnh gốc; điều kiện nguồn: U = 726 V, Ik = 77 kA, thời gian hồ quang 65 ms.*

Minh chứng khác là quan hệ năng lượng tác động với thời gian hồ quang ở Hình 1.4. Đồ thị sử dụng điều kiện U = 15 kV, Ik = 50 kA, khe hở 152 mm và khoảng cách làm việc 910 mm. Trong trường hợp tính toán này, năng lượng trên đơn vị diện tích tăng theo thời gian hồ quang. Không thể sử dụng đường này để xác định năng lượng tại một tủ khác nếu chưa xét lại điện áp, dòng, khoảng cách và cấu hình tương ứng. [TL1, mục 5.2–5.5 và Hình 5, tr. in 81–83; tr. PDF 5–7.]

![Năng lượng tác động theo thời gian hồ quang trong điều kiện của nguồn](hinh_minh_hoa/Hinh_1_4_Nang_luong_tac_dong_theo_thoi_gian_ho_quang.png)

*Hình 1.4. Năng lượng tác động theo thời gian hồ quang trong một trường hợp tính toán; trục tung là J/cm², trục hoành là ms.*

*Nguồn: TL1, Hình 5, tr. in 82, tr. PDF 6. Trích nguyên hình; điều kiện: U = 15 kV, Ik = 50 kA, khe hở 152 mm, khoảng cách làm việc 910 mm. Không phải đường đặc tính của nguyên mẫu.*

Hai minh chứng hỗ trợ nhu cầu rút ngắn khoảng thời gian từ xuất hiện sự cố đến tác động bảo vệ phù hợp. Tuy nhiên, rút ngắn thời gian phát hiện chỉ đóng góp một phần vào tổng thời gian loại trừ sự cố. Máy cắt và các phần tử phía sau có thời gian làm việc riêng; nguồn tổng quan dành các phần riêng để phân tích rơ-le, máy cắt và thiết bị loại trừ hồ quang. [TL1, mục 5.6 và 6, tr. in 83–85; tr. PDF 7–9.]

Từ các đặc điểm trên, đề tài nhận thấy cần nghiên cứu hệ thống phát hiện có phạm vi tín hiệu rõ ràng, đo được thời gian phản hồi và đánh giá được khả năng phân biệt sự kiện với tác động gây nhầm. Ý nghĩa của hệ thống nhúng nằm ở việc hiện thực hóa chuỗi thu nhận, quyết định và thông báo trạng thái trong điều kiện có thể đo kiểm. Chưa có cơ sở kết luận nguyên mẫu thay thế thiết bị bảo vệ công nghiệp hoặc bảo đảm an toàn cho công trình khi chưa được đánh giá tương ứng.

Từ bối cảnh và hậu quả đã trình bày, cần xác định các đại lượng và đặc tính kỹ thuật làm căn cứ xây dựng hệ thống. Phần tiếp theo phân tích sáu nhóm yêu cầu chính, đồng thời phân biệt yêu cầu đã có căn cứ với dữ liệu còn cần bổ sung.

# 1.2. Phân tích yêu cầu kỹ thuật của bài toán

## 1.2.1. Yêu cầu về điện áp

Điện áp trong bài toán gồm ba nhóm: điện áp hệ thống được giám sát, điện áp tín hiệu tại giao diện thu nhận và nguồn phụ trợ của bộ phát hiện. Điện áp hệ thống xác định bối cảnh thiết bị; điện áp tín hiệu liên quan đến khả năng tiếp nhận và bảo vệ đầu vào; nguồn phụ trợ liên quan đến trạng thái làm việc của bộ phát hiện. Không được thay thế các đại lượng này cho nhau. Hồ sơ Quảng Ninh quy định nguồn biến tần ba pha 6,6 kV ±10%, trong khi 1S23 có các biến thể nguồn phụ trợ DC riêng. [W1, Chương 4, tr. in 169/339; tr. PDF 252; W3, “Auxiliary Supply”, tr. in 5/11; tr. PDF 5.]

Trong cách tiếp cận quang của thiết bị thương mại, cảm biến đưa tín hiệu tới mô-đun, đầu ra mô-đun đưa đến đầu vào trạng thái của rơ-le. Sơ đồ này không cho phép suy ra vi điều khiển tiếp xúc trực tiếp với điện áp trung thế. Đối với nguyên mẫu, cần xác định riêng đường truyền tín hiệu, ranh giới cách ly và mức điện áp từng giao diện. [W3, “Description” và “Connection and Wiring Diagram”, tr. PDF 2, 7; phần liên hệ là phân tích của đề tài.]

Tiêu chí đánh giá ban đầu là lập được bảng giao diện với điện áp danh định, dải cho phép và điều kiện lỗi cho mỗi cổng thực sự sử dụng. Dải nguồn phụ trợ, mức tín hiệu đo và yêu cầu cách điện của đồ án chưa được chốt từ dữ liệu hiện có. Chúng cần được xác định sau khi lựa chọn cơ chế thu nhận và phạm vi lắp đặt. Điện áp 6,6 kV của trường hợp Quảng Ninh chỉ xác lập một bối cảnh trung thế, không xác lập toàn bộ dải điện áp của nguyên mẫu.

## 1.2.2. Yêu cầu về tần số

Tần số nguồn điện lực, tần số làm việc của tải qua biến tần, dải tần thông tin đo và tần số lấy mẫu là những đại lượng khác nhau. Hồ sơ Quảng Ninh ghi tần số nguồn biến tần 50 Hz ±5% và dải tần số đầu ra 0–50 Hz. Đây là yêu cầu thiết kế của biến tần, không phải kết quả đo vận hành tại nhà máy. [W1, Chương 4, “Thông số kỹ thuật biến tần được lựa chọn”, tr. in 169/339; tr. PDF 252.]

Đối với kênh dòng, nhu cầu băng thông phụ thuộc việc chỉ xác nhận điều kiện dòng hay phân tích dạng sóng. Đối với kênh quang, tốc độ biến đổi tín hiệu và đáp ứng chuỗi thu nhận là căn cứ đánh giá khả năng bám sự kiện. Không thể lấy riêng tần số điện lưới làm dải tần đầy đủ của dấu hiệu hồ quang. Nghiên cứu của Lezama lấy mẫu 5 kHz trên mạch nguồn 50 Hz, minh họa sự khác nhau giữa hai đại lượng; số liệu đó không tạo thành tần số lấy mẫu mặc định cho đồ án. [TL4, tóm tắt, tr. in 227; tr. PDF 1.]

Cách đánh giá phù hợp là xác định dải thông tin cần giữ cho từng kênh, sau đó kiểm tra đáp ứng toàn chuỗi thu nhận trong dải đó. Khi chưa lựa chọn tín hiệu và phương pháp xử lý, chương ghi nhận yêu cầu xác định băng thông, không tự đặt một dải tần đo hoặc chuyển cấu hình của công trình khác thành yêu cầu nguyên mẫu.

## 1.2.3. Yêu cầu về dòng điện

Dòng điện có thể là tín hiệu phát hiện hoặc tín hiệu xác nhận cho dấu hiệu khác. Với bảo vệ chớp hồ quang dựa trên ánh sáng và quá dòng, tổng quan kỹ thuật mô tả việc phối hợp hai điều kiện để tăng tính chắc chắn của quyết định. Hình 1.5 biểu diễn một nguyên lý như vậy. Đây là ví dụ trong nghiên cứu; hồ sơ Quảng Ninh chỉ yêu cầu kết hợp công nghệ đo dòng, chưa xác định phép logic cụ thể. [TL1, mục 5.6 và Hình 6, tr. in 83; tr. PDF 7; W1, Chương 4, tr. in 171/339; tr. PDF 254.]

![Nguyên lý phối hợp ánh sáng và quá dòng trong nghiên cứu nguồn](hinh_minh_hoa/Hinh_1_5_Nguyen_ly_phoi_hop_anh_sang_va_qua_dong.png)

*Hình 1.5. Ví dụ phối hợp ánh sáng và quá dòng bằng phép AND; Trip signal là tín hiệu tác động của hệ thống bảo vệ trong nguồn.*

*Nguồn: TL1, Hình 6, tr. in 83, tr. PDF 7. Trích nguyên hình; không phải sơ đồ đã xác nhận của Quảng Ninh hoặc kiến trúc đã lựa chọn của đồ án.*

Cần phân biệt dòng định mức tải, dòng sự cố tại phần tử sơ cấp và tín hiệu thứ cấp của bộ biến đổi đo lường. Dòng Ik trong hình thử nghiệm ở mục 1.1 không phải ngưỡng kích hoạt bộ phát hiện. Tài liệu còn lưu ý dòng hồ quang có thể thấp hơn dòng sự cố kim loại, ảnh hưởng thời gian làm việc của bảo vệ quá dòng. Vì vậy, chọn ngưỡng chỉ từ một dòng ngắn mạch lớn có thể bỏ qua điều kiện cần nghiên cứu. [TL1, mục 5.3, tr. in 81–82; tr. PDF 5–6.]

Nếu sử dụng dòng xác nhận, đề tài cần xác định vị trí lấy thông tin, dạng tín hiệu nhận được là dạng sóng hay trạng thái nhị phân, và khoảng thời gian mà điều kiện dòng có giá trị với sự kiện quang. Cách đánh giá phải kiểm tra được quang riêng, dòng riêng và tổ hợp được định nghĩa hợp lệ. Chưa có căn cứ chọn tỷ số biến dòng, ngưỡng quá dòng hoặc định mức đầu ra; các nội dung đó thuộc bước cụ thể hóa giao diện và phối hợp bảo vệ.

## 1.2.4. Yêu cầu về độ nhạy

Độ nhạy cần gắn với tín hiệu và điều kiện đánh giá. Ngưỡng tác động của mạch thu quang, khả năng chuyển đổi bức xạ của cảm biến và tỷ lệ sự kiện nhận đúng trên một tập thử là các đại lượng khác nhau. Không thể dùng tỷ lệ nhận dạng thay cho ngưỡng quang, cũng không thể dùng số cảm biến để suy ra độ bao phủ. Hướng dẫn 1S23 dành các phần riêng cho khoảng cách cảm biến và vị trí bố trí trong khoang tủ. [W4, “Sensor Installation”, tr. in/PDF 23–26.]

Từ đó, độ nhạy phải được đánh giá cùng đặc tính nguồn sáng, vị trí tương đối, khoảng cách, hướng thu, vật cản và ánh sáng nền. Một lần không nhận được sự kiện có thể liên quan đến bố trí quan sát, không chỉ đến ngưỡng điện. Giảm ngưỡng mà không xét ánh sáng nền cũng có thể làm tăng tác động ngoài mong muốn. Đây là phân tích yêu cầu của đề tài trên cơ sở hướng dẫn bao phủ vùng và xử lý trạng thái bị kích thích sáng kéo dài của hãng. [W4, “Sensor Placement”, tr. in/PDF 25; W3, “Arc Sensor Continuously Picked Up”, tr. in/PDF 3.]

Tiêu chí cần đạt ở giai đoạn này là mô tả được điều kiện để gọi một sự kiện là cần phát hiện, tập tác động gây nhầm và phương pháp ghi nhận bỏ sót, báo nhầm. Bộ nguồn chưa xác lập ngưỡng quang của nguyên mẫu hoặc xác suất phát hiện trong môi trường ứng dụng. Vì vậy, chương không tự đưa một tỷ lệ mục tiêu khi chưa có tập thử, cỡ mẫu và điều kiện đo cụ thể.

## 1.2.5. Yêu cầu về thời gian phản hồi

Thời gian phản hồi phải có hai mốc đo. Với bộ phát hiện, có thể quy định mốc đầu là thời điểm kích thích xuất hiện tại vị trí tham chiếu và mốc cuối là thời điểm đầu ra điện đạt điều kiện xác định. Nếu chỉ đo sau cảm biến hoặc chỉ đo thời gian thực thi chương trình, kết quả đã loại bỏ một phần chuỗi thu nhận và không cùng đại lượng với thời gian từ chớp sáng đến đầu ra. Bulletin 1S23 v01.0 định nghĩa “from flash to output operation” cho thông số dưới 2 ms. [W3, “Technical Data”, tr. in 5/11; tr. PDF 5.]

Ở cấp toàn hệ thống, thời gian còn liên quan đến giao diện đầu vào rơ-le, quyết định bảo vệ, đầu ra tác động và quá trình máy cắt loại trừ sự cố. Mô-đun nhanh không đủ chứng minh thời gian cắt cũng bằng thời gian mô-đun. Tổng quan kỹ thuật chỉ rõ khi phát hiện làm việc rất nhanh, phần đáng kể của thời gian hồ quang có thể nằm ở thiết bị sơ cấp chịu trách nhiệm loại trừ hồ quang. [TL1, mục 5.6 và 6.2, tr. in 83–84; tr. PDF 7–8.]

Độ rộng xung cần tách khỏi độ trễ xuất hiện xung. Bulletin 2025 nêu thời gian tác động đầu ra 1S23 dưới 2 ms và độ rộng xung 110 ms ±10 ms. Hai thông số mô tả hai đoạn thời gian khác nhau; xung duy trì lâu hơn không đồng nghĩa bộ phát hiện phản ứng chậm hơn. [W3, “Trip Output Circuit Operation” và “Technical Data”, tr. in/PDF 3, 5.]

Đối với đồ án, phương pháp đánh giá cần ghi được kích thích tham chiếu và đầu ra trên cùng cơ sở thời gian, nêu cách xác định cạnh tín hiệu và điều kiện thử. Chưa có ngân sách thời gian phân bổ cho các khối và chưa có giới hạn định lượng riêng của nguyên mẫu; thông số hãng chỉ là điểm đối chiếu. Thử bằng nguồn sáng thay thế phải được gọi đúng là đánh giá đáp ứng quang trong điều kiện thử, chưa phải thời gian loại trừ hồ quang thực tại nhà máy.

## 1.2.6. Yêu cầu về chu kỳ lấy mẫu

Chu kỳ lấy mẫu phải được xác định cho đúng kênh thu nhận. Nếu đo dạng sóng tương tự bằng ADC, chu kỳ quyết định khoảng cách thời gian giữa các giá trị đo. Nếu tiếp nhận trạng thái số hoặc sử dụng khối so sánh liên tục, cần xem xét độ trễ truyền, khả năng bắt sự kiện và cách xử lý đầu vào tương ứng. Khi kiến trúc chưa được lựa chọn, không có căn cứ mặc định mọi kênh đều dùng ADC.

Với lấy mẫu đều, tần số và chu kỳ liên hệ bởi \(f_s = 1/T_s\). Việc lựa chọn còn phụ thuộc băng thông sau điều hòa tín hiệu, lượng thông tin cần giữ và khoảng thời gian cho phép trước quyết định phát hiện. Chỉ lấy gấp đôi tần số nguồn không đủ xác lập khả năng quan sát một biến đổi nhanh. Sự khác nhau giữa nguồn 50 Hz và lấy mẫu 5 kHz trong nghiên cứu Lezama là ví dụ có phạm vi rõ, không quy định tần số thu nhận một kênh quang. [TL4, tóm tắt và mục 2, tr. in 227–229; tr. PDF 1–3.]

Cách đánh giá ở mức yêu cầu là đối chiếu khoảng lấy mẫu hoặc thời gian bắt sự kiện với tín hiệu tham chiếu, kiểm tra ảnh hưởng xử lý tới khả năng tiếp nhận sự kiện tiếp theo. Cần biết kênh nào lấy mẫu, dải thông nào được giữ và mốc phát hiện nào được sử dụng trước khi chốt giá trị. Bộ tài liệu 1S23 được khảo sát không công bố tần số lấy mẫu nội bộ; không thể suy ngược thông số đó từ thời gian đầu ra. [W3, “Technical Data”, tr. PDF 5; W4, “Documentation”, tr. PDF 5; giới hạn của tài liệu khảo sát.]

## 1.2.7. Tổng hợp yêu cầu kỹ thuật ban đầu

Bảng 1.1 tổng hợp sáu nhóm yêu cầu. Trạng thái có căn cứ tham chiếu chỉ thể hiện đã có tài liệu hỗ trợ phân tích, chưa có nghĩa giá trị đó được phê duyệt cho nguyên mẫu. Mục 1.3 sẽ đối chiếu yêu cầu trong một hồ sơ ứng dụng; mục 1.4 cung cấp đối chiếu ở cấp thiết bị thương mại.

*Bảng 1.1. Yêu cầu kỹ thuật ban đầu và dữ liệu cần hoàn thiện.*

| Mã yêu cầu | Nội dung | Giá trị/tiêu chí hoặc dữ liệu cần bổ sung | Căn cứ | Cách đánh giá | Trạng thái |
|---|---|---|---|---|---|
| YC-01 | Điện áp | Tách điện áp hệ thống, tín hiệu và nguồn phụ trợ; chưa chốt dải nguyên mẫu | Mục 1.2.1; W1, Ch. 4, tr. in 169, PDF 252; W3, tr. 5 | Rà soát bảng giao diện, đo mức tại các cổng đã chọn | Có căn cứ phân loại; thiếu dải áp dụng |
| YC-02 | Tần số | Nguồn biến tần trong hồ sơ: 50 Hz ±5%; dải thông kênh đo cần xác định riêng | Mục 1.2.2; W1, Ch. 4, tr. in 169, PDF 252 | Đối chiếu tần số nguồn và dải đáp ứng kênh thu nhận | Có giá trị tham chiếu; chưa chốt băng thông |
| YC-03 | Dòng điện | Xác định vị trí, dạng giao diện và vai trò xác nhận; chưa có ngưỡng hoặc tỷ số biến dòng | Mục 1.2.3; TL1, mục 5.3, 5.6; W1, Ch. 4, tr. in 171, PDF 254 | Kiểm tra từng điều kiện và tổ hợp theo logic được xác lập | Có căn cứ chức năng; thiếu định lượng |
| YC-04 | Độ nhạy | Xác định kích thích, ánh sáng nền, vùng quan sát và tập tác động gây nhầm | Mục 1.2.4; W4, tr. 23–26; W3, tr. 3 | Ghi bỏ sót, báo nhầm cùng điều kiện, cỡ mẫu và bố trí thử | Chưa có ngưỡng và tập thử của đồ án |
| YC-05 | Thời gian phản hồi | Định nghĩa mốc kích thích–đầu ra; tách độ trễ, độ rộng xung và thời gian cắt | Mục 1.2.5; TL1, mục 5.6, 6.2; W3, tr. 5 | Đo đồng thời tham chiếu và đầu ra, ghi điều kiện đo | Có định nghĩa; chưa có giới hạn nguyên mẫu |
| YC-06 | Chu kỳ lấy mẫu | Xác định kênh, băng thông và cơ chế bắt sự kiện trước khi chọn chu kỳ | Mục 1.2.6; TL4, mục 2; W3, tr. 5 | Đo chu kỳ hoặc độ trễ bắt sự kiện theo cơ chế thực tế | Phụ thuộc phương án thu nhận |

Các yêu cầu tạo đầu vào cho thiết kế nhưng chưa thành một bản đặc tính định lượng hoàn chỉnh. Việc chưa xác định bộ tiêu chuẩn áp dụng cho nguyên mẫu không có nghĩa lĩnh vực này không có tiêu chuẩn: tổng quan đề cập tiêu chuẩn thiết bị đóng cắt, còn Bulletin 1S23 công bố các hạng mục thử cùng tiêu chuẩn tương ứng. Cần xác định đúng đối tượng và phiên bản trước khi đặt yêu cầu tuân thủ cho đồ án. [TL1, mục 3.2, tr. in 78; tr. PDF 2; W3, “Compliance”, tr. in/PDF 6.]

Các yêu cầu ban đầu cần được xem trong bối cảnh cụ thể. Phần tiếp theo chọn Nhà máy Nhiệt điện Quảng Ninh làm trường hợp nghiên cứu, giới hạn ở hồ sơ công khai của dự án nâng cấp, cải tạo hệ thống xử lý khí thải.

# 1.3. Phân tích quy trình phát hiện và phối hợp bảo vệ hồ quang theo hồ sơ thiết kế tại Nhà máy Nhiệt điện Quảng Ninh

## 1.3.1. Giới thiệu nhà máy và cơ sở lựa chọn trường hợp nghiên cứu

Theo trang giới thiệu doanh nghiệp, Công ty Cổ phần Nhiệt điện Quảng Ninh quản lý, vận hành nhà máy gồm bốn tổ máy, tổng công suất 1.200 MW. Nguồn này xác nhận bối cảnh doanh nghiệp và quy mô nhà máy, không xác nhận hệ thống phát hiện hồ quang cụ thể đang vận hành. Thông tin được sử dụng ở đúng phạm vi đó. [W2, “Giới thiệu Công ty Cổ Phần Nhiệt Điện Quảng Ninh”, đoạn về quản lý và vận hành.]

Cơ sở lựa chọn trường hợp là tài liệu *Điều chỉnh Báo cáo Nghiên cứu khả thi* của dự án nâng cấp, cải tạo hệ thống xử lý khí thải nhà máy. Phần kỹ thuật mang tên Công ty Cổ phần Nhiệt điện Quảng Ninh và đơn vị tư vấn Viện Năng lượng. Trong Chương 4, hồ sơ quy định chức năng phát hiện hồ quang cho biến tần, kết hợp đo dòng và khả năng gửi tín hiệu tới máy cắt cấp nguồn. Đây là yêu cầu ứng dụng cụ thể để phân tích quan hệ giữa phát hiện và bảo vệ. [W1, Chương 4, tr. in 170–171/339; tr. PDF 253–254.]

Bản đọc là tệp gộp lưu công khai tại CafeF; nơi lưu bản sao không phải cơ quan thiết kế. Nội dung có tiêu đề dự án, tên chủ đầu tư, đơn vị tư vấn và hệ đánh số trang riêng của chương; trang đầu tệp có thông tin hiển thị ký số ngày 11/06/2026. Chương sử dụng bản này để phân tích hồ sơ, chưa coi thông tin hiển thị chữ ký là kết quả xác thực mật mã hoặc biên bản nghiệm thu. Chưa đối chiếu được cùng tệp với bản tải từ doanh nghiệp hoặc HNX là một giới hạn xuất xứ cần ghi nhận. [W1, tr. PDF 1 và phần đầu/cuối trang PDF 253–254.]

## 1.3.2. Phạm vi hệ thống và thiết bị được phân tích

Phạm vi được thu hẹp vào hệ biến tần phục vụ động cơ quạt khói mới trong dự án. Hồ sơ xem xét lựa chọn giải pháp truyền động, yêu cầu biến tần lắp sau biến áp cách ly và đề cập máy cắt đầu vào tự động ngắt điện khi có sự cố. Nội dung này cho phép nhận diện quan hệ giữa nguồn cấp, thiết bị biến đổi công suất và phần tử cắt, chưa cung cấp đủ sơ đồ hoàn công của toàn hệ thống điện nhà máy. [W1, Chương 4, tr. in 167–169/339; tr. PDF 250–252.]

Nguồn biến tần được quy định ba pha 6,6 kV ±10%, tần số nguồn 50 Hz ±5%. Phần an toàn nêu sự cố có hồ quang tại Power Cell hoặc máy biến áp và liên hệ yêu cầu kỹ thuật của hệ thống thiết bị 6,6 kV. Đây là căn cứ xác lập phạm vi trung thế của trường hợp nghiên cứu, không cho phép kết luận mọi tủ hạ thế hoặc mọi thiết bị trung thế của nhà máy đã có cùng giải pháp. [W1, Chương 4, tr. in 169 và 171/339; tr. PDF 252 và 254.]

Hồ sơ nêu cả công nghệ HV IGBT và LV IGBT trong phần yêu cầu biến tần. Việc nhắc Power Cell vì thế không được dùng để kết luận nhà máy đã lựa chọn một cấu trúc công suất cụ thể. Chương giữ các bộ phận được nêu trực tiếp trong yêu cầu an toàn, không bổ sung số cell, mã biến tần, mã cảm biến hoặc vị trí lắp. [W1, Chương 4, tr. in 169–171/339; tr. PDF 252–254.]

## 1.3.3. Yêu cầu phát hiện và phối hợp bảo vệ trong hồ sơ

Bảng 1.2 phân biệt nội dung quy định với ý nghĩa chức năng và giới hạn thông tin. Cách đọc này cần thiết vì yêu cầu phản hồi nhanh chưa tạo ra giá trị mili giây, còn yêu cầu kết hợp đo dòng chưa xác định cách thực hiện logic.

*Bảng 1.2. Nội dung bảo vệ hồ quang trong hồ sơ Quảng Ninh.*

| Nội dung hồ sơ | Ý nghĩa chức năng | Trang/mục | Giới hạn thông tin |
|---|---|---|---|
| Danh sách bảo vệ có chức năng phát hiện hồ quang | Phát hiện là yêu cầu trong đặc tính biến tần | W1, Ch. 4, thông số biến tần, tr. in 170/339; PDF 253 | Chưa xác nhận thiết bị đã lắp |
| Thiết bị phát hiện có phản hồi nhanh, nhận biết kịp thời sự cố có hồ quang | Có yêu cầu tốc độ trong chuỗi phát hiện–phản hồi | W1, Ch. 4, “Tiêu chuẩn an toàn”, tr. in 171/339; PDF 254 | Đoạn này không cho giới hạn thời gian định lượng |
| Kết hợp công nghệ đo dòng để tăng tính tin cậy | Dòng điện tham gia chức năng bảo vệ | Cùng vị trí, PDF 254 | Chưa nêu ngưỡng, vị trí đo, tỷ số biến dòng hoặc phép logic |
| Có khả năng gửi tín hiệu điều khiển tới máy cắt cấp nguồn | Phát hiện cần phối hợp với phần tử cắt nguồn | Cùng vị trí, PDF 254 | Chưa nêu mã máy cắt, giao diện, mạch trung gian hoặc thời gian mở |
| Xét phóng điện, ngắn mạch tại Power Cell hoặc máy biến áp | Chỉ ra bộ phận thuộc phạm vi sự cố | Cùng vị trí, PDF 254 | Không phải bản đồ bố trí cảm biến |
| Tủ và cơ cấu bảo vệ đáp ứng yêu cầu kỹ thuật, an toàn thiết bị 6,6 kV | Xem phát hiện cùng cách điện và hạn chế ảnh hưởng hồ quang | Cùng vị trí, PDF 254 | Chưa có kết quả thử hoặc nghiệm thu hệ thống đã lắp |

Bảng 1.2 xác nhận hồ sơ đặt ra chuỗi chức năng vượt ra ngoài việc hiển thị cảnh báo: bảo vệ phải có khả năng đưa tín hiệu tới máy cắt cấp nguồn. Tuy nhiên, hồ sơ không xác nhận nguyên lý cảm biến quang, mã rơ-le hoặc tên thương mại mô-đun. Lựa chọn thiết bị và chứng minh phối hợp cần tài liệu chi tiết hơn đoạn yêu cầu đang sử dụng. [W1, Chương 4, tr. in 171/339; tr. PDF 254.]

## 1.3.4. Trình tự chức năng phát hiện và phối hợp tác động

Trình tự trong Bảng 1.3 là cách phân tích yêu cầu chức năng từ hồ sơ, không phải quy trình thao tác của nhân viên vận hành. Các bước biểu diễn quan hệ xử lý ở mức khái niệm; tài liệu chưa xác định thứ tự thực thi nội bộ, độ đồng thời hoặc thời gian từng bước.

*Bảng 1.3. Trình tự chức năng xác lập từ yêu cầu thiết kế.*

| Bước phân tích | Chức năng được nhận diện | Căn cứ và giới hạn |
|---|---|---|
| 1 | Nhận biết sự cố có hồ quang trong phạm vi biến tần | W1, Ch. 4, tr. in 170–171; PDF 253–254. Chưa biết cơ chế cảm biến |
| 2 | Kết hợp thông tin dòng trong xử lý bảo vệ | W1, Ch. 4, tr. in 171; PDF 254. Chưa xác định logic AND, cửa sổ thời gian hoặc cách so ngưỡng |
| 3 | Tạo tín hiệu điều khiển gửi tới máy cắt cấp nguồn | Cùng trang. Chưa xác định giao diện và thiết bị trung gian |
| 4 | Phối hợp máy cắt cô lập nguồn khi có sự cố thuộc phạm vi | Cùng trang. Đây là mục đích thiết kế; chưa có thời gian cắt đo được hoặc nghiệm thu |

Về phân tích hệ thống, nhận biết hồ quang và sử dụng thông tin dòng có thể thuộc các phần tử khác nhau; hồ sơ chưa xác định cách phân bố đó. Khả năng gửi tín hiệu điều khiển cũng không chứng minh bộ phát hiện trực tiếp cấp dòng cho cuộn cắt. Bảng 1.3 vì thế giữ ranh giới giữa chức năng được yêu cầu và giải pháp phần cứng chưa được xác nhận.

Tài liệu đề cập DCS trong phạm vi tích hợp điều khiển biến tần ở các trang trước, nhưng điều đó chưa chứng minh đường tín hiệu bảo vệ hồ quang đi qua DCS. Không thể bổ sung từ đó các bước xác nhận trên màn hình, truyền SCADA, ghi sự kiện hoặc tự khôi phục. Những chức năng này cần sơ đồ bảo vệ, tài liệu vận hành và cấu hình thực tế riêng. [W1, Chương 4, tr. in 168–169 và 171/339; tr. PDF 251–252 và 254.]

## 1.3.5. Đối chiếu với yêu cầu của đề tài và giới hạn thông tin

Trường hợp Quảng Ninh cung cấp căn cứ ở cấp hồ sơ cho nhu cầu phát hiện trong một hệ trung thế, vai trò phối hợp thông tin dòng và yêu cầu kết nối phần tử cắt nguồn. Nó hỗ trợ YC-01, YC-02, YC-03 và YC-05 trong Bảng 1.1 ở mức bối cảnh và chức năng. Hồ sơ chưa xác lập độ nhạy quang hoặc chu kỳ lấy mẫu của nguyên mẫu. [W1, Chương 4, tr. in 169–171/339; tr. PDF 252–254.]

Để xác nhận hiện trạng, còn thiếu danh mục thiết bị đã cung cấp, bản vẽ hoàn công, vị trí đầu thu, cấu hình bảo vệ, biên bản thử và nghiệm thu. Không có các dữ liệu này, chương không khẳng định hệ thống đã lắp hoặc đang vận hành, không kết luận thời gian tác động đã đạt và không gán thiết bị thương mại cụ thể cho nhà máy. Trường hợp trung thế cũng chưa thay thế được khảo sát ứng dụng phía hạ thế.

Những giới hạn đó không làm mất giá trị của hồ sơ: yêu cầu thiết kế vẫn cho thấy phát hiện cần nằm trong chuỗi bảo vệ có mục đích cụ thể. Để bổ sung cách nhìn ở cấp thiết bị, phần tiếp theo khảo sát độc lập Mors Smitt 1S23. Việc khảo sát không hàm ý nhà máy đã dùng sản phẩm này.

# 1.4. Khảo sát thiết bị phát hiện hồ quang điện Mors Smitt 1S23

## 1.4.1. Giới thiệu thiết bị và phạm vi ứng dụng

Tệp MHTML trong bộ nguồn là trang giới thiệu *1S23 Arc Flash Module – 2 point sensors / 1 zone* của KMET. KMET là nơi giới thiệu, phân phối; tài liệu kỹ thuật đối chiếu mang thương hiệu RMS Mors Smitt. Hãng gọi 1S23 là mô-đun giao diện sự cố hồ quang, kết nối cảm biến quang với đầu vào trạng thái rơ-le bảo vệ. Cách nhận dạng này xác định chức năng sản phẩm rõ hơn việc xem nó như toàn bộ hệ thống cắt hồ quang. [TL5, tiêu đề và phần giới thiệu; W3, “Introduction”, tr. in/PDF 2.]

Hai tài liệu chính hãng được dùng là Technical Bulletin v01.0 ngày 24/03/2025 và User Guide Iss C ngày 06/06/2022. Đường dẫn cũ trong nguồn đã trả trang lỗi khi truy cập; PDF được tải từ liên kết tài liệu trên trang sản phẩm mới của hãng. Ngày phiên bản được đọc trong PDF, không lấy ngày thu thập của công cụ tìm kiếm làm ngày phát hành. [W3, chân trang 1–11; W4, “About This Manual”, tr. in/PDF 2.]

Hình 1.6 là ảnh chính trong bản MHTML KMET; dữ liệu ảnh đã đối chiếu với ảnh nhúng của tệp nguồn. Hình chỉ giúp nhận dạng mô-đun và cảm biến đi kèm, không xác nhận cấu hình đã lắp tại Quảng Ninh.

![Ảnh sản phẩm 1S23 và cảm biến trong trang KMET lưu tại bộ nguồn](hinh_minh_hoa/Hinh_1_6_Mo_dun_phat_hien_ho_quang_Mors_Smitt_1S23.png)

*Hình 1.6. Ảnh giới thiệu mô-đun 1S23 cùng cảm biến, dùng để nhận dạng sản phẩm khảo sát.*

*Nguồn: TL5, ảnh chính trang sản phẩm KMET lưu trong MHTML; [trang gốc](https://kmet.com.vn/1s23-arc-flash-monitor-2-point-sensors-1-zone), [ảnh gốc](https://cdn4283.cdn4s8.io.vn/media/anhsanpham/smitt/1s23-3.png). Đối chiếu bản lưu ngày 24/10/2026; giữ nguyên nội dung, trang không nêu giấy phép mở.*

## 1.4.2. Cấu hình và giao diện chức năng

1S23 dùng cảm biến quang 1S30, có biến thể một hoặc hai cảm biến. User Guide yêu cầu số cảm biến phù hợp biến thể đặt hàng; biến thể hai cảm biến không đương nhiên hoạt động đúng khi chỉ đấu một. Hai đầu thu cũng không mặc nhiên tạo hai vùng tác động độc lập: cấu trúc khảo sát có đầu ra sự cố chung, còn trang giới thiệu nguồn gọi sản phẩm là một vùng. [W3, “Two Part System”, tr. in/PDF 3; W4, “1S23 Connection diagram”, tr. in/PDF 12; TL5, tiêu đề.]

Giao diện chính gồm đầu nguồn phụ trợ, đầu cảm biến, đầu ra ARC FAULT và đầu ra SUPERVISION. Nguồn hãng phân biệt đầu ra sự cố với đầu ra giám sát tình trạng hệ thống, cảm biến. Đầu ra là khóa bán dẫn có phân cực, chuyển mạch phía âm nguồn, không phải tiếp điểm khô để đấu tùy ý vào mọi mạch ngoài. [W3, “Description”, tr. 2; “Outputs”, tr. 5; W4, “Scheme Wiring”, tr. 12–13.]

Hình 1.7 thể hiện nguồn, đầu cảm biến và hai dây tín hiệu đầu ra. Điểm có ý nghĩa với hệ thống nhúng là giao diện phải được mô tả cả chức năng và tính chất điện. Chỉ ghi có đầu ra cảnh báo chưa đủ để đánh giá khả năng kết nối thiết bị tiếp nhận.

![Sơ đồ đấu nối 1S23 với đầu cảm biến và hai đầu ra chuyển mạch âm](hinh_minh_hoa/Hinh_1_7_Dau_noi_1S23.png)

*Hình 1.7. Sơ đồ đấu nối 1S23: dây xanh là đầu ra sự cố, dây trắng là đầu ra giám sát; các đầu ra chuyển mạch phía âm.*

*Nguồn: W3, “1S23 Module Connection and Wiring Diagram”, tr. in 7/11, tr. PDF 7. Cắt vùng sơ đồ gốc, giữ nguyên ký hiệu và ghi chú; đây là sơ đồ sản phẩm hãng.*

Chỉ thị PWR và ARC giúp phân biệt trạng thái bình thường với sự kiện hoặc lỗi. Tài liệu còn mô tả giám sát tính liên tục cảm biến và giám sát hệ thống bằng watchdog. Điều này cho thấy không có tín hiệu sự cố và hệ thống sẵn sàng phát hiện là hai trạng thái cần phân biệt. [W3, “Front Panel Layout and LED Indications”, “System Supervision” và “Arc Sensor Supervision”, tr. in/PDF 3.]

## 1.4.3. Nguyên lý phát hiện và phối hợp với rơ-le bảo vệ

Khi cường độ sáng vượt ngưỡng tác động, khóa bán dẫn đầu ra sự cố đưa phía âm nguồn tới đầu vào trạng thái rơ-le. Mô-đun còn đưa tín hiệu giám sát tới một đầu vào khác. Theo mô tả này, 1S23 nhận tín hiệu cảm biến và tạo giao diện điện cho khâu bảo vệ phía sau. [W3, “Trip Output Circuit Operation” và “System Supervision and Sensor Supervision Output Circuit Operation”, tr. in/PDF 3.]

Với cấu hình kiểm tra dòng, logic phối hợp và phần tử quá dòng nằm ở rơ-le ngoài. User Guide đưa ví dụ có đầu vào ARC FAULT, đầu vào SUPERVISION, phần tử dòng và đầu ra rơ-le tới mạch cắt máy cắt. Đây là cấu hình mẫu của hãng, không phải bằng chứng về cấu hình nhà máy ở mục 1.3. [W4, “Example Schematic” và “Over Current Relay Configuration”, tr. in/PDF 13–14.]

Hãng nêu rõ đầu ra 1S23 dùng cho đầu vào trạng thái nhị phân chuyên dụng của rơ-le bảo vệ, không phù hợp để cắt trực tiếp qua rơ-le phụ hoặc cuộn cắt máy cắt. Đầu vào số tiếp nhận phải được cách ly và không dùng chung cực âm với đầu vào khác theo sơ đồ ví dụ. Vì vậy, trị số dòng đầu ra không thể được hiểu như quyền đấu trực tiếp tải chấp hành. [W4, tr. in/PDF 13–14.]

Từ đó, đề tài nhận thấy cần tách ba lớp khi đánh giá: nhận biết dấu hiệu, quyết định phối hợp bảo vệ và thực hiện loại trừ sự cố. Kết quả đo tại đầu ra mô-đun chỉ phản ánh chuỗi tới đầu ra đó. Muốn kết luận thời gian máy cắt phải đo hoặc có dữ liệu phù hợp của các phần tử sau, không cộng ghép những mô tả thiếu cùng điều kiện tham chiếu.

## 1.4.4. Thông số kỹ thuật liên quan đến đề tài

Bảng 1.4 tổng hợp thông số liên quan đến các yêu cầu ở mục 1.2. Giá trị thuộc sản phẩm theo phiên bản ghi kèm, không phải chỉ tiêu được chọn hoặc kết quả đạt của đồ án. Trong tài liệu hãng dùng dưới đây, trang in trùng trang PDF.

*Bảng 1.4. Thông số tham khảo của 1S23 và giới hạn diễn giải.*

| Thông số | Giá trị | Điều kiện/biến thể/phiên bản | Ý nghĩa với bài toán | Nguồn, trang |
|---|---|---|---|---|
| Cảm biến và số đầu thu | Một hoặc hai 1S30 | Theo biến thể đặt hàng | Xét đúng cấu hình, không suy số vùng từ số đầu thu | W3 v01.0, tr. 2–3; W4 Iss C, tr. 12 |
| Nguồn phụ trợ danh định | 24; 32; 48; 110; 125; 220; 240; 250 VDC | Các mức theo biến thể | Không phải một nguồn duy nhất làm việc liên tục 24–250 VDC | W3 v01.0, tr. 5 |
| Dải làm việc nguồn | ±20% điện áp danh định | Với mức danh định tương ứng | Cần ghi đúng biến thể khi đánh giá nguồn | W3 v01.0, tr. 5 |
| Công suất | Dưới 0,75 W khi giám sát; dưới 1,5 W trong 2 s ở mức lớn nhất | Cùng điều kiện 110 VDC | Không chuyển giá trị sang mọi nguồn khác | W3 v01.0, tr. 5 |
| Thời gian tác động đầu ra sự cố | Dưới 2 ms | Từ chớp sáng đến đầu ra; Bulletin v01.0 ngày 24/03/2025 | Thời gian mô-đun, chưa gồm máy cắt | W3 v01.0, tr. 5 |
| Độ rộng xung sự cố | 110 ms ±10 ms | Xung cố định, Bulletin v01.0 | Thời gian duy trì đầu ra, không phải độ trễ | W3 v01.0, tr. 3, 5 |
| Kiểu đầu ra | Khóa bán dẫn phân cực, chuyển mạch âm | Giao diện trạng thái | Đối chiếu cách ly, cực tính đầu vào rơ-le | W3 v01.0, tr. 5; W4 Iss C, tr. 13–14 |
| Dòng lớn nhất đầu ra sự cố | 3,1 A; 1,6 A; 0,75 A | Tương ứng nhóm nguồn 24/32/48 V; 110/125 V; 220/240/250 V | Không cho phép suy thành cắt cuộn máy cắt trực tiếp | W3 v01.0, tr. 5; W4 Iss C, tr. 14 |
| Dòng đầu ra giám sát | 70 mA trong 60 ms; 30 mA liên tục | Mọi biến thể trong bảng hãng | Phân biệt định mức ngắn hạn và liên tục | W3 v01.0, tr. 5 |
| Giám sát tính liên tục cảm biến | Dòng giám sát 2 mA; mất dòng thì bỏ healthy sau 1 s | Mô tả chức năng Bulletin | Thời gian báo lỗi khác thời gian nhận hồ quang | W3 v01.0, tr. 3 |
| Ánh sáng kéo dài | Vô hiệu trip nếu cảm biến bị kích thích hơn 500 ms | Đồng thời bỏ trạng thái giám sát bình thường | Cần xét mức sẵn sàng khi ánh sáng nền bất thường | W3 v01.0, tr. 3 |

Đối chiếu phiên bản cho thấy không nên tổng hợp bằng cách chọn trị số nhỏ nhất. Bulletin bản K ngày 13/06/2024 ghi dưới 1,5 ms, còn v01.0 ngày 24/03/2025 ghi dưới 2 ms và nêu rõ từ chớp sáng đến đầu ra. Chương dùng bản v01.0 cho Bảng 1.4, không suy ra mọi thiết bị lưu hành có cùng lịch sử phần cứng hoặc khác biệt này nhất thiết do thay đổi phần cứng. [W5, “Technical Data”, tr. in/PDF 5; W3, “Technical Data”, tr. in/PDF 5.]

Về độ rộng xung, User Guide Iss C ghi 100 ms trong bảng chỉ thị và xấp xỉ 100 ms trong phần thử, còn Bulletin v01.0 ghi 110 ms ±10 ms. User Guide quy định thứ tự ưu tiên là Technical Bulletin trước User Guide. Vì vậy, khi cần thông số có dung sai, chương dùng 110 ms ±10 ms theo Bulletin và giữ 100 ms như mô tả của bản hướng dẫn cũ hơn; không diễn giải thành hai độ trễ phát hiện. Khi mua hoặc kiểm định thiết bị cụ thể vẫn cần đối chiếu mã hàng và tài liệu đi kèm đúng thiết bị. [W4, “Documentation”, tr. 5; “Summary of Indications”, tr. 9; “Arc Trip Testing”, tr. 33; W3, tr. 3, 5.]

TL5 ghi dưới 2 ms và 110 ms ±10 ms, phù hợp với các giá trị tương ứng của Bulletin v01.0. Tuy nhiên, cách viết rút gọn 24–250 VDC trên trang giới thiệu cần đọc cùng bảng các mức danh định. Việc đối chiếu làm rõ vai trò tài liệu hãng trong kiểm chứng, thay vì chỉ dùng phần mô tả bán hàng. [TL5, phần giới thiệu và bảng thông số; W3, tr. 5.]

## 1.4.5. Bố trí cảm biến và kiểm tra chức năng theo hướng dẫn hãng

User Guide yêu cầu bố trí cảm biến bao phủ những khoang cần bảo vệ; nếu vùng giám sát lớn hơn vùng thu nhận thì cần nhiều đầu thu. Hình 1.8 trích hai ví dụ trong khoang máy cắt và khoang thanh cái. Dấu đánh dấu đã có trong nguồn, không phải vị trí do đề tài tự thiết kế. [W4, “Sensor Placement” và “Example Sensor Placement”, tr. in/PDF 25–26.]

![Ví dụ bố trí cảm biến tại khoang máy cắt và khoang thanh cái](hinh_minh_hoa/Hinh_1_8_Vi_du_bo_tri_1S30.png)

*Hình 1.8. Ví dụ bố trí cảm biến theo User Guide: trên là khoang máy cắt, dưới là khoang thanh cái.*

*Nguồn: W4, “Example Sensor Placement”, tr. in/PDF 26. Cắt hai ảnh cùng chú giải gốc, giữ nguyên dấu đánh dấu trong nguồn; không đại diện cho tủ tại Quảng Ninh.*

Hướng dẫn đưa khoảng cách khuyến nghị xấp xỉ 5–6 m khi bố trí 1S30A để chồng lấn vùng nhận biết. Đây là khuyến nghị trong hình học minh họa sản phẩm, không phải cam kết quan sát xuyên vách kín hoặc bảo vệ mọi khoang ở khoảng cách đó. Từ hướng dẫn, đề tài nhận thấy cần kiểm tra đường truyền ánh sáng và kết cấu tủ trước khi chuyển thông số bố trí thành yêu cầu lắp đặt. [W4, “Sensor Spacing”, tr. in/PDF 23; “Sensor Placement”, tr. in/PDF 25; phần liên hệ là phân tích của đề tài.]

Phần commissioning phân chia kiểm tra ban đầu, xác nhận nguồn và biến thể cảm biến, kiểm tra đầu ra giám sát và đầu ra hồ quang. Hãng sử dụng nguồn chớp sáng thích hợp để kích thích đầu thu; với cấu hình kiểm tra dòng, thử phải đồng thời tạo điều kiện cho phần tử dòng liên quan. Đây là kiểm tra chức năng theo hướng dẫn, không phải tạo hồ quang trung thế tại hiện trường. [W4, “Commissioning”, tr. in/PDF 30–33.]

Ý nghĩa đối với đồ án là đánh giá trạng thái sẵn sàng và lỗi cảm biến bên cạnh trường hợp nhận ánh sáng. Nguồn sáng yếu không kích hoạt đầu thu chưa đủ chứng minh thiết bị lỗi; đầu ra có tác động với đèn thử cũng chưa chứng minh khả năng bảo vệ mọi sự cố. Hướng dẫn lưu ý đèn chớp nhỏ có thể không đủ công suất cho phép thử. Vì vậy, kết quả phải ghi điều kiện kích thích và giới hạn kết luận. [W4, “ARC Trip Verification”, tr. 30; “SUPERVISION Output Verification” và “Arc Trip Testing”, tr. 32–33.]

## 1.4.6. Nội dung tham khảo cho hệ thống nhúng của đồ án

Khảo sát 1S23 cung cấp cách mô tả chức năng có thể tham khảo: xác định cảm biến tương thích, tách nguồn phụ trợ khỏi điện áp hệ thống, định nghĩa thời gian kích thích–đầu ra, phân biệt đầu ra sự cố và giám sát. Các điểm này liên hệ YC-01, YC-04 và YC-05. Phối hợp với rơ-le ngoài làm rõ YC-03 ở cấp giao diện và trách nhiệm xử lý, chưa quyết định nguyên mẫu tự đo dòng hay nhận trạng thái từ ngoài. [W3, tr. 2–5; W4, tr. 12–14; đối chiếu Bảng 1.1.]

Bộ tài liệu khảo sát không công bố cấu hình đầy đủ về phần cứng xử lý, tần số lấy mẫu, thuật toán nội bộ và ngưỡng quang định lượng để tái tạo thiết bị. Không thể từ thời gian dưới 2 ms suy ra chu kỳ ADC hoặc loại vi điều khiển. YC-02, YC-04 và YC-06 vẫn cần dữ liệu tín hiệu và cơ sở lý thuyết riêng trước khi chuyển thành lựa chọn thiết kế. [W3, “Technical Data”, tr. 5; W4, “Documentation”, tr. 5; giới hạn của các tài liệu đã đọc.]

Đề tài tiếp thu cách phân định chức năng và mô tả thông số, không mặc định sao chép số kênh, nguồn hoặc định mức đầu ra. So sánh với 1S23 chỉ có ý nghĩa khi đo theo cùng đại lượng và công bố điều kiện tương ứng. Các hạng mục thử theo tiêu chuẩn của sản phẩm thương mại cũng không chứng minh nguyên mẫu đã đáp ứng tiêu chuẩn đó. [W3, “Compliance”, tr. in/PDF 6; nhận xét về phạm vi đối chiếu.]

Khảo sát thiết bị đã bổ sung góc nhìn ở cấp mô-đun cho yêu cầu ứng dụng trong hồ sơ nhà máy. Phần kết luận tổng hợp những căn cứ đã có và dữ liệu còn cần làm rõ trước khi lựa chọn giải pháp.

# 1.5. Kết luận chương

Chương 1 đã xác định bài toán phát hiện chớp hồ quang trong phạm vi tủ điện và thiết bị liên quan, phân biệt phát hiện với toàn bộ quá trình bảo vệ, loại trừ sự cố. Minh chứng thử nghiệm được sử dụng với đúng điều kiện nguồn, không chuyển thành thống kê tần suất hoặc kết quả đồ án. Sáu nhóm yêu cầu gồm điện áp, tần số, dòng điện, độ nhạy, thời gian phản hồi và chu kỳ lấy mẫu đã được phân tích theo đại lượng, ý nghĩa và cách đánh giá; giá trị chưa đủ căn cứ được giữ ở trạng thái cần bổ sung dữ liệu.

Trường hợp Quảng Ninh cho thấy yêu cầu phát hiện nhanh, phối hợp đo dòng và gửi tín hiệu tới máy cắt đã được nêu trong hồ sơ thiết kế của phạm vi biến tần trung thế. Căn cứ này chưa xác nhận hiện trạng lắp đặt, vận hành. Khảo sát 1S23 được thực hiện độc lập, làm rõ giao diện, giám sát tình trạng và cách phân biệt độ trễ với độ rộng xung; chưa có bằng chứng trong bộ nguồn đã đọc để gán sản phẩm này cho nhà máy.

Trên cơ sở bối cảnh và yêu cầu ban đầu, Chương 2 sẽ trình bày cơ sở lý thuyết phục vụ phát hiện, thu nhận và xử lý tín hiệu, tiếp theo phân tích và lựa chọn linh kiện. Phạm vi điện áp nguyên mẫu, điều kiện độ nhạy, cơ chế phối hợp dòng, giới hạn thời gian và phương án lấy mẫu cần được cụ thể hóa trước khi chốt thiết kế. Đánh giá kết quả phải giữ ranh giới giữa thử chức năng phát hiện và chứng minh khả năng bảo vệ một hệ thống điện thực tế.

# Tài liệu tham khảo của Chương 1

**TL1 —** Lauri Kumpulainen, G. Amjad Hussain, Marc Rival, Matti Lehtonen, Kimmo Kauhaniemi, *Aspects of arc-flash protection and prediction*, Electric Power Systems Research 116, 2014, tr. 77–86. DOI: 10.1016/j.epsr.2014.05.011. Tệp: [Aspects of arc-flash protection and prediction.pdf](<Tham khảo/Aspects of arc-flash protection and prediction.pdf>).

**TL2 —** Vytenis Babrauskas, *Electric arc explosions—A review*, Fire Safety Journal 89, 2017, tr. 7–15. DOI: 10.1016/j.firesaf.2017.02.006. Tệp: [Electric arc explosions—A review.pdf](<Tham khảo/Electric arc explosions—A review.pdf>).

**TL3 —** Mahmood Matin, Amir Dehghanian, Mohammad Dastranj, Hossein Darijani, *Explainable artificial intelligence modeling of internal arc in a medium voltage switchgear based on different CFD simulations*, Heliyon 10, 2024, e29594. DOI: 10.1016/j.heliyon.2024.e29594. Tệp: [Explainable artificial intelligence modeling of internal arc in a medium voltage switchgear based on different CFD simulations.pdf](<Tham khảo/Explainable artificial intelligence modeling of internal arc in a medium voltage switchgear based on different CFD simulations.pdf>). CC BY 4.0 ghi tại trang PDF 1.

**TL4 —** Jinmi Lezama, Patrick Schweitzer, Etienne Tisserand, Jean-Baptiste Humbert, Serge Weber, Patrice Joyeux, *An embedded system for AC series arc detection by inter-period correlations of current*, Electric Power Systems Research 129, 2015, tr. 227–234. Tệp: [An embedded system for AC series arc detection by inter-period correlations of current.pdf](<Tham khảo/An embedded system for AC series arc detection by inter-period correlations of current.pdf>).

**TL5 —** KMET, *1S23 Arc Flash Module – 2 point sensors / 1 zone*, trang giới thiệu sản phẩm, không ghi ngày xuất bản trong phần sử dụng. Tệp: [1S23 Arc Flash Module – 2 point sensors _ 1 zone.mhtml](<Tham khảo/1S23 Arc Flash Module – 2 point sensors _ 1 zone.mhtml>). [URL nhận dạng trang nguồn](https://kmet.com.vn/1s23-arc-flash-monitor-2-point-sensors-1-zone). Nội dung trích từ MHTML đã đọc ngày 24/10/2026; thông số đối chiếu W3–W4.

**TL6 —** Liangshi Lin, Wei Gao, Gengjie Yang, *A DC arc fault location method for PV systems based on redundant antenna array and ellipse algorithm*, Solar Energy 274, 2024, 112588. DOI: 10.1016/j.solener.2024.112588. Tệp: [A DC arc fault location method for PV systems based on redundant antenna array and ellipse algorithm.pdf](<Tham khảo/A DC arc fault location method for PV systems based on redundant antenna array and ellipse algorithm.pdf>).

**W1 —** Công ty Cổ phần Nhiệt điện Quảng Ninh; Viện Năng lượng (tư vấn), *Dự án nâng cấp, cải tạo hệ thống xử lý khí thải Nhà máy Nhiệt điện Quảng Ninh — Điều chỉnh Báo cáo Nghiên cứu khả thi*, Chương 4 trong tệp gộp công khai có thông tin hiển thị ký số 11/06/2026 tại trang PDF 1. [Bản sao đã đọc tại CafeF](https://cafef1.mediacdn.vn/download/110626/qtp-tai-lieu-hop-ai-hoi-dong-co-dong-3-619481.pdf); [bản lưu kiểm chứng](nguon_web/qtp-full.pdf). Tệp có 688 trang; trang in 167–171/339 của Chương 4 tương ứng PDF 250–254. Truy cập 24/10/2026. Chưa đối chiếu được cùng tệp tại doanh nghiệp/HNX; CafeF là nơi lưu bản sao, không phải tác giả hồ sơ.

**W2 —** Công ty Cổ phần Nhiệt điện Quảng Ninh, *Giới thiệu Công ty Cổ Phần Nhiệt Điện Quảng Ninh*, trang “Giới thiệu chung”, hiển thị ngày 23/03/2017. [Trang doanh nghiệp đã đọc](https://quangninhtpc.com.vn/c3/gioi-thieu-f/Gioi-thieu-chung-2-204). Truy cập 24/10/2026. Dùng cho bối cảnh doanh nghiệp, không xác nhận hiện trạng bảo vệ hồ quang.

**W3 —** RMS Mors Smitt, *1S23 — ARC Fault Interface Module*, Technical Bulletin v01.0, 24/03/2025, 11 trang. [Trang sản phẩm hãng](https://morssmitt.com/product/1s23/); [PDF qua liên kết tải trên trang hãng](https://wabtecnl.katanapim.com/AttachmentDownload/Download/58?name=1s23-v01-0.pdf); [bản lưu đã đọc](nguon_web/1s23-v01-0-xac-minh.pdf). Truy cập, tải 24/10/2026; phiên bản kiểm tra ở chân trang PDF.

**W4 —** RMS Mors Smitt, *1S23 User Guide*, Iss C, 06/06/2022, 40 trang. [PDF qua liên kết tải trên trang hãng](https://wabtecnl.katanapim.com/AttachmentDownload/Download/568?name=user-guide-1s23-iss-c.pdf); [bản lưu đã đọc](nguon_web/user-guide-1s23-iss-c-xac-minh.pdf). Truy cập, tải 24/10/2026. Trang in trùng trang PDF; phiên bản và phạm vi ở trang 2, thứ tự ưu tiên tài liệu ở trang 5.

**W5 —** RMS Mors Smitt, *1S23 — ARC Fault Interface Module*, Technical Bulletin bản K, 13/06/2024, 11 trang. [Bản tài liệu hãng tại RI-TECH](https://www.ri-tech.cz/wp-content/uploads/2016/12/1s23-k.pdf); [bản lưu đã đọc](nguon_web/1s23-k.pdf). Truy cập, tải 24/10/2026. Chỉ dùng đối chiếu phiên bản với W3; ngày thư mục URL không được dùng thay ngày phiên bản trong PDF.
