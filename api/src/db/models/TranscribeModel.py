import uuid


from sqlmodel import SQLModel, Field


class Transcribe(SQLModel, table=True):

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    user_id: str

    file_path: str

    task_status: str

    result: str

