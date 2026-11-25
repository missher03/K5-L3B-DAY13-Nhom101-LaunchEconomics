# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Nhóm 101 - Đào Vũ Minh Khánh, Nguyễn Văn Quốc
- Nhóm được chấm: NHKT (L3B) · repo https://github.com/BSFactor/K5-L3B-DAY13-NHKT-LaunchEconomics · chấm trên commit `6f357f6`

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | "Go có điều kiện" khớp số: loại quoc_te (1,88×, thành công 27,3%), nêu power 0,64 nếu tác động thật 5 điểm, xem lại 100% 11.743–12.414 đ (0,98–1,03×) kèm điều kiện giảm xem lại theo bậc. Lưu ý: mục 3 so 12.000 đ bằng 4.599 đ chứ không dùng chi phí cả hệ thống 5.865 đ/yc (0,49×); nhóm có ghi "chưa cộng ca không thành công" nên không trừ điểm. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 5 | Phạm vi thu hẹp về noi_dia + hang_nang có lý do bằng số (0,22× và 0,69×), và hồ sơ một trang có nhãn. Nhưng trong `bang_chi_phi.md`, các bảng A3, A4, B1, B3 và số 12.414 đ ở B4 thiếu nhãn simulated, dù đều chứa tiền phút xem lại/làm lại. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia theo nhân viên 20 + 20, có 20 cụm mỗi nhóm, 859 hiệu dụng (DE 6,96, ≥ 299 yêu cầu/người), đối chứng chạy cùng lúc. Ba luật dừng có ngưỡng (6% / +2 điểm / 1 ca hoàn trùng; 6.000 đ; 40%), thời hạn (3 ngày, 2 tuần, 1 tuần) và người dừng (Giám đốc vận hành, PM, Trưởng nhóm CSKH). Góp ý nhỏ: vế KHÔNG THÌ của luật 1 và luật 3 viết như cho phép thay vì nêu việc bị cấm; trường `assignment` chưa ghi giá trị seed. |
| **Tổng** | | | | **25 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Pilot chỉ cho noi_dia + hang_nang (4.599 đ/việc kể cả cố định ở 45.000 yc/tháng, simulated). Điều kiện bổ sung: gắn nhãn simulated cho mọi số trong `bang_chi_phi.md`, và trong hồ sơ dùng chi phí cả hệ thống (5.865 đ/yc = 0,49×, simulated) khi so với nhân viên tự làm. Ngoài ra báo cáo cá nhân `2A202603884_NguyenMinhThanh.md` còn dùng từ bị cấm theo quy tắc 5 của lab, nên xoá đi.

**Một câu hỏi cho đội trình:** Pilot chia theo nhân viên hay depot, mỗi nhóm được bao nhiêu cụm? Nếu dưới 20 cụm thì nhóm chấp nhận đánh đổi gì, và luật dừng nào (ngưỡng, thời hạn, ai có quyền dừng) bảo vệ quyết định đó?

**Câu trả lời của đội trình (ghi lại tại buổi):** "Chưa hỏi được tại buổi" 
