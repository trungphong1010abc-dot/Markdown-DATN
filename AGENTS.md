# Hướng dẫn làm việc trong dự án

Áp dụng cho toàn bộ thư mục và các thư mục con. Đọc [DESIGN_RULES.md](DESIGN_RULES.md) trước khi chỉnh tài liệu hoặc thiết kế.

## Tôn trọng nội dung người dùng đã xóa

- **Không tự thêm lại phần người dùng đã xóa.** Chỉ khôi phục khi người dùng yêu cầu rõ ràng.
- Trong `module/01_Huong_dan_test_va_kiem_thu_module.md`, người dùng đã yêu cầu xóa các đoạn mở đầu về cấu hình cố định, thứ tự đọc, liên kết “Tài liệu bước sau” và đoạn giới thiệu ngay dưới “1. Bảng linh kiện module”. Không tự thêm lại các đoạn này, kể cả viết lại hoặc chuyển chỗ.
- Đọc bản hiện tại trên đĩa trước mỗi lần sửa. Không dùng bản trong lịch sử trò chuyện, Git, ZIP hoặc script cũ để ghi đè những chỉnh sửa mới của người dùng.
- Quy tắc này áp dụng cả đoạn mở đầu, ghi chú, bảng, hình, liên kết và mục nội dung. Không viết lại cùng ý bằng câu khác để đưa nội dung đã xóa trở lại.
- Nếu không rõ một phần bị thiếu có phải do người dùng xóa hay không, giữ nguyên trạng thái hiện tại. Nếu phần đó cần thiết để xử lý yêu cầu, hỏi rõ trước khi khôi phục.
- Nếu phát hiện việc xóa gây vấn đề kỹ thuật, nêu cụ thể vấn đề; không lấy lý do đó để tự khôi phục nội dung.

## Phạm vi chỉnh sửa

- Mạch quang node dùng cố định hai tầng RC sau TIA (mỗi tầng 1 kΩ/10 nF). Người dùng không thực hiện phương án nối thẳng hoặc so sánh hai cấu hình. Không tự thêm lại cách gọi/chọn L0–L2, thao tác tháo lọc hay nối tắt. Kiểm thử đo ngay trước/sau lọc trên mạch giữ nguyên.

- Hai module truyền thông node/gateway dùng nguyên bo theo ảnh người dùng đã cung cấp. Không tự kê thêm tụ nguồn, trở kéo, termination hoặc bias rời vào BOM module. Chỉ đề xuất bổ sung khi đã xác định mạch bo thực và có căn cứ cụ thể; không suy đủ thông số hoặc mức logic từ ảnh.

- **CT DL-CT08CL6-1000/1: tỷ số 1000:1 đã được người dùng xác nhận và chốt.** Dùng `Ithứ cấp = Isơ cấp / 1000` cho một lượt dây sơ cấp. Không tự ghi lại là “giả thiết” hoặc “chưa xác nhận”. Nguồn xác nhận là người dùng; không gọi là thông số đã đo hoặc datasheet hãng đã kiểm nếu chưa có bằng chứng đó. Việc chốt tỷ số không đồng nghĩa chốt burden, dải tuyến tính hoặc băng thông.

- Chỉ sửa file và phần được yêu cầu; giữ các phần khác nguyên trạng.
- Ưu tiên sửa cục bộ. Không dựng lại toàn bộ file từ script hoặc bản cũ khi chỉ cần sửa một phần.
- Không tự sửa tài liệu PCB/schematic khi yêu cầu chỉ liên quan module.
- Không tự tạo hoặc cập nhật ZIP, bản sao, tài liệu phụ hay ảnh nếu yêu cầu hiện tại không cần chúng.
- Trước khi hoàn thành, kiểm tra phần thay đổi không đưa lại nội dung đã bị xóa, không đổi thông số hoặc số lượng ngoài phạm vi yêu cầu.
