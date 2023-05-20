"""Set up LLM"""
import os
from dotenv import load_dotenv

from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings

# Set up llm
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLM = OpenAI(openai_api_key=OPENAI_API_KEY)
LLM_EMBEDDING = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)