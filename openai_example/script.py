from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("What's the key takeaways abut the world energy market? Please explain where you get the info from, referring to the 'data' folder")
print(response)
