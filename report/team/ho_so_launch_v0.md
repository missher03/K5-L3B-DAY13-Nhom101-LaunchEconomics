# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Nhóm 101 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** [simulated] (gấp 16,3× hóa đơn 274,7 đ/yc); phạm vi `noi_dia` + `hang_nang` cộng cố định 40 triệu/tháng: **4.599 đ** (0,38×) ở 45.000 yc/tháng [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống: **5.865 đ/yc = 0,49×** của 12.000 đ [simulated]; trong phạm vi `noi_dia` (2.696 đ = 0,22×) & `hang_nang` (8.221 đ = 0,69×); giới hạn 2 lần chạy rẻ nhất cả hệ thống (**6.901.220 đ**) [simulated] | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử: chính **82,83%** (994/1.200) · dùng bỏ qua gợi ý **27,12%** (48/177) · an toàn mở lại 7 ngày **4,25%** (51/1.200; phạm vi pilot 3,97%); đủ 10 event có `trace_id` | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 2 người gắn nhãn **18/20 = 90%** (khớp 20/20 sau chốt: 4 Do người dùng · 5 Hệ thống · 4 Ngữ cảnh · 4 Giới hạn · 3 Ngầm); đủ 5 ca khắc phục có ngưỡng đo và vai trò phụ trách | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Phạm vi `noi_dia` + `hang_nang` tại 12 depot (loại `quoc_te` 1,88× và `doi_tac`); chia theo `staff` (20 nhân viên/nhóm, MDE 0,06, `n_per_arm` 859 hiệu dụng / 5.980 thô); đủ 3 luật dừng `NẾU–TRONG–THÌ–KHÔNG THÌ` | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại ×2 lên **6.787 đ** (+51,8%); xem lại 100% lên **11.743–12.415 đ** (0,98–1,03×); giảm nửa khối lượng tăng cố định lên **2.370 đ/việc** [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go có điều kiện *(cho kế hoạch pilot phạm vi `noi_dia` + `hang_nang` tại 12 depot, bắt đầu 2026-12-07)*.

- Điều kiện 1: Bổ sung khoá chống trùng (idempotency key) và đối soát sổ cái mỗi giờ cho lỗi hệ thống hoàn trùng (ca 20, ca 7) trước ngày bắt đầu pilot — người phụ trách: Kỹ sư trưởng agent — ngày kiểm tra: 2026-12-05.
- Điều kiện 2: Giám đốc vận hành ký chấp nhận đánh đổi MDE 6 điểm (power ≈ 0,64 ở mức 5 điểm với 20 nhân viên/nhóm) — người phụ trách: Giám đốc vận hành LogiX-VN — ngày kiểm tra: 2026-12-05.
- Điều kiện 3: Bật đủ 10 event có `trace_id` và thay phút `simulated` bằng thời gian đo thật ngay sau tuần 1 của pilot — người phụ trách: Trưởng nhóm CSKH — ngày kiểm tra: 2026-12-14.
- Điều kiện 4: Thực hiện lộ trình giảm tỉ lệ xem lại theo bậc xuống dưới 50% sau bước 0.25 (vì xem lại 100% tốn 11.743–12.415 đ [simulated], không tiết kiệm so với 12.000 đ) — người phụ trách: PM trợ lý hoàn phí — ngày kiểm tra: 2026-12-20.
