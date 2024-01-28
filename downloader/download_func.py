import json
from django.http import HttpResponse
from pytube import YouTube
import io

def download_video(request, url):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution video stream
        video_stream = yt.streams.get_highest_resolution()

        # Create a buffer to hold the video content
        buffer = io.BytesIO()

        # Download the video to the buffer
        video_stream.stream_to_buffer(buffer)

        # Create a Django HttpResponse with appropriate headers
        response = HttpResponse(buffer.getvalue(), content_type='video/mp4')
        response['Content-Disposition'] = f'attachment; filename="{yt.title}.mp4"'

        # Include additional information in the response header
        response['X-Video-Info'] = json.dumps({
            'title': yt.title,
            'resolution': video_stream.resolution,
        })

        return response

    except Exception as e:
        return HttpResponse(f"Error: {e}")

def download_audio(request, url):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution audio stream (only audio)
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        # Create a buffer to hold the audio content
        buffer = io.BytesIO()

        # Download the audio to the buffer
        audio_stream.stream_to_buffer(buffer)

        # Create a Django HttpResponse with appropriate headers
        response = HttpResponse(buffer.getvalue(), content_type='audio/mpeg')
        response['Content-Disposition'] = f'attachment; filename="{yt.title}.mp3"'
        
        # Include additional information in the response header
        response['X-Audio-Info'] = json.dumps({
            'title': yt.title,
            'bitrate': audio_stream.bitrate,
        })

        return response

    except Exception as e:
        return HttpResponse(f"Error: {e}")
