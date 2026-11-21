# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Thuỳ Dương · Người gắn nhãn 2: Trần Thị Lý (gắn trong 8 phút, không trao đổi)

Hai cột "Nhãn người 1" và "Nhãn người 2" là bộ nhãn độc lập ban đầu, giữ nguyên để tính đồng thuận (người 1 chỉ chuẩn hóa chính tả "Ngâm" → "Ngầm"). Sau khi so nhãn, nhóm có dùng ChatGPT/Claude để giải thích định nghĩa khi thảo luận các ca lệch; cột "Nhãn thống nhất" là kết quả thảo luận của nhóm.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngầm | Ngữ cảnh | Không | Ngữ cảnh |
| 4 | Ngầm | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Ngầm | Ngầm | Có | Hệ thống |
| 8 | Giới hạn hệ thống | Hệ thống | Không | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Ngữ cảnh | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Ngầm | Ngầm | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 15 / 20 = 75% (dưới ngưỡng 80% → đã viết lại định nghĩa bên dưới)

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Ca 3: trợ lý hoàn về ví đúng thiết kế, khách đã báo nên lỗi không ẩn → Ngữ cảnh, không phải Ngầm.
- Ca 4: LogiX không có dữ liệu chặng nước ngoài, trợ lý không thể làm và đã nói rõ → Giới hạn hệ thống, không phải Ngầm.
- Ca 8: trợ lý có chính sách nhưng trích sai điều khoản, lỗi hiện ngay trong tin nhắn → Hệ thống, không phải Giới hạn.
- Ca 10: từ chối đúng chính sách bất khả kháng, chỉ mâu thuẫn với lời hứa trên ứng dụng → Ngữ cảnh, không phải Hệ thống.
- Ca 13: câu hỏi ngoài phạm vi là nguyên nhân gốc; trả lời chung chung là việc cần cải thiện → Giới hạn hệ thống, không phải Ngữ cảnh.
- Ca 7, 20 (hai người trùng Ngầm nhưng nhóm sửa ở cột thống nhất): sai thiết kế đã lộ ra (hệ thống nhận lỗi 503 / hoàn 2 lần do thiếu khoá chống trùng) → Hệ thống.

**Định nghĩa đã viết lại (do đồng thuận 75% < 80%):**
- **Ngầm** chỉ dùng khi mô tả cho thấy *không ai* (khách, nhân viên, hệ thống) nhận ra lỗi cho tới khi kiểm tra mẫu. Có người báo hoặc hệ thống đã nhận tín hiệu lỗi thì không phải Ngầm.
- **Hệ thống** = trợ lý làm *sai* thiết kế hoặc chính sách (tính sai, trích sai, báo sai, thiếu khoá chống trùng), lỗi đã lộ ra.
- **Ngữ cảnh** = trợ lý làm *đúng* thiết kế hoặc chính sách, nhưng giả định không khớp kỳ vọng của khách.
- **Giới hạn hệ thống** = trợ lý *không thể* làm (thiếu dữ liệu, ngoài phạm vi, dạng đầu vào không hỗ trợ), kể cả khi cách báo giới hạn chưa tốt.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `input_validation_failed` kèm `trace_id`; kiểm tra số tài khoản theo quy tắc ngân hàng trước mỗi lệnh hoàn; cảnh báo khi quá 2% yêu cầu/ngày | Hướng dẫn khách nhập lại; hiển thị ngân hàng và số tài khoản để khách xác nhận trước khi gửi lệnh hoàn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ giữa tin nhắn "đã hoàn" và bản ghi sổ cái thành công cùng `trace_id`; ngưỡng 0 ca không khớp | Chỉ báo thành công khi sổ cái xác nhận; sau 3 lần lỗi thì báo "đang xử lý" và chuyển nhân viên; dùng khoá chống trùng khi thử lại | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Ghi lý do mở lại và kết quả kiểm tra số tiền kèm `trace_id`; thống kê hằng tuần số ca khách báo hoàn thiếu nhưng tính đúng, rà soát khi có từ 1 ca | Tin nhắn luôn ghi cách tính: 30.000 đ × 50% = 15.000 đ, kèm căn cứ chính sách và nơi nhận tiền | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Event `handoff_to_staff` với lý do `ngoai_thoi_gian_luu_tru` và `trace_id`; kiểm tra hằng tuần, yêu cầu 100% ca có mã chuyển và tóm tắt | Báo rõ giới hạn tra cứu 12 tháng; chuyển nhân viên tra kho lưu trữ, giữ thông tin khách đã nhập | Trưởng nhóm CSKH |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn dưới 2 kg mỗi tuần, đối chiếu với bảng giá có hiệu lực; cảnh báo khi từ 1 đơn lệch | Xoá bộ nhớ đệm khi bảng giá đổi; ghi phiên bản bảng giá vào trace; rà soát 212 đơn bị ảnh hưởng và xử lý chênh lệch | Kế toán trưởng |

Các event, ngưỡng và tần suất trên là đề xuất cho pilot, chưa phải kết quả đo. Bảng khắc phục do người gắn nhãn 1 soạn với hỗ trợ của ChatGPT dựa trên tình huống trong đề bài.