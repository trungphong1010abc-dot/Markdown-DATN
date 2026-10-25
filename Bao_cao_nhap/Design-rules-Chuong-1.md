> **Đề tài:** Thiết kế hệ thống nhúng phát hiện chớp hồ quang điện (arc-flash) trong hệ thống điện hạ thế và trung thế.
>
> **Ghi chú bản thảo:** Báo cáo được viết theo tài liệu này hướng tới khoảng 10–14 trang A4 khi dàn trang bằng Times New Roman 13, giãn dòng khoảng 1,15; số trang thực tế phụ thuộc lề và kích thước hình. Markdown không quy định trực tiếp phông chữ hoặc số trang.
>
> **Vai trò tài liệu:** Đây là đặc tả biên soạn Chương 1 dành cho Codex, không phải nội dung báo cáo hoàn chỉnh. Bố cục mới trong tài liệu này thay thế bố cục cũ. File báo cáo cũ chỉ dùng tham khảo hình thức trình bày, tuyệt đối không coi nội dung và danh mục nguồn cũ là dữ liệu đã kiểm chứng.

# A. Phạm vi thao tác và sản phẩm cần hoàn thành

**Khóa nội dung mục 1.1 — người dùng xác nhận ngày 25/10/2026:**

- Mục **1.1 đã được chốt**, gồm toàn bộ nội dung từ heading `# 1.1.` đến trước heading `# 1.2.`, bao gồm các tiểu mục, câu chữ, trích dẫn, hình và chú thích. Không tự ý chỉnh sửa, viết lại, đổi bố cục hoặc cập nhật hình/số hình trong phạm vi này.
- **Chốt lại sau lần cập nhật bố cục và ví dụ ngày 25/10/2026:** Khi chỉnh bất kỳ phần nào khác hoặc viết các chương sau, giữ nguyên toàn bộ mục 1.1. Chỉ được sửa khi người dùng yêu cầu riêng việc sửa mục 1.1, hoặc khi làm các chương sau người dùng chủ động yêu cầu sửa các phần liên quan và nội dung trong mục 1.1 thuộc đúng phạm vi liên quan đó. Không tự suy ra quyền sửa từ nhu cầu đồng bộ hoặc rà soát chung; chỉ thay đổi phần được yêu cầu.
- Nếu phát hiện điểm chưa thống nhất với nội dung mới, nêu điểm đó để người dùng quyết định, không tự sửa mục 1.1. Quy tắc khóa này được ưu tiên hơn các hướng dẫn viết lại toàn chương, rà soát văn phong hoặc cập nhật đồng bộ bên dưới.
- Phạm vi làm việc hiện tại theo yêu cầu mới nhất: viết lại mục **1.3** về hệ thống tủ điện tại Nhà máy HEINEKEN Vũng Tàu; thay nguồn và ảnh của trường hợp cũ theo yêu cầu, đồng bộ mở đầu và kết luận; tạm giữ mục **1.2** để xử lý sau. Không sửa mục 1.1 hoặc 1.2 khi tổ chức lại mục 1.3.
- Các yêu cầu trước về đổi định dạng trích dẫn, chia lại bố cục và cập nhật ví dụ mục 1.1 đã hoàn thành trước lần chốt này; không còn là ngoại lệ cho những lần chỉnh sửa tiếp theo. Việc đổi số trích dẫn, hình hoặc chú thích trong mục 1.1 cũng tuân theo quy tắc khóa trên.
- Ngoại lệ riêng theo yêu cầu mới nhất ngày 25/10/2026: rà soát và sửa lối kể về nguồn trong toàn báo cáo, kể cả mục 1.1 và 1.2, theo B.5. Chỉ chỉnh cách diễn đạt, giữ dữ kiện, điều kiện thử, cấu trúc và giới hạn bằng chứng. Sau lần sửa này, mục 1.1 tiếp tục được khóa; không suy ra quyền chỉnh nội dung khác từ ngoại lệ văn phong.

1. Xác định thư mục thực tế trước khi thao tác. Ảnh người dùng cung cấp thể hiện `Bao_cao_nhap/` chứa `hinh_minh_hoa/`, `Tham khảo/` và `Chuong-1-Tong-quan-de-tai.md`. Nếu cấu trúc thực tế khác, xác định chính xác hai vùng nguồn và đầu ra, không tự tạo các thư mục trùng tên để né ranh giới.
2. `Tham khảo/` là vùng chỉ đọc: đọc toàn bộ danh mục nguồn, tìm nội dung phù hợp; không sửa, xóa, đổi tên hoặc di chuyển bất kỳ tệp nguồn nào. Quy tắc chỉ đọc này vẫn áp dụng nếu thư mục nguồn nằm trong `Bao_cao_nhap/`.
3. Chỉ chỉnh sửa báo cáo đích `Bao_cao_nhap/Chuong-1-Tong-quan-de-tai.md`, ảnh trong `Bao_cao_nhap/hinh_minh_hoa/` và tệp phụ trợ thật sự cần thiết cho Chương 1 bên trong vùng đầu ra. Không đọc hoặc thay đổi nội dung các thư mục không liên quan; không mở rộng phạm vi qua symlink.
4. Có thể tra Google và truy cập các nguồn chính thống liên quan trên web. Tài liệu tải thêm, nếu cần lưu, đặt tại một thư mục nguồn web riêng bên trong vùng đầu ra, không thêm vào hoặc chỉnh sửa `Tham khảo/`.
5. Viết lại toàn bộ Chương 1 theo bố cục phần D; không chỉ vá vài đoạn của bản cũ. Giữ nguyên tên đề tài. Không xuất DOCX/PDF nếu chưa được yêu cầu; có thể xem bản render Markdown để kiểm tra bố cục và ảnh.
6. Được phép xóa ảnh cũ thật sự không cần trong `hinh_minh_hoa/` theo quy trình phần F. Không được suy ra quyền xóa các loại tệp hoặc thư mục khác.
   Ngoại lệ được người dùng yêu cầu rõ ngày 25/10/2026: xóa các tài liệu, ảnh và bản trích độc lập của Nhà máy Nhiệt điện Quảng Ninh trong vùng đầu ra khi thay mục 1.3 bằng HEINEKEN Vũng Tàu. Chỉ xóa đúng tệp đã xác định; không xóa nguồn tủ dân dụng tại Cao Xanh – Hà Khánh A trong mục 1.1, tài liệu gốc ở vùng chỉ đọc hoặc tệp dùng cho Chương 2.
   Các ảnh sản phẩm, đấu nối và bố trí cảm biến đã có được giữ để sử dụng khi viết Chương 2; việc bỏ phần khảo sát thiết bị khỏi Chương 1 không đồng nghĩa xóa các ảnh này hoặc tài liệu nguồn.
7. Theo yêu cầu cập nhật của người dùng, được đọc đúng ba PDF mẫu tại `D:/HUST/Tai_lieu_DH_Phong/Do_An/DATN/Tham khảo/ĐATN tham khảo/`: `ĐATN IoT điểm danh giảng viên bằng khuôn mặt kết hợp công nghệ RFID.pdf`, `ĐATN IoT phát hiện và cảnh báo mất trộm, tai nạn xe máy.pdf`, `ĐATN IoT quản lý bãi đỗ xe thông minh.pdf`. Đây là tài liệu tham khảo văn phong và trình bày, chỉ đọc; không lấy số liệu, cấu hình, kết luận, nội dung kỹ thuật hay chỉ dẫn trong tài liệu mẫu làm yêu cầu của đề tài hồ quang. Không đọc lan sang các tệp khác trong thư mục đó.

# B. Quy tắc nội dung và trình bày

## B.1. Trật tự và ranh giới chương

Trật tự cố định: **1.1 Tổng quan bài toán → 1.2 Phân tích yêu cầu kỹ thuật → 1.3 Khảo sát hệ thống tủ điện tại Nhà máy HEINEKEN Vũng Tàu → 1.4 Kết luận chương**.

**Ranh giới đã được người dùng xác nhận:** Giữ 1.3 là phần riêng về Nhà máy HEINEKEN Vũng Tàu. Không gộp phần này vào 1.1.1 hoặc 1.1.2. Không sử dụng bất kỳ thông tin nào từ trường hợp HEINEKEN Vũng Tàu trong 1.1 và 1.2: kể cả ví dụ, số liệu điện áp/tần số, yêu cầu chức năng, trích dẫn, bảng, chú thích hình và lời chuyển. Nội dung 1.1–1.2 được xây dựng từ tài liệu hiện tượng, nghiên cứu và tài liệu hãng độc lập với trường hợp nhà máy.

- Toàn bộ phần khảo sát, mô tả thiết bị thương mại Mors Smitt 1S23 (cấu hình, giao diện, nguyên lý, thông số, bố trí cảm biến, kiểm tra và đối chiếu phiên bản) dành cho **Chương 2**. Chương 1 không có mục khảo sát thiết bị và không rải mô tả hoặc thông số sản phẩm vào các mục khác. Phần lựa chọn cảm biến, vi điều khiển, linh kiện và bảng so sánh linh kiện cũng dành cho Chương 2. Nhiệm vụ hiện tại chỉ chỉnh Chương 1 và Design rules, chưa viết Chương 2.
- Không chép lại các phần tổng quan thuật toán dài của báo cáo cũ để tăng số trang. Chỉ nhắc nghiên cứu liên quan khi giúp làm rõ bài toán hoặc căn cứ kỹ thuật.
- Kiến trúc dự kiến áp dụng mô hình node–gateway theo yêu cầu người dùng, được mô tả ngay dưới đây. Không tự chốt thêm số kênh, giao thức, nguồn cấp, ngưỡng hoặc điều kiện thử nếu chưa có căn cứ.
- Không kế thừa các chỉ tiêu cũ như 5 ms, 95/100, 100 bản ghi, 8 giờ, nguồn 24 VDC hoặc hai kênh quang như yêu cầu đã được chốt. Cấu hình sản phẩm tham khảo không tự động trở thành cấu hình đồ án.
- Phạm vi nguyên mẫu đã được người dùng xác nhận là **phát hiện và cảnh báo chớp hồ quang điện, không điều khiển cắt nguồn hoặc máy cắt**. Không viết chức năng cắt là “chưa chốt” hay hướng triển khai của nguyên mẫu. Phân biệt phạm vi này với chức năng bảo vệ, cắt điện trong tài liệu nguồn và hồ sơ nhà máy; không suy ra khả năng đáp ứng tiêu chuẩn công nghiệp.

**Mô hình thiết kế dự kiến — cập nhật theo yêu cầu người dùng ngày 25/10/2026:**

- Nguyên mẫu dự kiến gồm **một nút giám sát (node), một thiết bị trung tâm (gateway) và máy tính chạy phần mềm máy chủ (server)**. Đây là phương án dự kiến, chưa phải kết quả triển khai hoặc cấu hình đã kiểm nghiệm.
- Node là thiết bị nhúng thu nhận, xử lý tín hiệu để phát hiện chớp hồ quang tại tủ điện và gửi thông tin sự cố đến gateway. Gateway là thiết bị nhúng nhận thông tin từ node rồi chuyển đến máy chủ. Không chuyển nhiệm vụ phát hiện sang gateway hoặc máy chủ khi chưa có yêu cầu mới.
- Máy chủ chạy phần mềm tiếp nhận, hiển thị thông tin và cảnh báo khi có hồ quang; trong mô hình thử nghiệm có thể dùng laptop. Phân biệt phần mềm máy chủ với máy tính chạy phần mềm; không mặc định dùng máy chủ đám mây hoặc cần Internet. Chưa tự chốt hình thức còi, đèn hoặc kênh thông báo khác.
- Chương 1 giới thiệu vai trò và đường truyền thông tin **node → gateway → máy chủ** tại mục 1.1.1; cập nhật các phần liên quan về nguồn, thời gian, lấy mẫu, bảng yêu cầu và kết luận. Thiết kế chi tiết, giao thức, linh kiện và phần mềm được phân tích ở Chương 2. Không tự chọn Wi-Fi, LoRa, Ethernet, MQTT hoặc giao thức khác; không tự bổ sung số nút mở rộng, lưu trữ hay điều khiển hai chiều thành yêu cầu đã chốt.
- Phân biệt thời gian phát hiện tại node với thời gian truyền qua gateway và hiển thị cảnh báo trên máy chủ. Thời gian phản hồi của nguyên mẫu được xét đến khi cảnh báo xuất hiện trên máy chủ và tách thành các khoảng thu nhận, xử lý, truyền và hiển thị; không đưa thời gian rơ-le hay máy cắt vào yêu cầu nguyên mẫu. Phân biệt chu kỳ lấy mẫu với chu kỳ truyền dữ liệu và cập nhật hiển thị.
- Giữ sáu nhóm yêu cầu kỹ thuật về phát hiện; bổ sung yêu cầu truyền và hiển thị thông tin theo mô hình dự kiến. Mô hình là định hướng thiết kế của người dùng, không gán cho tài liệu nghiên cứu hoặc tài liệu trường hợp nhà máy. Không suy ra chức năng cắt máy cắt từ đường truyền này.

## B.2. Heading và văn phong

- Báo cáo đích không có heading `# CHƯƠNG 1...`; tên chương đã thể hiện qua tên file. Mở đầu bằng hai blockquote về đề tài và độ dài như đầu tài liệu này, rồi một đoạn giới thiệu chương.
- Dùng `# 1.1. ...`, `## 1.1.1. ...` và `### 1.1.1.1. ...`. Mục 1.1 được chia đến heading cấp 3 theo D.1 để tách các nhóm nội dung dễ đọc. Chưa tự chia lại các mục còn lại khi người dùng chưa yêu cầu. `# 1.4. Kết luận chương`; phần `# Tài liệu tham khảo` đặt cuối báo cáo, không đánh thành mục 1.5.
- Viết thành văn báo cáo tốt nghiệp: câu đầy đủ, đoạn văn có lập luận. Các câu hỏi 5W1H là công cụ rà soát, không phải mẫu hỏi–đáp phải chép vào báo cáo.
- Mỗi hình, bảng phải được nhắc trong nội dung và giải thích ý nghĩa; không chèn hình chỉ để đủ trang. Bảng dùng để tổng hợp số liệu, yêu cầu, nguồn hoặc đối chiếu; không biến toàn chương thành bảng.
- Không đưa lời giao việc, từ ngữ hội thoại, bình luận về bản cũ hoặc ký hiệu `%%...%%` vào báo cáo cuối.
- Phần thiếu dữ liệu cần diễn đạt thành giới hạn nghiên cứu cụ thể. Không để một con số đoán kèm nhãn “cần xác minh” rồi tiếp tục dùng số đó làm căn cứ.
- Áp dụng cách viết và cách gạch ý ở B.4 khi triển khai toàn bộ bố cục D. Không lặp máy móc một khuôn đoạn văn cho mọi tiểu mục.
- Áp dụng B.5 cho toàn văn: trình bày bằng giọng của người thực hiện đồ án, không viết yêu cầu như lời giao việc cho người thiết kế khác.

## B.3. Phân bổ độ dài tham khảo

| Thành phần | Dung lượng tương đối khi dàn trang |
|---|---:|
| Mở đầu và 1.1 | 3–4 trang |
| 1.2 | 3–4 trang |
| 1.3 | 2,5–3,5 trang |
| 1.4 và tài liệu tham khảo | 1–2 trang |

Các khoảng này là định hướng, không phải cam kết số trang. Ưu tiên nội dung có bằng chứng, không kéo dài bằng lặp ý hay phóng to hình.

## B.4. Văn phong và gạch ý theo ba đồ án mẫu — cập nhật 24/10/2026

### Cơ sở tham khảo cách trình bày

Đã đọc nội dung và xem bố cục trang ở các vị trí sau; số trang PDF đếm từ 1:

| Mẫu | Phần đã xem | Đặc điểm vận dụng |
|---|---|---|
| Điểm danh giảng viên bằng khuôn mặt kết hợp RFID | Chương 1, tr. in 1–5, PDF 13–17 | Đoạn dẫn đặt vấn đề; gạch đầu dòng có tên ý rồi giải thích; tách đối tượng, mục tiêu và yêu cầu chức năng |
| Phát hiện, cảnh báo mất trộm và tai nạn xe máy | Chương 1, tr. in 1–4, PDF 29–32 | Từ bối cảnh tới vấn đề cụ thể và mục tiêu; đánh số nhóm đối tượng/bước thực hiện; mỗi tiêu chí được giải thích bằng đoạn ngắn |
| Quản lý bãi đỗ xe thông minh | Chương 1, tr. in 1–4, PDF 13–16 | Đoạn văn dẫn nhập trước danh sách; gạch ý theo thành phần, tên thành phần được làm nổi; giải thích chức năng ngay sau tên ý |

Chỉ học cách tổ chức và nhịp văn. Không sao chép câu chữ, mở bài chung chung, lỗi chính tả, khẳng định chưa có căn cứ, nội dung quảng cáo hoặc thông tin liên hệ trong mẫu. Không đưa ba đồ án IoT vào danh mục nguồn kỹ thuật của Chương 1 hồ quang.

### Cách triển khai trong bản báo cáo

1. **Đoạn văn để giải thích, danh sách để phân ý.** Mỗi mục mở bằng nội dung chuyên môn hoặc vấn đề đang xét. Dùng đoạn văn khi cần mô tả hiện tượng, lập luận nguyên nhân–hậu quả hoặc liên hệ với nhiệm vụ đề tài. Khi có nhiều thành phần, đặc điểm, nguyên nhân hay yêu cầu song song, chuyển sang gạch đầu dòng thay vì dồn vào một đoạn dài.
2. **Gạch ý có nội dung.** Dùng dạng `- **Tên ý:** giải thích...`, thường 2–4 ý cùng nhóm. Mỗi ý gồm một hoặc vài câu đủ nghĩa; không liệt kê toàn danh từ, không kéo một ý thành cả trang. Không ấn định số ý nếu nội dung không cần. Chỉ lồng thêm cấp khi cần phân biệt bộ phận và chức năng; tránh danh sách nhiều tầng.
3. **Đánh số cho trình tự.** Phần 1.3.4 dùng các bước đánh số, có động từ và nội dung xử lý. Ghi một lần rằng đây là diễn giải chức năng từ hồ sơ thiết kế; không lặp lời giới hạn ở cuối mỗi bước. Không tự thêm bước ngoài nguồn.
4. **Mạch đặt vấn đề rõ ràng.** Đi từ hệ thống/thiết bị → sự cố và hậu quả → nhu cầu phát hiện → nhiệm vụ nghiên cứu. Không dùng các mở đầu chung như “trong thời đại công nghệ phát triển”, không viết triết lý về cách lập báo cáo.
5. **Câu trực tiếp, chủ thể cụ thể.** Ưu tiên các chủ thể như “hồ quang”, “cảm biến”, “đầu ra”, “máy cắt”, “hồ sơ thiết kế”. Hạn chế lặp “đề tài nhận thấy”, “cách giới hạn đó”, “đây là căn cứ”, “ở mức bối cảnh và chức năng”, “chương không...”. Không mở mọi tiểu mục bằng một định nghĩa rồi kết bằng cùng một đoạn “chưa có căn cứ”.
6. **Giới hạn được đặt đúng chỗ.** Giữ các phân biệt kỹ thuật cần thiết như độ trễ/độ rộng xung, thiết kế/hiện trạng và mô-đun/hệ bảo vệ. Không tạo mục riêng liệt kê thông tin nhà máy chưa xác minh. Chỉ giữ điều kiện và phân biệt thiết kế/hiện trạng ngay tại nội dung thực sự cần; giá trị chưa chốt đặt ở Bảng 1.1, khác biệt phiên bản thiết bị dành cho Chương 2. Không nhắc lại cùng một phủ định ở đoạn dẫn, chú thích ảnh, bảng và đoạn kết. Không bỏ giới hạn để tạo cảm giác đề tài đã có dữ liệu.
7. **Không tạo tệp kiểm chứng riêng.** Không tạo hoặc khôi phục `Kiem-chung-Chuong-1.md`, không xuất báo cáo kiểm chứng, nhật ký nguồn hoặc bảng kiểm thành một tài liệu giao riêng. Vẫn đọc nguồn, kiểm tra trích dẫn, số trang, bảng và liên kết trước khi hoàn thành; chỉ báo ngắn gọn kết quả trong tin nhắn kết thúc. Chi tiết thao tác tải, hash, giải mã và tìm nguồn không xuất hiện trong thân báo cáo.
8. **Bảng chỉ để đối chiếu.** Giữ bảng yêu cầu ban đầu và bảng nội dung hồ sơ theo đặc tả. Bảng thông số thiết bị thương mại dành cho Chương 2. Không thay các đoạn giải thích chức năng hoặc trình tự ngắn bằng bảng chỉ để trông có cấu trúc. Không lặp toàn bộ nội dung một bảng trong đoạn ngay sau bảng.
9. **Nguồn đi cùng nội dung.** Đặt trích dẫn cuối câu/đoạn hoặc cuối từng gạch ý có dữ kiện. Một nguồn có thể hỗ trợ cả danh sách ngắn nếu giới thiệu rõ và tất cả các ý nằm đúng phần nguồn đó. Không bỏ trích dẫn khi đổi đoạn văn thành gạch ý; không thêm dòng “phần liên hệ là phân tích của đề tài” vào trích dẫn, thay bằng lời văn tự nhiên khi thật sự có suy luận.
10. **Lời chuyển ngắn và có tác dụng.** Kết nối các phần bằng vấn đề tiếp theo cần giải quyết, không lặp “phần tiếp theo sẽ trình bày...” ở mọi tiểu mục. Kết luận tổng hợp kết quả, không kể lại toàn bộ thao tác biên soạn.

### Rà soát văn phong trước khi hoàn thành

- Có sự kết hợp giữa đoạn văn, gạch ý và bước đánh số, phù hợp nội dung thực tế.
- Đọc riêng các đoạn đầu/cuối mục: không lặp cùng cấu trúc và cùng lời tự giới hạn.
- Mỗi gạch ý có tên rõ và phần giải thích; các ý trong cùng nhóm cùng cấp nghĩa.
- Không có ghi nhận thao tác đọc nguồn, tải PDF hoặc kiểm kê trong thân báo cáo.
- Không dùng việc thiếu thông số làm nội dung chính của cả tiểu mục; vẫn giải thích được đại lượng, vai trò kỹ thuật và hướng đánh giá theo D.2.
- Viết lại toàn bộ phần diễn giải sau khi cập nhật quy tắc; không chỉ thêm vài gạch đầu dòng vào bản cũ.

## B.5. Giọng văn khách quan — cập nhật 24/10/2026

Người viết đồng thời là người phân tích và thiết kế hệ thống. Thân báo cáo trình bày đối tượng, cách phân tích, lựa chọn có căn cứ và phương pháp đánh giá của đồ án; không dùng giọng hướng dẫn hoặc giao nhiệm vụ cho một người thiết kế khác. Quy tắc này áp dụng cho tất cả các mục, đoạn dẫn, gạch ý, bảng và kết luận.

- **Trình bày trực tiếp, dứt khoát.** Với kiến thức và dữ kiện đã có căn cứ, nêu thẳng đặc điểm, chức năng hoặc quan hệ kỹ thuật; đặt trích dẫn ở cuối câu/đoạn. Không kể lại nguồn bằng các khuôn “tài liệu tổng quan đề cập…”, “nguồn xem X là…”, “nghiên cứu coi…”, “đây là thông tin do… công bố” khi tên nguồn không giúp giải thích nội dung. Ví dụ: viết “Đầu cáp là một trong các vị trí giám sát sự cố hồ quang trong tủ điện”, thay cho “Tổng quan kỹ thuật của tác giả… xem đầu cáp là một vị trí điển hình…”.
- **Không kể cách dùng hoặc thu thập nguồn trong thân báo cáo — yêu cầu ngày 25/10/2026:** Không viết “nội dung sử dụng thông tin dự án”, “nguồn dự án xác định”, “thông tin dự án đã đọc”, “nhà thầu liệt kê”, “phần chức năng được giải thích theo tài liệu” hoặc các câu tương tự. Viết thẳng chủ thể kỹ thuật và dữ kiện, đặt `[n]` cuối câu. Tác giả, nơi công bố, URL, ngày truy cập và thao tác đối chiếu nằm ở danh mục tài liệu, không trở thành nội dung lập luận. Ví dụ: “Gói cung cấp thiết bị của ABB cho dự án mở rộng năm 2018 gồm… [n]”, không viết “Theo thông báo đã đọc, nguồn cho biết…”. Quy tắc áp dụng cho mọi chương về sau.
- **Không xóa giới hạn kỹ thuật khi bỏ lối kể nguồn:** Giữ rõ phạm vi hợp đồng hoặc thiết kế, mốc thời gian, điều kiện thử và trạng thái chưa xác minh. Viết trực tiếp “Cấu hình bảo vệ hiện tại chưa được xác minh”, không kể quy trình tìm tài liệu. Tập trung giới hạn hiện trạng vào mục riêng, tránh lặp sau mỗi dữ kiện.
- **Chắc chắn theo đúng căn cứ.** Giữ tên tác giả khi phân tích công trình cụ thể, điều kiện thử nghiệm và kết quả riêng; giữ “hồ sơ quy định” khi phân biệt yêu cầu thiết kế với hiện trạng vận hành. Không biến phương án thành cấu hình đã chọn, yêu cầu thành kết quả đạt được hoặc khả năng thành kết luận tuyệt đối. Giới hạn dữ liệu được nêu gọn tại đúng mục, không rải lời dè dặt vào mọi câu.
- **Dùng chủ thể kỹ thuật cụ thể.** Viết “điện áp được chia thành…”, “thời gian phản hồi gồm…”, “cảm biến thu nhận…” hoặc “phương pháp đánh giá xét…”. Không dùng “đề tài này”, “đồ án này”, “đề tài tập trung”, “đồ án phân tích”, “đề tài nhận thấy”, “đối với đề tài” và các cách tự quy chiếu tương tự trong thân báo cáo. Giữ nguyên tên đề tài ở đầu file và tên tài liệu nguồn.
- **Dẫn phạm vi từ bối cảnh có căn cứ.** Nêu điều kiện ứng dụng, nguy cơ hoặc nhu cầu kỹ thuật trước khi xác định phạm vi. Ví dụ: “Nguy cơ hư hỏng và mất an toàn do hồ quang nội bộ đặt ra nhu cầu phát hiện sớm sự cố trong tủ điện. Từ bối cảnh đó, phạm vi nghiên cứu tập trung vào phát hiện chớp hồ quang điện trong tủ điện hạ thế và trung thế.” Không bịa thống kê về tình hình thực tế để tạo câu dẫn, không lặp máy móc mẫu này ở mọi mục.
- **Giải thích lý do phân chia.** Thay “cần tách ba loại điện áp” bằng “điện áp được chia thành ba nhóm: điện áp hệ thống, điện áp tín hiệu và nguồn phụ trợ. Cách phân chia này làm rõ điều kiện làm việc và giao diện của từng khối”. Câu viết thể hiện phân tích đang được trình bày và mục đích của nó.
- **Bỏ giọng sai khiến.** Không dùng các cách viết như “cần xác định”, “cần kiểm tra”, “phải lựa chọn”, “người thiết kế cần” để giao công việc của đồ án. Thay bằng nội dung thực chất: đại lượng được phân tích, yếu tố chi phối, phương pháp đánh giá hoặc trạng thái thông số.
- **Không thay từ máy móc.** Viết lại cả câu hoặc đoạn để giữ đúng ý và thời điểm. Không chỉ thay mọi chữ “cần” bằng “đồ án thực hiện”. Không biến một thông số chưa xác lập thành lựa chọn đã có, hoặc một phép đánh giá dự kiến thành kết quả đã đo.
- **Phân biệt phân tích với kết quả thực hiện.** Có thể dùng hiện tại để trình bày cách phân loại và giải thích. Chỉ dùng “đã đo”, “đã kiểm tra”, “đã lựa chọn” khi có dữ liệu chứng minh. Với nội dung chưa triển khai, nêu rõ cơ sở lựa chọn hoặc phương pháp dự kiến mà không viết như mệnh lệnh.
- **Giữ nguyên tính chất của yêu cầu nguồn.** Câu “hồ sơ thiết kế quy định…” hoặc “hãng yêu cầu…” được dùng khi mô tả đúng tài liệu và có trích dẫn; không chuyển thành lời cam kết nguyên mẫu đã đáp ứng. Quy tắc giọng văn không thay đổi các giới hạn bằng chứng.

| Cách viết loại bỏ trong báo cáo | Cách diễn đạt thay thế |
|---|---|
| Cần tách ba loại điện áp | Điện áp trong bài toán được chia thành ba nhóm… |
| Cần phân biệt độ trễ và độ rộng xung | Độ trễ thể hiện…, còn độ rộng xung thể hiện… |
| Cần xác định băng thông trước khi chọn tần số lấy mẫu | Việc lựa chọn tần số lấy mẫu dựa trên băng thông tín hiệu và phương pháp xử lý… |
| Khi đánh giá cần ghi rõ nguồn sáng và khoảng cách | Điều kiện đánh giá gồm loại nguồn sáng, khoảng cách và hướng thu… |
| Cần kiểm tra riêng từng tín hiệu và tổ hợp hợp lệ | Phương pháp đánh giá xét từng tín hiệu riêng và tổ hợp được định nghĩa hợp lệ… |
| Các thông số còn cần làm rõ | Các thông số chưa xác lập gồm…; cơ sở xác lập là… |

Rà soát toàn văn sau khi biên soạn: tìm các cụm “cần”, “phải”, “nên”, “yêu cầu người thiết kế”, đọc từng câu trong ngữ cảnh và chỉnh giọng giao việc. Không xóa các thuật ngữ có nghĩa chuyên môn như “tính cấp thiết” hoặc bóp méo yêu cầu bắt buộc của hồ sơ/hãng. Chỉ dẫn thao tác trong chính Design rules là hướng dẫn biên soạn, không phải câu văn để đưa nguyên vào báo cáo.

# C. Quy tắc nguồn và kiểm chứng

## C.1. Kiểm kê lại nguồn

- Kiểm kê tên tệp thực tế trong `Tham khảo/`; dùng tiêu đề và thông tin trong tài liệu để nhận dạng. Không sao chép số thứ tự tên tệp từ bản cũ vì có những tên không khớp bộ nguồn hiện tại.
- Đọc các nguồn liên quan trước khi viết; đối với nguồn không dùng, chỉ cần xác định phạm vi. Không cần trích tất cả tài liệu chỉ vì có sẵn.
- Ưu tiên bài báo gốc cho hiện tượng và phương pháp; tài liệu chủ đầu tư/đơn vị vận hành cho nhà máy; Technical Bulletin/User Guide chính hãng cho sản phẩm; nguồn cơ quan nhà nước, EVN hoặc công bố doanh nghiệp để xác minh bối cảnh.
- Google là công cụ tìm kiếm, không phải nguồn trích dẫn. Mở trang hoặc PDF gốc trước khi dùng; không dựa hoàn toàn vào đoạn trích tìm kiếm, ảnh thu nhỏ hay phần trả lời tự động.
- Khi tìm sự cố hồ quang trong tủ hạ thế tại Việt Nam, kiểm tra riêng điện áp, loại thiết bị, vị trí hồ quang và diễn biến sự cố. Không đổi một tin cháy nổ, chập điện hoặc tủ xuống cấp thành vụ chớp hồ quang nếu nguồn chưa xác nhận. Nếu chưa có trường hợp đủ căn cứ, nêu giới hạn của các nguồn đã kiểm tra; không khẳng định Việt Nam không có sự cố. Ví dụ quốc tế dùng hồ sơ có điện áp và diễn biến rõ, ưu tiên cơ quan điều tra an toàn lao động.
- Thông tin về tủ điện dân dụng tại Cao Xanh – Hà Khánh A là bối cảnh độc lập với Nhà máy HEINEKEN Vũng Tàu ở mục 1.3; chỉ dùng để minh họa tình trạng tủ hạ thế xuống cấp, không xem là vụ hồ quang đã được xác nhận.
- Không dùng đường dẫn tìm được nhưng chưa đọc làm bằng chứng cho một kết luận kỹ thuật. Nếu liên kết lỗi, tìm bản chính thức khác hoặc bản sao cùng tài liệu có thể kiểm tra xuất xứ; ghi đúng nơi truy cập.
- Nguồn riêng về Nhà máy HEINEKEN Vũng Tàu chỉ phục vụ phần 1.3, kết luận tổng hợp phù hợp và danh mục tài liệu; không đưa lên phần 1.1–1.2. Trong danh mục hiện tại, các nguồn này mang số [19], [20] và [21]; nếu đánh lại số thì vẫn giữ ranh giới theo bản chất nguồn.

## C.2. Đánh số nguồn và trích dẫn trong văn bản — cập nhật 25/10/2026

- Trong thân báo cáo, bảng và ghi nguồn hình, chỉ dùng số nguồn dạng `[1]`, `[2]`…; bỏ mã TL/W và thông tin mục, trang khỏi dấu trích dẫn. Mỗi ngoặc vuông chứa một số; câu có nhiều nguồn dùng `[1], [2]`. Đặt số nguồn cuối câu hoặc đoạn có dữ kiện, giữ thống nhất vị trí dấu câu.
- Đánh số theo thứ tự xuất hiện lần đầu trong toàn báo cáo; cùng một tài liệu luôn dùng lại cùng một số. Các chương sau tiếp tục danh mục chung, không bắt đầu lại từ `[1]`. Khi thêm nguồn làm thay đổi thứ tự, đồng bộ số nguồn và danh mục; việc này không cho phép viết lại nội dung đã khóa.
- Ghi tác giả, tên nguồn, năm, DOI/URL và ngày truy cập tại phần `Tài liệu tham khảo` cuối báo cáo. Một mục tương ứng một tài liệu hoặc trang web; không gộp nhiều trang web độc lập thành một số.
- Vẫn kiểm tra chính xác mục, hình, trang in và trang PDF khi đọc nguồn. Nếu cần giữ vị trí tra cứu chi tiết, đưa vào mục tài liệu tương ứng ở danh mục cuối báo cáo; không chèn chuỗi tra cứu dài vào thân bài. Trang PDF đếm từ 1.
- Nếu một câu có nhiều khẳng định mà nguồn chỉ chứng minh một phần, tách câu hoặc bổ sung nguồn phù hợp.
- Phân biệt nội dung nguồn với suy luận của tác giả. Khi trình bày suy luận, nêu trực tiếp quan hệ giữa căn cứ và nhận định, chẳng hạn “Từ các đặc điểm trên, phạm vi giám sát phụ thuộc vào…”. Không dùng lối tự quy chiếu như “đề tài nhận thấy”. Không dùng nhãn suy luận để hợp thức hóa chi tiết giả định về nhà máy.
- Không tạo DOI, tác giả, năm, số trang hoặc kết quả thử nghiệm từ trí nhớ. Không chép nguyên đoạn dài của nguồn.

## C.3. Tài liệu tham khảo ở cuối báo cáo

Đặt phần `# Tài liệu tham khảo` sau chương cuối cùng, dùng chung cho toàn báo cáo. Khi mới có Chương 1, đặt tạm phần này ở cuối file hiện tại; khi ghép các chương, chuyển xuống cuối báo cáo. Mỗi mục bắt đầu bằng `[n]` và khớp số trích dẫn trong nội dung. Ghi đủ tác giả/cơ quan, tên tài liệu, năm hoặc phiên bản, tạp chí/đơn vị xuất bản, DOI nếu có; giữ liên kết tệp nguồn để tra cứu. Nguồn trực tuyến ghi URL và ngày truy cập thực tế; không bịa ngày xuất bản.

Mẫu:

`[1] Tác giả, “Tên tài liệu,” tên tạp chí/đơn vị xuất bản, năm, trang. DOI: ...`

`[2] Cơ quan, “Tên trang hoặc tài liệu,” ngày xuất bản nếu có. [Trực tuyến]. Có tại: [Trang nguồn](URL). [Truy cập ngày dd/mm/yyyy].`

Mọi số trong nội dung phải tồn tại trong danh mục; mọi nguồn trong danh mục phải thực sự được dùng. Quy tắc số nguồn này thay thế các mẫu mã TL/W hoặc trích dẫn kèm mục/trang trong những hướng dẫn cũ bên dưới.

# D. Đặc tả chi tiết nội dung Chương 1

## D.0. Mở đầu chương

Viết một đoạn xác định mục tiêu và trình tự của chương. Lời dẫn gợi ý, có thể điều chỉnh câu chữ nhưng giữ ý:

> Chương này trình bày bối cảnh và tính cấp thiết của bài toán phát hiện chớp hồ quang điện trong hệ thống điện hạ thế và trung thế. Trên cơ sở xác định đối tượng nghiên cứu, chương phân tích các yêu cầu kỹ thuật ban đầu, khảo sát hệ thống tủ điện tại Nhà máy HEINEKEN Vũng Tàu và phân tích nhu cầu giám sát hồ quang điện. Các nội dung này tạo căn cứ cho việc nghiên cứu cơ sở lý thuyết và lựa chọn linh kiện ở chương tiếp theo.

## D.1. `# 1.1. Tổng quan bài toán phát hiện chớp hồ quang điện`

### `## 1.1.1. Đặt vấn đề`

- `### 1.1.1.1. Đối tượng nghiên cứu`: giới thiệu tủ điện hạ thế, trung thế; cấu tạo chung và chức năng các bộ phận. Hình minh họa được giải thích bằng tên tiếng Việt kèm tiếng Anh khi có nhãn gốc.
- `### 1.1.1.2. Bối cảnh ứng dụng`: trình bày nguy cơ, nhu cầu phát hiện và cảnh báo; giới thiệu vai trò node–gateway–máy chủ và các nội dung đánh giá nguyên mẫu.

- Trả lời: đối tượng chịu tác động là gì, ở đâu trong hệ thống, chức năng và cấu trúc nào liên quan đến bài toán?
- Giới thiệu trạm biến áp và phân phối hạ thế, trung thế; thu hẹp đến tủ điện, thiết bị đóng cắt, thanh cái, đầu cáp và các khoang cần quan tâm theo nguồn.
- Làm rõ đơn vị không gian: toàn trạm, dãy tủ, khoang tủ; chưa có khảo sát thì không tự chốt vị trí lắp của đồ án.
- Dùng 5W1H để rà soát tính đầy đủ, chọn câu hỏi phù hợp; không tạo thông tin chỉ để đủ sáu câu hỏi.
- Hình nếu dùng: ảnh/sơ đồ tủ hoặc trạm trong nguồn đã xác minh; phải nói rõ đó là minh họa cấu trúc, không phải nhà máy ở 1.3 nếu không cùng địa điểm.
- Lồng tính cấp thiết vào bối cảnh ứng dụng: từ đối tượng chịu tác động và hậu quả, trình bày mục đích phát hiện sớm, phân biệt tác động gây nhầm và đánh giá chuỗi phản hồi. Không tách thành tiểu mục riêng.

### `## 1.1.2. Hiện tượng hồ quang điện và chớp hồ quang điện`

- `### 1.1.2.1. Khái niệm và tác động`: giải thích thuật ngữ, phân biệt hồ quang đóng cắt và hồ quang sự cố; trình bày hậu quả, hình thử nghiệm và quan hệ năng lượng–thời gian với điều kiện nguồn đầy đủ.
- `### 1.1.2.2. Các trường hợp thực tế`: chia thành **a) Tại Việt Nam** và **b) Trên thế giới**. Ưu tiên các trường hợp chớp hồ quang trong tủ hạ thế có căn cứ. Phần Việt Nam nêu đúng giới hạn dữ liệu khi chưa xác định được vụ phù hợp; không lấy ví dụ khác điện áp hoặc khác hiện tượng để thay thế mà không giải thích.
- Định nghĩa, thống nhất thuật ngữ electric arc, arc fault, arc flash theo nguồn; giải thích phạm vi đề tài.
- Trình bày nguyên nhân, điều kiện hình thành và các biểu hiện liên quan đến phát hiện; nêu tác động đến thiết bị, con người và hoạt động nhà máy.
- Phân biệt hồ quang đóng cắt được thiết kế kiểm soát với sự cố ngoài vùng chức năng đó.
- Không đưa nghiên cứu hồ quang nối tiếp dân dụng AC hoặc định vị hồ quang DC/PV vào phần ví dụ thực tế của mục 1.1.2. Những nghiên cứu còn được dùng ở mục khác giữ đúng phạm vi, không chuyển nguyên chỉ số phát hiện sang bài toán chớp hồ quang trong tủ điện.
- Chỉ trình bày nền tảng vừa đủ; cơ chế chi tiết, công thức và thuật toán dành cho Chương 2.
- Lồng số liệu minh chứng vào phần giải thích hiện tượng và hậu quả: ảnh hư hỏng, điều kiện thử và quan hệ năng lượng–thời gian được đặt cạnh nội dung chuyên môn tương ứng.
- Mỗi số liệu ghi rõ đại lượng, đơn vị, phạm vi và điều kiện nguồn. Không biến thử nghiệm thành thống kê tai nạn hoặc suy ra tần suất khi không có mẫu số, thời gian quan sát và phương pháp phù hợp.
- Nếu thiếu thống kê tần suất, nêu giới hạn ngắn tại đoạn minh chứng, không biến phần này thành nhật ký nguồn. Kết nối hậu quả với nhiệm vụ phát hiện và lời dẫn sang 1.2.

Phần 1.1 có hai tiểu mục 1.1.1 và 1.1.2, mỗi tiểu mục chia tiếp thành hai heading cấp 3 như trên; không tạo heading 1.1.3. Các mục a), b) trong 1.1.2.2 dùng nhãn in đậm, không tạo thêm cấp heading. Khi sắp xếp lại nội dung, giữ trích dẫn sát nhận định và số hình liên tục theo thứ tự xuất hiện.

**Lời dẫn sang 1.2:**

> Bối cảnh ứng dụng và hậu quả của sự cố đặt ra các yêu cầu về thu nhận tín hiệu, độ nhạy và thời gian phản hồi của bộ phát hiện. Các yêu cầu này là cơ sở lựa chọn phương án thiết kế hệ thống nhúng.

## D.2. `# 1.2. Phân tích yêu cầu kỹ thuật của bài toán`

Mỗi tiểu mục phải có: đại lượng/đối tượng xét → ý nghĩa → căn cứ → giá trị hoặc giới hạn nếu đủ bằng chứng → cách đánh giá. Chưa xác định bộ tiêu chuẩn áp dụng không có nghĩa lĩnh vực không có tiêu chuẩn. Nếu Đồ án 1–2 không có trong vùng nguồn được phép, không viện dẫn nội dung giả định của chúng.

**Cập nhật theo yêu cầu người dùng ngày 25/10/2026:** Giữ sáu mục điện áp, tần số, dòng điện, độ nhạy, thời gian phản hồi và chu kỳ lấy mẫu; thêm mục 1.2.7 về truyền thông và cảnh báo, chuyển tổng hợp thành 1.2.8. Mỗi phần đi từ yêu cầu thực tế đến căn cứ tiêu chuẩn/nghiên cứu có trích dẫn `[n]`, sau đó nêu phạm vi nguyên mẫu. Viết ngắn gọn, giải thích thuật ngữ và số liệu, không liệt kê tiêu chuẩn không liên quan. Phân biệt yêu cầu tiêu chuẩn, kết quả nghiên cứu, ví dụ tính toán và lựa chọn của nhóm. Chỉ viện dẫn điều khoản chi tiết đã đọc; trang giới thiệu tiêu chuẩn chỉ dùng để xác nhận phạm vi. Không suy ra nguyên mẫu đạt chuẩn công nghiệp từ phép thử mô hình.

### `## 1.2.1. Yêu cầu về điện áp`
Phân biệt điện áp hệ thống giám sát, tín hiệu đo và nguồn phụ trợ. Không suy ra cảm biến hoặc vi điều khiển tiếp xúc trực tiếp với điện áp trung thế. Chưa có căn cứ không chốt dải điện áp nguyên mẫu.

### `## 1.2.2. Yêu cầu về tần số`
Xác định tần số hệ thống điện trong phạm vi có nguồn; phân biệt tần số điện lưới, dải tần tín hiệu cần xét và tần số lấy mẫu. Giải thích vai trò, không chỉ liệt kê con số.

### `## 1.2.3. Yêu cầu về dòng điện`
Làm rõ dòng điện được theo dõi, vai trò phát hiện/xác nhận, vị trí trong chuỗi đo nếu đã xác định. Phân biệt dòng định mức, dòng sự cố và tín hiệu thứ cấp. Chưa tự chọn ngưỡng, tỷ số biến dòng hay định mức đầu ra.

### `## 1.2.4. Yêu cầu về độ nhạy`
Định nghĩa độ nhạy đối với tín hiệu nào và trong điều kiện gì. Phân biệt ngưỡng quang, độ nhạy cảm biến và xác suất phát hiện. Nếu chỉ tiêu chưa định lượng, trình bày những dữ kiện cần có để xác định; không viết “độ nhạy cao” như tiêu chí hoàn chỉnh.

### `## 1.2.5. Yêu cầu về thời gian phản hồi`
Đánh giá thời gian từ kích thích tham chiếu đến khi cảnh báo hiển thị trên máy chủ; tách các khoảng thu nhận, xử lý tại node và truyền, hiển thị qua gateway–máy chủ. Nêu rõ mốc đo và cơ sở thời gian. Không đưa rơ-le, cơ cấu máy cắt hoặc thời gian loại trừ sự cố vào yêu cầu nguyên mẫu chỉ phát hiện và cảnh báo. Nếu dùng xung trong phép thử, phân biệt độ rộng xung với độ trễ phản hồi.

### `## 1.2.6. Yêu cầu về chu kỳ lấy mẫu`
Xác định kênh nào thực sự lấy mẫu và nhu cầu thông tin của kênh đó. Nếu kiến trúc chưa chọn, để đây là yêu cầu cần xác định theo cơ chế thu nhận, không mặc định mọi kênh dùng ADC. Khi có số liệu, kiểm tra đơn vị và quan hệ `f_s = 1/T_s`; không chọn tần số chỉ bằng cách gấp đôi tần số điện lưới.

### `## 1.2.7. Yêu cầu về truyền thông và cảnh báo`
Giải thích đường truyền node → gateway → máy chủ và vai trò từng khối. Trình bày thông tin nhận diện node, trạng thái sự kiện, cách đối chiếu thông tin nhận và trạng thái kết nối. Không mặc định dùng Internet, đám mây hoặc chốt giao thức. Chỉ có phát hiện và cảnh báo, không điều khiển cắt điện.

### `## 1.2.8. Tổng hợp yêu cầu kỹ thuật ban đầu`
Bảng bắt buộc mang tên **Các yêu cầu thiết kế được lựa chọn cho nguyên mẫu**, gồm bốn cột: **Nội dung | Yêu cầu nhóm lựa chọn | Căn cứ lựa chọn | Cách kiểm tra**. Trước bảng giải thích đây là phạm vi nhóm lựa chọn theo điều kiện đồ án tốt nghiệp, không phải tuyên bố đáp ứng đầy đủ tiêu chuẩn công nghiệp. Yêu cầu chức năng có thể được xác định trước; thông số chưa đủ căn cứ được cụ thể hóa ở Chương 2, không đặt số tùy ý. Dùng căn cứ độc lập với hồ sơ nhà máy. Không dùng thông số thiết bị thương mại làm chỉ tiêu mặc định; khảo sát sản phẩm dành cho Chương 2. Việc đối chiếu trường hợp nhà máy được thực hiện tại chính 1.3.

**Lời dẫn sang 1.3:**

> Sau phần phân tích yêu cầu kỹ thuật, mục 1.3 trình bày một trường hợp nghiên cứu riêng ở cấp hệ thống. Kết luận chương tổng hợp phạm vi và các yêu cầu làm cơ sở cho Chương 2.

## D.3. `# 1.3. Khảo sát hệ thống tủ điện tại Nhà máy HEINEKEN Vũng Tàu`

**Phạm vi được người dùng lựa chọn ngày 25/10/2026:** Thay toàn bộ trường hợp nhà máy cũ bằng HEINEKEN Vũng Tàu. Giữ nguyên mục 1.1 và 1.2; chỉ đồng bộ phần mở đầu, kết luận, nguồn và ảnh liên quan đến thay đổi này. Không viết Chương 2 trong đợt sửa này.

### Giới hạn bằng chứng

- Thông cáo HEINEKEN ngày 24/9/2022 xác nhận địa điểm, quy mô tại thời điểm khánh thành và cung cấp ảnh đúng nhà máy.
- Thông báo ABB ngày 21/5/2018 xác nhận phạm vi hợp đồng có tủ 22 kV, tủ 0,4 kV và các thiết bị liên quan; không biến thông báo hợp đồng thành danh mục hoàn công hoặc cấu hình hiện tại.
- Sea Power liệt kê hạng mục lắp đặt tủ trung thế ABB, máy biến áp, máy phát và tủ hòa đồng bộ tại dự án. Không suy ra mã tủ, tỷ số biến áp, cấu hình bảo vệ hoặc sơ đồ đấu nối từ danh mục ngắn.
- Phần nguy cơ và phương án giám sát là phân tích dựa trên tài liệu kỹ thuật độc lập; không nhận là quan sát hiện trường hoặc hệ thống đã lắp tại nhà máy. Chưa có bằng chứng HEINEKEN Vũng Tàu sử dụng 1S23, cảm biến quang, logic AND hoặc một ngưỡng phát hiện cụ thể.

### Bố cục

- `## 1.3.1. Giới thiệu nhà máy`: một đoạn ngắn về địa điểm, quy mô theo mốc nguồn và bối cảnh cấp điện; không chia nhỏ. Giữ ảnh đúng nhà máy, tên hình và nguồn, không thêm giải thích ảnh toàn cảnh dài dòng.
- `## 1.3.2. Phạm vi hệ thống tủ điện`: viết liền mạch, không chia nhỏ hoặc lập bảng chỉ để liệt kê nhà cung cấp. Tập trung hai nhóm tủ 22 kV và 0,4 kV, vai trò và giới hạn đối tượng giám sát. Trạm điện, máy biến áp và tủ hòa đồng bộ chỉ nêu ngắn để làm rõ phạm vi.
- `## 1.3.3. Nhu cầu giám sát hồ quang điện`: chia `### 1.3.3.1. Các vị trí có nguy cơ` và `### 1.3.3.2. Ý nghĩa của phát hiện và cảnh báo`. Nhận định nguy cơ không đồng nghĩa nhà máy đã xảy ra sự cố.
- `## 1.3.4. Liên hệ với hệ thống thiết kế`: chia `### 1.3.4.1. Chuỗi phát hiện và cảnh báo` và `### 1.3.4.2. Nội dung đánh giá nguyên mẫu`. Node phát hiện, gateway chuyển thông tin, máy chủ hiển thị; không điều khiển cắt điện.
- Theo yêu cầu mới nhất, bỏ toàn bộ mục 1.3.5; mục 1.3 kết thúc tại 1.3.4. Không tạo lại mục kiểm chứng hoặc danh sách thông tin chưa xác minh. Chương 2 khảo sát 1S23 như thiết bị tham khảo độc lập; không mặc định thiết bị được dùng tại nhà máy.

## D.4. `# 1.4. Kết luận chương`

Viết khoảng 2–3 đoạn: kết quả làm rõ bài toán; sáu nhóm yêu cầu; ý nghĩa và giới hạn của trường hợp nhà máy; liên hệ với cơ sở lý thuyết và thiết kế ở Chương 2. Không khảo sát sản phẩm, không bổ sung thông số hoặc chức năng mới. Chương 2 dành cho cơ sở lý thuyết, khảo sát thiết bị thương mại và phân tích lựa chọn linh kiện.

**Đoạn chuyển sang Chương 2:**

> Chương 1 trình bày bối cảnh, phạm vi nghiên cứu và các yêu cầu kỹ thuật ban đầu của bài toán phát hiện chớp hồ quang điện. Trên cơ sở đó, Chương 2 trình bày lý thuyết về phát hiện, thu nhận và xử lý tín hiệu, đồng thời phân tích, lựa chọn linh kiện. Những thông số chưa xác lập được xem xét cùng phương án thiết kế và điều kiện đánh giá của hệ thống.

# E. Nguồn khởi đầu cho việc nghiên cứu tiếp

Các URL sau là đầu mối để mở và kiểm tra lại, không phải danh mục tham khảo đã hoàn chỉnh của báo cáo mới. Chỉ đưa vào danh mục cuối khi đã đọc và thực sự sử dụng.

| Đầu mối | Vai trò và trạng thái |
|---|---|
| Các bài *Aspects of arc-flash protection and prediction*, *Electric arc explosions—A review*, *Explainable artificial intelligence modeling of internal arc in a medium voltage switchgear based on different CFD simulations* trong `Tham khảo/` | Ưu tiên rà soát cho hiện tượng, hậu quả và hình; kiểm tra tác giả, năm, hình và trang từ chính file. |
| Các bài phát hiện hồ quang AC, DC/PV và triển khai nhúng trong `Tham khảo/` | Nguồn hỗ trợ; phải ghi đúng loại sự cố và điều kiện nghiên cứu. |

Nếu không thể truy cập hoặc xác thực một đầu mối, tiếp tục hoàn thiện phần có bằng chứng và báo giới hạn; không dựng quy trình vận hành thực tế cho đủ mục. Việc thay nhà máy chỉ thực hiện theo yêu cầu người dùng; trường hợp hiện tại đã được lựa chọn rõ là HEINEKEN Vũng Tàu.

# F. Quy tắc ảnh và xử lý `hinh_minh_hoa/`

## F.1. Nguồn ảnh hợp lệ

- Chỉ dùng ảnh/hình đã có trong tài liệu nguồn hoặc hình tìm qua Google rồi truy về trang gốc có thể kiểm chứng, ưu tiên doanh nghiệp/nhà sản xuất/cơ quan/nghiên cứu gốc.
- Cấm tạo ảnh bằng AI, tạo lại hình bằng AI, dùng ảnh AI làm ảnh thực tế, tự vẽ hình thay thế để lấp chỗ thiếu. Với yêu cầu này, không dựng ảnh/sơ đồ bằng Python, SVG, Mermaid hoặc công cụ khác; dùng bảng/văn bản nếu chưa có hình gốc phù hợp.
- Được cắt đúng vùng hình từ PDF, trích ảnh nhúng, tải ảnh gốc, đổi định dạng và điều chỉnh kích thước để đọc được. Không thêm hoặc xóa thành phần nội dung, sửa nhãn, trục, số liệu; nếu hình khó đọc thì tìm bản tốt hơn hoặc bỏ.
- Ghi rõ thao tác cắt, nơi xuất xứ, phạm vi minh họa. Giữ các nhãn và chú giải cần thiết. Không gán ảnh phòng thử hay nhà máy khác cho nhà máy khảo sát.
- Tôn trọng điều kiện sử dụng và ghi công của nguồn. Chỉ trích phần hình phù hợp, không sao chép hàng loạt trang tài liệu.

## F.2. Kế hoạch hình dự kiến

Không ấn định số lượng bắt buộc. Khoảng 3–5 hình có ích là định hướng nếu đủ nguồn và phù hợp nội dung. Ảnh thiết bị thương mại dành cho Chương 2, không chèn để kéo dài Chương 1.

| Phần | Loại hình có thể dùng | Điều kiện |
|---|---|---|
| 1.1 | Cấu trúc tủ/trạm; ảnh thử nghiệm hoặc hậu quả hồ quang | Đúng ngữ cảnh, chú thích điều kiện, không lạm dụng ảnh hàn điện. |
| 1.2 | Hình gốc về quan hệ tín hiệu hoặc thời gian nếu thật sự hỗ trợ lập luận | Không suy thành yêu cầu nguyên mẫu; thiếu thì dùng bảng. |
| 1.3 | Ảnh chính thức Nhà máy HEINEKEN Vũng Tàu; ảnh tủ/sơ đồ chỉ dùng khi xác minh đúng dự án | Ảnh toàn cảnh chỉ chứng minh bối cảnh, không chứng minh có thiết bị phát hiện cụ thể. |

**Hình mục 1.3 cập nhật ngày 25/10/2026:** Hình 1.7 dùng ảnh toàn cảnh đầu tiên trong thông cáo khánh thành năm 2022 của HEINEKEN Việt Nam. Không dùng ảnh Campuchia trong bài ABB; không gán ảnh tủ sản phẩm chung thành ảnh tại nhà máy. Gỡ ảnh và tài liệu độc lập của trường hợp nhà máy cũ theo yêu cầu; không xóa nguồn đã khóa tại mục 1.1 hoặc tài liệu 1S23 dành cho Chương 2.

**Ảnh mục 1.3 — yêu cầu mới nhất:** Chỉ chèn ảnh hoặc sơ đồ đã xác minh thuộc chính Nhà máy HEINEKEN Vũng Tàu. Không có ảnh đúng đối tượng thì bỏ, không dùng ảnh sản phẩm hoặc sơ đồ ứng dụng chung của hãng để thay thế. Đã gỡ hai hình minh họa chung khỏi 1.3.2–1.3.3; các tệp có thể giữ làm tư liệu Chương 2, không xem là hình hiện trường nhà máy.

## F.3. Cú pháp và chú thích

Mục 1.3.1 giới thiệu ngắn nhà máy, không chia tiểu mục. Ảnh toàn cảnh Hình 1.7 chỉ giữ tên và nguồn; các hình kỹ thuật khác vẫn có lời giải thích ngắn, đủ ý.

**Giải thích hình và đặt tên hình — cập nhật theo yêu cầu người dùng ngày 25/10/2026:**

- Mỗi hình có đoạn giải thích ngắn ngay trước hoặc sau hình, thường 2–3 câu: hình thể hiện gì, chi tiết nào đáng chú ý và chi tiết đó giúp hiểu nội dung đang trình bày như thế nào. Chỉ rõ vị trí, màu sắc hoặc nhãn khi cần để người đọc đối chiếu; dùng từ dễ hiểu, không chỉ viết “Hình ... minh họa ...” rồi bỏ qua ý nghĩa.
- Tên hình dưới ảnh chỉ gồm số hình và tên nội dung ngắn gọn, ưu tiên một dòng. Không nhét phần giải thích cấu tạo, diễn biến, dịch nhãn, địa điểm hay điều kiện thử thành một đoạn dài trong tên hình. Ví dụ: “Hình 1.2. Hồ quang giữa các tiếp điểm máy cắt.” Phần giải thích đặt trong thân bài; nguồn đặt ở dòng riêng.
- Hình nhiều ảnh thành phần có lời giải thích ngắn theo từng vị trí hoặc nhãn để người đọc nhận ra từng trường hợp. Giữ các điều kiện thử và giới hạn có ý nghĩa trong đoạn giải thích hoặc ghi nguồn, không loại bỏ để rút ngắn tên hình.
- Áp dụng quy tắc cho hình mới và phần được người dùng yêu cầu sửa; quy tắc này không tự mở khóa các nội dung đã chốt tại mục 1.1.

Đánh số liên tục theo thứ tự xuất hiện, không giữ số cũ nếu đã đổi bố cục. Tên file không dấu, gọn, phản ánh nội dung; đường dẫn tương đối từ báo cáo:

```markdown
![Mô tả chính xác nội dung hình](hinh_minh_hoa/Hinh_1_1_Mo_ta_noi_dung.png)

*Hình 1.1. Tên hình ngắn gọn.*

*Nguồn: [1]. Cắt từ tài liệu, giữ nguyên nhãn và số liệu. Điều kiện thử hoặc giới hạn liên quan nếu có.*
```

Trong ghi nguồn hình, thay [1] bằng số tài liệu tương ứng; chi tiết số hình, trang in/PDF được đặt tại mục tài liệu đó trong danh mục cuối báo cáo. Với ảnh web, ghi tác giả/cơ quan, tiêu đề, URL trang gốc và ảnh gốc nếu truy được, ngày truy cập và thông tin giấy phép tại danh mục. Không trích trang kết quả Google làm nguồn ảnh. Đối với ảnh sản phẩm không có số hình, mô tả vị trí trên trang trong danh mục thay vì tạo số hình nguồn giả.

## F.4. Quy trình giữ/xóa ảnh cũ

1. Kiểm kê từng ảnh thực tế, mở xem nội dung, đọc các tham chiếu hiện có; không đánh giá chỉ từ tên file trong ảnh chụp thư mục.
2. Lập bảng làm việc: tên file | nội dung | nguồn đã xác minh | vị trí dùng trong bản mới | giữ/thay/xóa và lý do. Bảng chỉ dùng nội bộ trong quá trình thao tác, không tạo tệp kiểm chứng hoặc tài liệu giao riêng.
3. Ảnh có nội dung phù hợp và xác minh được nguồn có thể giữ; kiểm chứng lại hình/trang nguồn, không kế thừa chú thích cũ.
4. Viết xong bản mới và cập nhật các đường dẫn trước khi dọn ảnh. Kiểm tra ảnh còn được các tệp văn bản khác trong vùng đầu ra tham chiếu hay không; ảnh dùng cho tệp khác hoặc chưa rõ vai trò thì giữ và báo rõ.
5. Xóa từng ảnh xác định không dùng, không còn tham chiếu, trong đúng `hinh_minh_hoa/`. Không xóa cả thư mục, không dùng wildcard quét rộng, không lần theo symlink ra ngoài vùng cho phép.
6. Không kế thừa ảnh HEINEKEN từ bản cũ nếu chưa kiểm tra xuất xứ. Ảnh mới dùng đúng nhà máy Vũng Tàu; không dùng ảnh cơ sở khác chỉ vì cùng thương hiệu.
7. Kiểm tra lại toàn bộ liên kết ảnh sau khi xóa và báo danh sách ảnh đã xóa/giữ/thêm cùng lý do ngắn gọn.

# G. Điều kiện nghiệm thu bản báo cáo do Codex tạo

- [ ] Đúng đề tài, bố cục bốn phần 1.1–1.4 và cấp heading; có hai blockquote mở đầu.
- [ ] Có đoạn mở chương, chuyển 1.1→1.2, 1.2→1.3, 1.3→1.4 và kết nối Chương 1→Chương 2.
- [ ] Sáu nội dung yêu cầu ở 1.2 được định nghĩa; giá trị nào thiếu căn cứ không được tự chốt.
- [ ] Phần 1.3 đúng Nhà máy HEINEKEN Vũng Tàu và phạm vi nguồn dự án; không khẳng định đã khảo sát hiện trường, đã lắp hoặc vận hành khi chưa có bằng chứng.
- [ ] Giữ riêng mục 1.3; toàn bộ 1.1–1.2, kể cả bảng và chú thích, không có thông tin hoặc trích dẫn lấy từ trường hợp HEINEKEN Vũng Tàu.
- [ ] Toàn văn dùng giọng trình bày của người thực hiện đồ án theo B.5; không dùng “cần xác định”, “cần tách”, “cần kiểm tra” như lời giao việc cho người khác.
- [ ] Phần 1.4 là kết luận chương; không còn mục khảo sát hoặc thông số thiết bị thương mại trong Chương 1. Nội dung đó dành cho Chương 2.
- [ ] Lựa chọn linh kiện dành cho Chương 2; không đưa cấu hình hoặc kết quả thử của bản cũ thành dữ kiện mới.
- [ ] Mỗi thông số, số liệu, hình và kết luận về thực tế đều có nguồn hỗ trợ trực tiếp, đúng trang/mục.
- [ ] Danh mục và mã trích dẫn khớp hai chiều; URL đã truy cập được hoặc có giới hạn nêu rõ; không còn nguồn giả hoặc số trang đoán.
- [ ] Hình có nguồn, chú thích, đánh số liên tục, đọc được; không có ảnh AI hoặc hình tự tạo; không nhầm địa điểm/phạm vi.
- [ ] Đường dẫn ảnh hợp lệ, bảng Markdown hiển thị đúng; không còn ghi chú `%%...%%` hoặc câu giao việc trong báo cáo.
- [ ] Ảnh thừa đã rà soát và dọn trong phạm vi cho phép; không làm hỏng tham chiếu của tệp khác.
- [ ] Chỉ thay đổi trong vùng đầu ra; `Tham khảo/` giữ nguyên.
- [ ] Không tạo hoặc khôi phục tệp kiểm chứng riêng; vẫn kiểm tra nguồn và liên kết trước khi hoàn thành.
- [ ] Độ dài hướng tới 10–14 trang nhưng không tuyên bố đã đạt chính xác nếu chưa dàn trang.

Khi kết thúc, báo ngắn gọn: tệp đã sửa; nội dung mới; nguồn bổ sung; ảnh thêm/xóa; các giới hạn chưa giải quyết. Không tuyên bố mọi yêu cầu đã được kiểm chứng nếu vẫn thiếu dữ liệu.

## Quy tắc áp dụng khi viết tiếp

Trước mỗi lần viết mới hoặc chỉnh sửa báo cáo, đọc và tuân thủ Design-rules-Chuong-1.md, đặc biệt B.5. Duy trì quy tắc văn phong khi viết các chương tiếp theo; bố cục riêng Chương 1 chỉ áp dụng cho Chương 1. Yêu cầu mới nhất của người dùng được ưu tiên khi có xung đột. Trước khi hoàn thành, tìm các cụm “đề tài”, “đồ án”, “nghiên cứu này”, “thiết kế này” và đọc từng câu để loại bỏ lối tự quy chiếu; giữ nguyên tên đề tài và tên nguồn. Viết lại câu theo nội dung kỹ thuật và quan hệ nguyên nhân–kết quả, không chỉ thay từ.

Rà soát bổ sung trước khi hoàn thành: tìm “tài liệu tổng quan”, “đề cập”, “xem…là”, “coi…là”, “đây là thông tin”; đọc ngữ cảnh và viết trực tiếp nội dung khi không cần phân tích chính nguồn đó. Giữ đầy đủ trích dẫn sau khi sửa.
