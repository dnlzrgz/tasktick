from typing import Optional
from datetime import datetime
from ninja import Schema
from projects.schemas import ProjectOut


class ActivityIn(Schema):
    name: str
    description: Optional[str] = None
    start_date: datetime
    end_date: Optional[datetime] = None
    project_name: Optional[str] = None


class ActivityUpdate(Schema):
    name: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    project_name: Optional[str] = None


class ActivityOut(Schema):
    id: int
    name: str
    description: Optional[str] = None
    start_date: datetime
    end_date: Optional[datetime] = None
    project: Optional[ProjectOut] = None
