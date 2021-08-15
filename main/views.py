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
        'user' : user,
        'subjects': subjects
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')