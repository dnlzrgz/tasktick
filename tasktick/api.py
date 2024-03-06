from ninja import NinjaAPI
from ninja.security import django_auth

api = NinjaAPI(
    csrf=True,
    auth=django_auth,
)

api.add_router(
    "/activities/",
    "activities.api.router",
    tags=["activities"],
)
api.add_router(
    "/projects/",
    "projects.api.router",
    tags=["projects"],
)
