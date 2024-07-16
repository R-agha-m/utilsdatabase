from typing import Type

from beanie import Document

cache_by_pid: dict[
    int,
    Type[Document],
] = dict()

cache_by_filter: dict[
    str,
    dict | Type[Document] | list[Type[Document]]
] = dict()
