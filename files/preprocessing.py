from pdfminer.high_level import extract_text

class ReadingDocument:
    def pdf_reader(path):
        text = extract_text(path)
        return text