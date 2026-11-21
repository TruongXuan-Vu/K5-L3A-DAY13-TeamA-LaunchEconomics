# Team

## Thông tin nhóm

- Tên nhóm: TeamA
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-TeamA-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo: https://github.com/TruongXuan-Vu/K5-L3A-DAY13-TeamA-LaunchEconomics
- Nhánh nộp: main
- Commit chốt: <sẽ điền sau khi commit>

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Vũ Xuân Trường | 2A202603433 | 26ai.truongvx@vinuni.edu.vn | TruongXuan-Vu | Người viết code |
|   2 | Hoàng Bảo Nguyên | 2A202603384 | 26ai.nguyenhb@vinuni.edu.vn | Stormaka | Người kiểm số |
|   3 | Trần Thị Lý | 2A202603404 | 26ai.lytt@vinuni.edu.vn | lytrann236 | Người gắn nhãn 2, kiêm giữ hồ sơ |
|   4 | Nguyễn Thuỳ Dương | 2A202603388 | 26ai.duongnt8@vinuni.edu.vn | NTD-DUONG | Người gắn nhãn 1; B3, B4; D2 |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

## Nguyễn Thuỳ Dương — MSSV: 2A202603388

### Phần việc phụ trách

- Nhiệm vụ C: người gắn nhãn 1, phân loại 20 ca lỗi và soạn bảng khắc phục cho 5 loại lỗi.
- Nhiệm vụ B: bảng so sánh và câu trả lời B3, B4 về giới hạn chạy lại và xem lại 100%.
- Nhiệm vụ D: D2, năm câu kiểm tra khả năng tách tác động của pilot.

### Đóng góp cụ thể

- Cung cấp bộ nhãn ban đầu cho 20 ca; đối chiếu, sửa cách phân biệt Ngầm, Hệ thống, Ngữ cảnh và Giới hạn hệ thống với hỗ trợ của ChatGPT.
- Soạn bảng khắc phục 5 ca đại diện đủ 5 loại, có cách phát hiện đo được, biện pháp xử lý và vai trò phụ trách trong `report/team/bang_loi.md`.
- Điền bảng chi phí B3 cho giới hạn 1, 2, 3 lần chạy; giải thích vì sao 2 lần rẻ nhất cho cả hệ thống. Viết B4 với hai giả định thời gian làm lại 9 và 15,3 phút, ghi nhãn `simulated` và nguồn số tham khảo để nhóm đối chiếu output code.
- Hoàn thiện D2 trong `report/team/pilot_plan.yaml`: đối chứng đồng thời, ngẫu nhiên theo nhân viên với seed cố định, phân tầng theo depot, kiểm soát ảnh hưởng gián tiếp, chốt kế hoạch trước khi chạy và 20 cụm mỗi nhóm.
- Dùng ChatGPT hỗ trợ giải thích, rà soát và biên tập; không tự tạo bộ nhãn người 2 hoặc kết quả đồng thuận.

### Bằng chứng

- Nhánh làm việc: `label1`.
- `report/team/bang_loi.md`: bộ nhãn ban đầu và bảng khắc phục ở commit `dfed08c`; bản nhãn đã sửa theo xác nhận ở commit `548be28`.
- `report/team/bang_chi_phi.md`: hoàn thiện B3, B4 ở commit `bf8243e`.
- `report/team/pilot_plan.yaml`: hoàn thiện D2 ở commit `679bc03`.
