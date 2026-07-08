from pydantic import BaseModel
from typing import TypeVar, Generic, Any

DataT = TypeVar('DataT')

class Response(BaseModel, Generic[DataT]):
    value: DataT
    explanation: Any ## Contains JSON or str