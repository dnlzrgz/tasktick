from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.errors import HttpError
from activities.models import Activity
from activities.schemas import ActivityIn, ActivityUpdate, ActivityOut

router = Router()


@router.post("/", response=ActivityOut)
def create_activity(request, payload: ActivityIn):
    activity = Activity.objects.create(
        user=request.user,
        **payload.dict(),
    )
    return activity


@router.get("/", response=List[ActivityOut])
def read_activities(request):
    activities = Activity.objects.filter(user=request.user)
    return activities


@router.get("/{activity_id}", response=ActivityOut)
def read_activity(request, activity_id: int):
    activity = get_object_or_404(Activity, id=activity_id)
    if activity.user != request.user:
        raise HttpError(404, "Not Found: No Activity matches the given query.")

    return activity


@router.put("/{activity_id}", response=ActivityOut)
def update_activity(request, activity_id: int, payload: ActivityUpdate):
    activity = get_object_or_404(Activity, id=activity_id)
    if activity.user != request.user:
        raise HttpError(404, "Not Found: No Activity matches the given query.")

    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(activity, attr, value)

    activity.save()
    return activity


@router.delete("/{activity_id}", response=ActivityIn)
def delete_activity(request, activity_id: int):
    activity = get_object_or_404(Activity, id=activity_id)
    if activity.user != request.user:
        raise HttpError(404, "Not Found: No Activity matches the given query.")

    activity.delete()
    return activity
