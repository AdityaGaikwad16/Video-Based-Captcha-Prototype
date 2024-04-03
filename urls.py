from django.urls import path
from . import views 

urlpatterns = [
path('',views.login,name="login"), #path is needed to call function along with the name given
path('register/',views.register,name="register"),
path('captcha/',views.captcha,name="captcha"),
]

'''Here we are generating a ping that is we are creating a function which will return a statement or something when a
   user puts up a request to our app or anything.'''
    
'''Now we want to show a page as our root page at the time we run into server
   Thus we are going to set the path as empty string before views.projects'''