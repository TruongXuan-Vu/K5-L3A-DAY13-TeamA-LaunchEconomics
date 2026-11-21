"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

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
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


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
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    print()
    ket_qua = mo_hinh(runs, reqs)
    print('=== A2 · Mô hình chi phí từ trace ===')
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    print()
    print('=== A3 · Tách theo loại yêu cầu ===')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub_reqs = reqs[reqs.loai == loai]
        n = len(sub_reqs)
        tc = (sub_reqs.ket_qua == 'thanh_cong').sum()

        runs_loai = runs[runs['request_id'].isin(sub_reqs['request_id'])]
        so_lan_chay = len(runs_loai)
        lan_chay_yc = so_lan_chay / n

        r = mo_hinh(runs, sub_reqs)
        print(f'{loai:10s} n={n:4d} thanh_cong={tc:4d} ({tc/n*100:5.1f}%) '
              f'lan_chay/yc={lan_chay_yc:5.2f} cps={r["cps"]:8,.0f} '
              f'so_voi_12000={r["cps"]/12000:.2f}x')
    print()
    print('=== A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ===')
    r = mo_hinh(runs, reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])])
    tc = (reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])].ket_qua == 'thanh_cong').sum()
    print(f'thanh_cong_trong_pham_vi={tc}')
    print(f'viec_thanh_cong_moi_thang={45000*tc/1200:.0f}')
    print(f'chi_phi_co_dinh_moi_viec={40000000/(45000*tc/1200):,.0f}')
    print(f'cps_trong_pham_vi={r["tong"]/tc:,.0f}')
    print(f'cps_plus_co_dinh={r["tong"]/tc + 40000000/(45000*tc/1200):,.0f}')
    print(f'cps_plus_co_dinh_mot_nua={r["tong"]/tc + 40000000/(45000*tc/1200/2):,.0f}')

    print()
    print('=== B1 · Đổi từng yếu tố ===')
    kich_ban = {
        'Gia token gap doi': dict(gia_vao=52, gia_ra=260),
        'Gia token giam mot nua': dict(gia_vao=13, gia_ra=65),
        'Xem lai gap doi': dict(he_so_xem_lai=2),
        'Xem lai giam mot nua': dict(he_so_xem_lai=0.5),
        'Lam lai gap doi': dict(he_so_lam_lai=2),
        'Lam lai giam mot nua': dict(he_so_lam_lai=0.5),
        'Luong nhan vien tang 25%': dict(luong_phut=2500),
        'Chi cho chay toi da 2 lan': dict(max_lan_chay=2),
        'Chi cho chay 1 lan': dict(max_lan_chay=1),
    }
    goc = mo_hinh(runs, reqs)['cps']
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:30s} {cps:8,.0f} {(cps/goc - 1)*100:+6.1f}%')

    print()
    print('=== B2 · Doi mot cap ===')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'Gia token gap doi + xem lai gap doi: {cps_cap:,.0f} ({(cps_cap/goc-1)*100:+.1f}%)')

    print()
    print('=== B3 · Gioi han chay lai ===')
    for k in [1, 2, 3]:
        r = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - r['thanh_cong']
        he_thong = r['tong'] + khong_tc * 12000
        print(f'Gioi han {k} lan: tro ly={r["tong"]:>12,.0f} khong_thanh_cong={khong_tc:4d} '
              f'he_thong={he_thong:>12,.0f} cps={r["cps"]:8,.0f}')

    print()
    print('=== B4 · Xem lai 100% (noi_dia + hang_nang) ===')
    sub_reqs = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    sub_runs = runs[runs['request_id'].isin(sub_reqs['request_id'])]
    co_it_nhat_mot_ok = sub_runs[sub_runs['status'] == 'ok']['request_id'].nunique()
    so_ca_lam_lai = (sub_reqs['ket_qua'] == 'lam_lai').sum()
    tong_token_tool = mo_hinh(runs, sub_reqs)['token'] + mo_hinh(runs, sub_reqs)['tool']
    xem_lai_100 = co_it_nhat_mot_ok * 5 * LUONG_PHUT
    lam_lai_100 = so_ca_lam_lai * 9 * LUONG_PHUT
    tong_b4 = tong_token_tool + xem_lai_100 + lam_lai_100
    tc_b4 = (sub_reqs['ket_qua'] == 'thanh_cong').sum()
    print(f'co_it_nhat_mot_ok={co_it_nhat_mot_ok} xem_lai={xem_lai_100:,.0f}')
    print(f'so_ca_lam_lai={so_ca_lam_lai} lam_lai={lam_lai_100:,.0f}')
    print(f'tong_token_tool={tong_token_tool:,.0f}')
    print(f'tong_b4={tong_b4:,.0f} thanh_cong={tc_b4} cps={tong_b4/tc_b4:,.0f} '
          f'so_voi_12000={tong_b4/tc_b4/12000:.2f}x')
