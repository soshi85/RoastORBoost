from pathlib import Path
import pymupdf
from core.pdf_extractor import extract_text_from_pdf

def test_pdf_extraction(tmp_path: Path):
    pdf_path=tmp_path/"sample.pdf"
    doc=pymupdf.open();page=doc.new_page();page.insert_text((72,72),"Resume Test\nPython Backend");doc.save(pdf_path);doc.close()
    text=extract_text_from_pdf(str(pdf_path))
    assert "Resume Test" in text
    assert "Python Backend" in text
