import os
from typing import Annotated

from fastapi import File
from source.repositories import AbstractRepository

__all__ = ("FilesService",)


def prepare_data(file: Annotated[bytes, File()]) -> dict:
    """Prepares data for saving in the database."""
    _file_name = file.title().decode("utf-8")
    return {
        "name": _file_name,
        "file": file,
        "content_type": "bytes",
        "path": os.path.join(os.getcwd(), "files/") + _file_name,
        "size": file.__sizeof__(),
    }


class FilesService:
    """Represents interaction with file service and provides 'add()' and 'get()' methods."""

    __slots__ = ("files_repository",)

    def __init__(self, files_repository: AbstractRepository) -> None:
        self.files_repository: AbstractRepository = files_repository

    def add(self, file: Annotated[bytes, File()]) -> int:
        """Saves the file and its characteristics to the database."""
        prepared_data: dict = prepare_data(file=file)
        return self.files_repository.add(data=prepared_data)

    def retrieve(self, pk: int):
        """Just retrieves the file from the database by ID."""
        return self.files_repository.find(pk=pk)
