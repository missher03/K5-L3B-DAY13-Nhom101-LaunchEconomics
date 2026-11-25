# Báo cáo cá nhân — Nguyễn Văn Quốc - 2A202603864

## 1. Thông tin thành viên

- Họ tên: Nguyễn Văn Quốc
- MSSV: 2A202603864
- Email: quoc.nvsoict@gmail.com
- GitHub: missher03
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Người gắn nhãn 2 (Nhiệm vụ C — gắn nhãn độc lập 20 ca lỗi trong `report/team/bang_loi.md`).
- Giữ hồ sơ `report/team/ho_so_launch_v0.md` và tổng hợp báo cáo nhóm `report/team/group_report.md`.
- Hoàn thiện danh sách event có `trace_id`, kiểm tra chéo và bảng rủi ro kinh tế E2 trong `report/team/chi_so.md`.
- Tham gia hội đồng chấm chéo Gate 2a (`report/team/phieu_cham.md`).

## 3. Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR, so nhãn với Đào Vũ Minh Khánh đạt đồng thuận 18/20 = 90% trong `report/team/bang_loi.md`.
- Hoàn thiện 2 chỉ số tự đề xuất, 10 event có `trace_id`, kiểm tra chéo event–chỉ số và 3 dòng rủi ro kinh tế E2 trong `report/team/chi_so.md`.
- Tổng hợp đầy đủ 7 mục, nhãn trạng thái (`Giả lập`, `Xong, có bằng chứng`), vai trò phụ trách và 4 điều kiện đề xuất **Go có điều kiện** trong `report/team/ho_so_launch_v0.md`.
- Hoàn thiện `report/team/group_report.md` và cập nhật `TEAM.md`.

## 4. Bằng chứng

- `report/team/bang_loi.md`
- `report/team/chi_so.md`
- `report/team/ho_so_launch_v0.md`
- `report/team/group_report.md`
- `TEAM.md`

## 5. Công cụ AI đã dùng

- Sử dụng trợ lý AI (Antigravity) để lập kế hoạch chia việc song song (`task.md`), rà soát yêu cầu trong `CHECKPOINTS.md` / `RUBRIC.md`, kiểm tra cấu trúc các bảng trong `chi_so.md` và `ho_so_launch_v0.md`.
- Tự kiểm tra lại các con số E1 (`82,83%`, `27,12%`, `4,25%`) bằng lệnh Python đọc `src/logix_requests.csv` với `keep_default_na=False`, kiểm tra `yaml.safe_load` trên `pilot_plan.yaml`, kiểm tra không dùng từ cấm trong `report/team/`, và đối chiếu toàn bộ nhãn `simulated`.
- Dùng Claude soát bằng chứng trong hồ sơ nhóm NHKT để lập bản nháp `report/team/phieu_cham.md`; hội đồng nhóm 101 đọc lại từng dòng với hồ sơ của NHKT rồi chốt điểm 25/30.

## 6. Tự đánh giá

- Hoàn thành đầy đủ phần việc gắn nhãn 2, đặc tả chỉ số/event/rủi ro, hồ sơ launch v0 và báo cáo nhóm đúng tiến độ trước giờ duyệt chéo Gate 2a.
