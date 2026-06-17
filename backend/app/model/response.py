from pydantic import BaseModel

class Response(BaseModel):
    value: any
    explanation: str