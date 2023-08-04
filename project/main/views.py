from django.shortcuts import render


# Create your views here.
def index(request):
    data= {
        'title': 'Main Page',
        'values': ['service1', 'service2', 'service3', 'service4', 'service5'],
        'obj': {
            'master1': 'Kisha',
            'age': 30,
            'style': 'Dot work',
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, "main/about.html")


def contact(request):
    return render(request, "main/contact.html")
