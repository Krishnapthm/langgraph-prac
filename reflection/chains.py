from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import dotenv

dotenv.load_dotenv()


generation_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "you are a twitter techie influencer assitnt tasked with writing excellent twitter posts."
        "generate the best twitter post possible for the user's request."
        "if the user provides a cirtique, respont witht a revised version of your previous attmepts"
    ),
    MessagesPlaceholder(variable_name="messages"),
])

reflection_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "you are a twitter techie influencer grading a tweet. generate critique and recommnedations for the users tweet"
        "always provide detailed recomendations, including reuqests for length, virality, style etc"
    ),
    MessagesPlaceholder(variable_name="messages"),
])

llm=AzureChatOpenAI(model="gpt-4o-mini", api_version="2024-12-01-preview")

generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm