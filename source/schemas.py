from pydantic import BaseModel

__all__ = ("FileSchema",)


class FileSchema(BaseModel):
    id: int
    name: str
    file: bytes = b""
    content_type: str = ""
    path: str = ""
    size: int = 0

    class Config:
        from_attributes = True
