from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Board
from .models import food
from .form import FoodForm
from django.http import HttpResponse
# Create your views here.


def main(request):
    return render(request, 'main.html')

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],password=request.POST["password1"])
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'registration/signup.html')
    else:
        return render(request, 'registration/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'registration/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'registration/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('login')
    return render(request,'registration/login.html')


def community(request):
    boards = Board.objects.order_by('-id')
    context = {'boards': boards}
    return render(request, 'community.html', context)


def purchase(request):
    return render(request, 'purchase.html')

def foodreg (request):
    if request.method == "POST":
        # SAVE DATA
        form = FoodForm(request.POST)
        if form.is_valid():  # 정상적인 데이터인지를 검증
            foods = form.save(commit=False)  # form에서 가져오고 db에 저장안함
            foods.generate()  # db에 저장
            return redirect('main')
    else:
        form = FoodForm()
        return render(request, 'foodform.html', {"form": form})

def submit_food(request):
    user = User.objects.get(username=request.user.get_username())
    if request.method == "POST":
        fd=food.objects.create(
            name=request.POST["title"], username=user.username, body=request.POST["content"])
        return redirect('main')
    else:
        return redirect('foodreg')

def foodlist(request):
    foodlist = food.objects.order_by('-date')
    context = {'foodlist': foodlist}
    return render(request, 'foodlist.html', context)

def view_post(request, board_id):
    board = Board.objects.get(pk=board_id)
    board.view += 1
    board.save()
    context = {'board': board}
    return render(request, "read_post.html", context)

def write_post(request):
    return render(request, "write_post.html")

def submit_post(request):
    if request.method == "POST":
        board=Board.objects.create(
            subject=request.POST["title"], name=request.POST["name"], content=request.POST["content"])
        return redirect('community')
    else:
        return render(request, 'write_post.html')






