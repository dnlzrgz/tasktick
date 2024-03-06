from typing import Optional
from datetime import datetime
from ninja import Schema


class ActivityIn(Schema):
    name: str
    description: Optional[str] = None
    start_date: datetime
    end_date: Optional[datetime] = None


class ActivityUpdate(Schema):
    name: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None


class ActivityOut(Schema):
    id: int
    name: str
    description: Optional[str] = None
    start_date: datetime
    end_date: Optional[datetime] = None
