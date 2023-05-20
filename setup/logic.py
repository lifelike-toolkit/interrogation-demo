"""Defines character and story logic using Lifelike"""
from langchain.chains import RetrievalQA # Extra
from lifelike.StateManager.knowledge_tree import KnowledgeTree # Story logic
from lifelike import brain # Character Logic
from setup.story import *
from setup.llm import LLM, LLM_EMBEDDING

# Defines the game tree (story logic)
TREE = KnowledgeTree.from_texts(STORY_NAME, WORLD_KNOWLEDGE, LLM_EMBEDDING)
# Defines the retriever from tree
retriever = TREE.get_retriever(search_type='similarity', search_kwargs={'k': 4})
# Defines the QA chain
QA_CHAIN = RetrievalQA.from_llm(llm=LLM, retriever=retriever)
# Defines characters
characters = brain.Characters('characters.json')
characters.add(PLAYER_NAME, "")
characters.add(NPC_NAME, NPC_BACKGROUND)
# Initialize Conversation
conversations = brain.Conversations('conversations.json', characters, LLM)