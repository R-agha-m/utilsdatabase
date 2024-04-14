from typing import Type, Optional

from beanie import Document
from fastapi import status
from pydantic import BaseModel

HTTP_404_NOT_FOUND = status.HTTP_404_NOT_FOUND


async def check_item_existence():
        document: Type[Document],
        filter_: dict,
        fetch_links: bool = False,
        projection_model: Type[BaseModel] = None,
        raise_on_absence: bool = False,
        raise_on_existence: bool = False,
        sort: Optional[dict] = None,
        error_text: Optional[str | dict] = None,
        error_code: Optional[int] = None,
        error_message: Optional[str] = None,
) -> Document | None | BaseModel | Type[BaseModel]:

    obj = await document.find_one(
        filter_,
        fetch_links=fetch_links,
        projection_model=projection_model,
        sort=sort,
    )

    if obj:
        if raise_on_existence:
            if error_text is None:
                error_text = get_message(
                    message_name="duplicate_item",
                    message_kwargs={"item": document.Settings.name},
                    language="farsi",  # Hardcode
                )
            raise ProjectBaseException(
                code=error_code or HTTP_404_NOT_FOUND,
                success=False,
                data=None,
                error=error_text,
                message=error_message or error_text,
            )

    else:
        if raise_on_absence:
            if error_text is None:
                error_text = get_message(
                    message_name="item_not_found",
                    message_kwargs={"item": document.Settings.name},
                    language="farsi",  # Hardcode
                )
            raise ProjectBaseException(
                code=error_code or HTTP_404_NOT_FOUND,
                success=False,
                data=None,
                error=error_text,
                message=error_message or error_text,
            )

    return obj
