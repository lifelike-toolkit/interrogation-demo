"""
This file will demonstrate how the sequence tree for the game is built.
In this game, each sequence event will demonstrate the suspect's reaction to a topic being asked/talked about.
"""
from langchain.chains import RetrievalQA
from langchain.llms import LlamaCpp
from langchain.embeddings import LlamaCppEmbeddings

from lifelike.StateManager.knowledge_tree import KnowledgeTree

llm = LlamaCpp(model_path='setup/ggml-alpaca-7b-q4.bin')
llm_embedding = LlamaCppEmbeddings(model_path='setup/ggml-alpaca-7b-q4.bin')

tree = KnowledgeTree.from_texts(
    "dinnercase", 
    ["Emily William was poisoned to death", "Jason William poisoned Emily William", "Jason William is Emily William's older brother"], 
    llm_embedding, 
)

retriever = tree.get_retriever()

retrievalQA = RetrievalQA.from_llm(llm=llm, retriever=retriever)
