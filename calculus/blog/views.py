from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author' : 'minousa',
        'title' : 'post one',
        'content':'this is the first dummy post',
        'date_posted': 'june 13 2020'
    },

      {
        'author' : 'minous',
        'title' : 'post two',
        'content':'this is the second dummy post',
        'date_posted': 'june 14 2020'
    }
]

def home(request):

    context= {

        'posts': posts
    }

    
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'django dummy'})

#def contact(request):
   # return HttpResponse('<h1> hello visitor here is how to contact us </h1>')
    