# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | Trong đợt chạy thử: 82,83% (994/1.200), simulated |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | Trong đợt chạy thử: 27,12% (48/177), simulated |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | Trong đợt chạy thử: 4,25% (51/1.200), simulated |
| Dùng | Nhóm tự đề xuất: % yêu cầu ở nhóm can thiệp có nhân viên mở xem gợi ý trợ lý | Số yêu cầu có event `agent_suggestion_shown` chia tổng số yêu cầu của nhóm can thiệp (`arm == 'treatment'`) | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền phát hiện qua kiểm tra mẫu kế toán hằng tuần | Số đơn `so_tien_da_hoan != so_tien_dung` chia tổng số đơn được kiểm tra mẫu hằng tuần (bắt lỗi ngầm) | Không cần tính |

Theo phạm vi A3 đã chốt cho pilot (`noi_dia` + `hang_nang`), tỷ lệ mở lại trong 7 ngày là 39/982 = 3,97% (simulated).

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách / CSKH | `request_id, loai, so_tien, depot, arm, trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Trợ lý hoàn phí (Agent) | `run_id, attempt, tokens_in, tokens_out, tool_calls, status, trace_id` | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện CSKH | `staff_id, so_tien_de_xuat, trace_id` | Khi gợi ý của trợ lý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `staff_id, quyet_dinh (giu/sua/bo), phut_xem_lai_thuc, trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `staff_id, phut_lam_lai_thuc, ly_do, trace_id` | Khi nhân viên hoàn tất làm lại ca sai |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key, so_tien, ket_qua, trace_id` | Khi ghi nhận giao dịch hoàn tiền |
| `handoff_to_staff` | Trợ lý hoàn phí (Agent) | `reason, so_lan_chay, tom_tat, trace_id` | Khi vượt giới hạn lần chạy và chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at, trong_24h, trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | Khách hàng / Hệ thống ticket | `reopened_at, trong_7_ngay, reason, trace_id` | Khi khách mở lại yêu cầu sau khi đóng |
| `audit_sample_checked` | Bộ phận Kế toán | `so_tien_da_hoan, so_tien_dung, lech_tien, trace_id` | Khi kiểm tra mẫu ngẫu nhiên hằng tuần |

**Kiểm tra chéo:**

- **Chỉ số chính (% đóng trong 24h và không mở lại trong 7 ngày):** tính từ `refund_request_created`, `ticket_closed` (`trong_24h == true`) và không có `ticket_reopened` (`trong_7_ngay == true`) theo cùng `trace_id`.
- **Chỉ số dùng (tỉ lệ bỏ qua gợi ý):** tính từ `agent_suggestion_shown` (mẫu số) và `staff_review_decision` có `quyet_dinh` là `sua` hoặc `bo` (tử số).
- **Chỉ số an toàn (tỉ lệ lỗi lọt đến khách):** tính từ `ticket_reopened` (`trong_7_ngay == true`) chia tổng số `refund_request_created`.
- **Chỉ số dùng tự đề xuất (% mở xem gợi ý):** tính từ `agent_suggestion_shown` chia `refund_request_created` (trong nhóm can thiệp).
- **Chỉ số an toàn tự đề xuất (% đơn hoàn sai tiền qua kiểm tra mẫu):** tính từ `audit_sample_checked` (`lech_tien != 0` chia tổng số ca kiểm tra).

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | **+51,8%**, từ 4.472 đ lên **6.787 đ** [simulated] | Tỉ lệ `lam_lai` theo tuần > 7% | Thu hẹp phạm vi về `noi_dia`, rà soát 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải duy trì xem lại 100% kéo dài | **11.743 đ** (0,98×) với 9 phút/ca hoặc **12.415 đ** (1,03×) với 15,3 phút/ca [simulated] | Tỉ lệ yêu cầu được xem lại > 50% sau tuần 2 của pilot | Giảm tỉ lệ xem lại theo bậc khi tỉ lệ `sua + bo` < 15% | Trưởng nhóm CSKH |
| Khối lượng yêu cầu thấp hơn dự kiến | Cố định 40 triệu đ/tháng: **+1.185 đ/việc** (4.599 đ) ở 45.000 yc/tháng, **+2.370 đ/việc** (5.784 đ) nếu giảm một nửa [simulated] | Số việc thành công theo tuần < 50% kế hoạch | Dừng mở rộng bước rollout, rà soát lại chi phí cố định 40 triệu đ/tháng | Giám đốc vận hành LogiX-VN |
