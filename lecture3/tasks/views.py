from django.shortcuts import render

# Create your views here.
tasks = ["foo", "bar","ahsdisdh"]
def index(request):
    return render(request, "tasks/index.html", {
        'tasks': tasks
    }
    )