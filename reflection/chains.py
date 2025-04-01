from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent, tool
from langchain_community.tools import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import datetime


generation_prompt = ChatPromptTemplate.from_messages([
    {
        "system",
        "you are a twitter techie influencer assitnt tasked with writing excellent twitter posts."
        "generate the best twitter post possible for the user's request."
        "if the user provides a cirtique, respont witht a revised version of your previous attmepts"
    },
    MessagesPlaceholder(variable_name="messages"),
])

reflection_prompt = ChatPromptTemplate.from_messages([
    {
        "system",
        "you are a twitter techie influencer grading a tweet. generate critique and recommnedations for the users tweet"
        "always provide detailed recomendations, including reuqests for length, virality, style etc"
    },
    MessagesPlaceholder(variable_name="messages"),
])

llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash")

generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm