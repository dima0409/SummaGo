import json
import uuid

from pydantic import BaseModel, model_validator


class CreateMaterialFileDto(BaseModel):
    workbook_id: int
    theme_id: uuid.UUID

    @model_validator(mode="before")
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value
