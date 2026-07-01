from src.backend.rag.documents import load_pdf
from src.backend.rag.chunker import create_chunks
from src.backend.rag.pinecone_store import index


def process_pdf(uploaded_file, document_id, conv_id, filename):
    try:
        documents = load_pdf(uploaded_file)
        chunks = create_chunks(documents)

        records = []
        for i,chunk in enumerate(chunks):
            record = {
                "_id"             : f"{document_id}_{i}",
                "text"            : chunk.page_content,
                "filename"        : filename,
                "page"            : chunk.metadata['page'],
                "document_id"     : document_id,
                "conversation_id" : conv_id
            }
            records.append(record)
        index.upsert_records(
            namespace = conv_id,
            records   = records
        )

        return {
            "success": True,
            "chunks_count": len(chunks)
        }
    except Exception as e:
        raise
