from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
from utils.Video_Summarizer.prompt import get_prompt
from utils.Video_Summarizer.task_1 import video_frame_text
from utils.Video_Summarizer.task_2 import video_audio_text

load_dotenv()

def run_pipeline(video_file):
    llm = HuggingFaceEndpoint(
        model="meta-llama/Llama-3.1-8B-Instruct",
        temperature=0.2
    )
    
    model = ChatHuggingFace(llm=llm)

    parser = StrOutputParser()

    summary_prompt = get_prompt()

    chain = summary_prompt | model | parser


    
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(video_frame_text, video_file)
        future2 = executor.submit(video_audio_text, video_file)

        frame_text = future1.result()
        audio_text = future2.result()

    result = chain.invoke({
            "frame_text": frame_text,
            "audio_text": audio_text
        })

    return result