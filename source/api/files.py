import logging
from typing import Annotated

from fastapi import APIRouter, Depends, File, Response
from source.api.dependencies import files_service
from source.services import FilesService

logger: logging.Logger = logging.getLogger(name=__name__)  # TODO: configure logging

router = APIRouter(prefix="/api/v1/files", tags=["Files"])


@router.post(path="/")
def add_file(
    file: Annotated[bytes, File()],
    files_service_: Annotated[FilesService, Depends(files_service)],
):
    try:
        file_data = files_service_.add(file=file)
    except Exception as error:
        _error_message = f"An unexpected error occurred while saving the file to the database: `{error=}`"
        logger.exception(msg=_error_message)
        return Response(content=_error_message, status_code=400)

    return Response(content={"message": "File successfully saved", "data": file_data}, status_code=201)


@router.get(path="/{pk}")
def get_file(pk: int, files_service_: Annotated[FilesService, Depends(files_service)]):
    file_data = files_service_.retrieve(pk=pk)
    return Response(content={"file": file_data}, status_code=200)


@router.head(path="/{pk}")
def head_file(pk: int, files_service_: Annotated[FilesService, Depends(files_service)]):
    return Response(status_code=200 if files_service_.retrieve(pk=pk) else 400)
