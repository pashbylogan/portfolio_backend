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
