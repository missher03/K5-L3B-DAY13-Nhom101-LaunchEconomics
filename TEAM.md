# Team

## Thông tin nhóm

- Tên nhóm: Nhóm 101
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Nhom101-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/missher03/K5-L3B-DAY13-Nhom101-LaunchEconomics · nhánh nộp `main` · commit chốt: cập nhật sau lần push cuối

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Đỗ Quốc Khánh | 2A202603823 | 26ai.khanhdq2@vinuni.edu.vn | dqk2210 | Người viết code, nhiệm vụ A + B (`src/lab13.py`, `report/team/bang_chi_phi.md`) |
|   2 | Mai Lê Bá Vương | 2A202603872 | Chưa cung cấp | Chưa cung cấp | Thành viên 2 — D1, D2, E1, kế hoạch pilot |
|   3 | Đào Vũ Minh Khánh | 2A202603878 | Chưa cung cấp | Chưa cung cấp | Người gắn nhãn 1 (Nhiệm vụ C, QA & Hội đồng) |
|   4 | Nguyễn Văn Quốc | 2A202603864 | quoc.nvsoict@gmail.com | missher03 | Người gắn nhãn 2 kiêm giữ hồ sơ (Nhiệm vụ C, E, Báo cáo) |

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

## Đỗ Quốc Khánh — 2A202603823

### Phần việc phụ trách

- Nhiệm vụ A và B (thành viên 1): `src/lab13.py` phần A, B và `report/team/bang_chi_phi.md`.

### Đóng góp cụ thể

- Viết ba hàm A1, `mo_hinh`, phần A3, A4, B1–B4 trong `src/lab13.py`; trợ lý AI soát lại, sửa B4 và bổ sung các dòng in còn thiếu.
- Điền `report/team/bang_chi_phi.md`: bảng A1–A4, B1–B4, câu trả lời và mục Đối chiếu tay.
- Tính tay kiểm số: 5.600 lần gọi tool × 15 đ = 84.000 đ; 890 phút × 2.000 đ = 1.780.000 đ [simulated].

### Bằng chứng

- `python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT`.
- Chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn; chi phí cả hệ thống 5.865 đ mỗi yêu cầu = 0,49× của 12.000 đ [simulated].
- Báo cáo cá nhân: `report/team/2A202603823_DoQuocKhanh.md`.

## Mai Lê Bá Vương — 2A202603872

### Phần việc phụ trách

- Thành viên 2: tính cỡ mẫu D1, thiết kế pilot D2, tính các chỉ số E1 và chuẩn bị `report/team/pilot_plan.yaml`.

### Đóng góp cụ thể

- Tích hợp hàm tính D1 và E1 vào `src/lab13.py`, hoàn thiện kế hoạch pilot với 20 nhân viên mỗi nhóm và mức chênh thiết kế 6 điểm.
- Ghi ba chỉ số E1 vào `report/team/chi_so.md` để TV4 sử dụng; chốt scope `noi_dia` + `hang_nang` theo A3 của TV1.

### Bằng chứng

- D1: 859 yêu cầu hiệu dụng và 5.980 yêu cầu thô mỗi nhóm, 299 yêu cầu mỗi nhân viên, design effect 6,96.
- E1 trên dữ liệu giả lập: 994/1.200 = 82,83%; 48/177 = 27,12%; 51/1.200 = 4,25%.
- A3 của TV1: chi phí mỗi việc thành công là 2.696 đ cho `noi_dia`, 8.221 đ cho `hang_nang`, 22.515 đ cho `quoc_te` và 10.215 đ cho `doi_tac` (simulated).
- Tệp liên quan: `src/lab13.py`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`. Chạy Python và kiểm tra YAML bằng `yaml.safe_load` còn chờ môi trường có Python.


## Đào Vũ Minh Khánh - 2A202603878

### Phần việc phụ trách

- Nhiệm vụ C (bảng lỗi và cách khắc phục): `report/team/bang_loi.md`. Chuẩn bị và chấm chéo Gate 2a: `report/team/phieu_cham.md`. Chạy bộ lệnh kiểm tra checklist `SUBMISSION.md` trước khi nộp.

### Đóng góp cụ thể

- Tự gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR (bộ nhãn người 1), ghi vào `report/team/bang_loi.md`.
- So hai bộ nhãn, tính đồng thuận 18/20 = 90% (ngưỡng 80%); với 2 ca không trùng (ca 6, ca 17) chốt nhãn thống nhất và viết quy tắc phân biệt theo nguyên nhân gốc.
- Điền bảng khắc phục 5 ca đủ 5 loại (ca 1, 20, 16, 11, 5): mỗi dòng có event hoặc cách kiểm tra, ngưỡng, tần suất và một vai trò phụ trách.
- Chuyển tóm tắt bảng lỗi (4 · 5 · 4 · 4 · 3 ca theo 5 loại) cho thành viên 4 điền mục 5 của `report/team/ho_so_launch_v0.md`.
- Điền trước `report/team/phieu_cham.md` (thông tin nhóm, câu hỏi cho đội trình) và chuẩn bị bảng tìm bằng chứng cho ba tiêu chí C6–C8.

### Bằng chứng

- Commit `3968c3d` "TV3: bang_loi.md".
- `report/team/bang_loi.md`: 2 bộ nhãn 20 ca, đồng thuận 18/20 = 90%, quy tắc cho ca 6 và ca 17, bảng khắc phục 5 dòng đủ 5 loại.
- Phân bố nhãn thống nhất: Do người dùng 4 ca (1, 6, 9, 14) · Hệ thống 5 ca (2, 7, 8, 15, 20) · Ngữ cảnh 4 ca (3, 10, 16, 18) · Giới hạn hệ thống 4 ca (4, 11, 13, 19) · Ngầm 3 ca (5, 12, 17); khớp 20/20 với bảng tham khảo trong tài liệu hướng dẫn (ngưỡng 16/20).
- Bộ nhãn khớp 18/20 với bảng tham khảo; lệch ở ca 6 (tôi gắn Hệ thống) và ca 17 (tôi gắn Giới hạn hệ thống).
- `report/team/phieu_cham.md`: điểm và quyết định của hội đồng ghi tại buổi duyệt chéo 17:00.


## Nguyễn Văn Quốc — 2A202603864

### Phần việc phụ trách

- Người gắn nhãn 2 (Nhiệm vụ C — gắn nhãn độc lập 20 ca lỗi trong `report/team/bang_loi.md`).
- Giữ hồ sơ `report/team/ho_so_launch_v0.md` và tổng hợp báo cáo nhóm `report/team/group_report.md`.
- Hoàn thiện danh sách event có `trace_id`, kiểm tra chéo và bảng rủi ro kinh tế E2 trong `report/team/chi_so.md`.
- Tham gia hội đồng chấm chéo Gate 2a (`report/team/phieu_cham.md`).

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi (đạt đồng thuận 18/20 = 90% với Đào Vũ Minh Khánh) trong `report/team/bang_loi.md`.
- Hoàn thiện 2 chỉ số tự đề xuất, 10 event có `trace_id`, bảng kiểm tra chéo và 3 dòng rủi ro kinh tế E2 trong `report/team/chi_so.md`.
- Tổng hợp đầy đủ 7 mục, trạng thái, vai trò phụ trách và 4 điều kiện đề xuất trong `report/team/ho_so_launch_v0.md`.
- Hoàn thiện báo cáo nhóm `report/team/group_report.md` và cập nhật `TEAM.md`.

### Bằng chứng

- `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`.
- Báo cáo cá nhân: `report/team/2A202603864_NguyenVanQuoc.md`.
