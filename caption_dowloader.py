# Install necessary package
# !pip install youtube-transcript-api

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def save_transcript(youtube_url, output_file, language_code='en'):
    try:
        # Extract the video ID from the YouTube URL
        video_id = youtube_url.split("v=")[-1].split("&")[0]
        
        # Fetch the transcript
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        # Find the transcript in the desired language
        transcript = transcript_list.find_transcript([language_code])
        
        # Fetch and format the transcript
        transcript_data = transcript.fetch()
        formatter = TextFormatter()
        caption_text = formatter.format_transcript(transcript_data)
        
        # Save to a .txt file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(caption_text)
        
        print(f"Transcript saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
youtube_url = "https://www.youtube.com/watch?v=KGzF60KERZ4"  # Replace with your video URL
output_file = "transcript.txt"
save_transcript(youtube_url, output_file)
