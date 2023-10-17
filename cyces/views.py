from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from cyces.models import Blog


def home(request):
    return render(request, 'index.html')
    # html_tags = '''
    #     <h1>This is the Home Page</h1>
    #     <h3>Thanks for visiting us</h3>
    #     <p>MVT means:</p>
    #     <ul>
    #       <li>Model</li>
    #       <li>View</li>
    #       <li>Template</li>
    #     </ul>
    # '''
    # return HttpResponse(html_tags)


def blogs(request):
    # blogs_data = [
    #     {"title": "Blogs 1", "description": "This is blog 1 description."},
    #     {"title": "Blogs 2", "description": "This is blog 2 description."},
    #     {"title": "Blogs 2", "description": "This is blog 2 description."},
    # ]
    blogs_data = Blog.objects.all()
    context = {"blogs_data": blogs_data}
    return render(request, 'blogs.html', context=context)
