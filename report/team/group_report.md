# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Nhóm 101
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm dựng bộ hồ sơ launch v0 cho trợ lý hoàn phí của LogiX-VN để bảo vệ trước hội đồng Gate 2a (duyệt kế hoạch pilot). Nhóm chia 4 thành viên làm việc song song theo 5 nhiệm vụ A–E:

- **Thành viên 1 (Đỗ Quốc Khánh):** Mô hình chi phí mỗi việc thành công và phân tích độ nhạy (`src/lab13.py`, `report/team/bang_chi_phi.md`).
- **Thành viên 2 (Mai Lê Bá Vương):** Tính cỡ mẫu cụm, tính thử chỉ số và thiết kế kế hoạch pilot (`src/lab13.py`, `report/team/pilot_plan.yaml`).
- **Thành viên 3 (Đào Vũ Minh Khánh):** Gắn nhãn độc lập 20 ca lỗi, lập bảng khắc phục và chuẩn bị phiếu chấm (`report/team/bang_loi.md`, `report/team/phieu_cham.md`).
- **Thành viên 4 (Nguyễn Văn Quốc):** Gắn nhãn độc lập 20 ca lỗi, đặc tả chỉ số/event/rủi ro kinh tế, tổng hợp hồ sơ một trang và báo cáo nhóm (`report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`).

## 3. Giải pháp

- **Nhiệm vụ A & B (Kinh tế & Độ nhạy):** Chi tiết công thức, 3 phép thử A1 đạt (`1,20 · 1,25 · 1,25`), bảng A2–A4, độ nhạy B1–B4 và đối chiếu tay nằm trong [bang_chi_phi.md](bang_chi_phi.md) và `src/lab13.py`.
- **Nhiệm vụ C (Phân loại lỗi & Khắc phục):** Hai bộ nhãn độc lập (đồng thuận 18/20 = 90%), quy tắc cho 2 ca lệch (ca 6, ca 17) và bảng khắc phục 5 ca nằm trong [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (Kế hoạch pilot):** Tính cỡ mẫu hiệu dụng khi chia theo `staff` và 3 luật dừng đủ 4 vế nằm trong [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E (Chỉ số, Rủi ro & Hồ sơ Gate 2a):** Đặc tả 5 chỉ số E1, 10 event có `trace_id`, kiểm tra chéo và 3 dòng rủi ro kinh tế nằm trong [chi_so.md](chi_so.md); hồ sơ một trang nằm trong [ho_so_launch_v0.md](ho_so_launch_v0.md).

## 4. Kết quả

- **Kinh tế & Độ nhạy:** Chi phí mỗi việc thành công là **4.472 đ** [simulated] (gấp 16,3× hóa đơn 274,7 đ/yc); chi phí cả hệ thống là **5.865 đ/yc = 0,49×** của 12.000 đ [simulated]. Trong phạm vi pilot (`noi_dia` 2.696 đ = 0,22×, `hang_nang` 8.221 đ = 0,69×), cộng cố định 40 triệu/tháng cho **4.599 đ = 0,38×** ở 45.000 yc/tháng [simulated]. Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%) [simulated]. Nếu xem lại 100%, chi phí là **11.743–12.415 đ** (0,98–1,03×) [simulated].
- **Lỗi & Chỉ số đợt chạy thử:** Đồng thuận gắn nhãn **18/20 = 90%**. Chỉ số chính đợt chạy thử **82,83%** (994/1.200), bỏ qua gợi ý **27,12%** (48/177), mở lại 7 ngày **4,25%** (51/1.200; trong phạm vi pilot 3,97%).
- **Kế hoạch pilot & Đề xuất:** Chia theo `staff` (20 nhân viên/nhóm, MDE 0,06, `n_per_arm = 859` hiệu dụng / 5.980 thô). Đề xuất cuối: **Go có điều kiện** (4 điều kiện về khoá chống trùng, chấp nhận MDE 6 điểm, bật event `trace_id` đo thật và giảm xem lại theo bậc).
- **Kết quả duyệt chéo Gate 2a:** Nhóm 101 làm hội đồng chấm nhóm NHKT **25/30** (đề xuất khớp bằng chứng 10 · số giả lập và phạm vi 5 · pilot ra được quyết định 10), quyết định **Go có điều kiện**; chi tiết trong [phieu_cham.md](phieu_cham.md). Phiếu chấm nhóm 101 nằm trong repo của nhóm làm hội đồng cho nhóm 101.

## 5. Khó khăn và cách xử lý

- Thời gian xem lại và làm lại trong dữ liệu là giả lập (`_simulated`) -> Nhóm gắn nhãn `simulated` ở mọi con số liên quan và yêu cầu thay bằng phút đo thật qua event `staff_review_decision`, `staff_rework_completed` sau tuần 1 pilot.
- Đợt chạy thử chưa có nhóm đối chứng -> Nhóm không viết "trợ lý đã nâng chỉ số", chỉ báo cáo hiện trạng đợt chạy thử (82,83%) và thiết kế đối chứng song song theo `staff` trong `pilot_plan.yaml`.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- **Hạn chế:** Tổng số CSKH là 40 người (20 cụm/nhóm) nên không đủ lực cho MDE 5 điểm (chấp nhận MDE 6 điểm); tỉ lệ mở lại 7 ngày vẫn ở mức 4,25% (3,97% trong phạm vi).
- **Hướng cải thiện:** Bật đầy đủ 10 event có `trace_id`, bổ sung khoá chống trùng lệnh hoàn và kiểm tra mẫu kế toán hằng tuần (`audit_sample_checked`) để bắt lỗi ngầm.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359)
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com)
- Tài liệu `statsmodels`, lớp `NormalIndPower` (mục `stats.power`)
