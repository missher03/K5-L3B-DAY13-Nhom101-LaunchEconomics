# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py` (chạy trong thư mục `src/`). Mọi con số tính từ hai cột `_simulated` ghi nhãn `simulated`. Tổng chi phí và chi phí mỗi việc thành công đều chứa tiền giờ nhân viên từ hai cột này nên cũng gắn nhãn; toàn bộ B1–B4 tính từ các số đó. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

`python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT`.

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 (= (1 − 0,2²) ÷ 0,8) |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 (= 1 ÷ 0,8) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (= 1 ÷ 0,8; k triệt tiêu) |

## A2 · Mô hình chi phí từ trace

1.624 lần chạy của agent cho 1.200 yêu cầu: 1.200 lần thứ nhất, 258 lần thứ hai, 166 lần thứ ba. Tử số tính mọi lần chạy, kể cả lần lỗi; mẫu số chỉ đếm yêu cầu có `ket_qua` là `thanh_cong`.

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 (5.600 lần gọi) | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 (890 phút) | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 (1.132 phút) | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | token + tool + xem lại + làm lại | có phần simulated |
| Số việc thành công | 978 (trên 1.200 yêu cầu) | `ket_qua` | đếm từ dữ liệu |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | 329.585 ÷ 1.200 | đo từ trace |

Dòng *Trong đó* là một phần của Token + Tool (329.585 đ), không cộng thêm vào tổng.

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? Gấp **16,3 lần** (4.472 đ [simulated] ÷ 274,7 đ = 16,28). Hoá đơn chỉ có token và tool; chi phí thật có thêm 4.044.000 đ [simulated] tiền giờ nhân viên (xem lại + làm lại).
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại** chiếm nhiều nhất: 2.264.000 đ = **51,8%** [simulated]. Xem lại đứng thứ hai: 1.780.000 đ = **40,7%** [simulated]; token và tool chỉ chiếm **7,5%** (329.585 đ).

**Lưu ý khi so với 12.000 đ.** Số 4.472 đ [simulated] chỉ chia cho 978 việc trợ lý làm xong và chưa có tiền nhân viên làm thay 222 ca không thành công (148 `chuyen_nhan_vien` + 74 `lam_lai`). Muốn so với "nhân viên tự làm" phải dùng chi phí cả hệ thống trên mỗi yêu cầu: (4.373.585 + 222 × 12.000) ÷ 1.200 = 7.037.585 ÷ 1.200 = **5.865 đ = 0,49×** của 12.000 đ [simulated].

Các bảng sau có cột *So với 12.000 đ* theo cách thứ nhất (chi phí mỗi việc thành công của trợ lý ÷ 12.000 đ), dùng để so các loại yêu cầu và các kịch bản với nhau. Khi so sánh tổng thể với nhân viên tự làm, chỉ dùng số **5.865 đ = 0,49×** này.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% (783) | 1,11 | 2.696 đ [simulated] | 0,22× [simulated] |
| hang_nang | 158 | 74,1% (117) | 1,47 | 8.221 đ [simulated] | 0,69× [simulated] |
| quoc_te | 150 | 27,3% (41) | 2,32 | 22.515 đ [simulated] | 1,88× [simulated] |
| doi_tac | 68 | 54,4% (37) | 1,88 | 10.215 đ [simulated] | 0,85× [simulated] |

Tỉ lệ ok theo từng lần thử, chia cho số lần chạy có ở lần thử đó:

| Loại | Lần 1 | Lần 2 | Lần 3 |
| --- | ---: | ---: | ---: |
| noi_dia | 91,0% | 75,7% | 38,9% |
| hang_nang | 70,9% | 39,1% | 17,9% |
| quoc_te | 30,0% | 11,4% | 2,2% |
| doi_tac | 51,5% | 18,2% | 14,8% |

Cột *So với 12.000 đ* lấy chi phí mỗi việc thành công của trợ lý chia 12.000 đ, cùng cách với 4.472 đ ở A2: chưa cộng 12.000 đ cho ca không thành công của loại đó. Nếu cộng theo cách tính B3 rồi chia cho số yêu cầu thì được noi_dia 3.159 đ (0,26×), hang_nang 9.201 đ (0,77×), quoc_te 14.874 đ (1,24×), doi_tac 11.029 đ (0,92×) [simulated]. Loại nào trên 12.000 đ và loại nào dưới 12.000 đ không đổi.

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? **quoc_te không đáng**: 22.515 đ [simulated] mỗi việc thành công = **1,88 lần** 12.000 đ, và chỉ **27,3%** yêu cầu thành công (41/150). Chạy lại tới 3 lần **không giúp**: tỉ lệ ok theo lần thử là **30,0% → 11,4% → 2,2%** (45/150, 12/105, 2/93), vì lỗi lặp trên cùng một yêu cầu nên mỗi lần chạy lại chỉ tốn thêm tiền. **doi_tac** (10.215 đ = 0,85× [simulated], 54,4%) sát ngưỡng và có điều khoản riêng, nên cũng để ngoài phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Phạm vi có 982 yêu cầu và 900 việc thành công; chi phí trong phạm vi là 3.072.513 đ [simulated], tức 3.414 đ [simulated] mỗi việc thành công. Việc thành công mỗi tháng = khối lượng × 900 ÷ 1.200; chi phí cố định mỗi việc = 40.000.000 ÷ việc thành công mỗi tháng.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× [simulated] |
| Một nửa khối lượng (22.500 yêu cầu/tháng) | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× [simulated] |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? **Không đổi kết luận** ở cả hai khối lượng: **4.599 đ = 0,38×** [simulated] ở 45.000 yêu cầu/tháng và **5.784 đ = 0,48×** [simulated] ở 22.500 yêu cầu/tháng, đều rẻ hơn 12.000 đ. Khối lượng giảm một nửa thì cố định mỗi việc tăng gấp đôi (**1.185 → 2.370 đ**), nên chi phí cố định chỉ đáng lo khi lượng việc nhỏ. Hai số này chưa cộng 12.000 đ cho 82 ca không thành công trong phạm vi.

## B1 · Đổi từng yếu tố

Gốc (A2): 4.472 đ [simulated]. Thay đổi = (chi phí kịch bản ÷ chi phí gốc) − 1.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ [simulated] | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ [simulated] | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ [simulated] | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ [simulated] | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ [simulated] | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ [simulated] | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ [simulated] | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ [simulated] | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ [simulated] | −8,1% |

Tự kiểm tra: mỗi kịch bản "giảm một nửa" giảm đúng nửa mức "gấp đôi" (+5,6% → −2,8%; +40,7% → −20,3%; +51,8% → −25,9%). Hai dòng cuối cho chi phí giảm chỉ vì có thêm 12 ca và 97 ca chuyển sang nhân viên mà cột chi phí chưa tính 12.000 đ cho họ; tính cả hệ thống (B3) thì giới hạn 1 lần đắt nhất.

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated]. Bằng tổng hai tác động riêng (+5,6% + 40,7% = 46,3%), vì mô hình cộng tuyến tính: hai khoản tiền cộng vào cùng một tử số rồi chia cho 978 việc thành công.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: **1. số ca làm lại** (+51,8%) · **2. tỉ lệ xem lại** (+40,7%) · **3. lương nhân viên** (+23,1%). Giá token chỉ +5,6%, nên pilot phải theo dõi tỉ lệ làm lại và tỉ lệ xem lại, không phải giá token.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công, vì nhân viên phải làm thay.

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ [simulated] | 319 | 7.449.781 đ [simulated] | 4.111 đ [simulated] (thấp nhất) |
| 2 lần | 4.093.220 đ [simulated] | 234 | 6.901.220 đ [simulated] (rẻ nhất) | 4.237 đ [simulated] |
| 3 lần | 4.373.585 đ [simulated] | 222 | 7.037.585 đ [simulated] | 4.472 đ [simulated] |

Cột cuối chỉ tính tiền trợ lý (cách tính như A2), chưa cộng 12.000 đ cho số yêu cầu không thành công. Nếu cộng rồi chia cho số việc thành công thì được 8.456 đ, 7.144 đ và 7.196 đ [simulated].

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? **Rẻ nhất cho công ty là 2 lần: 6.901.220 đ** [simulated], ít hơn 3 lần **136.365 đ** [simulated] (7.037.585 − 6.901.220) và ít hơn 1 lần **548.561 đ** [simulated] (7.449.781 − 6.901.220). **Không trùng**: chi phí mỗi việc thành công thấp nhất lại ở **1 lần** (4.111 đ [simulated]). Chỉ tối ưu số đó sẽ đẩy thêm **85 việc** (319 − 234) sang nhân viên và làm công ty tốn thêm 548.561 đ [simulated].

## B4 · Nếu phải xem lại tất cả

Cách tính cho 982 yêu cầu `noi_dia` + `hang_nang`: token + tool 224.513 đ, cộng 948 yêu cầu có ít nhất một lần chạy ok × 5 phút × 2.000 đ = 9.480.000 đ, cộng 48 ca làm lại × 9 phút × 2.000 đ = 864.000 đ, được 10.568.513 đ; chia cho 900 việc thành công.

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: **11.743 đ = 0,98×** của 12.000 đ [simulated], tức gần như hoà. Nếu mỗi ca làm lại mất **15,3 phút** như trung bình cột `phut_lam_lai_simulated` của 74 ca (thay vì 9 phút) thì **12.415 đ = 1,03×** [simulated], đắt hơn nhân viên tự làm. Mức hoà vốn: mỗi lần xem lại tối đa **5,12 phút** (làm lại 9 phút) hoặc **4,80 phút** (làm lại 15,3 phút) [simulated].
- Kết quả này nói gì về thứ pilot cần học được? Xem lại 100% thì trợ lý gần như không tiết kiệm, vì tiền xem lại (9.480.000 đ) chiếm **89,7%** của tổng 10.568.513 đ [simulated]. Pilot phải học được hai số: **tỉ lệ xem lại** giảm an toàn được bao nhiêu phần trăm, và mỗi lần xem lại có ngắn hơn **5,12 phút** (hoặc **4,80 phút**) không. Phút `_simulated` phải được thay bằng phút đo thật sau tuần **1**.

## Đối chiếu tay

Tính tay từ hai file CSV để kiểm số in ra của `src/lab13.py`.

| Khoản | Cách tính tay | Tính tay | `src/lab13.py` in ra |
| --- | --- | ---: | ---: |
| Tiền gọi tool | Cộng cột `tool_calls` của 1.624 lần chạy được 5.600 lần gọi; 5.600 × 15 đ | 84.000 đ | 84.000 đ |
| Tiền xem lại | Cộng cột `phut_xem_lai_simulated` được 890 phút; 890 × 2.000 đ | 1.780.000 đ [simulated] | 1.780.000 đ |
| Chi phí mỗi việc thành công | (245.585 + 84.000 + 1.780.000 + 2.264.000) ÷ 978 = 4.373.585 ÷ 978 | 4.472 đ [simulated] | 4.472 đ |
| Tỉ trọng làm lại | 2.264.000 ÷ 4.373.585 | 51,8% [simulated] | 51,8% |
| Chi phí cả hệ thống trên mỗi yêu cầu | (4.373.585 + 222 × 12.000) ÷ 1.200 = 7.037.585 ÷ 1.200 | 5.865 đ [simulated] | 5.865 đ |
| Chi phí mỗi việc thành công khi xem lại 100% | (224.513 + 948 × 5 × 2.000 + 48 × 9 × 2.000) ÷ 900 = 10.568.513 ÷ 900 | 11.743 đ [simulated] | 11.743 đ |
