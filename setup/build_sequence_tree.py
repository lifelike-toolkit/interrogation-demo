"""
This file will demonstrate how the sequence tree for the game is built.
In this game, each sequence event will demonstrate the suspect's reaction to a topic being asked/talked about.
"""
import os
from dotenv import load_dotenv

from langchain.chains import RetrievalQA
from langchain.llms import LlamaCpp, OpenAI
from langchain.embeddings import LlamaCppEmbeddings, OpenAIEmbeddings

from lifelike.StateManager.knowledge_tree import KnowledgeTree

# Set up llm
load_dotenv()
# llm = LlamaCpp(model_path='setup/ggml-model-q4_0.bin')
# llm.client.verbose = False
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = OpenAI(openai_api_key=OPENAI_API_KEY)
llm_embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
llm_embedding.client.verbose = False

# Defines the game tree
# Focus on Ace Attorney style game.
# Every topic is 1 sentence. This contains Jason's version of the story. The metadata will describe what is happening in the story. Maybe the chief hands you new evidence if you talk about the right thing.
# The tree will also contains evidence topics. If a evidence that proves a contradiction in Jason's version is invoked during that topic, Jason will be fed with the new emotion prompt stored in the metadata.
# Certain topics have the strongest effects to weakening Jason, but the evidence to contradict those only come in late game.
tree = KnowledgeTree.from_texts(
    "dinnercase", 
    ["Jason William is being questioned about the death of Emily William",
    "Emily William, the victim in this case, is an 18 year-old female. She was poisoned to death at the dinner party, which was witnessed by only Peter and Jason. She died right before Peter William made an announcement. She is Jason William's sister, as well as Peter and Catherine's daughter.",
    "Peter William is Jason William and Emily William's father. He was present at the dinner party. He was the one who called the police after the murder. He witnessed Emily's murder. He kept the identity of the heir to his inheritance secret to everyone but Harvey Specter",
    "Jason William's family includes Peter William, Catherine William and Emily William, but Tina Bridges also lives with them and works as the family maid",
    "Harvey Specter is Peter William's lawyer. He is extrememly good at his job. He told Jason William that he was the heir to Peter William's inheritance a month ago",
    "Catherine William is Jason William and Emily William's mother, as well as Peter William's wife. She did not witness Emily's death as she was in a different room.",
    "The dinner party happened on Thursday. It was hosted the William family mansion by Peter William himself", 
    "The family maid is a woman named Tina Bridges. She was on vacation in a different city on Thursday",
    "Jason William is Emily William's brother. He is a 20-year old male who works as a software developer. He was present at the dinner party and witnessed Emily William's death. He is hiding a massive debt to the Yakuza."], 
    llm_embedding, 
)

# Defines the retriever from tree
retriever = tree.get_retriever(search_type='similarity', search_kwargs={'k': 4}) # hopefully will reduce the number of returned results

# Defines the QA chain
retrievalQA = RetrievalQA.from_llm(llm=llm, retriever=retriever)