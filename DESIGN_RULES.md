# Quy tắc thiết kế và trình bày

## Quy tắc ưu tiên

**Phần người dùng đã xóa phải tiếp tục được để xóa. Không tự thêm lại, kể cả dưới cách diễn đạt hoặc vị trí khác. Chỉ khôi phục khi người dùng yêu cầu rõ ràng.**

Bản hiện tại trên đĩa là cơ sở chỉnh sửa. Quy tắc này áp dụng cho cả đoạn mở đầu và phần giới thiệu; không mặc định chúng phải được bổ sung vào mỗi tài liệu.

**Giữ nguyên những phần người dùng đã tự chỉnh sửa.** Trước mỗi lần sửa file, đọc bản hiện tại trên đĩa. Nếu nhận thấy một phần đã được người dùng chỉnh sửa từ trước, không tự ý sửa lại, viết lại, định dạng lại hoặc ghi đè phần đó, trừ khi người dùng yêu cầu chỉnh sửa chính phần đó. Không dùng bản cũ để thay thế nội dung hiện tại. Nếu không chắc phần đó có phải do người dùng chỉnh sửa hay không, giữ nguyên; nếu cần thay đổi để thực hiện yêu cầu, hỏi rõ trước.

## Cấu hình đã chọn

- Mạch quang cố định: TIA_LIGHT → R6 1 kΩ → X → R7 1 kΩ → ADC_LIGHT/PA1; C5 10 nF từ X xuống GND, C6 10 nF từ ADC_LIGHT xuống GND (ký hiệu theo ảnh module). Hai trở và hai tụ là linh kiện lắp cố định. Không trình bày lựa chọn hoặc phép so sánh L0/L2; không hướng dẫn nối thẳng hoặc bỏ lọc. Kiểm đáp ứng xung trên nguyên mạch đã lắp.

- Module truyền thông node và gateway là hai bo hoàn chỉnh theo ảnh người dùng cung cấp. Dùng linh kiện phụ trợ đã tích hợp, không mặc định thêm R/C ngoài. Bộ đổi mức UART chỉ xem xét sau khi kiểm module thực; không coi ảnh là bằng chứng RO đã tương thích 3,3 V. Quy tắc này không loại các R/C cần cho CT, BIAS, MCP6002 và lọc analog tự lắp, cũng không loại linh kiện phụ trợ IC rời trong BOM PCB.

- **CT DL-CT08CL6-1000/1 có tỷ số 1000:1, đã chốt theo xác nhận của người dùng.** Với một lượt dây sơ cấp: `Iout = Iin / 1000`; ví dụ 10 A AC cho dòng thứ cấp danh định 10 mA. Không ghi tỷ số là giả thiết hoặc chưa xác nhận. Tỷ số danh định không thay thế kiểm tra burden cho phép, tuyến tính, bão hòa, dải dòng và đáp ứng tần số; không coi ví dụ này là số đo thực nghiệm.

- Một node: Blue Pill STM32F103, CT, BPW34, hai MCP6002 và module MAX3485 ở giai đoạn thử.
- PCB node dùng cấu hình trong BOM/schematic hiện hành; không tự đổi mã, giá trị, chân hoặc footprint.
- Một gateway: ESP32 DevKit và module MAX13487E hiện có. Gateway tiếp tục dùng module khi node chuyển sang PCB.
- Node dùng adapter 5 V riêng; gateway lấy nguồn USB laptop.
- Node–gateway dùng RS485; gateway–laptop dùng USB. Không tự bổ sung LoRa, pin, cloud hoặc chức năng ngắt điện.
- Mạch thực của module MAX13487E chưa được xác nhận; không đoán header hoặc mặc định mức UART tương thích ESP32.

## Lưu trữ phụ lục

- Khi người dùng yêu cầu tạo file phụ lục, lưu tại thư mục `Phu_luc/` ở gốc dự án. Không tạo trong `module/` hoặc `module/Phu_luc/`, trừ khi người dùng yêu cầu vị trí khác. Dùng đường dẫn ảnh và liên kết tương đối phù hợp với vị trí file.

## Trình bày tài liệu module

- Công thức toán phải dùng LaTeX trong Markdown: `$...$` cho công thức trong dòng, `$$` trên các dòng riêng để bao công thức đứng riêng; chừa dòng trống trước và sau khối công thức. Không đặt công thức trong khối mã hoặc dấu backtick. Viết đúng cú pháp chỉ số, phân số và đơn vị; không escape dấu `_` bên trong công thức thành `\_`.
- Viết tiếng Việt ngắn, dễ hiểu; mỗi bước một thao tác.
- Tiêu đề mục và tiêu đề in đậm dùng cụm từ cô đọng, ngắn gọn, thể hiện đúng nội dung; không dùng câu hỏi làm tiêu đề. Khi chỉ yêu cầu đổi tiêu đề, giữ nguyên từng chữ trong nội dung bên dưới.
- Trình bày trực tiếp nội dung kỹ thuật và đặt trích dẫn dạng [n] ngay sau ý được dẫn nguồn. Không thêm lời dẫn như “tài liệu cho biết”, “theo tài liệu” hoặc “phù hợp với quy luật trong tài liệu”; thông tin nguồn đặt ở mục tài liệu tham khảo.
- Phần 1 chỉ có ba mục: **1.1 Node**, **1.2 Gateway**, **1.3 Các phần bên ngoài**.
- Phần 2 chỉ có ba mục: **2.1 Nhận diện MCP6002 DIP-8**, **2.2 Nối dây node**, **2.3 Nối dây gateway**. Trong node chỉ chia nhóm bằng tiêu đề ngắn; giải thích R/C bằng chức năng, công thức và ví dụ tính cần thiết, không tách thành nhiều mục nhỏ lặp thao tác.
- Ảnh dùng trong Markdown chỉ giữ PNG; không tự tạo lại SVG hoặc ảnh không được sử dụng. Sau khi thay hình hoặc rút gọn nội dung, kiểm và xóa ảnh hết tham chiếu trong thư mục minh họa.
- Trong Node/Gateway, nhóm theo khối nguồn nếu có, MCU, dòng, quang và truyền thông. Không tạo khối không có trong thiết bị.
- Phần bên ngoài gồm nguồn cấp, dây, tải thử, nguồn sáng, dụng cụ và dự phòng; ghi rõ đồ dùng lại khi thử PCB.
- Ghi chú trong bảng phải ngắn, dùng từ dễ hiểu. Không lặp lại cả hướng dẫn đấu dây trong ô ghi chú.
- Giữ đủ linh kiện phụ trợ; phân biệt lắp cố định, có điều kiện và dự phòng. Không cộng trùng linh kiện trên module hoặc đồ tái sử dụng.
- Khi yêu cầu bảng mua bổ sung, dùng bốn cột: **Linh kiện cần bổ sung | Giai đoạn phục vụ | Số lượng mua mới | Lý do**.

## Tính chính xác và hình minh họa

- Không tự đổi thông số để rút gọn tài liệu. Lỗi kỹ thuật phải được chỉ rõ và sửa có căn cứ.
- Phân biệt cấu hình đề xuất, phép tính, giới hạn datasheet và số đo thực. Không tự điền kết quả hoặc ghi “đạt chuẩn”.
- Vẽ sơ đồ điện bằng SVG/công cụ kỹ thuật; không dùng ảnh AI hoặc pinout module phỏng đoán.
- Khi có yêu cầu tạo hình, đối chiếu hình với bảng chân, R/C, nguồn và GND; xuất PNG và dùng đường dẫn tương đối trong Markdown.
