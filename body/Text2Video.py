from pydantic import BaseModel

class Text2Video(BaseModel):
    text: str
    uuid: str
