from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
import random
from django.core.validators import validate_email
from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework.views import APIView

# Create your views here.
    
