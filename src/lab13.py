"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    p = float(p)
    if not 0 <= p <= 1:
        raise ValueError('p phải nằm trong [0, 1]')
    if k is not None and (not isinstance(k, int) or k < 1):
        raise ValueError('k phải là số nguyên dương hoặc None')
    if k is None:
        return math.inf if p == 0 else 1.0 / p
    if p == 0:
        return float(k)
    return (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    p = float(p)
    if not 0 <= p <= 1:
        raise ValueError('p phải nằm trong [0, 1]')
    if k is not None and (not isinstance(k, int) or k < 1):
        raise ValueError('k phải là số nguyên dương hoặc None')
    if k is None:
        return 0.0 if p == 0 else 1.0
    return 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    success = ti_le_thanh_cong(p, k)
    if success == 0:
        return math.inf
    return so_lan_chay_ky_vong(p, k) / success


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, hoa_don_moi_yc, xem_lai, lam_lai, tong, thanh_cong, cps.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - chay_lai: phần token + tool của lần chạy thứ 2 trở đi; đã nằm trong token và tool, không cộng thêm vào tong.
    - hoa_don_moi_yc: (token + tool) chia cho số yêu cầu.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - cps (chi phí mỗi việc thành công): tong chia thanh_cong; thanh_cong = 0 thì cps là inf.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    required_runs = {'request_id', 'attempt', 'tokens_in', 'tokens_out', 'tool_calls'}
    required_reqs = {
        'request_id', 'ket_qua', 'so_lan_chay',
        'phut_xem_lai_simulated', 'phut_lam_lai_simulated'
    }
    missing_runs = required_runs.difference(runs.columns)
    missing_reqs = required_reqs.difference(reqs.columns)
    if missing_runs or missing_reqs:
        raise ValueError(f'Thiếu cột: runs={sorted(missing_runs)}, reqs={sorted(missing_reqs)}')

    counted_runs = runs[runs['request_id'].isin(reqs['request_id'])]
    counted_reqs = reqs.copy()
    if max_lan_chay is not None:
        if not isinstance(max_lan_chay, int) or max_lan_chay < 1:
            raise ValueError('max_lan_chay phải là số nguyên dương hoặc None')
        counted_runs = counted_runs[pd.to_numeric(counted_runs['attempt']) <= max_lan_chay]
        over_limit = pd.to_numeric(counted_reqs['so_lan_chay']) > max_lan_chay
        counted_reqs.loc[over_limit, 'ket_qua'] = 'chuyen_nhan_vien'
        counted_reqs.loc[over_limit, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    token = (
        pd.to_numeric(counted_runs['tokens_in']).sum() * gia_vao
        + pd.to_numeric(counted_runs['tokens_out']).sum() * gia_ra
    ) / 1000.0
    tool = pd.to_numeric(counted_runs['tool_calls']).sum() * gia_tool
    runs_lai = counted_runs[pd.to_numeric(counted_runs['attempt']) > 1]
    chay_lai = (
        pd.to_numeric(runs_lai['tokens_in']).sum() * gia_vao
        + pd.to_numeric(runs_lai['tokens_out']).sum() * gia_ra
    ) / 1000.0 + pd.to_numeric(runs_lai['tool_calls']).sum() * gia_tool
    hoa_don_moi_yc = (token + tool) / len(reqs)
    xem_lai = pd.to_numeric(counted_reqs['phut_xem_lai_simulated']).sum() * luong_phut * he_so_xem_lai
    lam_lai = pd.to_numeric(counted_reqs['phut_lam_lai_simulated']).sum() * luong_phut * he_so_lam_lai
    thanh_cong = int(counted_reqs['ket_qua'].eq('thanh_cong').sum())
    tong = token + tool + xem_lai + lam_lai
    cps = tong / thanh_cong if thanh_cong else math.inf
    return {
        'token': token,
        'tool': tool,
        'chay_lai': chay_lai,
        'hoa_don_moi_yc': hoa_don_moi_yc,
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': cps,
    }


def tinh_d1():
    """Tính cỡ mẫu hai nhóm, hiệu ứng cụm và power cho phương án D1."""
    baseline_rate = 0.70
    target_5pp = 0.75
    target_6pp = 0.76
    alpha = 0.05
    target_power = 0.80
    icc = 0.02
    power_model = NormalIndPower()

    effect_5pp = abs(proportion_effectsize(baseline_rate, target_5pp))
    n_5pp_exact = power_model.solve_power(
        effect_size=effect_5pp,
        alpha=alpha,
        power=target_power,
        ratio=1,
        alternative='two-sided',
    )
    n_5pp = math.ceil(n_5pp_exact)

    mean_per_staff = 75
    de_75 = 1 + (mean_per_staff - 1) * icc
    clustered_raw_n = math.ceil(n_5pp * de_75)
    staff_per_arm = math.ceil(clustered_raw_n / mean_per_staff)

    max_effective_20_staff = 20 / icc
    max_effective_6_depots = 6 / icc

    effect_6pp = abs(proportion_effectsize(baseline_rate, target_6pp))
    n_6pp_exact = power_model.solve_power(
        effect_size=effect_6pp,
        alpha=alpha,
        power=target_power,
        ratio=1,
        alternative='two-sided',
    )
    n_6pp_statsmodels = math.ceil(n_6pp_exact)
    n_6pp_lab = 859
    staff_count = 20
    requests_per_staff = math.ceil(
        n_6pp_lab * (1 - icc) / (staff_count - n_6pp_lab * icc)
    )
    design_effect = 1 + (requests_per_staff - 1) * icc
    raw_requests_6pp = staff_count * requests_per_staff
    effective_n_6pp = raw_requests_6pp / design_effect
    power_at_5pp = power_model.power(
        effect_size=effect_5pp,
        nobs1=effective_n_6pp,
        alpha=alpha,
        ratio=1,
        alternative='two-sided',
    )

    return {
        'n_5pp_exact': n_5pp_exact,
        'n_5pp': n_5pp,
        'de_75': de_75,
        'clustered_raw_n': clustered_raw_n,
        'staff_per_arm': staff_per_arm,
        'max_effective_20_staff': max_effective_20_staff,
        'max_effective_6_depots': max_effective_6_depots,
        'n_6pp_exact': n_6pp_exact,
        'n_6pp_statsmodels': n_6pp_statsmodels,
        'n_6pp_lab': n_6pp_lab,
        'requests_per_staff': requests_per_staff,
        'design_effect': design_effect,
        'raw_requests_6pp': raw_requests_6pp,
        'effective_n_6pp': effective_n_6pp,
        'power_at_5pp': power_at_5pp,
    }


def tinh_e1(reqs):
    """Tính ba chỉ số E1 và tỷ lệ mở lại trong phạm vi pilot dự kiến."""
    primary_success = (reqs['dong_trong_24h'] == 1) & (
        reqs['mo_lai_trong_7_ngay'] == 0
    )
    reviewed = reqs[reqs['duoc_xem_lai'] == 1]
    ignored = reviewed['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    scope = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]

    return {
        'primary': (int(primary_success.sum()), len(reqs)),
        'usage': (int(ignored.sum()), len(reviewed)),
        'safety': (int((reqs['mo_lai_trong_7_ngay'] == 1).sum()), len(reqs)),
        'scope_reopen': (
            int((scope['mo_lai_trong_7_ngay'] == 1).sum()),
            len(scope),
        ),
    }


def in_ket_qua_d1(result):
    print('\nD1 · Cỡ mẫu (statsmodels NormalIndPower, hai phía)')
    print(
        f"a) 70% → 75%: n={result['n_5pp_exact']:.2f} trước làm tròn, "
        f"{result['n_5pp']:,} yêu cầu/nhóm"
    )
    print(
        f"b) m=75, ICC=0.02: DE={result['de_75']:.2f}, "
        f"{result['clustered_raw_n']:,} yêu cầu thô/nhóm, "
        f"{result['staff_per_arm']} nhân viên/nhóm"
    )
    print(
        f"c) 20 nhân viên/nhóm: trần hiệu dụng c/ICC="
        f"{result['max_effective_20_staff']:,.0f}, thấp hơn "
        f"{result['n_5pp']:,} cần cho mức chênh 5 điểm"
    )
    print(
        f"d) 6 depot/nhóm: trần hiệu dụng c/ICC="
        f"{result['max_effective_6_depots']:,.0f}, thấp hơn "
        f"{result['n_5pp']:,} cần cho mức chênh 5 điểm"
    )
    print(
        f"e) 70% → 76%: statsmodels n={result['n_6pp_exact']:.2f} "
        f"(làm tròn {result['n_6pp_statsmodels']:,}); dùng mốc lab "
        f"{result['n_6pp_lab']:,} hiệu dụng/nhóm; với 20 nhân viên cần "
        f"{result['requests_per_staff']} yêu cầu/người, "
        f"{result['raw_requests_6pp']:,} thô/nhóm, "
        f"DE={result['design_effect']:.2f}"
    )
    print(
        f"   Power nếu tác động thật là 5 điểm: "
        f"{result['power_at_5pp']:.3f}"
    )


def in_ket_qua_e1(result):
    print('\nE1 · Chỉ số trong đợt chạy thử (không có nhóm đối chứng)')
    labels = [
        ('Chính · đóng trong 24h, không mở lại 7 ngày', 'primary'),
        ('Dùng · bỏ qua gợi ý (sửa hoặc bỏ)', 'usage'),
        ('An toàn · mở lại trong 7 ngày', 'safety'),
    ]
    for label, key in labels:
        numerator, denominator = result[key]
        rate = numerator / denominator if denominator else float('nan')
        print(f'{label}: {numerator}/{denominator} = {rate:.2%} [simulated]')

    numerator, denominator = result['scope_reopen']
    rate = numerator / denominator if denominator else float('nan')
    print(
        f'Mở lại trong phạm vi noi_dia + hang_nang: '
        f'{numerator}/{denominator} = {rate:.2%} [simulated]'
    )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        dinh_dang = ',.1f' if ten == 'hoa_don_moi_yc' else ',.0f'
        print(f'{ten:12s} {gia_tri:>14{dinh_dang}}')
    # A2 · Các dòng còn lại của bảng: tỉ trọng từng khoản, hệ số so với hoá đơn, chi phí cả hệ thống.
    khong_thanh_cong = len(reqs) - ket_qua['thanh_cong']
    chi_phi_he_thong = ket_qua['tong'] + khong_thanh_cong * BASELINE
    moi_yeu_cau = chi_phi_he_thong / len(reqs)
    print(f'A2 · Trong tổng chi phí: làm lại {ket_qua["lam_lai"] / ket_qua["tong"]:.1%} [simulated], '
          f'xem lại {ket_qua["xem_lai"] / ket_qua["tong"]:.1%} [simulated], '
          f'token {ket_qua["token"] / ket_qua["tong"]:.1%}, tool {ket_qua["tool"] / ket_qua["tong"]:.1%}')
    print(f'A2 · Chi phí mỗi việc thành công gấp {ket_qua["cps"] / ket_qua["hoa_don_moi_yc"]:.1f} lần '
          f'hoá đơn chia số yêu cầu')
    # So với nhân viên tự làm phải dùng chi phí cả hệ thống trên mỗi yêu cầu, không dùng CPS một mình.
    print(f'A2 · Chi phí cả hệ thống (cộng {khong_thanh_cong} ca × {BASELINE:,.0f} đ): {chi_phi_he_thong:,.0f} đ = '
          f'{moi_yeu_cau:,.0f} đ/yêu cầu = {moi_yeu_cau / BASELINE:.2f}× {BASELINE:,.0f} đ [simulated]')
    # A3 · Tách mô hình theo loại yêu cầu.
    print('\nA3 · Chi phí theo loại yêu cầu')
    ket_qua_theo_loai = {}
    for loai, nhom_reqs in reqs.groupby('loai', sort=True):
        ids = set(nhom_reqs['request_id'])
        nhom_runs = runs[runs['request_id'].isin(ids)]
        model = mo_hinh(nhom_runs, nhom_reqs)
        ket_qua_theo_loai[loai] = model
        ti_le = model['thanh_cong'] / len(nhom_reqs) if len(nhom_reqs) else 0
        so_lan = len(nhom_runs) / len(nhom_reqs) if len(nhom_reqs) else 0
        # Cột "So với 12.000 đ" = CPS của trợ lý chia BASELINE, chưa cộng tiền nhân viên làm thay;
        # dòng còn lại cộng BASELINE cho mọi yêu cầu không thành công rồi chia cho số yêu cầu (cách tính B3).
        he_thong_moi_yc = (model['tong'] + (len(nhom_reqs) - model['thanh_cong']) * BASELINE) / len(nhom_reqs)
        print(f'{loai:12s} yêu_cầu={len(nhom_reqs):4d} thành_công={ti_le:.1%} '
              f'lần_chạy/yêu_cầu={so_lan:.3f} CPS={model["cps"]:,.2f} đ ({model["cps"] / BASELINE:.2f}× baseline), '
              f'cả_hệ_thống/yêu_cầu={he_thong_moi_yc:,.0f} đ ({he_thong_moi_yc / BASELINE:.2f}× baseline)')
    # Tỉ lệ ok theo từng lần thử, để trả lời "cho chạy lại tới 3 lần có giúp không".
    ok_theo_lan = runs.merge(reqs[['request_id', 'loai']], on='request_id').assign(
        ok=lambda bang: bang['status'].eq('ok')
    ).pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')
    for loai, dong in ok_theo_lan.iterrows():
        print(f'  Tỉ lệ ok theo lần thử · {loai}: ' + ' → '.join(f'{gia_tri:.1%}' for gia_tri in dong))

    # A4 · Chi phí cố định 40 triệu đồng/tháng cho phạm vi nội địa + hàng nặng.
    scope = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    scope_ids = set(scope['request_id'])
    scope_model = mo_hinh(runs[runs['request_id'].isin(scope_ids)], scope)
    # 45,000/month là toàn bộ nhu cầu; mẫu số giữ cả nhóm ngoài scope (đúng định nghĩa volume).
    scope_success_rate = scope_model['thanh_cong'] / len(reqs) if len(reqs) else 0
    print('\nA4 · Phạm vi noi_dia + hang_nang, chi phí cố định 40.000.000 đ/tháng')
    for volume in (45000, 22500):
        monthly_success = volume * scope_success_rate
        fixed_per_success = 40_000_000 / monthly_success if monthly_success else math.inf
        full_cps = scope_model['cps'] + fixed_per_success
        print(f'{volume:>6,d} yêu_cầu/tháng: thành_công~{monthly_success:,.0f}, '
              f'cố_định/thành_công={fixed_per_success:,.2f} đ, tổng_CPS={full_cps:,.2f} đ '
              f'({full_cps / BASELINE:.2f}× baseline)')

    # B1 · Độ nhạy một yếu tố. Các khoản nhân sự xuất phát từ phút simulated.
    def thay_doi_nhom(he_so_token=1.0, he_so_xem=1.0, he_so_lam=1.0,
                      luong=LUONG_PHUT, max_lan=None):
        return mo_hinh(
            runs, reqs,
            gia_vao=GIA_VAO * he_so_token,
            gia_ra=GIA_RA * he_so_token,
            gia_tool=GIA_TOOL,
            luong_phut=luong,
            he_so_xem_lai=he_so_xem,
            he_so_lam_lai=he_so_lam,
            max_lan_chay=max_lan,
        )

    b1 = [
        ('Giá token gấp đôi', thay_doi_nhom(he_so_token=2)),
        ('Giá token giảm một nửa', thay_doi_nhom(he_so_token=0.5)),
        ('Tỉ lệ xem lại gấp đôi', thay_doi_nhom(he_so_xem=2)),
        ('Tỉ lệ xem lại giảm một nửa', thay_doi_nhom(he_so_xem=0.5)),
        ('Số ca làm lại gấp đôi', thay_doi_nhom(he_so_lam=2)),
        ('Số ca làm lại giảm một nửa', thay_doi_nhom(he_so_lam=0.5)),
        ('Lương nhân viên tăng 25%', thay_doi_nhom(luong=LUONG_PHUT * 1.25)),
        ('Chỉ cho chạy tối đa 2 lần', thay_doi_nhom(max_lan=2)),
        ('Chỉ cho chạy 1 lần', thay_doi_nhom(max_lan=1)),
    ]
    print('\nB1 · Độ nhạy (thay đổi CPS so với A2)')
    for ten, model in b1:
        delta = (model['cps'] / ket_qua['cps'] - 1) * 100
        print(f'{ten:32s} CPS={model["cps"]:,.2f} đ  thay_đổi={delta:+.2f}%')
    # Tự kiểm tra: sáu dòng đầu đi theo cặp "gấp đôi" rồi "giảm một nửa" của cùng một yếu tố.
    for i in range(0, 6, 2):
        tang = b1[i][1]['cps'] / ket_qua['cps'] - 1
        giam = 1 - b1[i + 1][1]['cps'] / ket_qua['cps']
        print(f'  Tự kiểm tra {b1[i][0].replace("gấp đôi", "").strip()}: +{tang:.1%} → −{giam:.1%} '
              f'({"đúng nửa" if abs(giam - tang / 2) < 1e-9 else "LỆCH"})')

    # B2 · Cặp giá token ×2 và xem lại ×2; xếp hạng theo tác động tuyệt đối lớn nhất.
    pair = thay_doi_nhom(he_so_token=2, he_so_xem=2)
    print(f'\nB2 · Token ×2 và xem lại ×2: CPS={pair["cps"]:,.2f} đ '
          f'({(pair["cps"] / ket_qua["cps"] - 1) * 100:+.2f}%)')
    grouped_effects = {}
    for ten, model in b1:
        if 'token' in ten.lower():
            factor = 'Giá token'
        elif 'xem lại' in ten.lower():
            factor = 'Xem lại'
        elif 'làm lại' in ten.lower():
            factor = 'Làm lại'
        elif 'lương' in ten.lower():
            factor = 'Lương nhân viên'
        else:
            factor = 'Giới hạn số lần chạy'
        effect = abs(model['cps'] / ket_qua['cps'] - 1) * 100
        grouped_effects[factor] = max(grouped_effects.get(factor, 0), effect)
    for rank, (factor, effect) in enumerate(sorted(grouped_effects.items(), key=lambda x: x[1], reverse=True)[:3], 1):
        print(f'  {rank}. {factor}: tác động lớn nhất {effect:.2f}%')

    # B3 · Chi phí toàn hệ thống = chi phí trợ lý + BASELINE cho yêu cầu không thành công.
    # Cột "Chi phí mỗi việc thành công" của bảng B3 là CPS của trợ lý (model['cps']), chưa cộng BASELINE.
    print('\nB3 · Giới hạn chạy; fallback người = BASELINE 12.000 đ/yêu cầu không thành công')
    for limit in (1, 2, 3):
        model = thay_doi_nhom(max_lan=limit)
        failed = len(reqs) - model['thanh_cong']
        system_cost = model['tong'] + failed * BASELINE
        system_cps = system_cost / model['thanh_cong'] if model['thanh_cong'] else math.inf
        print(f'{limit} lần: trợ_lý={model["tong"]:,.2f} đ, không_thành_công={failed}, '
              f'toàn_hệ_thống={system_cost:,.2f} đ, CPS={model["cps"]:,.2f} đ, '
              f'CPS_hệ_thống={system_cps:,.2f} đ')

    # B4 · Kiểm tra biên: xem lại tất cả trường hợp có ít nhất một lần chạy OK.
    # Kịch bản chuẩn giả định 5 phút xem lại và 9 phút làm lại; đối chiếu thêm phút làm lại simulated.
    scope_runs = runs[runs['request_id'].isin(scope_ids)]
    reviewed_ids = set(scope_runs.loc[scope_runs['status'].eq('ok'), 'request_id'])
    review_cost_100 = len(reviewed_ids) * 5 * LUONG_PHUT
    rework_cases = int(scope['ket_qua'].eq('lam_lai').sum())
    rework_cost_assumption = rework_cases * 9 * LUONG_PHUT
    scope_tech_cost = scope_model['token'] + scope_model['tool']
    # Phút làm lại trung bình lấy trên MỌI ca có phut_lam_lai_simulated > 0 của cả mẫu (74 ca),
    # rồi nhân với số ca làm lại trong phạm vi; không lấy trung bình riêng trong phạm vi.
    rework_minutes = pd.to_numeric(reqs['phut_lam_lai_simulated'])
    rework_mean = rework_minutes[rework_minutes > 0].mean()
    simulated_rework_cost = rework_cases * rework_mean * LUONG_PHUT

    # Mức hoà vốn: số phút xem lại mỗi yêu cầu để chi phí B4 đúng bằng BASELINE.
    def phut_xem_lai_hoa_von(tien_lam_lai):
        return ((BASELINE * scope_model['thanh_cong'] - scope_tech_cost - tien_lam_lai)
                / (len(reviewed_ids) * LUONG_PHUT))

    def in_b4(ghi_chu, tien_lam_lai):
        tong_b4 = scope_tech_cost + review_cost_100 + tien_lam_lai
        cps_b4 = tong_b4 / scope_model['thanh_cong']
        print(f'  {ghi_chu}: tổng={tong_b4:,.0f} đ (token + tool {scope_tech_cost:,.0f}, '
              f'xem lại {review_cost_100:,.0f}, làm lại {tien_lam_lai:,.0f}) ÷ {scope_model["thanh_cong"]} '
              f'việc thành công = CPS {cps_b4:,.2f} đ ({cps_b4 / BASELINE:.2f}× baseline); '
              f'hoà vốn xem lại {phut_xem_lai_hoa_von(tien_lam_lai):.2f} phút/lần.')

    print(f'\nB4 · Xem lại 100% (simulated), noi_dia + hang_nang: {len(reviewed_ids)} yêu cầu × 5 phút, '
          f'{rework_cases} ca làm lại')
    in_b4('Làm lại 9 phút/ca (giả định của đề)', rework_cost_assumption)
    in_b4(f'Làm lại {rework_mean:.1f} phút/ca (trung bình {int((rework_minutes > 0).sum())} ca lam_lai '
          f'của cả mẫu, cột simulated)', simulated_rework_cost)

    # D1 · Cỡ mẫu hai nhóm và hiệu chỉnh thiết kế theo cụm.
    in_ket_qua_d1(tinh_d1())

    # E1 · Chỉ số của đợt chạy thử, tính từ cùng DataFrame reqs đã đọc ở đầu.
    in_ket_qua_e1(tinh_e1(reqs))
