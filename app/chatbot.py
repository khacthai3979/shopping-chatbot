
from google.cloud import dialogflow_v2 as dialogflow

import os
import uuid

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "newagent-yniy-e0fe1be386a2.json"

def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result.fulfillment_text

def get_bot_response(message):
    project_id = 'newagent-yniy'
    session_id = str(uuid.uuid4())
    language_code = 'vi'

    return detect_intent_texts(project_id, session_id, message, language_code)
