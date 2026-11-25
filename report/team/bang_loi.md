# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Đào Vũ Minh Khánh · Người gắn nhãn 2: Nguyễn Văn Quốc (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Hệ thống | Do người dùng | Không | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Giới hạn hệ thống | Ngầm | Không | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 18 / 20 = 90%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 6 — Do người dùng, không phải Hệ thống:** nguyên nhân gốc là khách chọn sai mục "Hoàn phí giao trễ" cho hàng vỡ; trợ lý xử lý đúng luồng đã chọn, còn việc không phát hiện mâu thuẫn giữa mục chọn và mô tả là phần cải thiện ở cột khắc phục.
- **Ca 17 — Ngầm, không phải Giới hạn hệ thống:** trợ lý vẫn trả lời được nhưng dùng bảng giá cũ, lệch 1.000–2.000 đ/đơn trên 212 đơn trong 9 ngày mà không khách nào mở lại và không cảnh báo nào kích, nên đây là sai không ai nhận ra chứ không phải "không thể trả lời".

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `bank_refund_rejected` (thuộc tính `trace_id`, `reason=sai_so_tai_khoan`); đếm theo ngày, cảnh báo khi > 1% số lệnh hoàn/ngày | Kiểm tra độ dài và checksum số tài khoản ngay khi khách nhập, bắt nhập lại lần 2 để so khớp trước khi tạo lệnh hoàn | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát sổ cái mỗi giờ: > 1 bản ghi hoàn tiền cho cùng mã vận đơn; ngưỡng 0 ca | Thêm khoá chống trùng (idempotency key = mã vận đơn) cho lệnh hoàn; yêu cầu gửi lại trong lúc đang xử lý thì trả "đang xử lý" | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Event `notification_sent` có giờ gửi trong 22:00–07:00 kèm số phản ánh "làm phiền"; tổng hợp theo tuần, ngưỡng 3 phản ánh/tuần | Tin thông báo rơi vào khung 22:00–07:00 được hẹn gửi lúc 07:00; tiền vẫn hoàn ngay | Trưởng nhóm CSKH |
| 11 | Giới hạn hệ thống | Event `input_unsupported` (thuộc tính `trace_id`, `type=audio`); theo dõi tỉ lệ theo ngày, xem xét khi > 2% số yêu cầu | Nói rõ chưa xử lý được tin thoại, kèm nút "Chuyển nhân viên" và nút nhập nhanh mã vận đơn; ghi nhận nhu cầu giọng nói cho phiên bản sau | PM trợ lý hoàn phí |
| 5 | Ngầm | Kiểm tra mẫu 100 đơn có mã giảm giá mỗi tuần, so số hoàn với giá sau giảm; ngưỡng 1% đơn lệch | Tính hoàn theo giá sau giảm; ghi `discount_code` và giá gốc/giá sau giảm vào trace để đối soát | Kế toán trưởng |
