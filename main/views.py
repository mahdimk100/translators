from django.shortcuts import render, HttpResponse
from translate import Translator

# Create your views here.

def home(request):
    if request.method == 'POST':
        text = request.POST['translate']
        language = request.POST['language']
        translator = Translator(to_lang=language)
        tranlation = translator.translate(text)
        return HttpResponse(tranlation)
    return render(request, 'main/index.html')