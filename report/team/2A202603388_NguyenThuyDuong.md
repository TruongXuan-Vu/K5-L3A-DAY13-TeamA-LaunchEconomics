# Báo cáo cá nhân — Nguyễn Thuỳ Dương

MSSV: 2A202603388. Email: 26ai.duongnt8@vinuni.edu.vn.

## 1. Thông tin thành viên

- Họ tên: Nguyễn Thuỳ Dương
- MSSV: 2A202603388
- Email: 26ai.duongnt8@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 1; phụ trách thêm B3, B4 và D2.

## 2. Phần việc phụ trách

- Phần C: gắn nhãn 20 ca theo 5 loại lỗi và xây dựng bảng phát hiện, khắc phục cho 5 ca đại diện.
- Phần B3: so sánh chi phí trợ lý, chi phí cả hệ thống và chi phí mỗi việc thành công khi giới hạn 1, 2, 3 lần chạy.
- Phần B4: giải thích tác động của việc xem lại 100% trong phạm vi `noi_dia` + `hang_nang`.
- Phần D2: hoàn thiện 5 câu kiểm tra khả năng tách tác động của pilot.

## 3. Đóng góp cụ thể

Tôi tự đưa ra bộ nhãn ban đầu cho 20 ca, sau đó dùng ChatGPT để kiểm tra và giải thích các ca nhầm. Bộ nhãn ban đầu khớp nhãn tham khảo 13/20 ca; sau đối chiếu tôi sửa 7 ca: 3, 4, 7, 8, 10, 13, 20. Bộ nhãn đã sửa được phân biệt với bộ nhãn ban đầu khi tính đồng thuận độc lập.

Tôi soạn bảng khắc phục cho các ca 1, 7, 18, 19, 17, đại diện đủ 5 loại lỗi. Mỗi ca có cách phát hiện đo được, biện pháp xử lý và một vai trò phụ trách; các ngưỡng và tần suất là đề xuất cho pilot, chưa phải kết quả đo thực tế.

Ở B3, tôi điền bảng và giải thích vì sao giới hạn 2 lần chạy có chi phí cả hệ thống thấp nhất: 6.901.220 đ, dù chi phí mỗi việc thành công thấp nhất thuộc giới hạn 1 lần (4.111 đ), đều có phần `simulated`. Số liệu lấy từ hướng dẫn đối chiếu, cần kiểm tra lại với output code của nhóm khi tích hợp.

Ở B4, tôi trình bày hai giả định thời gian làm lại: 9 phút/ca cho chi phí 11.743 đ/việc, còn 15,3 phút/ca cho 12.414 đ/việc (`simulated`, chưa gồm chi phí cố định). Pilot cần đo thời gian thực tế và xác định mức giảm xem lại vẫn an toàn.

Ở D2, tôi làm rõ phương án 20 nhân viên mỗi nhóm, chia ngẫu nhiên phân tầng theo depot với seed 20261121; đối chứng đồng thời, hạn chế chia sẻ gợi ý, chốt kế hoạch trước khi chạy và chỉ phân tích yêu cầu đủ 7 ngày theo dõi. Đây là kế hoạch đề xuất, chưa phải pilot đã thực hiện.

## 4. Bằng chứng

Nhánh làm việc: `label1`.

| Phần việc | File | Commit minh chứng |
| --- | --- | --- |
| Bộ nhãn ban đầu và bảng khắc phục 5 ca | `report/team/bang_loi.md` | `dfed08c` |
| Cập nhật nhãn sau đối chiếu | `report/team/bang_loi.md` | `548be28` |
| Hoàn thiện B3 và B4 | `report/team/bang_chi_phi.md` | `bf8243e` |
| Làm rõ D2 và các trường kế hoạch liên quan | `report/team/pilot_plan.yaml` | `679bc03` |

## 5. Công cụ AI đã dùng

Tôi dùng ChatGPT để giải thích đề và 5 loại lỗi, rà soát bộ nhãn tự làm, gợi ý bảng khắc phục, soạn câu trả lời B3–B4, hoàn thiện D2 và hỗ trợ thao tác Git.

Việc rà soát dựa trên mô tả từng ca trong đề, định nghĩa loại lỗi và số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`. Không coi số liệu do AI nêu là kết quả code đã được nhóm xác minh; B3–B4 có ghi nguồn và nhãn `simulated` để đối chiếu khi tích hợp. Không dùng AI tạo bộ nhãn độc lập của người 2 hoặc tự tạo kết quả đồng thuận.

Giới hạn kiểm tra: thay đổi D2 đã qua `git diff --check`; chưa xác nhận bằng `yaml.safe_load` trong môi trường hiện tại do thiếu thư viện `pyyaml`.

## 6. Tự đánh giá

Tôi đã hoàn thành các phần được giao: bộ nhãn người 1, bảng khắc phục, B3–B4 và D2. Qua bài làm, tôi hiểu rõ hơn cách phân biệt lỗi ngầm với lỗi hệ thống, cũng như việc chi phí mỗi việc thành công thấp nhất chưa chắc làm tổng chi phí công ty thấp nhất.

Điểm cần cải thiện là khả năng phân loại ngay từ lần đầu (13/20 ca đúng trước đối chiếu). Khi hoàn thiện bài nộp, cần đối chiếu B3–B4 với output code của nhóm và kiểm tra YAML trong môi trường đủ thư viện.
