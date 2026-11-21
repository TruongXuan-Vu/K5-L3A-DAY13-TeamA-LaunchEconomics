# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: ... · Người gắn nhãn 2: ... (gắn trong 8 phút, không trao đổi)

Cột “Nhãn người 1” là bản đã sửa sau đối chiếu với ChatGPT, theo bảng người 1 xác nhận. Khi tính đồng thuận độc lập, dùng bộ nhãn ban đầu lưu tại commit `dfed08c`, không dùng bản đã sửa này.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | ... | ... | ... |
| 2 | Hệ thống | ... | ... | ... |
| 3 | Ngữ cảnh | ... | ... | ... |
| 4 | Giới hạn hệ thống | ... | ... | ... |
| 5 | Ngầm | ... | ... | ... |
| 6 | Do người dùng | ... | ... | ... |
| 7 | Hệ thống | ... | ... | ... |
| 8 | Hệ thống | ... | ... | ... |
| 9 | Do người dùng | ... | ... | ... |
| 10 | Ngữ cảnh | ... | ... | ... |
| 11 | Giới hạn hệ thống | ... | ... | ... |
| 12 | Ngầm | ... | ... | ... |
| 13 | Giới hạn hệ thống | ... | ... | ... |
| 14 | Do người dùng | ... | ... | ... |
| 15 | Hệ thống | ... | ... | ... |
| 16 | Ngữ cảnh | ... | ... | ... |
| 17 | Ngầm | ... | ... | ... |
| 18 | Ngữ cảnh | ... | ... | ... |
| 19 | Giới hạn hệ thống | ... | ... | ... |
| 20 | Hệ thống | ... | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Ghi event `input_validation_failed` kèm `trace_id`; kiểm tra số tài khoản theo quy tắc ngân hàng trước mỗi lệnh hoàn, chặn khi không hợp lệ. | Hướng dẫn khách nhập lại; hiển thị ngân hàng và số tài khoản để xác nhận trước khi gửi lệnh hoàn. | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ giữa thông báo “đã hoàn” và bản ghi sổ cái thành công cùng `trace_id`; cảnh báo khi có ít nhất 1 ca không khớp. | Chỉ báo thành công khi sổ cái xác nhận; sau 3 lần lỗi, báo “đang xử lý” và chuyển nhân viên. Dùng khóa chống trùng khi thử lại. | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Ghi lý do mở lại và kết quả kiểm tra số tiền kèm `trace_id`; hằng tuần thống kê ca khách phản ánh hoàn thiếu nhưng tính đúng, rà soát khi có ít nhất 1 ca. | Tin nhắn ghi rõ cách tính: 30.000 đ × 50% = 15.000 đ, kèm căn cứ chính sách và nơi nhận tiền. | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Ghi event `handoff_to_staff` với lý do `ngoai_thoi_gian_luu_tru` và `trace_id`; kiểm tra hằng tuần, yêu cầu 100% ca này có mã chuyển và tóm tắt. | Thông báo giới hạn tra cứu 12 tháng; chuyển nhân viên tra kho lưu trữ, giữ thông tin khách đã cung cấp để không phải nhập lại. | Trưởng nhóm CSKH |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn dưới 2 kg/tuần, đối chiếu số tiền với bảng giá có hiệu lực tại thời điểm áp dụng; cảnh báo khi có ít nhất 1 đơn lệch. | Xóa bộ nhớ đệm khi bảng giá đổi; ghi phiên bản bảng giá vào trace; rà soát 212 đơn bị ảnh hưởng và xử lý khoản chênh lệch. | Kế toán trưởng |

Các event, ngưỡng cảnh báo và tần suất kiểm tra trên là đề xuất cho pilot, chưa phải kết quả đo thực tế. Nội dung bảng được soạn với hỗ trợ của ChatGPT dựa trên tình huống trong đề bài.
