import gradio as gr
from voice_interface import transcribe_audio, synthesize_speech
from rag_pipeline import get_answer

def agrisaarthi(audio):
    query = transcribe_audio(audio)
    response = get_answer(query)
    speech = synthesize_speech(response)
    return response, speech

demo = gr.Interface(
    fn=agrisaarthi,
    inputs=gr.Audio(source="microphone", type="filepath"),
    outputs=["text", "audio"]
)

demo.launch()
