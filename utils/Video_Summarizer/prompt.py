from langchain_core.prompts import PromptTemplate

def get_prompt():
    summary_prompt = PromptTemplate(
        input_variables=["frame_text", "audio_text"],
        template="""
    You are an expert content analyst.

    You are given two transcripts extracted from the same video:

    1. OCR Transcript (from video frames):
    ---------------------
    {frame_text}
    ---------------------

    2. Audio Transcript (from speech recognition):
    ---------------------
    {audio_text}
    ---------------------

    Your tasks:

    1. Merge both transcripts into a single coherent understanding.
    2. Remove duplicate or repeated information.
    3. Resolve minor inconsistencies using logical reasoning.
    4. Prefer information that appears in both sources.
    5. Preserve important facts, numbers, names, and technical terms.
    6. Do NOT invent new information.
    7. If conflicts exist and cannot be resolved, mention them briefly.

    Output Format:

    - Clean Combined Summary (well-structured paragraphs)
    - Key Points (bullet list)
    - Important Technical Terms (if any)

    Generate a clear, concise, and accurate summary.
    """
    )

    return summary_prompt