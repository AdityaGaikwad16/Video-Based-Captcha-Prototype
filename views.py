from django.shortcuts import render
# Create your views here
from django.http import HttpResponse

#we will now take a list of  dictionaries for our for loop
profiles = [
    {
        "id": "1",
        "name": "Cody Seibert",
        "description": "I'm a full stack web developer who probably spends too much time coding. A core contribute to the Mumble project and online instructor."
    },
    {
        "id": "2",
        "name": "Dennis Ivy",
        "description": "I build new projects just to tickle my brain and love teaching others how they're made. While I keep busy teaching courses, I still take interviews in search of a great team & projects that interest me."
    },
    {
        "id": "3",
        "name": "Mehdi",
        "description": " I am a Full-Stack Developer.  I am Currently learning, working my skills in web development. Open source enthusiast"
    },
    {
        "id": "4",
        "name": "Cody Seibert",
        "description": "I'm a full stack web developer who probably spends too much time coding. A core contribute to the Mumble project and online instructor."
    },
    {
        "id": "5",
        "name": "Mohammad Khaled",
        "description": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia"
    },
    {
        "id": "6",
        "name": "Praveen",
        "description": " I’m currently working on - Python, Django, Vue, Nuxt. I’m currently learning - Nodejs.  I’m looking to collaborate with - Any Business or Open Source Idea. Ask me about - Freelancing , Python , Django, Vuejs."
    },

]
def projects(request):
    number=7
    context={'page':page,'number':number,'profiles':profiles}
    return render(request, 'projects/projects.html',context)
def project(request, pk):
    return render(request, 'projects/single-project.html')
def login(request):
    return render(request, 'projects/login.html')
def register(request):
    page ='register'
    form=registrationForm()
    if request.method == 'POST':
        # Retrieve form data using request.POST dictionary
        form=registrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
    context={'page':page, 'form':form}        
    return render(request, 'projects/register.html',context)    
def captcha(request):
    return render(request, 'projects/captcha.html')

#Now instead of ping we request a html file to be rendered or shown for the path

#Now in line 8 as the template folder now is not present in our root folder we need to change our path. 

#We want to add data and variables thus here we have dictionary where message is the key accesing variable msg 

