from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo.models import Todo 
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

def home(request):
	all_items = Todo.objects.all()
	return render(request,"home.html", {"all_items":all_items})

def mark_todo_done(request, todo_id):
	todo = Todo.objects.get(pk=todo_id)
	todo.is_completed = True
	todo.save()

	return redirect('/home/')

def signup(request):
	if request.method=="POST":
		username = request.POST["username"]
		password = request.POST["password"]
		email = request.POST["email"]
		User.objects.create_user(email=email,password=password,username=username)

		
		return redirect('/home/')
		
	return render(request,'signup.html')

def signin(request):
	if request.method== "POST":
		username= request.POST["username"]
		password= request.POST["password"]

		user= authenticate(request, username=username,
		 password= password)
		if user != None:
			login(request, user)
			return redirect('/home/')

	return render(request,"signin.html")

def signout(request):
	
	logout(request)
	
	return redirect("/signin/")

def addtask(request):
    if request.method == "POST":
        print(request.POST)
        title = request.POST["title"]
        description = request.POST["description"]


        new_task = Todo.objects.create(title=title, description=description)

        return redirect("/addtask/")
    return render(request, "addtask.html")

def delete(request, todo_id):
	todo = Todo.objects.get(pk=todo_id)
	todo.delete()
	return redirect("/home/")



	
