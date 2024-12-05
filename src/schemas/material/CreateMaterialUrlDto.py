from pydantic import BaseModel


class CreateMaterialUrlDto(BaseModel):
    download_url: str
    workbook_id: int
    theme_id: int