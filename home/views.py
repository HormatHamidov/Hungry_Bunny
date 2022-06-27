from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from article.forms import ArticleForm
from article.models import Article,Like


def single_view(request):
    keyword = request.GET.get("keyword")    
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"single.html",{"articles":articles})
    articles = Article.objects.all()
    
    return render(request,"single.html",{"articles":articles})



def addarticle_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        return redirect('article:dashboard')
    
    return render (request,'addarticle.html',{'form':form})
  
def home_view(request):
    return render(request,'index.html',{})

def paypal_view(request):
    return render(request,'paypal.html',{})

def about_view(request):
    return render(request,'about.html',{})

def menu_view(request):
    return render(request,'menu.html',{})

def booking_view(request):
    return render(request,'booking.html',{})

def contact_view(request):
    return render(request,'contact.html',{})

def delete_view(request,id):
    article = get_object_or_404(Article,id=id)
    article.delete()   
    return redirect('article:dashboard')

def faq_view(request):
    return render(request,'FAQ.html',{})

def terms_view(request):
    return render(request,'terms.html',{})

def update_view(request,id):
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        return redirect("article:dashboard")
    return render(request,"update.html",{"form":form})

def dashboard_view(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        'articles':articles
    }
    return render (request,'dashboard.html',context)

def post_view(request):
    qs = Article.objects.all()
    user = request.user
    context = {
        'qs': qs,
        'user': user,
    }
    
    return render(request,'single.html',context)

def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Article.objects.get(id=post_id)
        
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
            
        like,created = Like.objects.get_or_create(user=user,post_id=post_id)
        
        if not created:
            if like.value == 'Like':
                like.value = 'UnLike' 
            else:
                like.value = 'Like'
        like.save()
    
    return redirect('article:single')





