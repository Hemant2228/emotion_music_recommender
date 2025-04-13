from flask import Flask, render_template_string, jsonify
import cv2
from deepface import DeepFace

app = Flask(__name__)

# Mapping emotions to Spotify playlists
emotion_to_playlist = {
    'happy': 'https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC',
    'sad': 'https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1',
    'angry': 'https://open.spotify.com/playlist/37i9dQZF1DWYxwmBaMqxsl',
    'surprise': 'https://open.spotify.com/playlist/37i9dQZF1DWTfrr8pte1rT',
    'fear': 'https://open.spotify.com/playlist/37i9dQZF1DX4sWSpwq3LiO',
    'disgust': 'https://open.spotify.com/playlist/37i9dQZF1DX7gtIfGVzmkY',
    'neutral': 'https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6'
}

def detect_emotion():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if ret:
        try:
            analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            emotion = analysis[0]['dominant_emotion']
            return emotion
        except Exception as e:
            print("Error analyzing emotion:", e)
            return "neutral"
    return "neutral"

@app.route('/')
def index():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Emotion-Based Music Recommender</title>
    </head>
    <body>
        <h1>🎵 Emotion-Based Music Recommender</h1>
        <button onclick="getPlaylist()">Get Mood Playlist</button>
        <p id="result"></p>
        <script>
            function getPlaylist() {
                fetch('/get_playlist')
                    .then(res => res.json())
                    .then(data => {
                        document.getElementById('result').innerHTML =
                            `Detected Emotion: <strong>${data.emotion}</strong><br>
                             <a href="${data.playlist}" target="_blank">Open Spotify Playlist</a>`;
                    });
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/get_playlist', methods=['GET'])
def get_playlist():
    emotion = detect_emotion()
    playlist_url = emotion_to_playlist.get(emotion, emotion_to_playlist['neutral'])
    return jsonify({'emotion': emotion, 'playlist': playlist_url})

if __name__ == '__main__':
    app.run(debug=True)

