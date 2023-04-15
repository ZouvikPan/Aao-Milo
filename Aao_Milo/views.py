from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    # return HttpResponse("This is Home Page")
    user = request.user
    hello = 'Hello World!'

    context = {
        'user': user,
        'hello': hello,
    }
    return render(request, 'main/home.html', context)
