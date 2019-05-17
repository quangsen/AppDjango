from django.shortcuts import render

def foodball_index(request):
    context = {
        'session': 'Sao toi khong dieu gi say ra'
    }
    return render(request, 'foodball_index.html', context)
