from api.fictionary import bp
from flask import Response, request
import os, openai, json

openai.api_key = os.getenv('OPEN_AI_KEY')

def define(model, prompt, num_return=1):
    completion = openai.Completion.create(model=model, prompt=prompt)
    return completion.choices[0].text

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
        prompt_template = "Define the word '{}' in a few sentences as if you were urban dictionary.".format(word)
        definition = define(os.getenv('OPEN_AI_MODEL'), prompt_template)
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
