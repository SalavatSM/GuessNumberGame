from django.shortcuts import render, redirect
import random


def home(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
        request.session['attempts'] = 0
    return render(request, 'game/home.html')


def guess(request):
    guess = int(request.POST['guess'])
    number = request.session['number']
    request.session['attempts'] += 1

    if guess < number:
        message = 'Too low'
    elif guess > number:
        message = 'Too high'
    else:
        message = 'You got it!'
        request.session.flush()

    return render(request, 'game/home.html', {'message': message})


