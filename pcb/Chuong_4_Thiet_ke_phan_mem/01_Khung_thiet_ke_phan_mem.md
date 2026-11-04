# 4.1. Phạm vi phần mềm

Đây là khung chuẩn bị Chương 4 — Thiết kế phần mềm. Phần mềm được phát triển và kiểm thử trước trên bộ module tại nhà, sau đó áp dụng sang PCB node với cấu hình phù hợp bo thực.

- **Chương 3:** thiết kế phần cứng PCB trong thư mục `pcb/Chuong_3_Thiet_ke_phan_cung/`.
- **Module nháp:** bộ dựng song song để kiểm thử và dự phòng trong `module_nhap/`, không đưa vào Chương 3.
- **Chương 4:** kiến trúc chương trình, lấy mẫu, xử lý dữ liệu, thuật toán và truyền thông.
- **Chương thực nghiệm:** lưu kết quả đo, sai số và đánh giá khả năng hoạt động của hệ thống.

# 4.2. Kiến trúc chương trình

| Thành phần | Nhiệm vụ dự kiến |
|---|---|
| Node STM32 | Thu hai kênh dòng và quang; xử lý dữ liệu; chạy thuật toán; trả kết quả qua RS485 |
| Gateway ESP32 | Hỏi node; tiếp nhận và kiểm tra bản tin; chuyển dữ liệu qua USB về laptop |
| Laptop | Hiển thị, lưu dữ liệu và hỗ trợ đối chiếu các lần thử |

Luồng dữ liệu: **cảm biến → mạch analog → ADC node → xử lý và thuật toán → RS485 → gateway → USB → laptop**.

# 4.3. Lấy mẫu và xử lý tín hiệu

Các nội dung sẽ thiết kế:

1. Chọn tần số lấy mẫu từng kênh theo tín hiệu cần quan sát và bộ lọc analog hiện có.
2. Chọn cơ chế định thời, thu mẫu và tổ chức bộ đệm; xác định cách phát hiện mất mẫu hoặc tràn bộ đệm.
3. Xác định mốc thời gian giữa hai kênh để kết hợp thông tin dòng và quang.
4. Xử lý mức nền, tính đặc trưng dòng và quang trên cửa sổ dữ liệu.
5. Phân biệt dữ liệu hợp lệ, tín hiệu bão hòa và lỗi thu mẫu.

Nhịp 1.000 mẫu/giây trong bài thử phần cứng là cấu hình kiểm sơ bộ, chưa phải cấu hình chính thức của thuật toán. Tần số lấy mẫu, kích thước cửa sổ, hệ số quy đổi và ngưỡng xử lý sẽ được ghi cùng căn cứ lựa chọn; giá trị hiệu chỉnh được đối chiếu với dữ liệu thực nghiệm.

# 4.4. Thuật toán nhận biết và trạng thái

Các nội dung sẽ xây dựng:

- Đặc trưng sử dụng từ kênh dòng và kênh quang.
- Điều kiện kết hợp hai kênh và khoảng thời gian xét sự kiện.
- Điều kiện xác nhận, duy trì và xóa trạng thái cảnh báo trên dữ liệu.
- Cách xử lý khởi động, dữ liệu thiếu, bão hòa và mất liên lạc.
- Các trường dữ liệu lưu lại để giải thích vì sao thuật toán đưa ra kết quả.

Ngưỡng và thời gian xác nhận chưa chốt trong khung này. Thử tải và chiếu đèn hỗ trợ kiểm luồng xử lý; kết luận khả năng phát hiện hồ quang được đánh giá riêng bằng thực nghiệm phù hợp.

# 4.5. Truyền thông và lưu dữ liệu

1. Kế thừa cấu hình UART thử hiện có 115200 baud, 8N1 làm điểm bắt đầu.
2. Thiết kế định dạng yêu cầu và phản hồi, gồm nhận diện bản tin, số thứ tự, dữ liệu đo, trạng thái và cơ chế kiểm lỗi.
3. Chọn chu kỳ hỏi, thời gian chờ và cách xử lý bản tin thiếu, sai hoặc trùng.
4. Tách nhịp thu mẫu tại node khỏi nhịp hỏi dữ liệu của gateway.
5. Thiết kế dữ liệu log gồm thời gian, phiên bản chương trình, cấu hình thử, dữ liệu đo và trạng thái lỗi.

# 4.6. Danh sách lưu đồ

| Lưu đồ sẽ vẽ | Nội dung |
|---|---|
| Tổng thể hệ thống | Quan hệ node, gateway và laptop |
| Chương trình node | Khởi tạo, thu mẫu, xử lý, cập nhật trạng thái và phản hồi |
| Thu nhận dữ liệu | Định thời, bộ đệm, dữ liệu sẵn sàng và lỗi thu mẫu |
| Thuật toán | Tính đặc trưng, kết hợp hai kênh và chuyển trạng thái |
| Truyền thông node | Nhận yêu cầu, kiểm bản tin, trả lời và đổi chiều RS485 |
| Chương trình gateway | Gửi yêu cầu, chờ phản hồi, xử lý lỗi và chuyển dữ liệu USB |
| Hiển thị và lưu log | Nhận dữ liệu, hiển thị trạng thái và lưu phiên thử |

# 4.7. Trình tự triển khai và kiểm thử

| Giai đoạn | Công việc | Đầu ra |
|---|---|---|
| Tại nhà — thiết kế | Chốt kiến trúc, cấu hình thu mẫu, giao thức và lưu đồ | Bản thiết kế đủ để viết chương trình |
| Tại nhà — phần mềm | Lập trình node, gateway và phần hiển thị/log; thử từng chức năng rồi ghép hệ thống module | Bộ module chạy toàn luồng, log thực và danh sách lỗi |
| Lab lần 1 — module | Mang hệ thống đã tích hợp để đo dạng sóng, đối chiếu tín hiệu trước/sau lọc trên nguyên mạch và dữ liệu phần mềm | Ảnh/CSV máy hiện sóng, cấu hình đo và các điểm cần hiệu chỉnh |
| Tại nhà — hoàn thiện và hàn PCB | Xử lý vấn đề từ lần đo module; hàn, kiểm nguồn PCB và xác nhận cấu hình chương trình phù hợp bo | PCB chạy được các bài thử chức năng trước khi tới lab |
| Lab lần 2 — PCB | Đo lại trên PCB với các điều kiện có thể đối chiếu với bộ module | Kết quả đo PCB và so sánh với module |

Hai lần lên lab là kế hoạch dự kiến. Kết quả module giúp kiểm chứng phần mềm và giữ bộ dự phòng; hoạt động của PCB vẫn được xác nhận bằng phép thử riêng. Các số đo và kết luận chỉ điền sau khi thực hiện.

# 4.8. Thứ tự công việc tiếp theo

1. Chốt dữ liệu đầu ra và yêu cầu của thuật toán.
2. Thiết kế lấy mẫu, bộ đệm và mốc thời gian hai kênh.
3. Chốt cấu trúc bản tin và dữ liệu log.
4. Vẽ lưu đồ node, thuật toán và gateway.
5. Viết chương trình, kiểm thử từng khối và tích hợp trên bộ module.
