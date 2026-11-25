# Báo cáo cá nhân — Đỗ Quốc Khánh (2A202603823)

## 1. Thông tin thành viên

- Họ tên: Đỗ Quốc Khánh
- MSSV: 2A202603823
- Email: 26ai.khanhdq2@vinuni.edu.vn
- GitHub: dqk2210
- Vai trong nhóm: Người viết code cho nhiệm vụ A và B.

## 2. Phần việc phụ trách

Nhiệm vụ A (mô hình chi phí) và B (bảng độ nhạy): `src/lab13.py` phần A, B và `report/team/bang_chi_phi.md`.

## 3. Đóng góp cụ thể

- Viết ba hàm A1, `mo_hinh`, phần A3, A4 và B1–B4 trong `src/lab13.py`. Trợ lý AI soát lại, sửa cách tính B4 và bổ sung các dòng in còn thiếu (xem mục 5).
- Điền `report/team/bang_chi_phi.md`: bảng A1, A2 (9 dòng), A3 (4 dòng), A4 (2 dòng), B1 (9 dòng), B2, B3 (3 dòng), B4, câu trả lời và mục Đối chiếu tay.
- Tính tay để kiểm số: 5.600 lần gọi tool × 15 đ = 84.000 đ; 890 phút × 2.000 đ = 1.780.000 đ [simulated]; (4.373.585 + 222 × 12.000) ÷ 1.200 = 5.865 đ [simulated].
- Điền thông tin cá nhân vào `TEAM.md`.

## 4. Bằng chứng

- File: `src/lab13.py`, `report/team/bang_chi_phi.md`.
- `python lab13.py` (trong `src/`) in `Ba phép thử đáp án biết trước: ĐẠT` với 1,20 · 1,25 · 1,25.
- Số chính: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn chia số yêu cầu (274,7 đ); chi phí cả hệ thống 5.865 đ mỗi yêu cầu = 0,49× của 12.000 đ [simulated].
- Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%) [simulated].
- B3: giới hạn 2 lần rẻ nhất cho công ty với 6.901.220 đ [simulated]. B4: xem lại 100% cho 11.743 đ = 0,98× [simulated]; tính 15,3 phút làm lại [simulated] thì 12.415 đ = 1,03× [simulated].
- 80 số trong `report/team/bang_chi_phi.md` khớp với số `src/lab13.py` in ra; so với bảng trong tài liệu hướng dẫn, lệch lớn nhất 0,39% (ngưỡng 2%).

## 5. Công cụ AI đã dùng

- Trợ lý AI trong OpenCode (mô hình GLM-5.4), dùng trong phiên làm Lab 13:
  - Soát `src/lab13.py`: kiểm tra hàm A1 và `mo_hinh`; sửa B4 để lấy trung bình 15,3 phút làm lại [simulated] trên 74 ca của cả mẫu; thêm mức hoà vốn; thêm các dòng in còn thiếu ở A2, A3 và B3.
  - Soạn nội dung `report/team/bang_chi_phi.md` từ số in ra của `src/lab13.py`.
  - Soạn file này và phần cá nhân trong `TEAM.md`.
- Cách kiểm tra: chạy lại `python lab13.py` trong `src/` và đọc kết quả in ra; tính tay các khoản ở mục 3; so từng số trong bảng với số trong tài liệu hướng dẫn.

## 6. Tự đánh giá

- Đủ bốn bước của thành viên 1: ba phép thử in `ĐẠT`; bảng A1–A4, B1–B4 có đủ số và nhãn `simulated`; lệch tối đa 0,39% so với tài liệu.
- Phần code và bảng có trợ lý AI soạn và soát, nên tôi cần đọc lại `src/lab13.py` để tự giải thích được công thức chi phí mỗi việc thành công và cách tính B3, B4.
- Việc còn lại: chạy `python lab13.py` trên máy của một thành viên khác trong nhóm trước khi nộp.
