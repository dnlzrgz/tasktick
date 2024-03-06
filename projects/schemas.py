from typing import Optional
from ninja import Schema


class ProjectIn(Schema):
    name: str
    description: Optional[str] = None
    color: Optional[str] = None


class ProjectUpdate(Schema):
    name: Optional[str] = None
    description: Optional[str] = None
    color: Optional[str] = None


class ProjectOut(Schema):
    id: int
    name: str
    description: Optional[str] = None
    color: Optional[str] = None
