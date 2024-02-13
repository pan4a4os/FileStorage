from source.repositories import FilesRepository
from source.services import FilesService

__all__ = ("files_service",)


def files_service() -> FilesService:
    return FilesService(FilesRepository())
