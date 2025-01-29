import fitz  # PyMuPDF

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path: str) -> str:
    try:
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)
        text = ""

        # Iterate through each page in the PDF
        for page_num in range(len(pdf_document)):
            # Load the page
            page = pdf_document.load_page(page_num)
            # Extract text from the page
            text += page.get_text()

        return text
    except Exception as e:
        # Print an error message if text extraction fails
        print(f"Failed to extract text from {pdf_path}: {e}")
        return ""