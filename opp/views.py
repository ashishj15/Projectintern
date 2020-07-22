
from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings

import random

from django.core.validators import validate_email
from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .models import UserProfile, Opportunites,Vote as Preference
from . import views
from friendship.models import Friend, Follow, Block


class Login(APIView):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)

            try:
                users = UserProfile.objects.get(user=user)

                if users.is_Organisation:
                  data = Opportunites.objects.all()
                  info = {'data': data}
                  return render(request,'orgindex.html',info)
                else:
                  alldata = Opportunites.objects.all()
                  cont = {'alldata': alldata}
                  return render(request,'userindex.html',cont)

            except:
                return render(request, 'login.html')


class SignUp(APIView):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        if request.POST['password'] == request.POST['cnfpassword']:

            try:
                validate_email(request.POST['email'])
            except:
                return render(request, 'signup.html', {"error": "Valid email Id please"})
            try:
                email = UserProfile.objects.get(request.POST['email'])
                return render(request, 'signup.html', {"error": "Account already exists"})
            except:
                pass
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username already exists'})
            except:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                userprofile = UserProfile(user=user, email=request.POST['email'], name=request.POST['name'],
                                          is_Organisation=False)
                user.email = request.POST['email']
                user.save()
                userprofile.save()
                return redirect('login')


class OrganisationSignUp(APIView):
    def get(self, request):
        return render(request, 'orgsignup.html')

    def post(self, request):
        if request.POST['password'] == request.POST['cnfpassword']:

            try:
                validate_email(request.POST['email'])
            except:
                return render(request, 'orgsignup.html', {"error": "Valid email Id please"})
            try:
                email = UserProfile.objects.get(request.POST['email'])
                return render(request, 'orgsignup.html', {"error": "Account already exists"})
            except:
                pass
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'orgsignup.html', {'error': 'Username already exists'})
            except:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                userprofile = UserProfile(user=user, email=request.POST['email'], name=request.POST['name'],
                                          is_Organisation=True)
                user.email = request.POST['email']
                user.save()
                userprofile.save()
                return redirect('login')

def index(request):
    alldata = Opportunites.objects.all()
    context = {'alldata': alldata}
    return render(request,"index.html",context)


def userindex(request):
    alldata = Opportunites.objects.all()
    cont = {'alldata': alldata}
    return render(request, 'userindex.html',cont)

class logout(APIView):
    def get(self, request):
        auth.logout(request)
        return redirect('index')

def orgindex(request):
     data = Opportunites.objects.all()
     info = {'data': data}
     return render(request, 'orgindex.html',info)
    
class addOpportunity(APIView):
    def get(self, request):
        opps = [
            "Workshops",
            "Applied Projects",
            "Research",
            "Internships",
            "STEM",
            "Sports",
            "Arts",
            "Politics,Speech and Social Studies","Music","Visual Arts"
        ]
        return render(request, 'addOpportunity.html', {"opportunities": opps,"error": "Please enter all the fields"})

    def post(self, request):
        if request.POST['name'] and request.POST['oppurl'] and request.POST['description'] and request.POST['date'] and request.POST['category']:
            opp = Opportunites(name=request.POST['name'], url=request.POST['oppurl'],
                               description=request.POST['description'], date=request.POST['date'], category=request.POST['category'])
            opp.save()
            return redirect('orgindex')
        else:
            return redirect('addopportunity')


@login_required(login_url='/login')
def postpreference(request, postid, userpreference):
        
        if request.method == "POST":
                eachpost= get_object_or_404(Opportunites, id=postid)
                obj=''
                valueobj=''

                try:
                        obj= Preference.objects.get(user= request.user, post= eachpost)
                        valueobj= obj.value #value of userpreference
                        valueobj= int(valueobj)
                        userpreference= int(userpreference)
                
                        if valueobj != userpreference:
                                obj.delete()


                                upref= Preference()
                                upref.user= request.user

                                upref.post= eachpost

                                upref.value= userpreference


                                if userpreference == 1 and valueobj != 1:
                                        eachpost.likes = eachpost.likes + 1
                                        eachpost.dislikes=eachpost.dislikes -1
                                elif userpreference == 2 and valueobj != 2:
                                        eachpost.dislikes += 1
                                        eachpost.likes -= 1
                                

                                upref.save()

                                eachpost.save()
                                alldata = Opportunites.objects.all()
                                cont = {'alldata': alldata}

                                return render (request, 'userindex.html', cont)

                        elif valueobj == userpreference:
                                obj.delete()
                        
                                if userpreference == 1:
                                        eachpost.likes -= 1
                                elif userpreference == 2:
                                        eachpost.dislikes -= 1

                                eachpost.save()

                                alldata = Opportunites.objects.all()
                                cont = {'alldata': alldata}

                                return render (request, 'userindex.html', cont)
                                
                        
        
                
                except Preference.DoesNotExist:
                        upref= Preference()

                        upref.user= request.user

                        upref.post= eachpost

                        upref.value= userpreference

                        userpreference= int(userpreference)

                        if userpreference == 1:
                                eachpost.likes += 1
                        elif userpreference == 2:
                                eachpost.dislikes +=1

                        upref.save()

                        eachpost.save()                            


                        alldata = Opportunites.objects.all()
                        cont = {'alldata': alldata}

                        return render (request, 'userindex.html', cont)


        else:
                eachpost= get_object_or_404(Post, id=postid)
                alldata = Opportunites.objects.all()
                cont = {'alldata': alldata}

                return render (request, 'userindex.html', cont)


def FollowUser(request, uname):
    current_user = request.user
    to_user = User.objects.get(username=uname)
    print(to_user)
    
    try:
        Follow.objects.add_follower(request.user, to_user) 
        friends = Follow.objects.following(request.user)
        context = {
            'friends': friends
        }
        return redirect('yourfriends')
    except:
        users = UserProfile.objects.exclude(user=request.user)
        profile = UserProfile.objects.get(user=request.user)
        friends = Follow.objects.following(request.user)
        print(friends)
        context = {
            'users': users,
            'profile': profile,
            'friends': friends,
            'error': 'You Already Follow this User'
        }
        return render(request, 'friends.html', context)

def unFollowUser(request, uname):
    current_user = request.user
    to_user = User.objects.get(username=uname)
    Follow.objects.remove_follower(request.user, to_user)
    friends = Follow.objects.following(request.user)
    context = {
        'friends': friends
    }
    return redirect('yourfriends')

def yourFriends(request):
    friends = Follow.objects.following(request.user)
    context = {
        'friends': friends
    }
    return render(request, 'following_list.html', context)
    
@login_required()
def allUsers(request):
    users = UserProfile.objects.exclude(user=request.user)
    profile = UserProfile.objects.get(user=request.user)
    friends = Follow.objects.following(request.user)
    print(friends)
    context = {
        'users': users,
        'profile': profile,
        'friends': friends,
    }

    return render(request, 'friends.html', context)




