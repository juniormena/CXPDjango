from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

#Login page
def signIn(request):
    template = './Login/login.html'
    if(request.method == 'GET'):
        return render(request, template)
    elif (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, template, {"error":"Usuario o contraseña incorrectos"})

#Logout
def signOut(request):
    logout(request)
    return redirect('/login/')