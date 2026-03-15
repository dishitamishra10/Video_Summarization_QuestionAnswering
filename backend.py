from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from utils.Youtube_QNA.url_to_id import get_videoID
from utils.Youtube_QNA.transcript import get_transcript
from utils.Youtube_QNA.vectorstore import create_vectorstore
from utils.Youtube_QNA.chain import build_chain
from utils.Video_Summarizer.model import run_pipeline
from utils.Video_Summarizer.delete_all import cleanup_generated_files
from fastapi import UploadFile, File
import tempfile



app = FastAPI()

class YoutubeRequest(BaseModel):
    url: str
    query: str


@app.get('/')
def welcome():
    return {'mesaage': 'Welcome to the video section' }

@app.post('/youtube-qna')
def youtube_qna(data: YoutubeRequest):
    id = get_videoID(data.url)

    if not id:
        raise HTTPException(status_code=400, detail="Video ID can not found")
    
    id = str(id)

    try:
        transcript = get_transcript(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Transcript error: {str(e)}")

    if not transcript:
        raise HTTPException(status_code=400, detail="Transcript not fetched.")
    
    vector_store = create_vectorstore(transcript)

    chain = build_chain(vector_store)

    try:
        answer = chain.invoke(data.query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {'answer': answer}




@app.post('/video-summarize')
async def video_summarize(video_file: UploadFile = File(...)):

    try:
        with tempfile.NamedTemporaryFile(delete=False) as tfile:
            contents = await video_file.read()
            tfile.write(contents)
            video_path = tfile.name

            output = run_pipeline(video_path)
            cleanup_generated_files()

            return {"answer": output}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Internal server error{str(e)}')