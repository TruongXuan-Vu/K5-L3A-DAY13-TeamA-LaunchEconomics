# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: TeamA · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc thành công [simulated] (978 việc thành công / 1.200 yêu cầu), gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); làm lại chiếm 51,8%, xem lại 40,7% [simulated] | Giả lập | Kỹ sư trưởng agent |
| 2 · Ba yếu tố nhạy nhất | 1) Số ca làm lại: gấp đôi → 6.787 đ (+51,8%) · 2) Tỉ lệ xem lại: gấp đôi → 6.292 đ (+40,7%) · 3) Lương nhân viên +25% → 5.506 đ (+23,1%) [simulated]; giá token gấp đôi chỉ +5,6% → pilot phải theo dõi tỉ lệ làm lại và xem lại, không phải giá token | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống, tính cả 222 ca nhân viên làm thay: (4.373.585 + 222 × 12.000) / 1.200 = 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated]; phạm vi pilot noi_dia + hang_nang, đã cộng cố định 40 tr/tháng: 4.599 đ = 0,38× [simulated]; quoc_te 1,88× (không đáng) | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử: chính (đóng trong 24h, không mở lại 7 ngày) 82,83% (994/1.200); dùng (bỏ qua gợi ý: sửa + bỏ) 27,12% (48/177); an toàn (mở lại trong 7 ngày) 4,25% (51/1.200); 10 event có `trace_id`, mỗi chỉ số tính được từ event (`chi_so.md`) | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 15/20 = 75% (< 80%, đã viết lại định nghĩa Ngầm/Hệ thống/Ngữ cảnh/Giới hạn); nhãn thống nhất: 4 Do người dùng · 5 Hệ thống · 4 Ngữ cảnh · 4 Giới hạn · 3 Ngầm; 5 cách khắc phục đủ 5 loại, mỗi cách có ngưỡng và vai trò phụ trách (`bang_loi.md`) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên 20 + 20 (phân tầng theo depot), phạm vi noi_dia + hang_nang; mức chênh 5 điểm cần 1.251/nhóm nhưng 20 người chỉ đạt tối đa 1.000 → chấp nhận mức chênh 6 điểm (859/nhóm, DE 6,96, m ≥ 299); 3 luật dừng có ngưỡng, thời hạn, người dừng; quyết định 2027-01-05 (`pilot_plan.yaml`) | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Xem lại 100% (noi_dia + hang_nang) → 11.743 đ/việc = 0,98× của 12.000 đ, và 12.414 đ = 1,03× nếu làm lại 15,3 phút/ca như dữ liệu: gần như không tiết kiệm hoặc đắt hơn [simulated]; số ca làm lại gấp đôi → +51,8% [simulated]; giới hạn 2 lần chạy rẻ nhất cho cả hệ thống (6.901.220 đ so với 7.037.585 đ ở 3 lần) [simulated] | Giả lập | Kế toán trưởng |

**Đề xuất: Go có điều kiện** — pilot chỉ noi_dia + hang_nang (4.599 đ = 0,38× của 12.000 đ, đã cộng cố định [simulated]); loại quoc_te (1,88×) và doi_tac (0,85×). Con số bất lợi: xem lại 100% còn 0,98× [simulated]; với 40 nhân viên chỉ đo được mức chênh 6 điểm (power ≈ 0,64 nếu tác động thật là 5 điểm); đồng thuận nhãn lỗi 75%.

- Thêm khoá chống trùng và đối soát sổ cái theo giờ (ca 7, 20) trước ngày bắt đầu — Kỹ sư trưởng agent — kiểm tra 2026-12-01.
- Ký chấp nhận mức chênh 6 điểm và power 0,64 ở mức 5 điểm — Giám đốc vận hành — 2026-12-01.
- Bật đủ 10 event có `trace_id` (gồm `ticket_closed` cho chỉ số chính); thay phút xem lại/làm lại simulated bằng phút đo thật sau tuần 1 — PM trợ lý hoàn phí — 2026-12-08.
- Có kế hoạch giảm xem lại theo bậc (khi sửa + bỏ < 15%), vì xem lại 100% gần như không tiết kiệm — Trưởng nhóm CSKH — 2026-12-15.