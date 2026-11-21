# Báo cáo cá nhân — HoangBaoNguyen-2A202603384

## 1. Thông tin thành viên

- Họ tên: Hoàng Bảo Nguyên
- MSSV: 2A202603384
- Email: 26ai.nguyenhb@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người kiểm số

## 2. Phần việc phụ trách

- Tính tay độc lập một số con số của nhiệm vụ A, B, D, E và đối chiếu với output của `src/lab13.py` (người viết code chạy) và với số đáp án (lệch cho phép ≤ 2%).
- Báo lỗi cho người viết code khi số lệch; chỉ chép số vào hồ sơ sau khi đã khớp.
- Điền `report/team/bang_chi_phi.md` (A1–A4, B1–B4) với nhãn `simulated` cho mọi số tính từ cột `_simulated`.
- Rà `chi_so.md` và `ho_so_launch_v0.md` trước khi gửi hội đồng Gate 2a: số khớp với bảng chi phí, đủ nhãn `simulated`, không có từ cấm.

## 3. Đóng góp cụ thể

- **A2, tính tay chi phí mỗi việc thành công.** Cộng cột thô của hai file CSV (không qua `mo_hinh`), rồi tự nhân giá: token = 5.771,712 × 26 + 734,774 × 130 = 245.585 đ; tool = 5.600 × 15 = 84.000 đ; xem lại = 890 phút × 2.000 = 1.780.000 đ [simulated]; làm lại = 1.132 × 2.000 = 2.264.000 đ [simulated]; tổng 4.373.585 đ ÷ 978 việc thành công = **4.472 đ** [simulated]. Khớp `lab13.py`; gấp 16,3 lần hoá đơn chia số yêu cầu (274,7 đ).
- **A3, phát hiện lỗi in trong code.** Cột `lan_chay/yc` in 0,22 · 0,69 · 1,88 · 0,85, trùng hệt cột `so_voi_12000`. Số lần chạy mỗi yêu cầu không thể nhỏ hơn 1; tính tay số lần chạy ÷ số yêu cầu: noi_dia 916/824 = **1,11**, hang_nang 232/158 = 1,47, quoc_te 348/150 = 2,32, doi_tac 128/68 = 1,88. Báo người viết code sửa; bản push sau đã đúng.
- **A3, A4 kiểm tay:** noi_dia (130.987 + 47.700 + 942.000 + 990.000) ÷ 783 = 2.696 đ = 0,22× [simulated]; A4: 40.000.000 ÷ 33.750 = 1.185 đ/việc, cộng 3.414 đ = 4.599 đ = 0,38× [simulated].
- **B1–B4:** dự đoán B1 trước khi code chạy (mô hình cộng tuyến tính, ví dụ token gấp đôi = (4.373.585 + 245.585) ÷ 978 = 4.723 đ); kiểm quy tắc "giảm một nửa = ½ mức tăng khi gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9); kiểm B2 = 5,6% + 40,7% = 46,3%; kiểm B3 "cả hệ thống" = tổng trợ lý + 12.000 × số yêu cầu không thành công (giới hạn 2 lần rẻ nhất 6.901.220 đ); kiểm B4 = 10.568.513 ÷ 900 = 11.743 đ = 0,98× [simulated]; tính thêm phút làm lại trung bình thật 15,3 phút/ca (74 ca) → 1,03× [simulated] và mức hoà vốn 5,1 phút mỗi lần xem lại.
- **D1:** kiểm cỡ mẫu 1.251/nhóm (công thức ra 1.250,7), DE = 1 + 74 × 0,02 = 2,48, giới hạn 20 ÷ 0,02 = 1.000 và 6 ÷ 0,02 = 300, m ≥ 841,82 ÷ 2,82 → 299; tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại 4,25% (51/1.200), trong phạm vi 3,97% (39/982); power 0,64 nếu chọn mức chênh 6 điểm mà tác động thật là 5 điểm.
- **E1, E2:** kiểm ba chỉ số 82,83% (994/1.200), 27,12% (48/177), 4,25% (51/1.200). Phát hiện danh sách event thiếu `ticket_closed` nên chỉ số chính ("đóng trong 24 giờ") chưa tính được từ event, và thiếu `audit_sample_checked` mà chỉ số an toàn tự đề xuất cần; viết lại phần kiểm tra chéo theo event; sửa tỉ lệ làm lại trong phạm vi từ 4% thành 4,9% (48/982).
- **Hồ sơ launch v0:** sửa hoá đơn 275 → 274,7 đ cho khớp bảng chi phí; thêm con số bất lợi 1,03× vào mục 7; cập nhật số event thành 10.

## 4. Bằng chứng

- Commit `8ada45e` trên nhánh `HoangBaoNguyen_2A202603384`: "docs: điền bảng chi phí A1-B4, sửa chi_so và hồ sơ launch" (`report/team/bang_chi_phi.md`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`).
- `report/team/bang_chi_phi.md`: toàn bộ bảng A1–A4, B1–B4 và các câu trả lời.
- Lỗi cột `lan_chay/yc` ở A3: phát hiện qua tính tay, đã báo người viết code và được sửa trong bản push sau.
- Bảng tính tay A2 ở mục 3 có thể làm lại bằng Excel: `=SUM(E:E)` trên `logix_runs.csv` ra 5.771.712 token vào; `=COUNTIF(G:G,"thanh_cong")` trên `logix_requests.csv` ra 978.

## 5. Công cụ AI đã dùng

- **Claude Code (Claude, Anthropic)** trong VS Code, dùng để:
  - Giải thích đề, công thức (vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công, vì sao chạy lại không giúp quoc_te, cỡ mẫu khi chia theo cụm).
  - Cộng các cột thô trong hai file CSV bằng lệnh `awk`, độc lập với code `lab13.py` của nhóm, để có số làm đầu vào cho phép tính tay.
  - Đối chiếu output của `lab13.py` với số đáp án trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, và soạn nội dung các bảng, câu trả lời trong hồ sơ.
- **Cách tự kiểm tra:**
  - Tự làm lại phép nhân giá và phép chia của A2 (4.472 đ) và A3 noi_dia (2.696 đ) từ tổng cột thô.
  - Mỗi số đều so với hai nguồn: output của `lab13.py` do người viết code chạy, và số đáp án; chỉ chép khi cả hai khớp (lệch ≤ 2%).
  - Dùng các phép kiểm có quy luật: số lần chạy mỗi yêu cầu phải ≥ 1; "giảm một nửa" = ½ "gấp đôi"; B2 = tổng hai tác động riêng.
  - Chạy `yaml.safe_load` cho `pilot_plan.yaml` và tìm từ "production" trong `report/team/` trước khi push.
- Không dùng AI để bịa số, nhãn lỗi hay kết quả duyệt chéo. Không tham gia gắn nhãn 20 ca lỗi (việc của hai người gắn nhãn, làm độc lập).

## 6. Tự đánh giá

- **Làm tốt:** mọi số trong `bang_chi_phi.md` đã được đối chiếu với code và đáp án; phát hiện được hai lỗi có thể mất điểm (cột `lan_chay/yc` in sai ở A3, thiếu event `ticket_closed` khiến chỉ số chính chưa đo được).
- **Chưa tốt:** dựa nhiều vào trợ lý AI để cộng cột và soạn nội dung; phần tính tay chủ yếu là bước nhân giá và chia, chưa tự đếm toàn bộ bằng Excel. Bảng chi phí được push muộn, sau khi các phần D, E đã lên `main`.
- **Lần sau:** tự tính tay trước khi người viết code chạy để phép kiểm thật sự độc lập, và push bảng chi phí ngay sau mỗi checkpoint thay vì gom lại cuối buổi.
