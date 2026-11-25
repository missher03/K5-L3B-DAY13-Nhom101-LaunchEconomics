# Phân công song song không phụ thuộc — Lab 13 (Nhóm 4 người)

> **Nguyên tắc chia việc:** Mỗi thành viên phụ trách **một luồng độc lập và sở hữu file riêng** ngay từ phút đầu tiên để **không ai phải chờ ai** và **không bị conflict Git**. Chỉ có **2 điểm đồng bộ ngắn**: Sync 1 (5 phút, riêng TV3 & TV4 so nhãn) và Sync 2 (15 phút lúc 16:30, cả nhóm ghép số liệu & chốt đề xuất trước giờ duyệt chéo 17:00).

---

## 1. Quy tắc bắt buộc (cả 4 người tự tuân thủ trong file của mình)

1. `src/lab13.py` phải qua đủ 3 phép thử A1 (`1,20 · 1,25 · 1,25` → in `ĐẠT`).
2. Mọi con số tính từ `phut_xem_lai_simulated` và `phut_lam_lai_simulated` phải gắn nhãn **`simulated`**.
3. Mỗi câu trả lời **≤ 3 dòng**, có **ít nhất 1 con số**.
4. **Tuyệt đối không dùng từ `"production"`** trong `report/team/` (Gate 2a chỉ duyệt **pilot**).
5. Đọc `logix_requests.csv` bằng `pd.read_csv('logix_requests.csv', keep_default_na=False)`. Không sửa `logix_runs.csv`, `logix_requests.csv`, `lab13_starter.py`. Không commit `.venv/`, `.env` hoặc file nháp tạm.
6. Cột *Người phụ trách* chỉ ghi **1 vai trò cụ thể** (không ghi "cả đội").

---

## 2. Bốn luồng làm việc song song (14:00 – 16:30)

### Luồng 1 — Thành viên 1: Toàn bộ Kinh tế & Độ nhạy (Nhiệm vụ A + B)
- **File sở hữu độc quyền:** `src/lab13.py` (phần A, B) · `report/team/bang_chi_phi.md`
- **Phụ thuộc ai?** **Không phụ thuộc ai.** Bắt đầu làm ngay từ 14:00.
- **Công việc cụ thể:**
  1. Cài `.venv` trong `src/`, chạy `python -c "import pandas, numpy, scipy, statsmodels; print('san sang')"`.
  2. Viết 3 hàm **A1** trong `src/lab13.py` (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`), chạy `kiem_tra_dap_an_biet_truoc()` phải in `ĐẠT`.
  3. Viết `mo_hinh(runs, reqs, ...)` (**A2**): trả về 7 key (`token`, `tool`, `xem_lai`, `lam_lai`, `tong`, `thanh_cong`, `cps`). Tử số tính mọi dòng `runs`; mẫu số chỉ đếm `ket_qua == 'thanh_cong'`.
  4. Viết **A3** (tách theo 4 giá trị `loai`: `noi_dia`, `hang_nang`, `quoc_te`, `doi_tac`) và **A4** (`noi_dia` + `hang_nang` cộng cố định `40.000.000 đ/tháng` ở mức `45.000` và `22.500` yêu cầu/tháng).
  5. Viết **B1** (9 kịch bản), **B2** (cặp token ×2 & xem lại ×2 + xếp hạng top 3), **B3** (giới hạn 1, 2, 3 lần chạy + chi phí cả hệ thống), **B4** (xem lại 100% cho `noi_dia` + `hang_nang`).
  6. Tự tính tay ít nhất 1 khoản (ví dụ tổng tiền token hoặc hóa đơn/yêu cầu) để kiểm chứng, rồi điền trọn vẹn các bảng **A1–A4, B1–B4** và câu trả lời vào `report/team/bang_chi_phi.md` (gắn nhãn `simulated` ở *Xem lại* và *Làm lại*).
- **Đầu ra giao lúc Sync 2 (16:30):**
  - Con số `cps` tổng, `cps` theo từng `loai` (để TV2 chốt `scope` trong `pilot_plan.yaml`), top 3 yếu tố nhạy nhất & số liệu B1–B4 (để TV4 điền `ho_so_launch_v0.md` và bảng rủi ro E2 trong `chi_so.md`).

---

### Luồng 2 — Thành viên 2: Cỡ mẫu Pilot, Chỉ số E1 & `pilot_plan.yaml` (Nhiệm vụ D + code E1)
- **File sở hữu độc quyền:** `src/lab13_de.py` *(file tạm cá nhân để không đụng `lab13.py` với TV1, sẽ gộp vào `lab13.py` và xóa lúc 16:30)* · `report/team/pilot_plan.yaml`
- **Phụ thuộc ai?** **Không phụ thuộc ai** trong 95% thời gian (mọi tham số D1 đã cho sẵn trong đề: `baseline=0.70`, `mde=0.05`, `alpha=0.05`, `power=0.80`, `ICC=0.02`; chỉ số E1 tính thẳng từ `logix_requests.csv`). Chỉ xác nhận lại 1 dòng `scope` với TV1 lúc 16:30.
- **Công việc cụ thể:**
  1. Cài `.venv` trong `src/` trên máy mình (đáp ứng yêu cầu "chạy hết trên 1 máy khác trong nhóm").
  2. Trong `src/lab13_de.py`, dùng `statsmodels` (`proportion_effectsize`, `NormalIndPower`) tính **5 câu D1**:
     - a) Chia theo yêu cầu; b) Theo nhân viên (`m=75`); c) 20 nhân viên/nhóm; d) 6 depot/nhóm; e) Mức chênh 6 điểm (`859`/nhóm), 20 nhân viên/nhóm.
  3. Tính tỉ lệ `mo_lai_trong_7_ngay == 1` hiện tại từ `logix_requests.csv`.
  4. Tính **3 chỉ số đầu bảng E1** trên 1.200 yêu cầu:
     - Chính: `%` `dong_trong_24h == 1 & mo_lai_trong_7_ngay == 0`
     - Dùng: tỉ lệ bỏ qua gợi ý `(sua + bo) / duoc_xem_lai == 1`
     - An toàn: `%` `mo_lai_trong_7_ngay == 1`
  5. Điền trước toàn bộ `report/team/pilot_plan.yaml`:
     - Phần chú thích `#` đầu file: 5 câu D1, 5 câu D2 (*tách được tác động*), đánh đổi nếu `< 20` cụm/nhóm, tỉ lệ `mo_lai_trong_7_ngay`.
     - Toàn bộ các trường YAML (`owner`, `assignment`, `primary_metric`, `identifiability`, **3 luật dừng** đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`, `rollback`, `decision_date`, `simulated_inputs`).
     - Chạy kiểm tra: `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"` và `grep -v '^ *#' ../report/team/pilot_plan.yaml | grep -n '?'`.
- **Đầu ra giao lúc Sync 2 (16:30):**
  - Ghép code D1 + E1 vào `TODO CP4` của `src/lab13.py` (chạy lại cả file để tự tay chạy phần A–B của TV1, đáp ứng quy tắc 2 người tự chạy code).
  - Giao 3 con số chỉ số E1 cho TV4 điền vào `chi_so.md` và `ho_so_launch_v0.md`.

---

### Luồng 3 — Thành viên 3: Bảng lỗi (Nhiệm vụ C) & Chuẩn bị Hội đồng / QA
- **File sở hữu độc quyền:** `report/team/bang_loi.md` · `report/team/phieu_cham.md`
- **Phụ thuộc ai?** Chỉ cần **5 phút Sync 1** với TV4 để đối chiếu 20 nhãn độc lập; toàn bộ thời gian còn lại làm độc lập 100%.
- **Công việc cụ thể:**
  1. **8 phút đầu (14:00–14:08):** Đọc mục "Hai mươi ca lỗi" trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, tự gắn nhãn độc lập cả 20 ca theo 5 loại Google PAIR (`Do người dùng`, `Hệ thống`, `Ngữ cảnh`, `Giới hạn hệ thống`, `Ngầm`) ra file nháp riêng (không trao đổi với TV4).
  2. **Sync 1 (5 phút cùng TV4):** Chép 2 bộ nhãn vào `report/team/bang_loi.md`, tính % đồng thuận (phải ≥ 16/20 = 80%; nếu thấp hơn thì thống nhất lại định nghĩa), chốt *Nhãn thống nhất*.
  3. **Làm độc lập phần còn lại của `bang_loi.md`:**
     - Viết 1 câu quy tắc phân biệt cho mỗi ca không trùng.
     - Chọn 5 ca (đủ 5 loại Google PAIR), điền bảng khắc phục: cách phát hiện **đo được** (event, ngưỡng, tần suất) và **1 vai trò** phụ trách.
  4. **Chuẩn bị trước cho phần Duyệt chéo & QA:**
     - Đọc kỹ `RUBRIC.md` (C6–C8) và điền sẵn khung `report/team/phieu_cham.md` (thông tin nhóm chấm).
     - Chuẩn bị sẵn kịch bản câu hỏi phản biện cho buổi bảo vệ 17:00 và bộ lệnh kiểm tra checklist `SUBMISSION.md` (`yaml.safe_load`, `grep '?'`, `grep -rni production ../report/team`).
- **Đầu ra giao lúc Sync 2 (16:30):**
  - Tóm tắt 5 loại lỗi & cách khắc phục chính (1 dòng) cho TV4 điền Mục 5 `ho_so_launch_v0.md`.

---

### Luồng 4 — Thành viên 4: Chỉ số, Event, Rủi ro & Hồ sơ Launch v0 (Nhiệm vụ E + Báo cáo)
- **File sở hữu độc quyền:** `report/team/chi_so.md` · `report/team/ho_so_launch_v0.md` · `report/team/group_report.md` · `TEAM.md`
- **Phụ thuộc ai?** Chỉ cần **8 phút đầu** gắn nhãn độc lập + **5 phút Sync 1** với TV3; từ 14:15 đến 16:30 làm độc lập toàn bộ phần khung & nội dung chữ, chỉ chừa ô số liệu để điền lúc Sync 2 (16:30).
- **Công việc cụ thể:**
  1. **8 phút đầu (14:00–14:08):** Gắn nhãn độc lập 20 ca lỗi ra file nháp riêng, rồi họp **Sync 1 (5 phút)** với TV3 để chốt bộ nhãn vào `bang_loi.md`.
  2. **Làm độc lập `report/team/chi_so.md`:**
     - Dựng bảng **E1**: giữ 3 chỉ số chuẩn (chừa ô số cho TV2 điền lúc 16:30), tự đề xuất thêm **1 chỉ số dùng** và **1 chỉ số an toàn** (kèm công thức).
     - Viết trọn vẹn bảng **Danh sách event** (≥ 6 event, mỗi event có `Ai tạo`, `Thuộc tính chính` chứa `trace_id`, `Thời điểm`) và mục **Kiểm tra chéo** (chỉ rõ mỗi chỉ số E1 tính từ event nào).
     - Dựng sẵn ≥ 2 dòng **E2 · Rủi ro kinh tế** (chọn các rủi ro trọng tâm như *tỉ lệ xem lại tăng* hoặc *làm lại tăng*, ghi sẵn `Dấu hiệu theo dõi`, `Hành động`, `Người phụ trách` là 1 vai trò; chừa ô `Tác động đã tính` điền số từ TV1 lúc 16:30).
  3. **Làm độc lập `report/team/ho_so_launch_v0.md`:**
     - Điền thông tin nhóm/lớp, chuẩn hóa cột *Trạng thái* (`Xong, có bằng chứng` / `Chưa` / `Giả lập`) và cột *Người phụ trách* (1 vai trò) cho đủ 7 mục; chừa ô *Con số chính* để điền lúc 16:30.
  4. **Làm độc lập `TEAM.md` & `report/team/group_report.md`:**
     - Điền thông tin nhóm, bảng 4 thành viên, khung 8 mục trong `group_report.md` (≤ 2 trang).

---

## 3. Lịch trình đồng bộ & Chốt bài (chỉ 2 lần gặp nhau)

| Mốc giờ | Hoạt động | Ai tham gia | Việc cần xong |
| :--- | :--- | :--- | :--- |
| **14:00 – 14:08** | Làm độc lập ngay từ đầu | TV1 (A–B), TV2 (D–E1), TV3 & TV4 (gắn nhãn 20 ca) | Không ai chờ ai |
| **14:08 – 14:13** | **Sync 1 (5 phút)** | Chỉ **TV3 & TV4** | So 20 nhãn độc lập, tính % đồng thuận → TV3 giữ `bang_loi.md`, TV4 chuyển sang `chi_so.md` & hồ sơ |
| **14:13 – 16:30** | Chạy song song toàn lực | Cả 4 người (4 file/nhánh riêng) | TV1 xong `bang_chi_phi.md`; TV2 xong `pilot_plan.yaml` + code D1/E1; TV3 xong `bang_loi.md` + QA; TV4 xong khung `chi_so.md`, `ho_so_launch_v0.md`, `group_report.md` |
| **16:30 – 16:55** | **Sync 2 (25 phút — Ghép bài)** | **Cả 4 người** | 1. Gộp `lab13_de.py` vào `src/lab13.py` (TV2 chạy lại toàn bộ `lab13.py` trên máy mình, xóa file tạm).<br>2. Chốt `scope` trong `pilot_plan.yaml`.<br>3. Điền các ô số còn trống vào `chi_so.md` và `ho_so_launch_v0.md`.<br>4. Cả nhóm chốt **Đề xuất** cuối (`Go` / `Go có điều kiện` / `No-go`).<br>5. TV3 chạy `yaml.safe_load`, kiểm `?` và kiểm từ cấm `production`. |
| **17:00 – 17:45** | Duyệt chéo Gate 2a | TV1 & TV2 (bảo vệ) · TV3 & TV4 (chấm nhóm `n + 1`) | Gửi `ho_so_launch_v0.md` cho hội đồng; hoàn thiện `phieu_cham.md` |
| **17:45 – 18:00** | Đóng gói & Push | Cả 4 người | Hoàn thiện `group_report.md`, `TEAM.md`, mỗi người copy `MSSV_HoTen.md` thành file riêng, commit & push |
| **Trước 23:59** | Nộp LMS | **Từng thành viên** | Mỗi người tự nộp cùng link repo nhóm lên LMS |
