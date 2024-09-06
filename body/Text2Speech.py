from pydantic import BaseModel

class Text2Speech(BaseModel):
    text: str
