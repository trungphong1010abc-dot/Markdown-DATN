> **Đề tài:** Thiết kế hệ thống nhúng phát hiện chớp hồ quang điện (arc-flash) trong hệ thống điện hạ thế và trung thế.
>
> **Ghi chú bản thảo:** Báo cáo được viết theo tài liệu này hướng tới khoảng 10–14 trang A4 khi dàn trang bằng Times New Roman 13, giãn dòng khoảng 1,15; số trang thực tế phụ thuộc lề và kích thước hình. Markdown không quy định trực tiếp phông chữ hoặc số trang.
>
> **Vai trò tài liệu:** Đây là đặc tả biên soạn Chương 1 dành cho Codex, không phải nội dung báo cáo hoàn chỉnh. Bố cục mới trong tài liệu này thay thế bố cục cũ. File báo cáo cũ chỉ dùng tham khảo hình thức trình bày, tuyệt đối không coi nội dung và danh mục nguồn cũ là dữ liệu đã kiểm chứng.

# A. Phạm vi thao tác và sản phẩm cần hoàn thành

1. Xác định thư mục thực tế trước khi thao tác. Ảnh người dùng cung cấp thể hiện `Bao_cao_nhap/` chứa `hinh_minh_hoa/`, `Tham khảo/` và `Chuong-1-Tong-quan-de-tai.md`. Nếu cấu trúc thực tế khác, xác định chính xác hai vùng nguồn và đầu ra, không tự tạo các thư mục trùng tên để né ranh giới.
2. `Tham khảo/` là vùng chỉ đọc: đọc toàn bộ danh mục nguồn, tìm nội dung phù hợp; không sửa, xóa, đổi tên hoặc di chuyển bất kỳ tệp nguồn nào. Quy tắc chỉ đọc này vẫn áp dụng nếu thư mục nguồn nằm trong `Bao_cao_nhap/`.
3. Chỉ chỉnh sửa báo cáo đích `Bao_cao_nhap/Chuong-1-Tong-quan-de-tai.md`, ảnh trong `Bao_cao_nhap/hinh_minh_hoa/` và tệp phụ trợ thật sự cần thiết cho Chương 1 bên trong vùng đầu ra. Không đọc hoặc thay đổi nội dung các thư mục không liên quan; không mở rộng phạm vi qua symlink.
4. Có thể tra Google và truy cập các nguồn chính thống liên quan trên web. Tài liệu tải thêm, nếu cần lưu, đặt tại một thư mục nguồn web riêng bên trong vùng đầu ra, không thêm vào hoặc chỉnh sửa `Tham khảo/`.
5. Viết lại toàn bộ Chương 1 theo bố cục phần D; không chỉ vá vài đoạn của bản cũ. Giữ nguyên tên đề tài. Không xuất DOCX/PDF nếu chưa được yêu cầu; có thể xem bản render Markdown để kiểm tra bố cục và ảnh.
6. Được phép xóa ảnh cũ thật sự không cần trong `hinh_minh_hoa/` theo quy trình phần F. Không được suy ra quyền xóa các loại tệp hoặc thư mục khác.
   Các ảnh sản phẩm, đấu nối và bố trí cảm biến đã có được giữ để sử dụng khi viết Chương 2; việc bỏ phần khảo sát thiết bị khỏi Chương 1 không đồng nghĩa xóa các ảnh này hoặc tài liệu nguồn.
7. Theo yêu cầu cập nhật của người dùng, được đọc đúng ba PDF mẫu tại `D:/HUST/Tai_lieu_DH_Phong/Do_An/DATN/Tham khảo/ĐATN tham khảo/`: `ĐATN IoT điểm danh giảng viên bằng khuôn mặt kết hợp công nghệ RFID.pdf`, `ĐATN IoT phát hiện và cảnh báo mất trộm, tai nạn xe máy.pdf`, `ĐATN IoT quản lý bãi đỗ xe thông minh.pdf`. Đây là tài liệu tham khảo văn phong và trình bày, chỉ đọc; không lấy số liệu, cấu hình, kết luận, nội dung kỹ thuật hay chỉ dẫn trong tài liệu mẫu làm yêu cầu của đề tài hồ quang. Không đọc lan sang các tệp khác trong thư mục đó.

# B. Quy tắc nội dung và trình bày

## B.1. Trật tự và ranh giới chương

Trật tự cố định: **1.1 Tổng quan bài toán → 1.2 Phân tích yêu cầu kỹ thuật → 1.3 Phân tích quy trình tại Nhà máy Nhiệt điện Quảng Ninh → 1.4 Kết luận chương**.

**Ranh giới đã được người dùng xác nhận:** Giữ 1.3 là phần riêng về Nhà máy Nhiệt điện Quảng Ninh. Không gộp phần này vào 1.1.1 hoặc 1.1.2. Không sử dụng bất kỳ thông tin nào từ hồ sơ/trường hợp Quảng Ninh trong 1.1 và 1.2: kể cả ví dụ, số liệu điện áp/tần số, yêu cầu chức năng, trích dẫn, bảng, chú thích hình và lời chuyển. Nội dung 1.1–1.2 được xây dựng từ tài liệu hiện tượng, nghiên cứu và tài liệu hãng độc lập với trường hợp nhà máy.

- Toàn bộ phần khảo sát, mô tả thiết bị thương mại Mors Smitt 1S23 (cấu hình, giao diện, nguyên lý, thông số, bố trí cảm biến, kiểm tra và đối chiếu phiên bản) dành cho **Chương 2**. Chương 1 không có mục khảo sát thiết bị và không rải mô tả hoặc thông số sản phẩm vào các mục khác. Phần lựa chọn cảm biến, vi điều khiển, linh kiện và bảng so sánh linh kiện cũng dành cho Chương 2. Nhiệm vụ hiện tại chỉ chỉnh Chương 1 và Design rules, chưa viết Chương 2.
- Không chép lại các phần tổng quan thuật toán dài của báo cáo cũ để tăng số trang. Chỉ nhắc nghiên cứu liên quan khi giúp làm rõ bài toán hoặc căn cứ kỹ thuật.
- Không tự chốt kiến trúc nguyên mẫu, số kênh, giao thức, nguồn cấp, ngưỡng hoặc kế hoạch thử nếu chưa có căn cứ.
- Không kế thừa các chỉ tiêu cũ như 5 ms, 95/100, 100 bản ghi, 8 giờ, nguồn 24 VDC hoặc hai kênh quang như yêu cầu đã được chốt. Cấu hình sản phẩm tham khảo không tự động trở thành cấu hình đồ án.
- Phân biệt phát hiện, cảnh báo, lệnh tác động, phối hợp bảo vệ và loại trừ sự cố. Không mặc định đồ án điều khiển cắt máy cắt hoặc đã đáp ứng tiêu chuẩn công nghiệp.

## B.2. Heading và văn phong

- Báo cáo đích không có heading `# CHƯƠNG 1...`; tên chương đã thể hiện qua tên file. Mở đầu bằng hai blockquote về đề tài và độ dài như đầu tài liệu này, rồi một đoạn giới thiệu chương.
- Dùng `# 1.1. ...`, `## 1.1.1. ...`; chỉ dùng cấp `###` khi cần, không chia sâu thành quá nhiều mục bốn cấp. `# 1.4. Kết luận chương`; cuối cùng `# Tài liệu tham khảo của Chương 1` không đánh thành mục 1.5.
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
6. **Giới hạn được đặt đúng chỗ.** Giữ các phân biệt kỹ thuật cần thiết như độ trễ/độ rộng xung, thiết kế/hiện trạng và mô-đun/hệ bảo vệ. Tập trung giới hạn nhà máy vào 1.3.5, giá trị chưa chốt vào Bảng 1.1, khác biệt phiên bản thiết bị dành cho Chương 2. Không nhắc lại cùng một phủ định ở đoạn dẫn, chú thích ảnh, bảng và đoạn kết. Không bỏ giới hạn để tạo cảm giác đề tài đã có dữ liệu.
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

## B.5. Giọng trình bày của người thực hiện đồ án

Người viết đồng thời là người phân tích và thiết kế hệ thống. Thân báo cáo trình bày đối tượng, cách phân tích, lựa chọn có căn cứ và phương pháp đánh giá của đồ án; không dùng giọng hướng dẫn hoặc giao nhiệm vụ cho một người thiết kế khác. Quy tắc này áp dụng cho tất cả các mục, đoạn dẫn, gạch ý, bảng và kết luận.

- **Dùng chủ thể và hành động rõ ràng.** Viết “đồ án phân biệt…”, “trong thiết kế này, điện áp được chia thành…”, “phép đánh giá sử dụng…”, hoặc mô tả trực tiếp đối tượng. Không lạm dụng “ta”, “chúng ta” hay lặp “đồ án” ở đầu mọi câu.
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
- Không dùng đường dẫn tìm được nhưng chưa đọc làm bằng chứng cho một kết luận kỹ thuật. Nếu liên kết lỗi, tìm bản chính thức khác hoặc bản sao cùng tài liệu có thể kiểm tra xuất xứ; ghi đúng nơi truy cập.
- Nguồn riêng về Quảng Ninh chỉ phục vụ phần 1.3, kết luận tổng hợp phù hợp và danh mục tài liệu; không đưa lên phần 1.1–1.2. Trong hệ mã hiện tại, không dùng W1 hoặc W2 tại 1.1–1.2; nếu đánh lại mã thì vẫn giữ ranh giới theo bản chất nguồn, không chỉ theo mã.

## C.2. Mã nguồn và trích dẫn trong văn bản

- Gán mã ổn định `TL1`, `TL2`… cho tài liệu có sẵn và `W1`, `W2`… cho nguồn web bổ sung. Mã chỉ được gán sau khi kiểm kê, không giữ nguyên mã cũ một cách máy móc.
- Trích gần nhận định: `[TL1, mục 3.2, tr. in 78; tr. PDF 2]` hoặc `[W2, phần “...”]`. Đây là mẫu cú pháp; phải thay bằng vị trí thực sự đã kiểm tra.
- Nếu trang in và số trang PDF khác nhau, phân biệt hai hệ. Trang PDF đếm từ 1; không lấy chỉ số 0-based của công cụ làm số trang trích dẫn.
- Nếu một câu có nhiều khẳng định mà nguồn chỉ chứng minh một phần, tách câu hoặc bổ sung nguồn phù hợp.
- Phân biệt nội dung nguồn với suy luận của tác giả. Trong lời văn dùng “Từ các đặc điểm trên, đề tài nhận thấy...” khi thật sự là phân tích. Không dùng nhãn suy luận để hợp thức hóa chi tiết giả định về nhà máy.
- Không tạo DOI, tác giả, năm, số trang hoặc kết quả thử nghiệm từ trí nhớ. Không chép nguyên đoạn dài của nguồn.

## C.3. Danh mục cuối chương

Mỗi mục có đủ thông tin xác minh được: mã, tác giả/cơ quan, tiêu đề chính xác, năm hoặc phiên bản, tạp chí/đơn vị xuất bản, DOI nếu đã xác minh; tên tệp thực tế cho nguồn nội bộ. Nguồn web có URL tới trang/PDF đã đọc và ngày truy cập thực tế. Không bịa ngày xuất bản nếu trang không ghi.

Mẫu:

`**TLx —** Tác giả, *Tên tài liệu*, tạp chí/đơn vị, năm, DOI đã kiểm chứng. Tệp: \`tên-tệp-thực-tế.pdf\`.`

`**Wx —** Cơ quan, *Tên trang hoặc tài liệu*, phiên bản/ngày nếu có. [Trang nguồn](URL). Truy cập ngày thực tế.`

Mọi mã trong nội dung phải tồn tại trong danh mục; mọi nguồn trong danh mục phải thực sự được dùng.

# D. Đặc tả chi tiết nội dung Chương 1

## D.0. Mở đầu chương

Viết một đoạn xác định mục tiêu và trình tự của chương. Lời dẫn gợi ý, có thể điều chỉnh câu chữ nhưng giữ ý:

> Chương này trình bày bối cảnh và tính cấp thiết của bài toán phát hiện chớp hồ quang điện trong hệ thống điện hạ thế và trung thế. Trên cơ sở xác định đối tượng nghiên cứu, chương phân tích các yêu cầu kỹ thuật ban đầu, phân tích quy trình phát hiện và phối hợp bảo vệ theo hồ sơ thiết kế tại Nhà máy Nhiệt điện Quảng Ninh. Các nội dung này tạo căn cứ cho việc nghiên cứu cơ sở lý thuyết và lựa chọn linh kiện ở chương tiếp theo.

## D.1. `# 1.1. Tổng quan bài toán phát hiện chớp hồ quang điện`

### `## 1.1.1. Đối tượng nghiên cứu và bối cảnh ứng dụng`

- Trả lời: đối tượng chịu tác động là gì, ở đâu trong hệ thống, chức năng và cấu trúc nào liên quan đến bài toán?
- Giới thiệu trạm biến áp và phân phối hạ thế, trung thế; thu hẹp đến tủ điện, thiết bị đóng cắt, thanh cái, đầu cáp và các khoang cần quan tâm theo nguồn.
- Làm rõ đơn vị không gian: toàn trạm, dãy tủ, khoang tủ; chưa có khảo sát thì không tự chốt vị trí lắp của đồ án.
- Dùng 5W1H để rà soát tính đầy đủ, chọn câu hỏi phù hợp; không tạo thông tin chỉ để đủ sáu câu hỏi.
- Hình nếu dùng: ảnh/sơ đồ tủ hoặc trạm trong nguồn đã xác minh; phải nói rõ đó là minh họa cấu trúc, không phải nhà máy ở 1.3 nếu không cùng địa điểm.
- Lồng tính cấp thiết vào bối cảnh ứng dụng: từ đối tượng chịu tác động và hậu quả, trình bày mục đích phát hiện sớm, phân biệt tác động gây nhầm và đánh giá chuỗi phản hồi. Không tách thành tiểu mục riêng.

### `## 1.1.2. Hiện tượng hồ quang điện và chớp hồ quang điện`

- Định nghĩa, thống nhất thuật ngữ electric arc, arc fault, arc flash theo nguồn; giải thích phạm vi đề tài.
- Trình bày nguyên nhân, điều kiện hình thành và các biểu hiện liên quan đến phát hiện; nêu tác động đến thiết bị, con người và hoạt động nhà máy.
- Phân biệt hồ quang đóng cắt được thiết kế kiểm soát với sự cố ngoài vùng chức năng đó.
- Phân biệt nghiên cứu hồ quang nối tiếp AC, hồ quang DC/PV với bài toán chớp hồ quang trong tủ điện; không chuyển nguyên chỉ số phát hiện giữa các phạm vi.
- Chỉ trình bày nền tảng vừa đủ; cơ chế chi tiết, công thức và thuật toán dành cho Chương 2.
- Lồng số liệu minh chứng vào phần giải thích hiện tượng và hậu quả: ảnh hư hỏng, điều kiện thử và quan hệ năng lượng–thời gian được đặt cạnh nội dung chuyên môn tương ứng.
- Mỗi số liệu ghi rõ đại lượng, đơn vị, phạm vi và điều kiện nguồn. Không biến thử nghiệm thành thống kê tai nạn hoặc suy ra tần suất khi không có mẫu số, thời gian quan sát và phương pháp phù hợp.
- Nếu thiếu thống kê tần suất, nêu giới hạn ngắn tại đoạn minh chứng, không biến phần này thành nhật ký nguồn. Kết nối hậu quả với nhiệm vụ phát hiện và lời dẫn sang 1.2.

Phần 1.1 chỉ có hai tiểu mục 1.1.1 và 1.1.2. Nội dung số liệu minh chứng và tính cấp thiết được tích hợp vào hai tiểu mục trên, không giữ hoặc tạo lại heading 1.1.3. Khi sắp xếp lại nội dung, giữ trích dẫn sát nhận định và số hình liên tục theo thứ tự xuất hiện.

**Lời dẫn sang 1.2:**

> Từ bối cảnh và hậu quả của sự cố, đồ án phân tích các đại lượng và đặc tính kỹ thuật của hệ thống phát hiện. Những nội dung này là cơ sở xây dựng hệ thống nhúng ở các chương sau.

## D.2. `# 1.2. Phân tích yêu cầu kỹ thuật của bài toán`

Mỗi tiểu mục phải có: đại lượng/đối tượng xét → ý nghĩa → căn cứ → giá trị hoặc giới hạn nếu đủ bằng chứng → cách đánh giá. Chưa xác định bộ tiêu chuẩn áp dụng không có nghĩa lĩnh vực không có tiêu chuẩn. Nếu Đồ án 1–2 không có trong vùng nguồn được phép, không viện dẫn nội dung giả định của chúng.

### `## 1.2.1. Yêu cầu về điện áp`
Phân biệt điện áp hệ thống giám sát, tín hiệu đo và nguồn phụ trợ. Không suy ra cảm biến hoặc vi điều khiển tiếp xúc trực tiếp với điện áp trung thế. Chưa có căn cứ không chốt dải điện áp nguyên mẫu.

### `## 1.2.2. Yêu cầu về tần số`
Xác định tần số hệ thống điện trong phạm vi có nguồn; phân biệt tần số điện lưới, dải tần tín hiệu cần xét và tần số lấy mẫu. Giải thích vai trò, không chỉ liệt kê con số.

### `## 1.2.3. Yêu cầu về dòng điện`
Làm rõ dòng điện được theo dõi, vai trò phát hiện/xác nhận, vị trí trong chuỗi đo nếu đã xác định. Phân biệt dòng định mức, dòng sự cố và tín hiệu thứ cấp. Chưa tự chọn ngưỡng, tỷ số biến dòng hay định mức đầu ra.

### `## 1.2.4. Yêu cầu về độ nhạy`
Định nghĩa độ nhạy đối với tín hiệu nào và trong điều kiện gì. Phân biệt ngưỡng quang, độ nhạy cảm biến và xác suất phát hiện. Nếu chỉ tiêu chưa định lượng, trình bày những dữ kiện cần có để xác định; không viết “độ nhạy cao” như tiêu chí hoàn chỉnh.

### `## 1.2.5. Yêu cầu về thời gian phản hồi`
Nêu rõ hai mốc đo; phân biệt thu nhận, xử lý, xuất đầu ra, rơ-le ngoài, cơ cấu máy cắt và thời gian loại trừ toàn sự cố. Không đồng nhất thời gian của mô-đun với thời gian cắt toàn hệ thống; không nhầm độ rộng xung với độ trễ.

### `## 1.2.6. Yêu cầu về chu kỳ lấy mẫu`
Xác định kênh nào thực sự lấy mẫu và nhu cầu thông tin của kênh đó. Nếu kiến trúc chưa chọn, để đây là yêu cầu cần xác định theo cơ chế thu nhận, không mặc định mọi kênh dùng ADC. Khi có số liệu, kiểm tra đơn vị và quan hệ `f_s = 1/T_s`; không chọn tần số chỉ bằng cách gấp đôi tần số điện lưới.

### `## 1.2.7. Tổng hợp yêu cầu kỹ thuật ban đầu`
Bảng bắt buộc: mã yêu cầu | nội dung | giá trị/tiêu chí hoặc thông số chưa xác lập | căn cứ | cách đánh giá | trạng thái. Sáu yêu cầu trên là trục chính; bảng tổng hợp không phải yêu cầu thứ bảy. Dùng căn cứ độc lập với hồ sơ Quảng Ninh. Không dùng thông số thiết bị thương mại làm ví dụ hoặc chỉ tiêu; khảo sát sản phẩm dành cho Chương 2. Việc đối chiếu trường hợp nhà máy được thực hiện tại chính 1.3, không đưa dữ liệu hoặc trích dẫn từ đó lên bảng này.

**Lời dẫn sang 1.3:**

> Sau phần phân tích yêu cầu kỹ thuật, mục 1.3 trình bày một trường hợp nghiên cứu riêng ở cấp hệ thống. Kết luận chương tổng hợp phạm vi và các yêu cầu làm cơ sở cho Chương 2.

## D.3. `# 1.3. Phân tích quy trình phát hiện và phối hợp bảo vệ hồ quang theo hồ sơ thiết kế tại Nhà máy Nhiệt điện Quảng Ninh`

### D.3.a. Giới hạn bằng chứng phải giữ

Trường hợp đã chọn: Công ty Cổ phần Nhiệt điện Quảng Ninh, phạm vi thiết bị trong dự án nâng cấp, cải tạo hệ thống xử lý khí thải. Hồ sơ đã được đọc ở giai đoạn lập dàn ý là tài liệu điều chỉnh Báo cáo nghiên cứu khả thi, Chương 4, trang in 170–171/339, có yêu cầu phát hiện hồ quang, kết hợp đo dòng điện và gửi tín hiệu điều khiển tới máy cắt cấp nguồn; đề cập sự cố tại Power Cell hoặc máy biến áp và thiết bị 6,6 kV. Codex phải mở lại, kiểm tra phạm vi và vị trí trước khi trích vào báo cáo.

Đây là **yêu cầu hồ sơ thiết kế**, chưa đủ để kết luận **đã lắp đặt/đang vận hành**. Giữ tên mục “theo hồ sơ thiết kế” trừ khi có tài liệu hiện trạng được xác thực. Không gán công nghệ cảm biến quang hoặc logic AND cụ thể cho nhà máy nếu hồ sơ không nói. Không thay bằng HEINEKEN chỉ vì file cũ có sẵn nội dung và ảnh.

### `## 1.3.1. Giới thiệu nhà máy và cơ sở lựa chọn trường hợp nghiên cứu`
Giới thiệu ngắn từ nguồn doanh nghiệp/EVN/cơ quan chính thức; nêu lý do chọn gắn với tài liệu kỹ thuật thực sự. Không viết lịch sử doanh nghiệp dài hoặc cam kết đã có đủ bản vẽ và dữ liệu vận hành.

### `## 1.3.2. Phạm vi hệ thống và thiết bị được phân tích`
Khoanh vùng hệ biến tần trung thế trong dự án; chỉ mô tả quan hệ nguồn cấp, máy cắt, máy biến áp, khối công suất và bảo vệ khi có nguồn. Không suy rộng sang toàn nhà máy hoặc phía hạ thế nếu tài liệu chỉ mô tả một phạm vi trung thế. Một trường hợp trung thế không tự chứng minh toàn bộ yêu cầu hạ thế của đề tài.

### `## 1.3.3. Yêu cầu phát hiện và phối hợp bảo vệ trong hồ sơ`
Lập bảng: nội dung hồ sơ | ý nghĩa chức năng | trang/mục | giới hạn thông tin. Phân biệt nội dung hồ sơ quy định với giải thích của người viết. Không tự tạo ngưỡng, mã rơ-le, loại cảm biến, vị trí lắp hoặc thời gian định lượng.

### `## 1.3.4. Trình tự chức năng phát hiện và phối hợp tác động`
Diễn giải bằng danh sách bước đánh số kèm đoạn giải thích ngắn theo B.4, chỉ ở mức tài liệu cho phép. Phân biệt nhận biết sự cố, phối hợp đo dòng và xuất tín hiệu tới máy cắt. Không tự thêm SCADA, DCS, ghi sự kiện, khôi phục tự động hoặc quy trình thao tác người vận hành. Nếu có sơ đồ gốc phù hợp thì trích; nếu không, dùng danh sách và lời văn, không tự vẽ ảnh thay thế. Thiếu dữ liệu phải được nói rõ ở phần giới hạn phù hợp.

### `## 1.3.5. Đối chiếu với yêu cầu của đề tài và giới hạn thông tin`
Đối chiếu với 1.2; phân loại thông tin đã có và chưa có. Liệt kê các khoảng trống cụ thể như số lượng/vị trí cảm biến, ngưỡng, mã thiết bị, sơ đồ đấu dây, dữ liệu nghiệm thu/vận hành. Không dùng tài liệu sản phẩm 1S23 để lấp khoảng trống thành sự thật của nhà máy.

**Lời dẫn sang 1.4:**

> Trường hợp nhà máy làm rõ quan hệ giữa phát hiện sự cố, thông tin dòng điện và tác động cắt nguồn. Phần kết luận tổng hợp bài toán, các yêu cầu kỹ thuật và giới hạn thông tin của chương.

## D.4. `# 1.4. Kết luận chương`

Viết khoảng 2–3 đoạn: kết quả làm rõ bài toán; sáu nhóm yêu cầu; ý nghĩa và giới hạn của trường hợp nhà máy; liên hệ với cơ sở lý thuyết và thiết kế ở Chương 2. Không khảo sát sản phẩm, không bổ sung thông số hoặc chức năng mới. Chương 2 dành cho cơ sở lý thuyết, khảo sát thiết bị thương mại và phân tích lựa chọn linh kiện.

**Đoạn chuyển sang Chương 2:**

> Chương 1 trình bày bối cảnh, phạm vi nghiên cứu và các yêu cầu kỹ thuật ban đầu của bài toán phát hiện chớp hồ quang điện. Trên cơ sở đó, Chương 2 trình bày lý thuyết về phát hiện, thu nhận và xử lý tín hiệu, đồng thời phân tích, lựa chọn linh kiện. Những thông số chưa xác lập được xem xét cùng phương án thiết kế và điều kiện đánh giá của đồ án.

# E. Nguồn khởi đầu cho việc nghiên cứu tiếp

Các URL sau là đầu mối để mở và kiểm tra lại, không phải danh mục tham khảo đã hoàn chỉnh của báo cáo mới. Chỉ đưa vào danh mục cuối khi đã đọc và thực sự sử dụng.

| Đầu mối | Vai trò và trạng thái |
|---|---|
| Các bài *Aspects of arc-flash protection and prediction*, *Electric arc explosions—A review*, *Explainable artificial intelligence modeling of internal arc in a medium voltage switchgear based on different CFD simulations* trong `Tham khảo/` | Ưu tiên rà soát cho hiện tượng, hậu quả và hình; kiểm tra tác giả, năm, hình và trang từ chính file. |
| Các bài phát hiện hồ quang AC, DC/PV và triển khai nhúng trong `Tham khảo/` | Nguồn hỗ trợ; phải ghi đúng loại sự cố và điều kiện nghiên cứu. |
| https://quangninhtpc.com.vn/d6/news/Thong-bao-moi-hop-Dai-hoi-dong-co-dong-thuong-nien-2026-5-217-1976 | Đầu mối trang doanh nghiệp; có thể lỗi truy cập. Không mặc định tài liệu đại hội thường niên này chính là hồ sơ công bố tháng 6. |
| https://hnx.vn/vi-vn/ModuleIssuer/UC_Issuer/Details/QTP/UC | Công bố thông tin QTP, kiểm tra tài liệu ngày 11/06/2026 và đường dẫn gốc liên quan. |
| https://cafef1.mediacdn.vn/download/110626/qtp-tai-lieu-hop-ai-hoi-dong-co-dong-3-619481.pdf | Bản sao công khai tài liệu doanh nghiệp đã tải và đọc ở giai đoạn lập dàn ý. Đầu mối nội dung kỹ thuật Chương 4, trang in 170–171/339. Ưu tiên tìm cùng tài liệu trên trang doanh nghiệp/HNX; nếu dùng bản sao, ghi đúng tác giả tài liệu và nơi lưu bản sao, không gọi CafeF là chủ đầu tư hoặc nguồn xuất bản gốc. |

Nếu không thể truy cập hoặc xác thực một đầu mối, tiếp tục hoàn thiện phần có bằng chứng và báo giới hạn; không dựng quy trình vận hành thực tế cho đủ mục. Không đổi nhà máy tùy ý; chỉ đề xuất đổi khi có lý do và bằng chứng tốt hơn.

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
| 1.3 | Ảnh chính thức Nhà máy Nhiệt điện Quảng Ninh; sơ đồ đúng phạm vi nếu có trong hồ sơ | Ảnh toàn cảnh chỉ chứng minh bối cảnh, không chứng minh có thiết bị phát hiện cụ thể. |

## F.3. Cú pháp và chú thích

Đánh số liên tục theo thứ tự xuất hiện, không giữ số cũ nếu đã đổi bố cục. Tên file không dấu, gọn, phản ánh nội dung; đường dẫn tương đối từ báo cáo:

```markdown
![Mô tả chính xác nội dung hình](hinh_minh_hoa/Hinh_1_1_Mo_ta_noi_dung.png)

*Hình 1.1. Nội dung và phạm vi minh họa.*

*Nguồn: TLx, Hình y, tr. in a (tr. PDF b). Cắt từ tài liệu, giữ nguyên nhãn và số liệu. Điều kiện thử hoặc giới hạn liên quan nếu có.*
```

Với ảnh web: nguồn là tác giả/cơ quan, tiêu đề, [trang gốc](URL), [ảnh gốc](URL) nếu truy được, ngày truy cập thực tế, thông tin giấy phép/ghi công nếu có. Không trích trang kết quả Google làm nguồn ảnh. Đối với ảnh sản phẩm không có số hình, mô tả vị trí trên trang thay vì tạo số hình nguồn giả.

## F.4. Quy trình giữ/xóa ảnh cũ

1. Kiểm kê từng ảnh thực tế, mở xem nội dung, đọc các tham chiếu hiện có; không đánh giá chỉ từ tên file trong ảnh chụp thư mục.
2. Lập bảng làm việc: tên file | nội dung | nguồn đã xác minh | vị trí dùng trong bản mới | giữ/thay/xóa và lý do. Bảng chỉ dùng nội bộ trong quá trình thao tác, không tạo tệp kiểm chứng hoặc tài liệu giao riêng.
3. Ảnh có nội dung phù hợp và xác minh được nguồn có thể giữ; kiểm chứng lại hình/trang nguồn, không kế thừa chú thích cũ.
4. Viết xong bản mới và cập nhật các đường dẫn trước khi dọn ảnh. Kiểm tra ảnh còn được các tệp văn bản khác trong vùng đầu ra tham chiếu hay không; ảnh dùng cho tệp khác hoặc chưa rõ vai trò thì giữ và báo rõ.
5. Xóa từng ảnh xác định không dùng, không còn tham chiếu, trong đúng `hinh_minh_hoa/`. Không xóa cả thư mục, không dùng wildcard quét rộng, không lần theo symlink ra ngoài vùng cho phép.
6. Ảnh HEINEKEN cũ không được dùng để minh họa nhà máy Quảng Ninh. Nếu không còn mục đích hoặc tham chiếu nào khác, đó là ứng viên xóa; không xóa tự động chỉ vì tên có HEINEKEN.
7. Kiểm tra lại toàn bộ liên kết ảnh sau khi xóa và báo danh sách ảnh đã xóa/giữ/thêm cùng lý do ngắn gọn.

# G. Điều kiện nghiệm thu bản báo cáo do Codex tạo

- [ ] Đúng đề tài, bố cục bốn phần 1.1–1.4 và cấp heading; có hai blockquote mở đầu.
- [ ] Có đoạn mở chương, chuyển 1.1→1.2, 1.2→1.3, 1.3→1.4 và kết nối Chương 1→Chương 2.
- [ ] Sáu nội dung yêu cầu ở 1.2 được định nghĩa; giá trị nào thiếu căn cứ không được tự chốt.
- [ ] Phần 1.3 đúng Nhà máy Nhiệt điện Quảng Ninh và phạm vi hồ sơ; không khẳng định đã khảo sát hiện trường, đã lắp hoặc vận hành khi chưa có bằng chứng.
- [ ] Giữ riêng mục 1.3; toàn bộ 1.1–1.2, kể cả bảng và chú thích, không có thông tin hoặc trích dẫn lấy từ trường hợp Quảng Ninh.
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
