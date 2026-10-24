from pathlib import Path
import re

root=Path(__file__).resolve().parents[2]
rp=root/'Design-rules-Chuong-1.md'
r=rp.read_text(encoding='utf8')
r=r.replace('**1.1 Tổng quan bài toán → 1.2 Phân tích yêu cầu kỹ thuật → 1.3 Trường hợp nhà máy Việt Nam → 1.4 Thiết bị thương mại 1S23 → 1.5 Kết luận chương**','**1.1 Tổng quan bài toán → 1.2 Phân tích yêu cầu kỹ thuật → 1.3 Phân tích quy trình tại Nhà máy Nhiệt điện Quảng Ninh → 1.4 Kết luận chương**')
r=r.replace('- Phần lựa chọn cảm biến, vi điều khiển, linh kiện, bảng so sánh linh kiện và lý do chọn linh kiện chuyển sang **Chương 2 – Cơ sở lý thuyết** theo yêu cầu của người dùng. Nhiệm vụ hiện tại không viết Chương 2.','- Toàn bộ phần khảo sát, mô tả thiết bị thương mại Mors Smitt 1S23 (cấu hình, giao diện, nguyên lý, thông số, bố trí cảm biến, kiểm tra và đối chiếu phiên bản) dành cho **Chương 2**. Chương 1 không có mục khảo sát thiết bị và không rải mô tả hoặc thông số sản phẩm vào các mục khác. Phần lựa chọn cảm biến, vi điều khiển, linh kiện và bảng so sánh linh kiện cũng dành cho Chương 2. Nhiệm vụ hiện tại chỉ chỉnh Chương 1 và Design rules, chưa viết Chương 2.')
r=r.replace('`# 1.5. Kết luận chương`; cuối cùng `# Tài liệu tham khảo của Chương 1` không đánh thành mục 1.6.','`# 1.4. Kết luận chương`; cuối cùng `# Tài liệu tham khảo của Chương 1` không đánh thành mục 1.5.')
r=r.replace('| Mở đầu và 1.1 | 2,5–3 trang |\n| 1.2 | 2–2,5 trang |\n| 1.3 | 2–2,5 trang |\n| 1.4 | 2,5–3 trang |\n| 1.5 và tài liệu tham khảo | 1–2 trang |','| Mở đầu và 1.1 | 3–4 trang |\n| 1.2 | 3–4 trang |\n| 1.3 | 2,5–3,5 trang |\n| 1.4 và tài liệu tham khảo | 1–2 trang |')
r=r.replace('khác biệt phiên bản vào 1.4.4','khác biệt phiên bản thiết bị dành cho Chương 2')
r=re.sub(r'7\. \*\*Tách báo cáo khỏi nhật ký làm việc\.\*\*[^\n]+','7. **Không tạo tệp kiểm chứng riêng.** Không tạo hoặc khôi phục `Kiem-chung-Chuong-1.md`, không xuất báo cáo kiểm chứng, nhật ký nguồn hoặc bảng kiểm thành một tài liệu giao riêng. Vẫn đọc nguồn, kiểm tra trích dẫn, số trang, bảng và liên kết trước khi hoàn thành; chỉ báo ngắn gọn kết quả trong tin nhắn kết thúc. Chi tiết thao tác tải, hash, giải mã và tìm nguồn không xuất hiện trong thân báo cáo.',r)
r=r.replace('Giữ bảng yêu cầu ban đầu, bảng nội dung hồ sơ và bảng thông số 1S23 theo đặc tả.','Giữ bảng yêu cầu ban đầu và bảng nội dung hồ sơ theo đặc tả. Bảng thông số thiết bị thương mại dành cho Chương 2.')
r=r.replace('xem xét một trường hợp ứng dụng tại Việt Nam và khảo sát thiết bị phát hiện hồ quang điện thương mại.','phân tích quy trình phát hiện và phối hợp bảo vệ theo hồ sơ thiết kế tại Nhà máy Nhiệt điện Quảng Ninh.')
r=r.replace('Có thể dẫn sang 1.4 để đối chiếu sản phẩm; việc đối chiếu trường hợp nhà máy được thực hiện tại chính 1.3, không đưa dữ liệu hoặc trích dẫn từ đó lên bảng này.','Không dùng thông số thiết bị thương mại làm ví dụ hoặc chỉ tiêu; khảo sát sản phẩm dành cho Chương 2. Việc đối chiếu trường hợp nhà máy được thực hiện tại chính 1.3, không đưa dữ liệu hoặc trích dẫn từ đó lên bảng này.')
r=r.replace('Phần khảo sát thiết bị thương mại tiếp đó làm rõ cách triển khai chức năng ở cấp mô-đun.','Kết luận chương tổng hợp phạm vi và các yêu cầu làm cơ sở cho Chương 2.')
start=r.index('**Lời dẫn bắt buộc về ý sang 1.4:**')
end=r.index('**Đoạn chuyển sang Chương 2:**',start)
r=r[:start]+'''**Lời dẫn sang 1.4:**

> Trường hợp nhà máy làm rõ quan hệ giữa phát hiện sự cố, thông tin dòng điện và tác động cắt nguồn. Phần kết luận tổng hợp bài toán, các yêu cầu kỹ thuật và giới hạn thông tin của chương.

## D.4. `# 1.4. Kết luận chương`

Viết khoảng 2–3 đoạn: kết quả làm rõ bài toán; sáu nhóm yêu cầu; ý nghĩa và giới hạn của trường hợp nhà máy; liên hệ với cơ sở lý thuyết và thiết kế ở Chương 2. Không khảo sát sản phẩm, không bổ sung thông số hoặc chức năng mới. Chương 2 dành cho cơ sở lý thuyết, khảo sát thiết bị thương mại và phân tích lựa chọn linh kiện.

'''+r[end:]
r='\n'.join(line for line in r.splitlines() if not (line.startswith('| ') and any(x in line for x in ['File MHTML','https://kmet.com.vn/','https://www.morssmitt.com/','| 1.4 | Ảnh 1S23'])))+'\n'
r=r.replace('Khoảng 5–8 hình có ích là định hướng nếu đủ nguồn và phù hợp độ dài.','Khoảng 3–5 hình có ích là định hướng nếu đủ nguồn và phù hợp nội dung. Ảnh thiết bị thương mại dành cho Chương 2, không chèn để kéo dài Chương 1.')
r=r.replace('Có thể nằm trong ghi chú làm việc, không phải mục nội dung báo cáo.','Chỉ dùng nội bộ trong quá trình thao tác, không tạo tệp kiểm chứng hoặc tài liệu giao riêng.')
r=r.replace('Bảng có thể nằm trong ghi chú làm việc, không phải mục nội dung báo cáo.','Bảng chỉ dùng nội bộ trong quá trình thao tác, không tạo tệp kiểm chứng hoặc tài liệu giao riêng.')
r=r.replace('bố cục 1.1–1.5','bố cục bốn phần 1.1–1.4')
r=r.replace('1.3→1.4, 1.4→1.5','1.3→1.4')
r=r.replace('- [ ] Phần 1.4 đúng 1S23, đối chiếu hãng, xử lý khác biệt phiên bản và thông số; không gán 1S23 cho nhà máy 1.3.','- [ ] Phần 1.4 là kết luận chương; không còn mục khảo sát hoặc thông số thiết bị thương mại trong Chương 1. Nội dung đó dành cho Chương 2.')
r=r.replace('- [ ] Chỉ thay đổi trong vùng đầu ra; `Tham khảo/` giữ nguyên.','- [ ] Chỉ thay đổi trong vùng đầu ra; `Tham khảo/` giữ nguyên.\n- [ ] Không tạo hoặc khôi phục tệp kiểm chứng riêng; vẫn kiểm tra nguồn và liên kết trước khi hoàn thành.')
rp.write_text(r,encoding='utf8')

p=root/'Chuong-1-Tong-quan-de-tai.md'
s=p.read_text(encoding='utf8')
start=s.index('# 1.4. Khảo sát thiết bị')
end=s.index('# 1.5. Kết luận chương',start)
s=s[:start]+s[end:].replace('# 1.5. Kết luận chương','# 1.4. Kết luận chương',1)

def paragraph(starts,new):
    global s
    pattern=r'^'+re.escape(starts)+r'[^\n]*'
    s,n=re.subn(pattern,lambda _:new,s,count=1,flags=re.M)
    assert n==1,starts

paragraph('Chương 1 trình bày bài toán','Chương 1 trình bày bài toán phát hiện chớp hồ quang điện, phân tích các yêu cầu kỹ thuật và quy trình phát hiện, phối hợp bảo vệ theo hồ sơ thiết kế tại Nhà máy Nhiệt điện Quảng Ninh. Kết quả phân tích là cơ sở cho phần lý thuyết và thiết kế hệ thống ở Chương 2.')
paragraph('Hình 1.1 cho thấy kết cấu','Hình 1.1 cho thấy kết cấu của tủ trung thế KMZ_31 được sử dụng trong nghiên cứu về hồ quang nội bộ. Tủ có vách bao và đường thoát khí riêng. Khi phân tích vùng giám sát, đồ án xem xét không gian từng khoang và kết cấu ngăn chia bên trong tủ. [TL3, Hình 5, tr. in/PDF 7.]')
paragraph('Phạm vi giám sát được xem xét','Phạm vi giám sát được xem xét từ toàn trạm, dãy tủ đến từng khoang tủ. Trong đó, vị trí thu nhận ánh sáng được phân tích theo vùng sự cố và kết cấu khoang. Tài liệu tổng quan minh họa một hệ bảo vệ có các cảm biến quang kết hợp với đo dòng; hình học và vùng đặt đầu thu là dữ liệu của phương án bố trí, không chỉ là số lượng cảm biến. [TL1, mục 5.6 và Hình 7, tr. in 83; tr. PDF 7.]')
paragraph('- **Điện áp tín hiệu:**','- **Điện áp tín hiệu:** Là mức điện áp tại các giao diện thu nhận và xử lý, mô tả điều kiện kết nối giữa đầu thu, khối điều hòa và khối xử lý. Đại lượng này được phân tích theo chức năng từng khối, không đồng nhất với điện áp hệ thống.')
paragraph('- **Nguồn phụ trợ:**','- **Nguồn phụ trợ:** Là nguồn nuôi bộ phát hiện và các khối liên quan. Trong phân tích thiết kế, nguồn nuôi được mô tả riêng với tín hiệu đo và điện áp thiết bị giám sát. Sự phân chia giữa cảm biến, khối vào/ra và rơ-le được minh họa trong cấu trúc hệ bảo vệ của tài liệu tổng quan. [TL1, mục 5.6 và Hình 7, tr. in 83; tr. PDF 7.]')
paragraph('- **Tín hiệu đưa vào bộ phát hiện:**','- **Tín hiệu đưa vào bộ phát hiện:** Là thông tin dòng do khối đo hoặc phần tử bảo vệ cung cấp cho quá trình xử lý. Trong cấu trúc bảo vệ quang–dòng được tổng quan, đo dòng và cảm biến ánh sáng cung cấp hai nhóm thông tin phối hợp. [TL1, mục 5.3, 5.6 và Hình 7, tr. in 81–83; tr. PDF 5–7.]')
paragraph('Vị trí đầu thu là một phần','Vị trí đầu thu là một phần của điều kiện đánh giá. Tài liệu tổng quan trình bày cảm biến điểm và cảm biến dạng vòng, đồng thời mô tả việc phân vùng phát hiện bằng các đầu thu quang. Vì vậy, độ nhạy được phân tích cùng vùng quan sát và đặc điểm bố trí. [TL1, mục 5.6, tr. in 83; tr. PDF 7.]')
paragraph('Thời gian phản hồi có ý nghĩa','Thời gian phản hồi được mô tả bằng hai mốc: thời điểm kích thích tham chiếu xuất hiện và thời điểm đầu ra điện đạt trạng thái tác động. Cách mô tả này giữ nguyên phần thu nhận trong phạm vi đánh giá, thay vì chỉ tính thời gian thực thi chương trình. Ở cấp hệ bảo vệ, tài liệu tổng quan phân biệt khâu phát hiện với phần tử thực hiện loại trừ hồ quang. [TL1, mục 5.6 và 6.2, tr. in 83–84; tr. PDF 7–8.]')
paragraph('Ngoài độ trễ, đầu ra còn có độ rộng xung.','Ngoài độ trễ xuất hiện đầu ra, một đầu ra dạng xung còn có thời gian duy trì trạng thái tác động. Độ rộng xung mô tả khoảng duy trì đó, còn độ trễ phản hồi mô tả khoảng từ kích thích đến tác động. Trong phép đánh giá, hai đại lượng được ghi nhận riêng; chúng không thay thế cho nhau hoặc cho thời gian máy cắt ngắt mạch.')
paragraph('Yêu cầu của đề tài là xác định cơ chế','Đồ án phân tích cơ chế thu nhận của từng kênh làm cơ sở lựa chọn chu kỳ. Phương pháp kiểm tra đối chiếu thời điểm nhận sự kiện với tín hiệu tham chiếu và xem xét khả năng tiếp nhận khi bộ xử lý thực hiện nhiệm vụ khác. Giá trị chu kỳ của nguyên mẫu chưa được xác lập trong chương này; việc lựa chọn được thực hiện cùng phương án thu nhận và xử lý tín hiệu ở Chương 2.')
paragraph('| YC-01 |','| YC-01 | Điện áp | Ba nhóm: điện áp hệ thống, điện áp tín hiệu, nguồn phụ trợ; dải từng cổng theo phương án nguyên mẫu | Mục 1.2.1; TL1, mục 5.6, Hình 7, tr. in 83/PDF 7 | Kiểm tra nguồn và đo mức đầu vào–đầu ra | Chưa chốt dải nguyên mẫu |')
paragraph('| YC-03 |','| YC-03 | Dòng điện | Phân tích vị trí, dạng tín hiệu và điều kiện phối hợp; ngưỡng theo phương án thu nhận | Mục 1.2.3; TL1, mục 5.3, 5.6 | Kiểm tra từng tín hiệu và tổ hợp hợp lệ | Chưa chốt giao diện, ngưỡng |')
paragraph('| YC-04 |','| YC-04 | Độ nhạy | Mô tả nguồn kích thích, bố trí thu nhận, ánh sáng nền và tình huống gây nhầm | Mục 1.2.4; TL1, mục 5.6, tr. in 83/PDF 7 | Ghi nhận đúng, bỏ sót, báo nhầm trên tập thử xác định | Chưa xác lập điều kiện đánh giá |')
paragraph('| YC-05 |','| YC-05 | Thời gian phản hồi | Đo từ kích thích tham chiếu đến đầu ra; phân biệt với độ rộng xung và thời gian cắt | Mục 1.2.5; TL1, mục 5.6, 6.2 | Đo đồng thời tham chiếu và đầu ra | Đã xác định đại lượng; chưa chốt giới hạn |')
paragraph('Phạm vi thiết bị là cơ sở xem xét tiêu chuẩn','Phạm vi thiết bị là cơ sở xem xét tiêu chuẩn áp dụng trong quá trình xác lập yêu cầu. Tài liệu tổng quan đề cập các tiêu chuẩn liên quan đến thiết bị đóng cắt. Việc lựa chọn bộ tiêu chuẩn cho nguyên mẫu dựa trên đối tượng và điều kiện áp dụng cụ thể, không suy ra khả năng tuân thủ chỉ từ chức năng phát hiện. [TL1, mục 3.2, tr. in 78; tr. PDF 2.]')
paragraph('Bảng 1.1 tổng hợp yêu cầu','Bảng 1.1 tổng hợp yêu cầu và các thông số làm cơ sở thiết kế. Các nghiên cứu về hiện tượng và bảo vệ hồ quang cung cấp căn cứ phân tích; giá trị chưa xác lập được trình bày theo trạng thái của phương án thiết kế.')
paragraph('Sau phần phân tích yêu cầu kỹ thuật,','Sau phần phân tích yêu cầu kỹ thuật, mục 1.3 trình bày một trường hợp nghiên cứu riêng ở cấp hệ thống. Kết luận chương tổng hợp phạm vi và các yêu cầu làm cơ sở cho Chương 2.')
paragraph('Trường hợp này làm rõ yêu cầu phối hợp','Trường hợp nhà máy làm rõ quan hệ giữa phát hiện sự cố, thông tin dòng điện và tác động cắt nguồn trong hồ sơ thiết kế. Phần kết luận tổng hợp các yêu cầu kỹ thuật và giới hạn thông tin của chương.')
paragraph('Hồ sơ thiết kế tại Nhà máy Nhiệt điện Quảng Ninh đặt ra','Hồ sơ thiết kế tại Nhà máy Nhiệt điện Quảng Ninh đặt ra yêu cầu phát hiện hồ quang, kết hợp đo dòng và gửi tín hiệu tới máy cắt trong phạm vi hệ biến tần trung thế. Dữ liệu hiện có xác lập được yêu cầu của hồ sơ, chưa xác nhận hiện trạng lắp đặt và vận hành của hệ bảo vệ. Các thông số chưa xác lập của nguyên mẫu được tiếp tục phân tích cùng phương án thiết kế.')
paragraph('Trên cơ sở đó, Chương 2 sẽ trình bày','Trên cơ sở đó, Chương 2 trình bày cơ sở lý thuyết về phát hiện, thu nhận và xử lý tín hiệu, khảo sát thiết bị thương mại và phân tích lựa chọn linh kiện. Những thông số chưa xác lập trong Bảng 1.1 được xem xét cùng phương án thiết kế và điều kiện đánh giá của hệ thống.')
for code in ['TL5','W3','W4','W5']:
    s=re.sub(r'^\*\*'+code+r' —[^\n]*\n*','',s,flags=re.M)
assert not re.search(r'1S23|1S30|\b(?:TL5|W3|W4|W5)\b|# 1\.5\.',s)
p.write_text(s.rstrip()+'\n',encoding='utf8')
print('Updated Design rules and Chapter 1 to four sections; retained image assets for Chapter 2.')
