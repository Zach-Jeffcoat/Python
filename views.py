from django.shortcuts import render, redirect

# Create your views here.
def homepage(request):
    return render (request, 'homepage.html')

def result(request):
    request.session['name'] = request.POST['name']
    request.session['dojo'] = request.POST['dojo']
    request.session['lang'] = request.POST['lang']
    request.session['comment'] = request.POST ['comment']
    return redirect('/result/data')

def data(request):
    return render(request, 'result.html')
    #request.session['name'] = request.POST['name']
    #request.session['dojo'] = request.POST['dojo']
    #request.session['lang'] = request.POST['lang']
    #request.session['comment'] = request.POST ['comment']

