from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Board, Comment, food, Recommend, Location, Notification
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from math import sqrt, sin, cos, atan2, radians
# Create your views here.

def main(request):
    user = User.objects.get(username=request.user.get_username())
    ranks = get_recommendations(user, similarity=sim_pearson)
    result = []
    for item in ranks:
        for object in food.objects.all().filter(name=item):
            result.append(object)
    result.reverse()
    return render(request, 'main.html', {'ranks': result, 'user': user})

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"])
            location = Location(user=user)
            location.save()
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
    page = request.GET.get('page', 1)
    paginator = Paginator(boards, 20)
    try:
        lines = paginator.page(page)
    except PageNotAnInteger:
        lines = paginator.page(1)
    except EmptyPage:
        lines = paginator.page(paginator.num_pages)
    context = {'boards': lines}
    return render(request, 'community.html', context)

def foodlist(request):
    user = User.objects.get(username=request.user.get_username())
    R = 6373.0
    foodlist = food.objects.order_by('-date')
    near_foodlist = []
    lat_from_purchaser = radians(float(user.location.lat))
    lng_from_purchaser = radians(float(user.location.lng))
    for object in foodlist:
        lat_from_seller = radians(float(object.lat))
        lng_from_seller = radians(float(object.lng))
        dlat = lat_from_purchaser - lat_from_seller
        dlng = lng_from_purchaser - lng_from_seller
        a = sin(dlat / 2) ** 2 + cos(lat_from_seller) * cos(lat_from_purchaser) * sin(dlng / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        if distance < 3: #거리변경가능
            near_foodlist.append(object)
    page = request.GET.get('page', 1)
    paginator = Paginator(near_foodlist, 8)
    try:
        lines = paginator.page(page)
    except PageNotAnInteger:
        lines = paginator.page(1)
    except EmptyPage:
        lines = paginator.page(paginator.num_pages)
    context = {'foodlist': lines}
    return render(request, 'foodlist.html', context)

def purchase(request):
    return render(request, 'foodlist.html')

def foodreg (request):
    return render(request, 'foodform.html')

def submit_food(request):
    user = User.objects.get(username=request.user.get_username())
    if request.method == "POST":
        if 'image' in request.FILES:
            photo = request.FILES["image"]
        else:
            photo = request.POST["image"]
        food.objects.create(
            name=request.POST["title"], seller=user, body=request.POST["content"],
            price=request.POST["price"], photo=photo, lat=user.location.lat, lng=user.location.lng)
        return redirect('main')
    else:
        return redirect('foodreg')

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
        if 'image' in request.FILES:
            photo = request.FILES["image"]
        else:
            photo = request.POST["image"]
        Board.objects.create(
            subject=request.POST["title"], name=request.POST["name"], content=request.POST["content"],
        photo=photo)
        return redirect('community')
    else:
        return render(request, 'write_post.html')

def view_food(request, food_id):
    fd = food.objects.get(pk=food_id)
    fd.view += 1
    fd.save()
    user = User.objects.get(username=request.user.get_username())
    it = Recommend.objects.filter(viewer=user, item=fd.name).exists()
    if it == False:
        Recommend.objects.create(viewer=user, item=fd.name, view=1)
    else:
        item = Recommend.objects.get(viewer=user, item=fd.name)
        item.view += 1
        item.save()
    context = {'food': fd}
    return render(request, 'read_food.html', context)

def view_food1(request, food_id):
    return redirect('food_view', food_id=food_id)

def comment_write(request, board_id):
    user = User.objects.get(username=request.user.get_username())
    if request.method == 'POST':
        post = Board.objects.get(pk=board_id)
        content = request.POST["content"]
        Comment.objects.create(post=post, comment_writer=user.username, comment_contents=content)
        return redirect('community_view', board_id=board_id)

def purchase(request, food_id):
    user = User.objects.get(username=request.user.get_username())
    if request.method == 'POST':
        fd = food.objects.get(pk=food_id)
        Notification.objects.create(seller=fd.seller, purchaser=user.username)
        return render(request, 'chatting.html', {'food': fd})

def search1(request):
    word = request.POST["word"]
    return redirect('search_food', word=word)

def search_food(request, word):
    all_food = food.objects.all()
    word = word
    result = []
    for object in all_food.filter(name__contains=word):
        result.append(object)
    for object in all_food.filter(body__contains=word):
        result.append(object)
    result = list(set(result))
    result.sort(key=lambda object : object.date)
    result.reverse()
    page = request.GET.get('page', 1)
    paginator = Paginator(result, 8)
    try:
        lines = paginator.page(page)
    except PageNotAnInteger:
        lines = paginator.page(1)
    except EmptyPage:
        lines = paginator.page(paginator.num_pages)
    return render(request, 'foodlist.html', {'foodlist': lines})

def search2(request):
    word = request.POST["word"]
    return redirect('search_post', word=word)

def search_post(request, word):
    all_post = Board.objects.all().order_by('-id')
    word = word
    result = []
    for object in all_post.filter(subject__contains=word):
        result.append(object)
    for object in all_post.filter(content__contains=word):
        result.append(object)
    result = list(set(result))
    result.sort(key=lambda object: object.id)
    result.reverse()
    page = request.GET.get('page', 1)
    paginator = Paginator(result, 20)
    try:
        lines = paginator.page(page)
    except PageNotAnInteger:
        lines = paginator.page(1)
    except EmptyPage:
        lines = paginator.page(paginator.num_pages)
    return render(request, 'community.html', {'boards': lines})

def get_latlng(request):
    user = User.objects.get(username=request.user.get_username())
    if request.method == 'GET':
        lat = request.GET.get('lat')
        lng = request.GET.get('lng')
        user.location.lat = lat
        user.location.lng = lng
        user.location.save()
    return redirect('main')

def sim_distance(person1, person2):
    # 공통 항목 추출
    si = dict()
    for item in person1.recommendation.item.all:
        if person2.recommendation.objects.filter(item=item.item).exists():
            si[item.item] = 1
    # 공통 평가 항목이 없는 경우 0 리턴
    if len(si) == 0: return 0
    # person1의 item이 person2에서도 존재한다면, person1과 person2의 item 평점 차이의 제곱한 값을 더한 후 제곱 근을 계산
    sum_of_squares = sum([(person1.recommendation.objects.get(item=item.item).view - person2.recommendation.objects.get(item=item.item).view)**2
                          for item in person1.recommendation.all if person2.recommendation.objects.filter(item=item.item).exists()])
    return 1/(1+sqrt(sum_of_squares))

def sim_pearson(p1, p2):
    # 같이 평가한 항목들의 목록을 구함
    si = dict()
    for item in Recommend.objects.filter(viewer=p1):
        if Recommend.objects.filter(item=item.item, viewer=p2).exists():
            si[item.item] = 1
    # 공통 항목 개수
    n = len(si)
    # 공통 항목이 없으면 0 리턴
    if n==0: return 0
    # 모든 선호도를 합산
    sum1 = sum([Recommend.objects.get(viewer=p1, item=it).view for it in si])
    sum2 = sum([Recommend.objects.get(viewer=p2, item=it).view for it in si])
    # 제곱의 합을 계산
    sum1Sq = sum([(Recommend.objects.get(viewer=p1, item=it).view)**2 for it in si])
    sum2Sq = sum([(Recommend.objects.get(viewer=p2, item=it).view)**2 for it in si])
    # 곱의 합을 계산
    pSum = sum([Recommend.objects.get(viewer=p1, item=it).view * Recommend.objects.get(viewer=p2, item=it).view for it in si])
    # 피어슨 점수 계산
    num = pSum - (sum1*sum2/n)
    den = sqrt((sum1Sq-pow(sum1,2)/n) * (sum2Sq-pow(sum2,2)/n))
    if den==0: return 0
    r = num/den
    return r

def top_matches(person, n, similarity=sim_pearson):
    scores = [(similarity(person, other), other)
              for other in User.objects.all() if other!=person]
    scores.sort()
    scores.reverse()
    return scores[:n]

def get_recommendations(person, similarity=sim_pearson):
    totals = dict()
    simSums = dict()
    for other in User.objects.all():
        # 나를 제외 하고
        if other == person: continue
        sim = similarity(person, other)  # person과 other 사이의 상관계수 점수를 구함
        # 0 이하 점수는 무시
        if sim<=0: continue
        for item in Recommend.objects.filter(viewer=other):   # ohter가 본 영화들의 list
            # 내가 보지 못한 영화만 대상
            if Recommend.objects.filter(viewer=person, item=item.item).exists()==False:
                # 유사도 * 점수
                totals.setdefault(item.item, 0)
                totals[item.item] += Recommend.objects.get(viewer=other, item=item.item).view*sim  # other가 평가한 영화의 점수 * person과 other의 상관계수
                # 유사도 합계
                simSums.setdefault(item.item, 0)
                simSums[item.item] += sim
    # 정규화된 목록 생성
    print(simSums)
    rankings = [ (total/simSums[item], item) for item, total in totals.items() ]
    rankings1 = [item for item, total in totals.items()]
    # 정렬된 목록 리턴
    rankings.sort()
    rankings1.sort()
    rankings.reverse()
    rankings1.reverse()
    return rankings1
