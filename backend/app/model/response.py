from pydantic import BaseModel

class Response(BaseModel):
    value: str
    explanation: str