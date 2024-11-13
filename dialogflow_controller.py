import os
from google.cloud import dialogflow_v2 as dialogflow

def detect_intent(session_id, text, language_code='pt-BR'):
    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
    credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

    if not project_id or not credentials_path:
        raise ValueError("As credenciais do Dialogflow não foram configuradas corretamente.")

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(request={"session": session, "query_input": query_input})
        return response.query_result.fulfillment_text
    except Exception as e:
        print(f"Erro ao processar a mensagem: {e}")
        return "Desculpe, não entendi sua pergunta."
