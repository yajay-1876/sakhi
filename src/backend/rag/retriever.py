from src.backend.rag.pinecone_store import index


def retrieve_chunks(
        conv_id: str,
        query: str,
        top_k: int = 3
):
    response = index.search(
        namespace=conv_id,
        query={
            "inputs":{"text": query},
            "top_k": top_k
        }
    )
    answer_text=[]
    for hit in response['result']['hits']:
        if hit['_score']>0.30:
            answer_text.append(f"Filename: {hit['fields']['filename']}\n"
                               f"Page: {hit['fields']['page']}\n"
                               f"{hit['fields']['text']}\n")
    return "\n\n".join(answer_text)


# import pprint
# query="what is the first I asked you in this chat"
# print(f"query:{query}")
# response=retrieve_chunks("a06ed09e-f321-46bb-8c30-a4faa1eded0f",query)
# pprint.pp(response)