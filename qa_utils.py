from QA.qa_sestem_template_text import system_template_text, user_template_text
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from QA.qa_text_model import QandAText

def generate_cunstomer_qa(product_features,user_QA,openai_api_key,creativity):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text)
    ])
    model = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key,
                       temperature=creativity)
    output_parser = PydanticOutputParser(pydantic_object=QandAText)
    chain = prompt | model | output_parser
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "product_features": product_features,
        "user_QA": user_QA
    })
    return result