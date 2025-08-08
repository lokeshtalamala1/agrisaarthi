from transformers import pipeline

qa_pipeline = pipeline("question-answering")

def answer_question(question, context):
    return qa_pipeline(question=question, context=context)['answer']
