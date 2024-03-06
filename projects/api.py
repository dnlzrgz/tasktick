from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.errors import HttpError
from projects.models import Project
from projects.schemas import ProjectIn, ProjectUpdate, ProjectOut

router = Router()


@router.post("/", response=ProjectOut)
def create_project(request, payload: ProjectIn):
    activity = Project.objects.create(
        user=request.user,
        **payload.dict(),
    )
    return activity


@router.get("/", response=List[ProjectOut])
def read_projects(request):
    projects = Project.objects.filter(user=request.user)
    return projects


@router.get("/{project_id}", response=ProjectOut)
def read_project(request, project_id: int):
    project = get_object_or_404(Project, id=project_id)
    if project.user != request.user:
        raise HttpError(404, "Not Found: No Project matches the given query.")

    return project


@router.put("/{project_id}", response=ProjectOut)
def update_project(request, project_id: int, payload: ProjectUpdate):
    project = get_object_or_404(Project, id=project_id)
    if project.user != request.user:
        raise HttpError(404, "Not Found: No Project matches the given query.")

    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(project, attr, value)

    project.save()
    return project


@router.delete("/{project_id}", response=ProjectIn)
def delete_project(request, project_id: int):
    project = get_object_or_404(Project, id=project_id)
    if project.user != request.user:
        raise HttpError(404, "Not Found: No Project matches the given query.")

    project.delete()
    return project
