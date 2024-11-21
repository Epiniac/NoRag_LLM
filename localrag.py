from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
import chainlit as cl
import tiktoken
import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

#Load the uploaded Document from S3
load = TextLoader("./text.txt")
document = load.load()
print(type(document))
encoding = tiktoken.encoding_for_model("text-embedding-ada-002")

#Embeddings and vector 
embeddings = OpenAIEmbeddings(api_key = openai.api_key)
vector_store = FAISS.from_documents(document, embeddings)
retriever = vector_store.as_retriever()

#Initialize the project
llm = Ollama(model="llama3.2")

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Bonjour utilisateur, comment puis-je vous aider?").send()

