from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
import os
import getpass

os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key: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')

loader = DirectoryLoader(".\Kanoon", glob="**/*.pdf", show_progress=True, use_multithreading=True, silent_errors=True)
docs = loader.load()
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_overlap=100)

document_chunks = text_splitter.split_documents(docs)

import streamlit as st

