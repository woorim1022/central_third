from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):   #디테일 함수가 실행되기 위해선 몇번 객체를 다룰 것인지에 대한 정보 추가로 필
    blog_detail = get_object_or_404(Blog, pk = blog_id)                  #두번쨰 인자를 넘겨주는 대상은 url(이용자와 직접 상호작용하는 메시지 역할)
    return render(request, 'detail.html', {'blog':blog_detail})