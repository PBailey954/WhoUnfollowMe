from flask import Flask, request, render_template
import json
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def extract_usernames(data):
    return {entry["string_list_data"][0]["value"] for entry in data}

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    results = None
    if request.method == 'POST':
        followers_file = request.files.get('followers')
        following_file = request.files.get('following')

        if followers_file and following_file:
            followers_path = os.path.join(UPLOAD_FOLDER, 'followers.json')
            following_path = os.path.join(UPLOAD_FOLDER, 'following.json')
            followers_file.save(followers_path)
            following_file.save(following_path)

            with open(followers_path) as f:
                followers_data = json.load(f)
            with open(following_path) as f:
                following_data = json.load(f)

            followers = extract_usernames(followers_data)
            following = extract_usernames(following_data["relationships_following"])

            not_following_back = sorted(following - followers)
            not_followed_back = sorted(followers - following)
            mutuals = sorted(followers & following)

            results = {
                "not_following_back": not_following_back,
                "not_followed_back": not_followed_back,
                "mutuals": mutuals
            }

    return render_template("index.html", results=results)

if __name__ == '__main__':
    app.run(debug=True)
