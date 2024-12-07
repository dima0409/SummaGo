from pydantic import BaseModel


class MaterialDto(BaseModel):

    url: str
    name: str
    status: str
    result: str
    workbook_id: int
