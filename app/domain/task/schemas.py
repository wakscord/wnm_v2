from dataclasses import dataclass

from fastapi import status
from pydantic import BaseModel, validator

from app.common.exceptions import APIException


@dataclass(frozen=True)
class Task(BaseModel):
    node_id: str
    subscribers: list[str]
    message: dict


class TaskAddRequest(BaseModel):
    subscribers: list[str]
    message: dict

    @validator("subscribers")
    def check_subscribers(values) -> list[str]:
        if not values:
            raise APIException(code=status.HTTP_400_BAD_REQUEST, message="올바르지 않은 요청입니다. (subscribers)")
        return values