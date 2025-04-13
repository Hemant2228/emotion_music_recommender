# 🎵 Emotion-Based Music Recommender

This project is an AI-powered web app that detects your **emotion through your webcam** and suggests a matching **Spotify playlist**. Whether you're feeling happy, sad, or angry — there's music to match your mood!

---

## 💡 Overview

**Problem:** People often struggle to find music that fits their current emotion.  
**Solution:** An AI-based system that captures your facial expression and suggests a playlist based on your mood.

---

## 🧠 How It Works

1. Your webcam captures a live image.
2. DeepFace detects your **dominant emotion**.
3. A playlist is suggested based on your mood.

---

## 🛠️ Technologies Used

- **Python** – Core language  
- **Flask** – Web framework  
- **OpenCV** – Webcam capture  
- **DeepFace** – Facial emotion detection  
- **TensorFlow & tf-keras** – Backend for DeepFace  
- **HTML/JavaScript** – Front-end  
- **Spotify** – Playlist recommendation

---

## 🔗 Emotion-to-Playlist Mapping

| Emotion   | Playlist |
|-----------|----------|
| 😊 Happy     | [Happy Vibes](https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC) |
| 😢 Sad       | [Sad Songs](https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1) |
| 😠 Angry     | [Angry Mood](https://open.spotify.com/playlist/37i9dQZF1DWYxwmBaMqxsl) |
| 😲 Surprise  | [Surprise Soundtrack](https://open.spotify.com/playlist/37i9dQZF1DWTfrr8pte1rT) |
| 😨 Fear      | [Calm Down](https://open.spotify.com/playlist/37i9dQZF1DX4sWSpwq3LiO) |
| 🤢 Disgust   | [Cleanse Vibes](https://open.spotify.com/playlist/37i9dQZF1DX7gtIfGVzmkY) |
| 😐 Neutral   | [Chill Hits](https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6) |

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.x
- Webcam
- `pip` package manager

### 📦 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/emotion-music-recommender.git
cd emotion-music-recommender

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
