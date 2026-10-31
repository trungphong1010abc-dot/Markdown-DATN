# Giải thích chọn linh kiện, nguyên lý schematic và kiểm chứng PCB

## 1. Khối nguồn: J1, U1, C1, C2

### 1.1. Vì sao chọn các linh kiện này?

J1 nhận adapter 5 V–2 A, phích DC 5.5 mm. Kích thước 5.5 mm chưa xác định đường kính lỗ trong hoặc cực tính. Chọn jack thực khớp phích và kiểm tiếp điểm bằng đồng hồ trước khi khóa footprint.

U1 LD1117S33TR tạo 3,3 V cho MCU và các IC node. LDO điều chỉnh phần tử nối tiếp bằng hồi tiếp để giữ điện áp ra, phần điện áp dư biến thành nhiệt. C1 10 µF–16 V hỗ trợ đầu vào; C2 22 µF–16 V hỗ trợ đầu ra và ổn định vòng điều khiển. Tụ đầu ra cần đáp ứng điện dung/ESR theo datasheet; không thay tantalum bằng tụ khác chỉ dựa vào cùng số µF. Tab SOT-223 của U1 nối OUT/3V3. [ST LD1117](https://www.st.com/resource/en/datasheet/ld1117.pdf)

Dòng ghi 2 A trên adapter là khả năng cấp của adapter, không phải dòng có thể lấy từ rail 3V3. Ước lượng công suất LDO: `P ≈ (Vin − Vout) × Iout + Vin × Iq`. Ví dụ tính với 5 V, 3,3 V, Iout=0,2 A, chưa kể Iq: P≈0,34 W. Dòng 0,2 A là điểm tính thử, chưa phải dòng node đã đo. Tản nhiệt còn phụ thuộc diện tích đồng, nhiệt độ môi trường và package.

### 1.2. Đo để chứng minh

1. Tắt nguồn, kiểm chập +5V–GND và +3V3–GND; chờ tụ nạp khi đo điện trở, không kết luận chập chỉ từ một tiếng bíp ngắn.
2. Kiểm cực jack và cực C1/C2, cấp nguồn lần đầu bằng nguồn bàn giới hạn dòng nếu có.
3. Đo Vin tại U1.3 và Vout tại U1.2; sau đó đo tại chân nguồn U2, U3, U4, U5 để phát hiện sụt áp đường mạch.
4. Đo dòng vào node bằng ampe kế mắc nối tiếp. Nếu chỉ đo dòng vào, ghi Iin; chưa coi đó là Iout của LDO vì còn dòng tĩnh và nhánh nguồn khác nếu có.
5. Đo ripple 3V3 bằng scope với dây mass ngắn; ghi băng thông đo, cách ghép AC/DC và vị trí probe. Thu thêm lúc MCU lấy mẫu và RS485 phát.
6. Ghi nhiệt độ vỏ U1, nhiệt độ phòng, thời gian từ lúc bật; đo đến khi nhiệt độ gần ổn định. Nhiệt vỏ chưa phải nhiệt mối nối.

| Chế độ | Vin tại U1 (V) | 3V3 tại MCU/U5 (V) | Iin (mA) | Ripple (mVpp) | T vỏ/T phòng (°C) | File scope |
|---|---|---|---|---|---|---|
| MCU chờ | … | … / … | … | … | … / … | … |
| ADC chạy | … | … / … | … | … | … / … | … |
| ADC + RS485 phát | … | … / … | … | … | … / … | … |

Đối chiếu nguồn đo với dải làm việc của từng IC và sai số U1 theo điều kiện datasheet. Nếu rail sụt khi phát, dùng ảnh scope và số dòng để phân biệt thiếu nguồn/tản nhiệt với lỗi firmware. Không kết luận ổn định chỉ từ điện áp DC trung bình.

## 2. Khối MCU: U2, nguồn, Y1, reset và SWD

### 2.1. Chọn MCU và ngoại vi tối thiểu

STM32F103C8T6 LQFP-48 có ADC, DMA, UART và SWD phù hợp hai kênh đo và truyền RS485. Cấu hình tài nguyên theo 64 KiB Flash, 20 KiB SRAM; kiểm lượng RAM thật qua linker map. Ba tụ C3/C4/C5 đặt gần ba VDD để cấp dòng xung cục bộ; C9 bổ sung điện dung rail. C6/C10 lọc VDDA phục vụ ADC. C7 thuộc NRST, C11 thuộc thạch anh. [ST DS5319](https://www.st.com/resource/en/datasheet/stm32f103c8.pdf)

Y1=8 MHz, CL=18 pF; C8/C11=27 pF. Hai tụ tải và ký sinh tạo tải nhìn từ thạch anh: `CL ≈ C8×C11/(C8+C11) + Cstray`. Với hai tụ bằng 27 pF và giả sử Cstray=4,5 pF, CL≈18 pF. Ký sinh 4,5 pF là giả thiết tính, phải kiểm khả năng khởi động trên bo. [Abracon ABM3B](https://abracon.com/Resonators/abm3b.pdf), [ST AN2867](https://www.st.com/resource/en/application_note/an2867-oscillator-design-guide-for-stm8afals-stm32-mcus-and-mpus-stmicroelectronics.pdf)

R1 kéo BOOT0 về thấp để chọn khởi động Flash. BT1 kéo NRST xuống GND khi nhấn; C7 hỗ trợ lọc nhiễu reset. H1 đưa SWDIO/SWCLK/NRST và nguồn tham chiếu ra đầu nạp. Dùng nhầm đầu ra nguồn của ST-Link làm VTref có thể cấp chồng nguồn; kiểm đầu nạp thực trước khi nối.

### 2.2. Đo clock, ADC và khả năng chạy

1. Nạp firmware kiểm tra qua SWD; ghi mã phiên bản và dung lượng Flash/RAM từ bản build.
2. Cho firmware xuất thông tin nguồn clock, PLL, tần số timer và cờ khởi động HSE. Nếu đo MCO/timer ở chân có thể truy cập thì ghi cấu hình chia tần; không suy tần số chỉ từ biến cấu hình.
3. Tránh đặt probe tải lớn trực tiếp vào chân thạch anh vì probe có thể làm sai dao động. Đo tín hiệu clock đã đệm nếu có thể.
4. Thử bật nguồn và nhấn reset lặp lại; gợi ý 20 lần mỗi phép thử, ghi số lần khởi động thành công và thời gian lên bản tin đầu tiên. Đây là số lần thử đề xuất cho bàn lab.
5. Kiểm ADC bằng nguồn DC biết trước ở mức trong dải 0–VDDA, đo đồng thời bằng đồng hồ. Khi đưa nguồn chuẩn vào PA0/PA1 phải tách đường ra analog tương ứng, không ép nguồn chuẩn đối đầu đầu ra op-amp; tắt nguồn trước khi đổi dây. Giữ nguyên các tầng RC.
6. So thời gian thu N mẫu với đồng hồ/tín hiệu timer để xác nhận fs thực; đếm overrun, mất DMA và số mẫu thiếu. Hai kênh scan được lấy ở hai thời điểm khác nhau.

ADC 12 bit: `V ≈ count × VDDA/4095`, VDDA lấy từ phép đo thực. Với VDDA=3,3 V, một bước lượng tử khoảng 0,806 mV. Sai số ADC còn có offset, gain, nhiễu, thời gian lấy mẫu và trở kháng nguồn; một bước lượng tử chưa phải độ chính xác hệ thống.

| Phép thử | Giá trị tham chiếu | Giá trị đọc/đo | Sai lệch | Số lần/lỗi | File |
|---|---|---|---|---|---|
| ADC DC mức thấp/giữa/cao | … V | … count / … V | … mV | … | … |
| Clock/timer | … Hz | … Hz | … % | … | … |
| fs từng kênh | … sample/s | … sample/s | … % | … mẫu thiếu | … |
| Bật nguồn/reset | … lần | … lần thành công | — | … lỗi | … |

## 3. Khối dòng và BIAS: U3, P1, R2–R5, C12, C13

### 3.1. Bản chất mạch

R5 từ 3V3 xuống M và R4 từ M xuống GND tạo cầu chia. `VM=V3V3×R4/(R4+R5)`; hai trở 10 kΩ cho VM≈1,65 V khi nguồn 3,3 V, dòng chia≈0,165 mA. U3B hồi tiếp điện áp đầu ra vào đầu đảo tạo bộ đệm: đầu ra bám VM nhưng có khả năng cấp/nhận dòng tốt hơn cầu chia. BIAS là mức nền của tín hiệu, không phải GND. Sai số trở, offset op-amp và tải làm BIAS thực lệch giá trị lý tưởng.

CT DL-CT08CL6-1000/1 có tỷ số **1000:1 đã chốt theo xác nhận người dùng**. Với một lượt dây sơ cấp: `Is=Ip/1000`. R2 mắc song song thứ cấp đổi dòng thành điện áp; một đầu burden về BIAS để sóng AC dao động quanh giữa dải ADC. U3A đệm tín hiệu trước R3/C12. C13 là tụ nguồn U3; không dùng C13 thay cho tụ lọc tín hiệu C12.

Ví dụ tính với Ip=5 A RMS, R2=150 Ω, dòng sin: Is=5 mA, Vburden,RMS=0,75 V; biên độ đỉnh≈1,061 V. Nếu BIAS=1,65 V thì tín hiệu lý tưởng nằm khoảng 0,589–2,711 V. Công suất burden≈3,75 mW. Phép tính chưa xác nhận burden cho phép, dải tuyến tính hoặc băng thông CT; cũng chưa chứng minh đo được 5 A trên bo thực.

R3=1 kΩ và C12=100 nF tạo lọc bậc một: `fc=1/(2πRC)≈1,59 kHz`; `|H(f)|=1/sqrt(1+(f/fc)²)`. Tại 50 Hz mô hình gần 1; tại 9 kHz còn khoảng 0,174, tương đương −15,2 dB. Nếu cần đặc trưng quanh 9 kHz, phải dùng dữ liệu để đánh giá giới hạn mạch hiện hành trước khi quyết định sửa thiết kế. Tăng fs không khôi phục thành phần analog đã suy giảm.

### 3.2. Đo và hiệu chuẩn dòng

1. Khi chưa có dòng sơ cấp, đo VM, BIAS, U3.1 và PA0; ghi nhiễu RMS và min/max. Probe dùng GND của bo làm tham chiếu.
2. Dùng lại bộ thử cách ly 12 VAC và các nhánh tải trong [file module](../module/01_Huong_dan_test_va_kiem_thu_module.md). Burden luôn nối vào CT trước khi chạy dòng; tắt dòng sơ cấp trước khi tháo thứ cấp.
3. Với 12 VAC và mỗi nhánh 50 Ω, dòng tính danh định là 0,24 A/nhánh; 1/2/3 nhánh cho khoảng 0,24/0,48/0,72 A. Đo dòng tham chiếu thực, không dùng các số danh định thay cho số đo. Mỗi trở tiêu tán khoảng 2,88 W nếu thực sự có 12 V RMS.
4. Thu waveform tại U3.1 và PA0 cùng thời điểm; nếu đo riêng điện áp hai đầu R2 thì dùng phép đo vi sai phù hợp. Không kẹp mass scope vào BIAS vì có thể kéo BIAS xuống đất.
5. Đo không tải và ít nhất ba mức dòng; lặp mỗi mức ba lần. Giữ một lượt/điểm độc lập để kiểm chéo hiệu chuẩn.
6. Nếu dùng N lượt dây sơ cấp xuyên CT để tăng ampere-vòng, ghi rõ N và dùng `Is=N×Ip/1000`; kết quả không đại diện tự động cho trường hợp một lượt ở dòng lớn.

Với N mẫu điện áp sau ADC, trừ trung bình: `vAC[i]=v[i]−mean(v)`; `VAC,RMS=sqrt(mean(vAC²))`. Dùng cửa sổ đủ chu kỳ, ví dụ 0,2 s chứa 10 chu kỳ ở 50 Hz. Độ nhạy đo: `S=VAC,RMS/Iref` (V/A). Sau khi xác định S từ các điểm hiệu chuẩn: `Iđo=VAC,RMS/S`; `e%=100×(Iđo−Iref)/Iref`. Không chia khi Iref=0; báo nhiễu không tải riêng. Với N lượt, quy đổi Iref theo đại lượng đang báo cáo và ghi rõ phép quy đổi.

| Mức/lần | N lượt | Iref thực (A RMS) | VAC tại U3.1/PA0 (V RMS) | Iđo (A) | Sai số (%) | Min/max, clipping | File |
|---|---|---|---|---|---|---|---|
| Không tải / … | 1 | 0 | … / … | … | — | … | … |
| Một nhánh / … | 1 | … | … / … | … | … | … | … |
| Hai nhánh / … | 1 | … | … / … | … | … | … | … |
| Ba nhánh / … | 1 | … | … / … | … | … | … | … |
| Kiểm chéo / … | 1 | … | … / … | … | … | … | … |

Dữ liệu này chứng minh độ nhạy, độ lặp và sai lệch trong dải đã thử. Muốn khẳng định dải dòng lớn hơn hoặc đáp ứng tần số phải có phép thử tương ứng; phép đo 50 Hz không xác nhận băng thông CT.

## 4. Khối quang: D1, U4, R6/C15 và hai tầng RC

### 4.1. Photodiode và TIA

D1 trong BOM mới là ams OSRAM BPW 34 S-Z, tên thư viện BPW_34_S-Z; kiểm symbol A/K và footprint đúng mã này. Photodiode tạo dòng phụ thuộc phổ và công suất ánh sáng nhận. Nó thu vùng nhìn thấy/cận hồng ngoại; không dùng số lux hoặc khoảng cách đơn lẻ thay cho năng lượng quang tới cảm biến. [ams OSRAM BPW 34 S-Z](https://ams-osram.com/products/photodetectors/photodiodes/osram-dil-smt-bpw-34-s/)

U4A dùng hồi tiếp âm qua R6 để giữ đầu đảo gần BIAS; dòng quang đi qua mạng hồi tiếp tạo điện áp đầu ra. Với cực A về GND, K vào đầu đảo theo file số 1, mô hình DC là `Vout≈BIAS+Iphoto×R6`. R6=10 kΩ cho độ nhạy lý tưởng 10 mV/µA. Đây là khuếch đại chuyển dòng–áp (TIA), không phải bộ khuếch đại điện áp chỉ xác định bằng tỷ số hai điện trở.

C15=100 pF song song R6 làm trở kháng hồi tiếp giảm ở tần số cao, hỗ trợ ổn định với điện dung photodiode và đầu vào. `1/(2πR6C15)≈159 kHz` chỉ là tần số đặc trưng mạng hồi tiếp; băng thông toàn TIA còn phụ thuộc op-amp, cảm biến và ký sinh. MCP6002 có GBW điển hình 1 MHz, không đồng nghĩa TIA đạt băng thông 1 MHz. U4B cấu hình follower ở BIAS, không cấp tải ngoài. [Microchip MCP6002](https://www.microchip.com/en-us/product/MCP6002)

### 4.2. Hai tầng lọc quang cố định

Đường tín hiệu: `U4.1 → R11 → X → R12 → PA1`; C17 từ X xuống GND, C18 từ PA1 xuống GND. Mỗi tầng 1 kΩ/10 nF. Hai tầng không có bộ đệm giữa nên tải lẫn nhau. Mô hình lý tưởng, bỏ qua trở kháng ra U4 và tải ADC: `H(s)=1/[1+3sRC+(sRC)²]`.

Mỗi RC xét riêng có fc≈15,9 kHz; toàn mạng có điểm −3 dB khoảng 6,0 kHz. Tại 25 kHz và 50 kHz, độ suy giảm tính khoảng 13,9 dB và 22,2 dB. Các số này chưa đủ chứng minh chống alias cho mọi dạng tín hiệu. Đo trước/sau lọc trên nguyên mạch đã lắp để xác định xung mục tiêu có bị thấp đỉnh hoặc kéo dài cạnh không.

### 4.3. Đo nền, độ nhạy và bão hòa

1. Ghi mã D1 thực, R6/C15, nguồn 3V3, khoảng cách, góc và nguồn sáng. Giữ nguyên vị trí khi so các lượt.
2. Che kín cảm biến, đo BIAS, TIA_LIGHT và PA1; lưu min/max và nhiễu.
3. Đo dưới ánh sáng phòng, sau đó chiếu đèn ở các khoảng cách đã ghi. Lặp mỗi điều kiện ba lần.
4. Ghi trường hợp chạm rail hoặc không trở về nền. Kiểm BIAS, nguồn, ánh sáng nền và hồi tiếp khi xuất hiện bão hòa/rung.
5. Tính `ΔV=VTIA,sáng−VTIA,che`, `ΔIphoto≈ΔV/R6`. Ví dụ ΔV=0,10 V, R6=10 kΩ cho ΔIphoto≈10 µA; đây là ví dụ tính, không phải số đo.

| Điều kiện/lần | Khoảng cách/góc | BIAS (V) | TIA/PA1 (V) | Nhiễu (mVpp) | Clipping | File |
|---|---|---|---|---|---|---|
| Che kín / … | … | … | … / … | … | … | … |
| Phòng / … | … | … | … / … | … | … | … |
| Chiếu đèn / … | … | … | … / … | … | … | … |

### 4.4. Đo đáp ứng xung

1. Dùng LED ngoài bo với điện trở hạn dòng, máy phát mức phù hợp LED; kiểm dòng kích. Bắt đầu xung 1 ms, tiếp đến 100 µs, ví dụ lặp 10 Hz; đây là điều kiện khảo sát ban đầu.
2. Với scope hai kênh, lượt 1 đo kích LED và TIA_LIGHT; lượt 2 đo TIA_LIGHT và PA1. Giữ nguyên mạch hai RC trong mọi lượt.
3. Đo độ rộng xung quang từ waveform TIA, đỉnh so với nền, thời gian lên và độ trễ theo cùng mức ngưỡng. Cạnh kích điện LED chưa phải mốc quang chính xác tuyệt đối.
4. Thu ADC với fs thực đã xác nhận; số mẫu trên xung gần `fs×txung`. Ví dụ xung 100 µs cho khoảng 5 mẫu ở 50 ksample/s và 10 mẫu ở 100 ksample/s.
5. Phát số xung biết trước, gợi ý 100 xung mỗi điều kiện; ghi ngưỡng nhận firmware, số phát, số nhận và số báo thừa.

Tỷ lệ giữ đỉnh: `K%=100×ΔVPA1/ΔVTIA`, dùng nền riêng của mỗi điểm. Tỷ lệ bỏ sót: `100×Nbỏ/Nphát`; báo thừa ghi riêng. Không tính tỷ số khi biên độ tham chiếu gần nhiễu. Thống nhất độ trễ là từ mốc nào đến mốc nào, ở ngưỡng bao nhiêu.

| Độ rộng đo thực (µs) | fs/kênh (sample/s) | ΔVTIA/ΔVPA1 (V) | K (%) | Trễ/ngưỡng | Phát/nhận/báo thừa | File |
|---|---|---|---|---|---|---|
| … | … | … / … | … | … | … / … / … | … |

Phép thử LED kiểm chứng đáp ứng với nguồn sáng và xung đã dùng. Để kết luận khả năng nhận dạng hồ quang cần dữ liệu đại diện và đánh giá thuật toán riêng; không đổi kết quả thử LED thành khoảng cách phát hiện hồ quang.

## 5. Khối RS485: U5, C16, R7–R10, J2

### 5.1. Vì sao cần từng linh kiện?

U5 MAX3485 biến TX/RX logic 3,3 V thành tín hiệu vi sai A/B. Receiver quyết định theo điện áp chênh A−B; dây GND tham chiếu giúp kiểm soát điện áp common-mode trong cấu hình đang dùng. PB0 điều khiển chung DE và /RE: thấp để nhận, cao để phát. R7 10 kΩ kéo trạng thái mặc định về nhận khi MCU chưa chủ động điều khiển; C16 là tụ nguồn cục bộ U5. [ADI MAX3485](https://www.analog.com/media/en/technical-documentation/data-sheets/MAX3483-MAX3491.pdf)

R9 là termination khi node nằm ở đầu tuyến và cấu hình cáp yêu cầu. R8/R10 330 Ω lắp theo schematic mới: R8 kéo A lên 3V3, R10 kéo B xuống GND. Kiểm mạng bias thực trên gateway trước khi ghép bus; không suy rằng gateway đã có bias chỉ từ tên module. Termination hấp thụ phản xạ, bias đặt trạng thái bus lúc không phát; hai chức năng khác nhau. Trạng thái lắp R9 cần ghi cùng loại/chiều dài cáp và phần cứng hai đầu. [TI RS485 Design Guide](https://www.ti.com/lit/an/slla272d/slla272d.pdf)

### 5.2. Đo điện và kiểm bản tin

1. Tắt nguồn hai đầu, ghi trạng thái R9 và các linh kiện thực đã có trên bus; kiểm A/B/GND. Điện trở đo giữa A/B có thể bị ảnh hưởng mạng bias và IC, không chỉ termination.
2. Nếu biết hai đầu đều có 120 Ω và bỏ qua nhánh khác, điện trở tương đương là 60 Ω. Đây là giá trị tính để đối chiếu, không phải yêu cầu ép mọi bus đo đúng 60 Ω.
3. Cấp nguồn, đo VAB nghỉ và waveform khi truyền. Dùng probe vi sai hoặc hai kênh cùng tham chiếu GND rồi tính CH1−CH2; không kẹp mass scope trực tiếp vào A/B.
4. Quan sát UART_TX, RS485_DIR và A/B: DIR phải giữ phát đến khi bit stop cuối rời UART. Dùng cờ Transmission Complete phù hợp firmware, không chỉ cờ buffer trống.
5. Chạy truyền lặp với SEQ và cơ chế kiểm lỗi của giao thức; ghi số yêu cầu, phản hồi hợp lệ, lỗi kiểm tra, timeout, mất/trùng SEQ. Nếu giao thức chưa có CRC thì ghi đúng cơ chế hiện có.
6. Thử rút cáp rồi nối lại; ghi thời điểm thao tác, báo OFFLINE/STALE và lần phản hồi hợp lệ đầu tiên. Dữ liệu cũ phải có tuổi dữ liệu để phân biệt với số đo 0.

| Cáp/chiều dài | R9 và termination đầu kia | Baudrate | VAB nghỉ (V) | Số yêu cầu/hợp lệ | Timeout/lỗi/SEQ thiếu | File |
|---|---|---|---|---|---|---|
| … | … | … | … | … / … | … | … |

Không có lỗi trong N gói chỉ chứng minh phiên thử N gói với cấu hình đã ghi, chưa chứng minh xác suất lỗi bằng 0 cho mọi môi trường.

## 6. Kiểm tích hợp và lưu bằng chứng

### 6.1. Kiểm băng thông dữ liệu trước khi chạy

115200 baud, khung 8N1 có tối đa lý thuyết `115200/10=11.520 byte/s`, còn phải trừ overhead và thời gian đổi chiều. Hai kênh 50 ksample/s, mỗi mẫu 2 byte tạo 200.000 byte/s. Vì vậy truyền các đại lượng tóm tắt định kỳ; waveform ngắn lưu buffer và tải riêng theo khả năng firmware. Hai buffer 2048 mẫu uint16 chiếm 8192 byte, cần cộng thêm DMA, stack và các cấu trúc khác trong SRAM 20 KiB.

Không tự ghi cấu hình 32 ksample/s cho CT đồng thời 50 ksample/s cho quang nếu firmware chưa thực hiện được lịch đó. Khi dừng thu để truyền phải ghi khoảng thời gian mất quan sát.

### 6.2. Chạy một phiên có mốc thao tác

1. Ghi mã PCB, mã linh kiện thực, firmware, fs từng kênh, sample time ADC, baudrate, cáp, trạng thái R9/R8/R10, dụng cụ và ngày đo.
2. Chạy không tải; lần lượt bật tải, tắt tải, bật lại, chiếu/che cảm biến. Ghi thời điểm từng thao tác.
3. Chạy liên tục, gợi ý ít nhất 10 phút cho phiên khảo sát đầu; lưu nguồn, BIAS, min/max ADC, số reset, mất mẫu và lỗi truyền.
4. Thực hiện phiên ngắt/nối cáp riêng để không trộn với kiểm độ ổn định bình thường.
5. Mở lại CSV và waveform để kiểm cột, đơn vị, số hàng và timestamp; giữ dữ liệu gốc cùng bảng tính kết quả.

CSV tóm tắt nên có: thời gian PC, node_id, boot_id/uptime, SEQ, trạng thái kết nối, tuổi dữ liệu, dòng RMS hoặc count chưa hiệu chuẩn, mức quang, min/max ADC, cờ sự kiện và số lỗi/mất mẫu. Waveform cần trục thời gian hoặc fs, đơn vị, kênh đo, số mẫu, VDDA và hệ số hiệu chuẩn đã áp dụng.

### 6.3. Chứng minh từng kết luận bằng dữ liệu nào?

| Kết luận muốn đưa vào báo cáo | Bằng chứng cần có | Giới hạn phải ghi |
|---|---|---|
| Nguồn đủ cho node | Điện áp/ripple lúc phát, dòng, nhiệt theo thời gian | Chế độ tải và nhiệt độ phòng đã thử |
| ADC lấy mẫu đúng | fs đo thực, test DC tham chiếu, bộ đếm mất mẫu | Sample time, số kênh, firmware |
| Đo dòng có độ nhạy và độ lặp xác định | Các mức Iref, waveform, đường hiệu chuẩn và điểm kiểm chéo | Dải dòng/tần số đã thử, số lượt dây CT |
| Thu được xung quang mục tiêu | Waveform trước/sau lọc, độ rộng thực, tỷ lệ giữ đỉnh, phát/nhận/báo thừa | Nguồn sáng, nền, khoảng cách, ngưỡng |
| Bus làm việc trong phiên thử | Số gói, số lỗi, waveform A/B, SEQ | Cáp, tốc độ, thời gian và môi trường thử |
| Phục hồi kết nối | Timestamp thao tác, OFFLINE và phản hồi đầu tiên | Chính sách timeout/tuổi dữ liệu |

Trước mỗi phép thử, ghi mục tiêu cần đạt của dự án: sai số dòng tối đa, xung nhỏ nhất, tỷ lệ bỏ sót/báo thừa, độ trễ và thời gian chạy. Nếu chưa chốt các giới hạn này thì kết quả chỉ là số liệu khảo sát, chưa đủ để ghi đạt yêu cầu.

| Hạng mục | Mục tiêu trước khi đo | Kết quả thực | Bằng chứng/tên file | Kết luận và việc còn thiếu |
|---|---|---|---|---|
| Nguồn | … | … | … | … |
| ADC/clock | … | … | … | … |
| Dòng | … | … | … | … |
| Quang tĩnh/xung | … | … | … | … |
| RS485/tích hợp | … | … | … | … |

## 7. Đối chiếu tài liệu

- [01 — BOM_LIST và hướng dẫn vẽ schematic](01_BOM_LIST_va_huong_dan_ve_schematic_PCB.md): Designator, giá trị, package và các bảng nối chân.
- [Hướng dẫn test và kiểm thử module](../module/01_Huong_dan_test_va_kiem_thu_module.md): bộ tải cách ly, cách thử dòng/quang và lưu số liệu trước PCB.
- Các datasheet chính hãng được liên kết tại từng khối. Tỷ số CT 1000:1 dùng theo xác nhận người dùng; burden, dải tuyến tính và băng thông cần căn cứ riêng.
