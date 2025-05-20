from langchain_openai import ChatOpenAI
from langchain_code.promts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv