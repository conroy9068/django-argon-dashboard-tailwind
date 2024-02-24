from django.shortcuts import render


def index(request):
    return render(request, 'assessments/index.html')


# Add this new view function
def new(request):
    # Your logic for handling the creation of a new assessment
    return render(request, 'assessments/new.html')
