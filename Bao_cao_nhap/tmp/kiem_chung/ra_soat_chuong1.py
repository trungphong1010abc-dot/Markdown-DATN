from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tmp/reader'))
import fitz

report = ROOT / 'Chuong-1-Tong-quan-de-tai.md'
text = report.read_text(encoding='utf-8-sig')
body, bibliography = text.split('# Tài liệu tham khảo của Chương 1')
used = set(re.findall(r'\b(?:TL|W)\d+\b', body))
refs = set(re.findall(r'^\*\*((?:TL|W)\d+) —', bibliography, re.M))
assert used == refs, (used, refs)
assert re.findall(r'^# (1\.[1-5])\.', body, re.M) == ['1.1','1.2','1.3','1.4','1.5']
assert re.findall(r'^\*Hình (1\.\d+)\.', body, re.M) == [f'1.{i}' for i in range(1,9)]
assert re.findall(r'^\*Bảng (1\.\d+)\.', body, re.M) == [f'1.{i}' for i in range(1,4)]
assert '%%' not in text
general = body.split('# 1.1.',1)[1].split('# 1.3.',1)[0]
assert not re.search(r'Quảng Ninh|\bW[12]\b|6[,.]6\s*kV|50 Hz ±5%|Power Cell|DCS|biến tần',general)
assert not re.search(r'cần (?:tách|xác định|kiểm tra|phân biệt|được)|người thiết kế cần',body)
links = re.findall(r'!?\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))\)', text)
local = [a or b for a,b in links if not (a or b).startswith(('http:', 'https:'))]
assert all((ROOT / p).is_file() for p in local), [p for p in local if not (ROOT / p).is_file()]
tables = []
for line in text.splitlines():
    if line.startswith('|'):
        if not tables or tables[-1][-1] is None:
            tables.append([])
        tables[-1].append(line)
    elif tables and tables[-1] and tables[-1][-1] is not None:
        tables[-1].append(None)
for rows in tables:
    rows = [r for r in rows if r is not None]
    assert len({r.count('|') for r in rows}) == 1, rows

initial = json.loads((ROOT/'tmp/kiem_chung/source_hashes.json').read_text(encoding='utf-8-sig'))
for item in initial:
    p = Path(item['Path'])
    assert hashlib.sha256(p.read_bytes()).hexdigest().upper() == item['Hash'], str(p)
pdfs = ['qtp-full.pdf','1s23-v01-0-xac-minh.pdf','user-guide-1s23-iss-c-xac-minh.pdf','1s23-k.pdf']
checked_pdfs = {p:len(fitz.open(ROOT/'nguon_web'/p)) for p in pdfs}
result = {
    'source_files_unchanged': len(initial),
    'reference_codes': sorted(refs),
    'valid_local_links': len(local),
    'figures':8,
    'tables':3,
    'quang_ninh_separate_from_sections_1_1_and_1_2':True,
    'instructional_prose_phrases_removed':True,
    'pdf_page_counts':checked_pdfs,
    'whitespace_word_count':len(text.split()),
    'characters':len(text),
    'note':'Không xuất DOCX/PDF; chưa xác nhận số trang A4 thực tế.'
}
(ROOT/'tmp/kiem_chung/ket-qua-kiem-tra.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(result,ensure_ascii=False,indent=2))
