from django.shortcuts import render
import random
import math
from datetime import datetime
import json
import requests

# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')

def lorempic(request):
    return render(request, 'utilities/lorempic.html')