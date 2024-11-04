from django.shortcuts import  * 
from django.http import * 
import random
from django.contrib import *

def index(request):
    if request.method == 'POST':
        request.session['name'] = request.POST.get('name')
        request.session['random_number'] = random.randint(1, 100)
        request.session['attempts'] = 0
        request.session['feedback'] = None
        request.session['background'] = 'white'
        return redirect('/')
    return render(request, 'index.html')

def guess(request):
    if request.method == 'POST':
        user_guess = int(request.POST.get('guess'))
        request.session['attempts'] += 1
        random_number = request.session['random_number']
        difference = user_guess - random_number

        if difference == 0:
            request.session['feedback'] = 'Correct!'
            request.session['background'] = 'green'
        elif abs(difference) <= 10:
            request.session['feedback'] = 'Lil bit high' if difference > 0 else 'Lil bit low'
        elif abs(difference) <= 20:
            request.session['feedback'] = 'Bit big number' if difference > 0 else 'Bit low number'
        else:
            request.session['feedback'] = 'Too high!' if difference > 0 else 'Too low!'

        if request.session['attempts'] >= 10 and request.session['feedback'] != 'Correct!':
            request.session['feedback'] = 'You Lose!'
            request.session['background'] = 'red'

        return redirect('/')
    return redirect('/')

def restart(request):
    request.session.clear()
    return redirect('/')

def highscore(request):
    highscore_data = request.session.get('highscore', [])
    return render(request, 'highscore.html', {'highscore': highscore_data})

def save_score(request):
    if request.session.get('feedback') == 'Correct!':
        highscore_data = request.session.get('highscore', [])
        highscore_data.append({'name': request.session['name'], 'attempts': request.session['attempts']})
        request.session['highscore'] = sorted(highscore_data, key=lambda k: k['attempts'])
    return redirect('/highscore')
