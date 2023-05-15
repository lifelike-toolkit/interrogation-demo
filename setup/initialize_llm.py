from langchain.llms import LlamaCpp
from langchain.embeddings import LlamaCppEmbeddings

llm = LlamaCpp(model_path='setup/ggml-model-q4_0.bin')
llm_embedding = LlamaCppEmbeddings(model_path='setup/ggml-model-q4_0.bin')