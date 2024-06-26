from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import assemblyai as aai

def index(request):
    return render(request, 'home/index.html')

def upload_audio(request):
    if request.method == 'POST' and 'audio' in request.FILES:
        # Replace with your AssemblyAI API key
        aai.settings.api_key = "200dd1e192294c11bb38d30e8f6fcadc"

        audio_file = request.FILES['audio']

        # Get the selected language from the form
        language_code = request.POST.get('language')


        # Configure AssemblyAI transcriber with the selected language
        config = aai.TranscriptionConfig(language_code=language_code)
        transcriber = aai.Transcriber(config=config)

        transcript = transcriber.transcribe(audio_file)

        if transcript.status == aai.TranscriptStatus.error:
            return JsonResponse("Transcription error: {}".format(transcript.error))
        else:
            return JsonResponse({'transcript_text': transcript.text}, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'transcript_text': 'Please audio or video file only'})