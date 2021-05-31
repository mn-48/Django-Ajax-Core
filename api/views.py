from django.shortcuts import render


# Create your views here.

def  HomeView(request):
    # sss = request.GET.get['buyer_id']
    if request.method=="POST":
        subject = request.POST['buyer_id']
        print(subject)
    return render(request, 'home.html', context={})