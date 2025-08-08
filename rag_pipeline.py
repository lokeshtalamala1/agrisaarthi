from model_utils import answer_question

CONTEXT = "Groundnut should be sown in early June for the best yield in Kharif season."

def retrieve_context(query):
    return CONTEXT

def get_answer(query):
    context = retrieve_context(query)
    return answer_question(query, context)
