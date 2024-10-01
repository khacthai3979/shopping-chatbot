
import google.cloud.dialogflow_v2 as dialogflow
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Dap391m/Mental-Health-Chatbot-Vietnam/assistant-sell-kigg-366e21828f16.json"

def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result.fulfillment_text

def get_bot_response(message):
    project_id = 'assistant-sell-kigg'
    session_id = '115900352141775868446'
    language_code = 'vi'

    return detect_intent_texts(project_id, session_id, message, language_code)
