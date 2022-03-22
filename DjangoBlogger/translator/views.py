from . import translate
from django.shortcuts import render


# Create your views here.

def translator_view(request):
    if request.method != 'POST':
        return render(request, 'translator.html')
    else:
        original_text = request.POST['my_textarea']
        output = translate.trans(original_text)
        return render(request, 'translator.html', {'output_text':output, 'original_text':original_text})
