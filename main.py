from flask import Flask, jsonify, request
import spotipy
import spotipy.util as util

app = Flask(__name__)

scope = 'user-follow-read'
client_id = '7100ea2475d847b3b5d6d99d5e53e6c8'
client_secret = 'a4fa499a6e834355b423bbd09ada85d2'

username='spotify:user:22np7rylgc3jz7lndwz3d7m6y'

token = util.prompt_for_user_token(username,scope,client_id,client_secret,'https://example.com/callback/')

@app.route('/search', methods=['POST'])
def query_spotify():
    print(request)
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.search(q=request.json.get('query'), type='artist')
    return jsonify(results)
