from api.fictionary import bp
from api.fictionary.fictionary_logic import authenticate_api_key, define
from flask import Response, request


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
