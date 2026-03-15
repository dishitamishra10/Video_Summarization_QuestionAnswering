from serpapi import GoogleSearch
import os

def get_transcript(video_id: str):
    try:
        params = {
            "api_key": '7cf5a57090a6e5e7e9bd986cac132c20e18f3651a5580166e46804f6c1cfb8a0',
            'engine': 'youtube_video_transcript',
            'v': video_id
        }

        search = GoogleSearch(params)
        result = search.get_dict()

        return ' '.join(s.get('snippet', '') for s in result['transcript'])
    
    except Exception as e:
        print(f"Error has occured. ", e)
        return ''
    

# transcript = get_transcript('We7BZVKbCVw')
# print(transcript)