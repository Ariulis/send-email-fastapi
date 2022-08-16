from typing import List

from fastapi import Form, UploadFile, File
from pydantic import BaseModel

from . import logger


class UserSchema(BaseModel):
    message: str
    template: bool
    # file: List[UploadFile]
    file: List[dict]

    @classmethod
    @logger.catch
    def as_form(
        cls,
        message: str = Form(''),
        template: bool = Form(False),
        # file: List[UploadFile] = File([])
        file: List[dict] = Form([]),
    ):
        return cls(
            message=message,
            template=template,
            file=file
        )
