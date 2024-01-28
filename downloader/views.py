from django.shortcuts import render
from django.http import HttpResponse
from .download_func import download_video,download_audio

def convert(request):
    response = None  # Initialize the response variable
    loading = "true"  # Default value for loading
    # response = None  # Initialize the response variable
    if request.method == 'POST':
        link = request.POST.get('link', '')
        loading = "true"
        print(loading)
        button_clicked = request.POST.get('submit_button')
        if button_clicked == 'Download Video':
            response = download_video(request, link)
        elif button_clicked == 'Download Audio':
            response = download_audio(request, link)
        # Check if the download was successful
        
        print(loading)
        if isinstance(response, HttpResponse):
            loading = "false"
            print(loading)
            return response   # Return the response directly
 
        # If there was an error, you might want to handle it, e.g., by rendering an error page
        return render(request, 'error.html', {'error_message': response})

    # Render the initial form
    return render(request, 'home.html', {'loading': loading})
