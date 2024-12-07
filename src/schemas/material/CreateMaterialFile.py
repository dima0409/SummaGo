from fastapi import UploadFile
from pydantic import BaseModel


class CreateMaterialFileDto(BaseModel):
    file: UploadFile
    workbook_id: int
    theme_id: int