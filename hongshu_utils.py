from hongshu_system_template_text import system_template_text, user_template_text
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from xiaohongshu_model import Xiaohongshu

# import os


def generate_xiaohongshu(theme,manner_speaking,Reference_Topic,Reference_Text, openai_api_key,creativity):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text)
    ])
    model = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key,temperature=creativity)
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    chain = prompt | model | output_parser
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme,
        "manner_speaking": manner_speaking,
        "Reference_Topic": Reference_Topic,
        "Reference_Text": Reference_Text
    })
    return result