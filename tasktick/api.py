from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/")
def home(request):
    return "hello, world"
