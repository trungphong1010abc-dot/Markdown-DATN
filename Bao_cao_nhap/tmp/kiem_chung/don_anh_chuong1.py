from pathlib import Path
import json
import re

root=Path(__file__).resolve().parents[2]
folder=(root/'hinh_minh_hoa').resolve()
assert folder.parent==root and not folder.is_symlink()
rename={
 'Hinh_1_8_Cau_truc_tu_trung_the_KMZ_31.jpg':'Hinh_1_1_Cau_truc_tu_trung_the_KMZ_31.jpg',
 'Hinh_1_6_Thanh_cai_ha_the_nong_chay_do_ho_quang.jpg':'Hinh_1_3_Thanh_cai_ha_the_nong_chay_do_ho_quang.jpg',
 'Hinh_1_5_Nang_luong_tac_dong_theo_thoi_gian_ho_quang.png':'Hinh_1_4_Nang_luong_tac_dong_theo_thoi_gian_ho_quang.png',
 'Hinh_1_7_Nguyen_ly_phoi_hop_anh_sang_va_qua_dong.png':'Hinh_1_5_Nguyen_ly_phoi_hop_anh_sang_va_qua_dong.png',
 'Hinh_1_12_Mo_dun_phat_hien_ho_quang_Mors_Smitt_1S23.png':'Hinh_1_6_Mo_dun_phat_hien_ho_quang_Mors_Smitt_1S23.png'
}
remove=[
 'Hinh_1_1_Ho_quang_dien_giua_hai_dien_cuc.jpg',
 'Hinh_1_3_Phan_biet_Arc_Flash_va_Arc_Blast.jpg',
 'Hinh_1_4_Cac_dang_su_co_ho_quang_noi_tiep_va_song_song.png',
 'Hinh_1_9_Bo_tri_cam_bien_quang_va_do_dong.png',
 'Hinh_1_10_He_thu_nghiem_do_dong_phat_hien_ho_quang.jpg',
 'Hinh_1_11_Nguyen_mau_phat_hien_ho_quang_noi_tiep.jpg',
 'Hinh_1_13_Phan_loai_giai_phap_bao_ve_ho_quang.jpg',
 'Hinh_1_14_Nha_may_HEINEKEN_Vung_Tau.jpg'
]
report=root/'Chuong-1-Tong-quan-de-tai.md'
content=report.read_text(encoding='utf8')
assert all(name not in content for name in remove)
for old,new in rename.items():
    source=folder/old
    target=folder/new
    assert source.resolve().parent==folder and target.resolve().parent==folder
    assert source.is_file() and not source.is_symlink() and not target.exists()

# Hai tệp trung gian do tác vụ này tạo được cập nhật trước khi kiểm tra tham chiếu.
(root/'tmp/chuong1-hoan-chinh.md').write_text(content,encoding='utf8')
order=root/'tmp/kiem_chung/anh-order.txt'
order.write_text('\n'.join(p.name for p in folder.iterdir() if p.name not in remove),encoding='utf8')

# Chỉ xét tham chiếu dùng ảnh trong tài liệu, không coi chuỗi tên trong mã kiểm kê là liên kết.
references=[]
for p in root.rglob('*'):
    if not p.is_file() or p.suffix.lower() not in {'.md','.html','.txt','.json','.css'}:
        continue
    rel=p.relative_to(root)
    if rel.parts[0]=='Tham khảo' or 'pdf_deps' in rel.parts or 'reader' in rel.parts:
        continue
    s=p.read_text(encoding='utf8',errors='ignore')
    for name in remove:
        if name in s:
            references.append((str(rel),name))
assert not references, references

for old,new in rename.items():
    (folder/old).rename(folder/new)
    content=content.replace('hinh_minh_hoa/'+old,'hinh_minh_hoa/'+new)
report.write_text(content,encoding='utf8')
(root/'tmp/chuong1-hoan-chinh.md').write_text(content,encoding='utf8')

deleted=[]
for name in remove:
    target=folder/name
    assert target.resolve().parent==folder and target.is_file() and not target.is_symlink()
    target.unlink()
    deleted.append(name)
result={'renamed':rename,'deleted':deleted,'kept_unresolved':[],'remaining':[p.name for p in folder.iterdir()]}
(root/'tmp/kiem_chung/ket-qua-don-anh.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
order.write_text('\n'.join(result['remaining']),encoding='utf8')
print(json.dumps(result,ensure_ascii=False,indent=2))
