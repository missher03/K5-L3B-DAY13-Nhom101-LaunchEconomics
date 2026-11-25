# Báo cáo cá nhân — Mai Lê Bá Vương

## 1. Thông tin thành viên

- Họ tên: Mai Lê Bá Vương
- MSSV: 2A202603872
- Email: Chưa cung cấp
- Vai trong nhóm: Thành viên 2 — phụ trách D1, D2, kế hoạch pilot và code tính E1.

## 2. Phần việc phụ trách

- Tính cỡ mẫu cho các cách chia pilot, chọn phương án 20 nhân viên can thiệp và 20 đối chứng, đồng thời ghi rõ đánh đổi về mức chênh có thể phát hiện.
- Tính thử ba chỉ số E1 từ 1.200 yêu cầu và chuẩn bị số liệu bàn giao cho TV4.
- Hoàn thiện `pilot_plan.yaml` với cách chia, rollout, luật dừng, cách rollback và ngày quyết định dự kiến.

## 3. Đóng góp cụ thể

- Tích hợp hàm tính D1 bằng `NormalIndPower` và `proportion_effectsize`, cùng hàm tính E1 nhận DataFrame vào `src/lab13.py` sau khi TV1 hoàn tất A/B.
- Hoàn thiện kế hoạch pilot. Mốc thiết kế là 859 yêu cầu hiệu dụng mỗi nhóm, 299 yêu cầu mỗi nhân viên, 5.980 yêu cầu thô mỗi nhóm và design effect 6,96.
- Ghi ba tỷ lệ E1 vào `report/team/chi_so.md` và chốt scope `noi_dia` + `hang_nang` theo A3 của TV1. Hai loại ngoài scope là `quoc_te` và `doi_tac`.

## 4. Bằng chứng

- D1 theo mốc hướng dẫn: 1.251 yêu cầu mỗi nhóm cho mức chênh 5 điểm; với 20 nhân viên mỗi nhóm, trần hiệu dụng là 1.000. Phương án 6 điểm có power khoảng 0,64 nếu tác động thật chỉ là 5 điểm.
- E1 trên dữ liệu giả lập: chỉ số chính 994/1.200 = 82,83%; bỏ qua gợi ý 48/177 = 27,12%; mở lại trong 7 ngày 51/1.200 = 4,25%.
- Theo A3 của TV1, chi phí mỗi việc thành công là 2.696 đ (`noi_dia`), 8.221 đ (`hang_nang`), 22.515 đ (`quoc_te`) và 10.215 đ (`doi_tac`), đều simulated.
- Tỷ lệ mở lại trong scope A3 là 39/982 = 3,97% (simulated). Các kết quả E1 được đối chiếu trực tiếp với CSV.
- Bằng chứng nằm trong `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml` và `report/team/chi_so.md`.

## 5. Công cụ AI đã dùng

- Dùng ChatGPT/Codex để hỗ trợ viết hàm tính, điền bản nháp kế hoạch và giải thích cách tính cỡ mẫu.
- Đối chiếu các số E1 bằng cách đọc CSV và so với mốc trong hướng dẫn. Ngày 25/11 nhóm đã chạy lại `python3 lab13.py` (in ba phép thử ĐẠT, D1 và E1 khớp) và `yaml.safe_load` trên `pilot_plan.yaml` (đọc được, không còn dấu `?`).

## 6. Tự đánh giá

- Đã chuẩn bị phần D1, D2 và E1, đồng thời nêu rõ đánh đổi power 0,64 khi thiết kế cho mức chênh 6 điểm.
- Phạm vi đã được cập nhật theo A3 của TV1. `lab13.py` và kiểm tra YAML đã chạy đạt trước khi nộp.
