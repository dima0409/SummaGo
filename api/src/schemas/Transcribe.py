import uuid

from pydantic import BaseModel


class TranscribeModel(BaseModel):
    id: uuid.UUID
    user_id: str
    file_name: str
    task_status: str
    result: str

class TranscribeCreateModel(BaseModel):
    file_name: str


class TranscribeUpdateModel(BaseModel):
    id: uuid.UUID
    task_status: str
    result: str