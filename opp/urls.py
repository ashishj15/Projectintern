from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import url
from . import views
from django.urls import path,include

urlpatterns=[
    path("",views.index,name="index"),
    path('userindex/', views.userindex, name='userindex'),
    path('orgindex/', views.orgindex, name='orgindex'),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.SignUp.as_view(), name='signup'),
    path('orgsignup/', views.OrganisationSignUp.as_view(), name='orgsignup'),
    path('logout/', views.logout.as_view(), name='logout'),
    path('addopportunity/', views.addOpportunity.as_view(), name='addOpportunity'),
    path('friends/', views.allUsers, name='allusers'),
    path('follow/<str:uname>/', views.FollowUser, name='follow'),
    path('unfollow/<str:uname>/', views.unFollowUser, name='unfollow'),
    path('yourfriends/', views.yourFriends, name='yourfriends'),
    # path('posts/', include(posts.urls), name-'posts'),
    #path('vote/<int:pk>',views.VoteToggle.as_view() , name="upvote"),
    url(r'^posts/(?P<postid>\d+)/preference/(?P<userpreference>\d+)/$',views.postpreference, name='postpreference'),
]