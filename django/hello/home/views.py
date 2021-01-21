from django.shortcuts import render

# Index Page
def index(request):
    return render(request,'index.html')
# About Page
def about(request):
    return render(request,'about.html')
# Portfolio Page
def portfolio(request):
    return render(request,'portfolio.html')
# Blog Page
def blog(request):
    return render(request,'blog.html')
# Blog Post Page
def blogPost(request):
    return render(request,'blog-post.html')
# Contact Page
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
    return render(request,'contact.html')

