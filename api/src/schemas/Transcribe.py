import uuid

from pydantic import BaseModel


class TranscribeModel(BaseModel):
    id: uuid.UUID
    user_id: str
    file_path: str
    task_status: str
    result: str

class TranscribeCreateModel(BaseModel):
    file_path: str


