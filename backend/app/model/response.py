from pydantic import BaseModel
from typing import TypeVar, Generic

DataT = TypeVar('DataT')

class Response(BaseModel, Generic[DataT]):
    value: DataT
    explanation: str