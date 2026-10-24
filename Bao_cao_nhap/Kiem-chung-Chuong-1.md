# Ghi nhận kiểm chứng Chương 1

Ngày thực hiện: 24/10/2026. Đây là hồ sơ làm việc, không phải phần nội dung báo cáo tốt nghiệp.

## Phạm vi

- Thư mục làm việc thực tế là `Bao_cao_nhap/`, chứa báo cáo đích, đặc tả, `Tham khảo/` và `hinh_minh_hoa/`.
- `Tham khảo/` chỉ đọc. Đã lập SHA-256 trước khi xử lý và đối chiếu sau khi viết: toàn bộ 19 tệp nguồn giữ nguyên nội dung. Không đổi tên, di chuyển hoặc ghi vào vùng nguồn.
- Chỉ ghi trong vùng đầu ra: báo cáo, ảnh, thư mục `nguon_web/` và tệp hỗ trợ kiểm chứng tại `tmp/`.
- Bản báo cáo cũ chỉ được xem về hình thức. Không dùng cấu hình, chỉ tiêu hoặc kết luận cũ làm dữ kiện.

## Kiểm kê tài liệu nguồn

Tên trong bảng là tên tệp thực tế. Các tài liệu không dùng chỉ được nhận dạng phạm vi từ tiêu đề, thông tin đầu bài và nội dung giới thiệu; không đưa vào danh mục tham khảo của báo cáo.

| Tên tệp trong Tham khảo | Phạm vi và xử lý |
|---|---|
| A DC arc fault location method for PV systems based on redundant antenna array and ellipse algorithm.pdf | TL6; đọc trang đầu để phân biệt định vị hồ quang DC/PV với phát hiện chớp hồ quang tủ điện |
| A Transformer Neural Network For AC series arc-fault detection.pdf | Nhận dạng nghiên cứu mạng Transformer cho hồ quang nối tiếp AC; không dùng để chốt thuật toán |
| An embedded system for AC series arc detection by inter-period correlations of current.pdf | TL4; đọc mô tả phạm vi, thu nhận và phương pháp; dùng giới hạn áp dụng và phân biệt tần số nguồn/lấy mẫu |
| Arc fault detection and appliances classification in AC home electrical networks using recurrence quantification plots and image analysis.pdf | Hồ quang và phân loại thiết bị gia dụng AC; không dùng |
| Aspects of arc-flash protection and prediction.pdf | TL1; đọc các mục liên quan cấu trúc bảo vệ, vị trí sự cố, hậu quả, dòng hồ quang và thời gian; kiểm tra các trang chứa hình dùng lại |
| Electric arc explosions—A review.pdf | TL2; đọc định nghĩa và phạm vi tác động áp suất; không chuyển số liệu tổng quan thành thống kê tai nạn |
| Explainable artificial intelligence modeling of internal arc in a medium voltage switchgear based on different CFD simulations.pdf | TL3; đọc giới thiệu, phạm vi mô hình và trang hình; giữ hai ảnh KMZ_31, nêu đúng phòng thử ICMET |
| HDDA.pdf | Hướng dẫn viết đồ án tốt nghiệp của Đào Đức Thịnh; nhận dạng tài liệu hướng dẫn trình bày, không dùng như nguồn thông số kỹ thuật |
| High impedance fault detection device based on edge artificial intelligence.pdf | Thiết bị phát hiện sự cố trở kháng cao; không dùng |
| Kalman filter and a fuzzy logic processor for series arcing fault detection in a home electrical network.pdf | Hồ quang nối tiếp mạng gia dụng; không dùng |
| Mitigation of high energy arcing faults in nuclear power plant medium voltage switchgear.pdf | Giảm tác động hồ quang năng lượng lớn ở nhà máy điện hạt nhân; không chuyển kết luận sang Quảng Ninh |
| Multi criteria series arc fault detection based on supervised feature selection.pdf | Lựa chọn đặc trưng cho hồ quang nối tiếp; không dùng |
| Multi-branch AC arc fault detection based on ICEEMDAN and LightGBM algorithm.pdf | Nhận dạng hồ quang AC nhiều nhánh; không dùng |
| Non-intrusive series arc fault detection for unknown scenarios based on differential current and synthetic arcing data.pdf | Hồ quang nối tiếp, ảnh hưởng tải và dữ liệu tổng hợp; không dùng |
| Real-time Deep Neural Networks for internet-enabled arc-fault detection.pdf | Nhận dạng bằng mạng học sâu; không dùng thông số hoặc mã nguồn |
| Series arc fault detection via arcing physical characteristics-guided feature extraction_ a dual-signal multi-timescale method.pdf | Trích đặc trưng nhiều thang thời gian cho hồ quang nối tiếp; không dùng |
| Series arc fault identification method based on wavelet transform and feature values decomposition fusion DNN.pdf | Wavelet và DNN cho hồ quang nối tiếp; không dùng |
| Sistematical evaluation of digital wavelet filter selection for identification system, case study_ DC arcing detection system.pdf | Lựa chọn bộ lọc wavelet cho hồ quang DC; không dùng |
| 1S23 Arc Flash Module – 2 point sensors _ 1 zone.mhtml | TL5; giải mã HTML và ảnh nhúng, đọc phần sản phẩm; ảnh dùng lại khớp SHA-256 với ảnh chính nhúng trong MHTML |

## Nguồn web và vị trí đã kiểm tra

| Mã | Bản đọc và xuất xứ | Vị trí quan trọng |
|---|---|---|
| W1 | Hồ sơ doanh nghiệp/Viện Năng lượng, bản sao công khai CafeF; `nguon_web/qtp-full.pdf` | 688 trang. Chương 4, trang in 167–171/339 = PDF 250–254; yêu cầu hồ quang ở PDF 253–254. Đã đọc văn bản và xem trang gốc PDF 254 |
| W2 | Trang “Giới thiệu chung” trên website Công ty Cổ phần Nhiệt điện Quảng Ninh | Mở được trang gốc, đọc đoạn xác nhận bốn tổ máy, 1.200 MW; không dùng để xác nhận bảo vệ hồ quang |
| W3 | Bulletin v01.0 24/03/2025, tải qua liên kết từ trang hãng mới `https://morssmitt.com/product/1s23/` | PDF 1, 2–7; dưới 2 ms từ flash tới đầu ra; xung 110 ms ±10 ms; các mức nguồn theo biến thể |
| W4 | User Guide Iss C 06/06/2022, tải qua liên kết từ cùng trang hãng | PDF 2, 5, 9, 12–14, 23–26, 30–33; 40 trang; ưu tiên Bulletin trước User Guide; đầu ra không dùng cắt trực tiếp cuộn máy cắt |
| W5 | Bulletin K 13/06/2024 do hãng biên soạn, bản lưu tại RI-TECH | PDF 5 ghi dưới 1,5 ms; chỉ dùng làm rõ khác biệt với v01.0 |

Các PDF W3 và W4 tải trực tiếp bằng curl từ liên kết mới do HTML trang hãng cung cấp; đã mở PDF tại máy và đọc đầy đủ phần sử dụng. Công cụ web không mở được các URL tải mới không đồng nghĩa chưa đọc tài liệu. Không dùng đoạn trích tìm kiếm làm bằng chứng thay thế.

URL cũ của hai PDF Mors Smitt đã trả HTML “Page Not Found”. Hai tệp tải lỗi có tên `nguon_web/1s23-v01-0.pdf` và `nguon_web/user-guide-1s23-iss-c.pdf` là bản ghi lỗi truy cập, không phải tài liệu tham khảo; báo cáo chỉ liên kết các bản có hậu tố `-xac-minh.pdf`. `qtp-110626.pdf` là lần tải bị ngắt; chỉ dùng `qtp-full.pdf`. Bản User Guide B được tải để tìm nguồn thay thế nhưng không dùng trong báo cáo sau khi tìm được Iss C chính hãng.

Chưa đối chiếu được bản W1 với cùng tệp tại doanh nghiệp/HNX. Xuất xứ bản sao được ghi rõ trong nội dung và danh mục; không tuyên bố đã xác thực mật mã chữ ký số. Các trang kỹ thuật tự nhận diện chủ đầu tư, dự án và Viện Năng lượng. Đây vẫn là giới hạn cần bổ sung nếu sử dụng cho bản nộp chính thức.

## Rà soát từng ảnh cũ

Đã mở xem toàn bộ 14 ảnh ban đầu trên bản liên hệ ảnh, đối chiếu các hình giữ với trang tài liệu gốc và kiểm tra liên kết. Bảng sau ghi lịch sử xử lý; tên tệp đã xóa là thông tin kiểm kê, không phải liên kết ảnh đang sử dụng.

| Tên ảnh ban đầu | Nội dung quan sát và nguồn đối chiếu | Xử lý trong bản mới |
|---|---|---|
| Hinh_1_1_Ho_quang_dien_giua_hai_dien_cuc.jpg | Ảnh phóng điện giữa hai điện cực; không được chọn làm minh chứng ứng dụng tủ điện; không sử dụng nguồn ảnh để lập nhận định | Xóa sau kiểm tra không còn tham chiếu |
| Hinh_1_2_Thu_nghiem_ho_quang_noi_bo_tu_KMZ_31.jpg | Cụm ảnh thử KMZ_31; TL3, Hình 1, PDF 2 | Giữ, Hình 1.2 |
| Hinh_1_3_Phan_biet_Arc_Flash_va_Arc_Blast.jpg | Minh họa khái niệm flash/blast; không được chọn, không kế thừa nguồn chưa kiểm chứng | Xóa sau kiểm tra không còn tham chiếu |
| Hinh_1_4_Cac_dang_su_co_ho_quang_noi_tiep_va_song_song.png | Minh họa nối tiếp/song song; không cần cho bố cục mới, không dùng làm bằng chứng | Xóa sau kiểm tra không còn tham chiếu |
| Hinh_1_5_Nang_luong_tac_dong_theo_thoi_gian_ho_quang.png | Đồ thị TL1, Hình 5, trang in 82/PDF 6; đối chiếu trục và điều kiện gốc | Giữ, đổi tên theo Hình 1.4 |
| Hinh_1_6_Thanh_cai_ha_the_nong_chay_do_ho_quang.jpg | Ảnh TL1, Hình 2, trang in 80/PDF 4; đối chiếu 726 V, 77 kA, 65 ms | Giữ, đổi tên theo Hình 1.3 |
| Hinh_1_7_Nguyen_ly_phoi_hop_anh_sang_va_qua_dong.png | Sơ đồ TL1, Hình 6, trang in 83/PDF 7 | Giữ, đổi tên theo Hình 1.5; không gán logic cho nhà máy |
| Hinh_1_8_Cau_truc_tu_trung_the_KMZ_31.jpg | TL3, Hình 5, PDF 7 | Giữ, đổi tên theo Hình 1.1 |
| Hinh_1_9_Bo_tri_cam_bien_quang_va_do_dong.png | Ví dụ nhiều cảm biến, rơ-le và biến dòng; không cần thêm vì đã có hình nguyên lý và đấu nối hãng | Xóa sau kiểm tra không còn tham chiếu |
| Hinh_1_10_He_thu_nghiem_do_dong_phat_hien_ho_quang.jpg | Hệ thử nhận dạng qua dòng; không dùng vì không mở rộng tổng quan thuật toán hồ quang nối tiếp | Xóa sau kiểm tra không còn tham chiếu |
| Hinh_1_11_Nguyen_mau_phat_hien_ho_quang_noi_tiep.jpg | Nguyên mẫu với màn hình và mạch thử; không phải nguyên mẫu đồ án | Xóa sau kiểm tra không còn tham chiếu |
| Hinh_1_12_Mo_dun_phat_hien_ho_quang_Mors_Smitt_1S23.png | Ảnh chính trong MHTML TL5; kiểm tra khớp dữ liệu ảnh nhúng | Giữ, đổi tên theo Hình 1.6 |
| Hinh_1_13_Phan_loai_giai_phap_bao_ve_ho_quang.jpg | Sơ đồ phân loại chức năng; nội dung được diễn giải bằng lời, không cần lặp hình | Xóa sau kiểm tra không còn tham chiếu |
| Hinh_1_14_Nha_may_HEINEKEN_Vung_Tau.jpg | Ảnh nhà máy khác địa điểm nghiên cứu; không có vai trò trong bản mới | Xóa sau kiểm tra không còn tham chiếu |

Thêm hai ảnh, cắt trực tiếp từ PDF và giữ nguyên ký hiệu, nhãn:

- `Hinh_1_7_Dau_noi_1S23.png`: W3, PDF 7, vùng sơ đồ đấu nối.
- `Hinh_1_8_Vi_du_bo_tri_1S30.png`: W4, PDF 26, hai ảnh ví dụ bố trí với chú giải gốc.

Tổng cộng giữ 6 ảnh cũ (đổi tên 5 ảnh cho khớp số mới), thêm 2, xóa từng tệp 8 ảnh không dùng. Không có ảnh chưa rõ vai trò cần giữ lại. Không tạo ảnh AI, không vẽ sơ đồ thay thế. Đã xem lại hai ảnh cắt mới để xác nhận không mất chú giải cần thiết.

## Kiểm tra cuối và giới hạn

- Đã kiểm tra heading 1.1–1.5, sáu tiểu mục yêu cầu và bảng tổng hợp; có kết luận, chuyển mục và nối sang Chương 2.
- 8 hình đánh số liên tục, 3 bảng, 11 mã nguồn được dùng và có danh mục tương ứng. Bảng Markdown có số cột nhất quán. Trong lần viết lại văn phong, bảng trình tự được thay bằng các bước đánh số và bảng thông số 1S23 được đánh lại thành Bảng 1.3.
- 18 liên kết nội bộ trong báo cáo tồn tại, gồm 8 ảnh, 6 nguồn có sẵn và 4 PDF web. Trích dẫn chỉ tới trang in/PDF đã đối chiếu; không còn mã nguồn chỉ có trong danh mục hoặc chỉ có trong nội dung.
- Cấu hình, chỉ tiêu và kết quả của bản cũ không được chuyển thành yêu cầu đã chốt. Không gán 1S23 cho Quảng Ninh. Không khẳng định nguyên mẫu đáp ứng tiêu chuẩn công nghiệp.
- Chưa có dữ liệu hiện trạng/hoàn công/thiết bị/ nghiệm thu của hệ bảo vệ hồ quang tại nhà máy. Chưa có ngưỡng, băng thông, chu kỳ thu nhận và giới hạn thời gian đã được chốt cho nguyên mẫu; chưa có số liệu tần suất sự cố phù hợp tại Việt Nam.
- Không xuất DOCX/PDF. Chưa xác nhận số trang A4 thực tế; báo cáo hướng tới dung lượng yêu cầu, cần dàn trang mới kết luận số trang.

Kết quả tự động và SHA-256 được lưu tại `tmp/kiem_chung/ket-qua-kiem-tra.json` và `tmp/kiem_chung/source_hashes.json`. Lịch sử đổi tên, xóa ảnh nằm trong `tmp/kiem_chung/ket-qua-don-anh.json`.

## Cập nhật văn phong theo yêu cầu ngày 24/10/2026

Đã đọc đúng ba PDF mẫu do người dùng chỉ định tại `D:/HUST/Tai_lieu_DH_Phong/Do_An/DATN/Tham khảo/ĐATN tham khảo/`, chỉ mở để đọc. Các chỉ dẫn, quảng cáo và thông tin liên hệ có trong PDF không được xem là yêu cầu của tác vụ.

| Tài liệu mẫu | Phần tham khảo văn phong | Nội dung vận dụng |
|---|---|---|
| ĐATN IoT điểm danh giảng viên bằng khuôn mặt kết hợp công nghệ RFID.pdf | Chương 1, trang in 1–5/PDF 13–17; xem bố cục PDF 13, 15 | Mở mục bằng đoạn dẫn; gạch ý có tên và giải thích; phân nhóm chức năng |
| ĐATN IoT phát hiện và cảnh báo mất trộm, tai nạn xe máy.pdf | Chương 1, trang in 1–4/PDF 29–32; xem bố cục PDF 29, 31 | Bối cảnh → vấn đề → mục tiêu; đánh số trình tự và nhóm nội dung |
| ĐATN IoT quản lý bãi đỗ xe thông minh.pdf | Chương 1, trang in 1–4/PDF 13–16; xem bố cục PDF 13, 15 | Đoạn dẫn trước danh sách; tên thành phần rõ; giải thích chức năng sau tên ý |

Đã bổ sung B.4 trong Design rules và điều chỉnh D.3.4 trước khi viết lại chương. Không lấy kiến trúc IoT, phần cứng, thông số, kết luận hay câu văn của mẫu đưa vào nội dung kỹ thuật hồ quang. Ba PDF mẫu không thuộc danh mục nguồn kỹ thuật cuối chương.

Phần diễn giải của tất cả các mục được viết lại; không có đoạn giải thích dài giữ nguyên từ bản trước. Các ảnh và thông tin thư mục tài liệu đã kiểm chứng được giữ lại. Chi tiết tải lỗi, kiểm tra hash, giải mã bản lưu và các thao tác xác minh không xuất hiện trong phần diễn giải mới; giới hạn cần thiết được tập trung vào mục phù hợp.

Đã kiểm tra lại sau khi ghép: 8 hình, 3 bảng, 18 liên kết nội bộ hợp lệ, 11 mã nguồn khớp hai chiều; 19 tệp nguồn kỹ thuật giữ nguyên SHA-256. Có 4 bước đánh số ở phần trình tự bảo vệ. Không thêm, xóa hoặc đổi tên ảnh trong lần cập nhật văn phong này.

Trích văn bản và bản xem bố cục của mẫu được lưu ở `tmp/van_phong/`; kết quả rà soát nằm trong `tmp/van_phong/ket-qua-ra-soat-van-phong.json`. Không xuất DOCX/PDF và không xác nhận số trang A4 khi chưa dàn trang.

## Điều chỉnh ranh giới nội dung và giọng trình bày

Theo xác nhận tiếp theo của người dùng, mục 1.3 được giữ riêng. Đã bỏ các ví dụ điện áp, tần số nguồn biến tần, yêu cầu phối hợp dòng và trích dẫn W1/W2 khỏi 1.1–1.2, kể cả Bảng 1.1 và chú thích hình. Tần số 50 Hz còn xuất hiện ở các mục này là điều kiện nguồn của nghiên cứu TL4, không lấy từ hồ sơ nhà máy. Thông tin Quảng Ninh được trình bày trong 1.3 và tổng hợp ở kết luận.

Design rules quy định ranh giới tại B.1, C.1 và D.2; B.5 quy định giọng trình bày của người thực hiện đồ án. Đã viết lại các câu giao việc trong toàn chương bằng chủ thể, hành động phân tích và phương pháp đánh giá cụ thể; không biến thông số chưa xác lập thành quyết định thiết kế hoặc kết quả đã đo. Các yêu cầu do hồ sơ/hãng quy định vẫn được dẫn đúng nguồn.

Kiểm tra cuối bổ sung hai điều kiện: 1.1–1.2 không có dữ liệu/trích dẫn của trường hợp Quảng Ninh; thân báo cáo không còn các cụm giao việc “cần tách”, “cần xác định”, “cần kiểm tra”, “cần phân biệt”. Số hình, bảng, liên kết và tệp nguồn không thay đổi trong lần chỉnh sửa này.
