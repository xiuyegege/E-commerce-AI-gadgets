from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

class QandAText(BaseModel):
    customer_questions: List[str] = Field(description="模拟用户提出的10个问题",min_items=1, max_items=350)
    customer_answer: List[str] = Field(description="模拟老客户对10个问题给出的10个回答",min_items=1, max_items=2600)
