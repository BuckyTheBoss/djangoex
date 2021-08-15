from django.shortcuts import render

# Create your views here.

def homepage(request):
    user = {
        'first_name' : "Bobby",
        'last_name' : "McFarrin"
    } 
    subjects = [
        {
            'title' : "How to setup Django",
            'author': "Maria"
        },
        {
            'title' : "How to cake an amazing pie",
            'author' : "Chef Mark"
        }
    ]
    context = {
        'u' : user,
        'subs': subjects
    }
    return render(request, 'main/index.html', context)

def about(request, name):
    if len(name) > 10:
        text = 'damn thats a long name'
    else:
        text = 'you chill'
    return render(request, 'main/about.html', {'name': name, 'message': text})

def calc(request, num=100):

    context = {
        'div': num / 10,
        'mult': num * 10,
        'add': num + 10,
        'sub': num - 10
    }
    return render(request, 'main/calc.html', context)