from dotenv import load_dotenv
import os
from langchain_community.llms.ollama import Ollama
from langchain_openai import OpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage

from openaikey import get_openai_key

key = get_openai_key()

llms = [OpenAI(model="gpt-3.5-turbo-instruct", api_key=key), 
        Ollama(model="llama2")]

model_names = ["gpt-3.5-turbo-0125", "llama3"]

# First prompt
prompt = """
    I want you to tell me if the following game review is positive or negative.

    Review: It’s a great thing that Open Roads is an incredibly short experience, because when it comes to actually playing it, there just isn’t much there. Thankfully, its story and characters do more than enough to make experiencing Open Roads worthwhile, at least once.
    """
# Final prompt
prompt = """
    I want you to tell me if the following game review is positive or negative.

    Review: It’s a great thing that Open Roads is an incredibly short experience, because when it comes to actually playing it, there just isn’t much there. Thankfully, its story and characters do more than enough to make experiencing Open Roads worthwhile, at least once.

    The final response should be in the following format:
    prompt: restate the prompt with context
    sentiment: "positive" or "negative"
    reasoning: reason for giving the sentiment
"""

for i, llm in enumerate(llms):
    chain = llm | StrOutputParser()
    response = chain.invoke(prompt)
    result = f"{model_names[i].upper()}\n{response}\n_________________________\n"
    print(result)