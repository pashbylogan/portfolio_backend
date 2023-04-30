from api.fictionary import bp
from flask import Response, request
import os, openai

openai.api_key = os.getenv('OPENAI_API_KEY')

def define(model, prompt, num_return=1):
    models = openai.Model.list()
    return models

API_KEYS = {os.getenv('API_KEY')}
def authenticate_api_key(func):
    def wrapper(*args, **kwargs):
        api_key = request.headers.get("API-KEY")
        if api_key is None:
            return "API Key is missing", 401

        if api_key not in API_KEYS:
            return "Invalid API Key", 401

        return func(*args, **kwargs)

    return wrapper

@bp.route('/')
def index():
    return 'This is The Main Blueprint'

@bp.route('/word', methods=["POST"])
@authenticate_api_key
def word():
    data = request.json
    word = data['word']

    try:
        definition = define(word, None)
    except Exception as e:
        print(e)
        definition = "This word is undefinable. Good job..."

    resp_data = json.dumps(
            {'definition': definition}
        )
    response = Response(resp_data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = True
    return response  # return data with 200 OK
