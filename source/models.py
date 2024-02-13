from config.db import Base
from source.schemas import FileSchema
from sqlalchemy.orm import Mapped, mapped_column

__all__ = ("Files",)


class Files(Base):
    __tablename__ = "files"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    file: Mapped[bytes]
    content_type: Mapped[str]
    path: Mapped[str]
    size: Mapped[int]

    def to_json(self) -> FileSchema:
        return FileSchema(
            id=self.id, name=self.name, file=self.file, content_type=self.content_type, path=self.path, size=self.size
        )
