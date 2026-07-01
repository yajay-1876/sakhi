import pymupdf
from langchain_core.documents import Document

def load_pdf(file_bytes: bytes):
    pdf = pymupdf.open(stream=file_bytes, filetype="pdf")
    documents = []

    for page_no, page in enumerate(pdf):
        text= page.get_text()

        documents.append(Document(
            page_content=text,
            metadata={"page":page_no+1}
        ))
    pdf.close()
    return documents