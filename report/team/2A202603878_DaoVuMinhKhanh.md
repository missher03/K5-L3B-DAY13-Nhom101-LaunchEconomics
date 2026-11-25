# Báo cáo cá nhân — Đào Vũ Minh Khánh (2A202603878)

## 1. Thông tin thành viên

- Họ tên: Đào Vũ Minh Khánh
- MSSV: 2A202603878
- Email: daovuminhkhanh@gmail.com
- GitHub: https://github.com/iamdvmk
- Vai trong nhóm: Người gắn nhãn 1 (thành viên 3), phụ trách bảng lỗi (nhiệm vụ C) và kiểm tra checklist nộp bài, chấm chéo Gate 2a.

## 2. Phần việc phụ trách

Nhiệm vụ C (bảng lỗi và cách khắc phục): `report/team/bang_loi.md`. Chuẩn bị và chấm chéo Gate 2a: `report/team/phieu_cham.md`. Chạy bộ lệnh kiểm tra checklist `SUBMISSION.md` trước khi nộp.

## 3. Đóng góp cụ thể

- Tự gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR (bộ nhãn người 1), ghi vào `report/team/bang_loi.md`.
- So hai bộ nhãn, tính đồng thuận 18/20 = 90% (ngưỡng 80%); với 2 ca không trùng (ca 6, ca 17) chốt nhãn thống nhất và viết quy tắc phân biệt theo nguyên nhân gốc.
- Điền bảng khắc phục 5 ca đủ 5 loại (ca 1, 20, 16, 11, 5): mỗi dòng có event hoặc cách kiểm tra, ngưỡng, tần suất và một vai trò phụ trách.
- Chuyển tóm tắt bảng lỗi (4 · 5 · 4 · 4 · 3 ca theo 5 loại) cho thành viên 4 điền mục 5 của `report/team/ho_so_launch_v0.md`.
- Điền trước `report/team/phieu_cham.md` (thông tin nhóm, câu hỏi cho đội trình) và chuẩn bị bảng tìm bằng chứng cho ba tiêu chí C6–C8.

## 4. Bằng chứng

- Commit `3968c3d` "TV3: bang_loi.md".
- `report/team/bang_loi.md`: 2 bộ nhãn 20 ca, đồng thuận 18/20 = 90%, quy tắc cho ca 6 và ca 17, bảng khắc phục 5 dòng đủ 5 loại.
- Phân bố nhãn thống nhất: Do người dùng 4 ca (1, 6, 9, 14) · Hệ thống 5 ca (2, 7, 8, 15, 20) · Ngữ cảnh 4 ca (3, 10, 16, 18) · Giới hạn hệ thống 4 ca (4, 11, 13, 19) · Ngầm 3 ca (5, 12, 17); khớp 20/20 với bảng tham khảo trong tài liệu hướng dẫn (ngưỡng 16/20).
- Bộ nhãn khớp 18/20 với bảng tham khảo; lệch ở ca 6 (tôi gắn Hệ thống) và ca 17 (tôi gắn Giới hạn hệ thống).
- `report/team/phieu_cham.md`: điểm và quyết định của hội đồng ghi tại buổi duyệt chéo 17:00.

## 5. Công cụ AI đã dùng

- Claude (claude.ai), dùng trong phiên làm Lab 13:
  - Đề xuất nhãn thống nhất và quy tắc phân biệt cho ca 6, ca 17; soạn nháp bảng khắc phục 5 ca.
  - Chạy thử `src/lab13.py`, kiểm tra ô trống, dấu `?` và từ cấm trong `report/team/`; gợi ý cách điền `phieu_cham.md`; soạn nháp file này.
  - Dùng Claude soát bằng chứng trong hồ sơ nhóm NHKT để lập bản nháp `report/team/phieu_cham.md`; hội đồng nhóm 101 đọc lại từng dòng với hồ sơ của NHKT rồi chốt điểm 25/30.
- Cách kiểm tra: đối chiếu nhãn thống nhất với định nghĩa 5 loại trong đề bài và bảng tham khảo trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; đọc lại từng dòng bảng khắc phục để chắc có event, ngưỡng, tần suất và đúng một vai trò; tự chạy `python lab13.py` thấy dòng `ĐẠT`.

## 6. Tự đánh giá

- Bảng lỗi đạt các mốc của C3: hai bộ nhãn, đồng thuận 90% (≥ 80%), khớp đáp án 20/20 (≥ 16/20), bảng khắc phục đủ 5 loại.
- Bộ nhãn sai 2/20 ca: ca 6 gắn theo chỗ cần sửa thay vì nguyên nhân gốc (khách chọn sai mục); ca 17 nhầm "dùng dữ liệu cũ" với "không thể trả lời", trong khi điểm mấu chốt là không ai nhận ra.