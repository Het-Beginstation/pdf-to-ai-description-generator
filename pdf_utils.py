import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path: str) -> str:
    try:
        pdf_document = fitz.open(pdf_path)
        text = ""
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
        return text
    except Exception as e:
        print(f"Failed to extract text from {pdf_path}: {e}")
        return ""