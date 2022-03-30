from datetime import datetime
import requests
import sqlite3
from deepface import DeepFace

def getNonExistantPerson():
    r = requests.get("https://thispersondoesnotexist.com/image").content
    return r

def savePicture(pictureBytes, fileName):
    with open(fileName, "wb") as f:
        f.write(pictureBytes)

def main():
    #initDB();
    pictureBytes = getNonExistantPerson();
    fileName = "images/" + str(datetime.now()) + ".jpg"
    savePicture(pictureBytes, fileName);
    analyze = DeepFace.analyze(fileName)

    #analyze={'emotion': {'angry': 5.725119045507654e-07, 'disgust': 9.583050847315866e-15, 'fear': 5.003701009087536e-07, 'happy': 99.38417673110962, 'sad': 9.116245536233691e-07, 'surprise': 9.39774125185977e-06, 'neutral': 0.6158128380775452}, 'dominant_emotion': 'happy', 'region': {'x': 137, 'y': 188, 'w': 727, 'h': 727}, 'age': 32, 'gender': 'Woman', 'race': {'asian': 5.955861914763716e-08, 'indian': 5.5438975632426946e-08, 'black': 3.7364089686825475e-11, 'white': 99.98656511306763, 'middle eastern': 0.0058048186474479735, 'latino hispanic': 0.007629213359905407}, 'dominant_race': 'white'}
    dominantEmotion=analyze['dominant_emotion']
    print(dominantEmotion)

main();