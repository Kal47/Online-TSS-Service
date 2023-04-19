from django.shortcuts import render
from tts.dectalk.say import sayToOggFile, sayToWavFile
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PhraseForm

#template
class DecTalkView(TemplateView):
	template_name = 'dectalk.html'   

#view
@csrf_exempt
def DecTalkPostView(request):
	if request.method == 'POST':
		form = PhraseForm(request.POST)
		if form.is_valid():
			phrase = form.cleaned_data['phrase']
			sayToWavFile('static/temp', phrase)
			return HttpResponseRedirect('')
	else:
		form = NameForm()
	return render(request, 'name.html', {'form': form})
