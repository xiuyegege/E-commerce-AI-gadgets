from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

class SellerText(BaseModel):
    seller_assess: List[str] = Field(description="用户的10条好评反馈",min_items=1, max_items=1500)