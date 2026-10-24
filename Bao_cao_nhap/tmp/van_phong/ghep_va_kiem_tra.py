from pathlib import Path
import re
import hashlib
import json
import difflib

root = Path(__file__).resolve().parents[2]
work = root/'tmp/van_phong'
report = root/'Chuong-1-Tong-quan-de-tai.md'
old = report.read_text(encoding='utf8')
body = (work/'chuong1-noi-dung-moi.md').read_text(encoding='utf8')
figures = re.findall(r'!\[[^\n]+\n\n\*Hình [^\n]+\n\n\*Nguồn:[^\n]+', (work/'hinh-da-kiem-chung.md').read_text(encoding='utf8'))
assert len(figures)==8
for n,figure in enumerate(figures,1):
    assert body.count('{{HINH_'+str(n)+'}}')==1
    body=body.replace('{{HINH_'+str(n)+'}}',figure)
body=body.replace(r'\(f_s = 1/T_s\)', '$f_s = 1/T_s$')
new=body.rstrip()+'\n\n'+(work/'tai-lieu-tham-khao.md').read_text(encoding='utf8')
assert '{{' not in new
assert re.findall(r'^# (1\.\d+)\.',new,re.M)==['1.1','1.2','1.3','1.4','1.5']
assert re.findall(r'^\*Hình (1\.\d+)\.',new,re.M)==[f'1.{i}' for i in range(1,9)]
assert re.findall(r'^\*Bảng (1\.\d+)\.',new,re.M)==[f'1.{i}' for i in range(1,4)]
main,bib=new.split('# Tài liệu tham khảo của Chương 1')
codes=set(re.findall(r'\b(?:TL|W)\d+\b',main))
refs=set(re.findall(r'^\*\*((?:TL|W)\d+) —',bib,re.M))
assert codes==refs
links=re.findall(r'!?\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))\)',new)
local=[a or b for a,b in links if not (a or b).startswith(('http:','https:'))]
assert all((root/p).is_file() for p in local)
assert '%%' not in new
assert not any(x in main for x in ['SHA-256','giải mã','tải lỗi','thông tin hiển thị ký số','đường dẫn cũ','phần liên hệ là phân tích'])
initial=json.loads((root/'tmp/kiem_chung/source_hashes.json').read_text(encoding='utf-8-sig'))
assert all(hashlib.sha256(Path(x['Path']).read_bytes()).hexdigest().upper()==x['Hash'] for x in initial)

paragraphs=lambda s: [p for p in s.split('\n\n') if len(p)>100 and not p.startswith(('#','>','*','!','|','-'))]
new_paragraphs=paragraphs(body)
old_paragraphs=set(paragraphs(old.split('# Tài liệu tham khảo')[0]))
same=[p for p in new_paragraphs if p in old_paragraphs]
result={
 'new_word_count':len(new.split()),
 'new_characters':len(new),
 'figures':len(figures),
 'tables':3,
 'local_links':len(local),
 'reference_codes':sorted(refs),
 'bullet_items':len(re.findall(r'^- ',main,re.M)),
 'numbered_steps':len(re.findall(r'^\d+\. ',main,re.M)),
 'unchanged_long_explanation_paragraphs':len(same),
 'unchanged_technical_sources':len(initial),
 'a4_pages':'Chưa dàn trang, không xác nhận số trang thực tế.'
}
report.write_text(new,encoding='utf8')
(work/'ket-qua-ra-soat-van-phong.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(result,ensure_ascii=False,indent=2))
