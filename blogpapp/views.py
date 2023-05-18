from django.shortcuts import render
from .models import *
from django.shortcuts import render,redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from taggit.managers import TaggableManager, TaggedItem
from taggit.models import Tag
from django.contrib.sitemaps import Sitemap
# Create your views here.
def home(request):
    home = Home.objects.all()
    posts = Post.objects.select_related('category_id').select_related('author').all().order_by('-created_on')
    # postss = list(posts)
    # for x in postss:
    #     print(x.category_id.category_slug)
    category = Category.objects.all().order_by('id')[:8]
    # print(type(home))
    popularpost = Post.objects.all().order_by('-read_count')
    print(popularpost.query)
    context = {'home':home,'category':category,'posts':posts,'popularpost':popularpost}
    return render(request,'frontend/home.html',context)

def single(request, slug):
    home = Home.objects.all()
    singlepost = Post.objects.select_related('category_id').select_related('author').filter(slug = slug)
    # relatedpost = Post.objects.tag.similar_objects()[:3]
    # print(relatedpost)
    for x in singlepost:
      x.read_count = x.read_count + 1
      x.save()
  
    category = Category.objects.all().order_by('id')[:8]
    context = {'home':home,'singlepost':singlepost,'category':category}
    return render(request,'frontend/single.html',context)

def category(request, slug):
    home = Home.objects.all()
    category = Category.objects.all().order_by('id')[:8]
    categorydata = Category.objects.filter(category_slug = slug)
    for x in categorydata:
     id = x.id
     allcpost = Post.objects.select_related('category_id').select_related('author').filter(category_id = id)
     print(allcpost.query)
    context = {'home':home,'category':category,'allcpost':allcpost}
    return render(request,'frontend/category.html',context)    

def tagbyposts(request, slug):
    home = Home.objects.all()
    category = Category.objects.all().order_by('id')[:8]
    tags = Tag.objects.filter(slug=slug).values_list('name', flat=True)
    tagbypost = Post.objects.select_related('category_id').select_related('author').filter(tag__name__in=tags)
    print(tagbypost.query)
    context = {'home':home,'category':category,'allcpost':tagbypost}
    return render(request,'frontend/category.html',context)   


def contact(request):
    home = Home.objects.all()
    # print(type(home))
    context = {'home':home,'category':category}
        
    if request.method == "POST":
            name = request.POST['name']
            email  = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            print(name)
            if len(name) > 4:
                contact = Contact(name=name,email=email,subject=subject,message=message)
                contact.save()
                messages.success(request,'Successfully Form Submit')
                return redirect('/contact')
            else:
                messages.error(request,'First Name Should Be more then 4 chars')
                return redirect('/contact')    
    return render(request,'frontend/contact.html',context)        




