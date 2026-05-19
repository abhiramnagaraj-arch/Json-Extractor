from pydantic import BaseModel
from typing import List

class ExtractedDocument(BaseModel):
    section_id: str
    title: str
    category_tags: List[str]
    short_snippet: str
    description: str
    faqs: List[str]
