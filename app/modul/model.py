from pydantic import BaseModel
from typing import List

class Request(BaseModel):
    review_text: List[str]