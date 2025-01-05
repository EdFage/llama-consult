from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext, load_index_from_storage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

documents = SimpleDirectoryReader("data").load_data()

# bge-base embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# ollama
Settings.llm = Ollama(model="llama3", request_timeout=360.0)

# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="data/indexed_data")

# load index
index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)