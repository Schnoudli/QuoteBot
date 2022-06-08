from datetime import datetime
import requests
import sqlite3
from random import randrange
from PIL import Image, ImageFont, ImageDraw
from deepface import DeepFace

def getNonExistantPerson():
    r = requests.get("https://thispersondoesnotexist.com/image").content
    return r

def savePicture(pictureBytes, fileName):
    with open(fileName, "wb") as f:
        f.write(pictureBytes)

def getRandomQuote():
    connection = sqlite3.connect('quotes.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Quotes WHERE used='0'")
    nbQuotes = cursor.fetchall()

    randID = randrange(len(nbQuotes));
    query = "SELECT quote FROM Quotes WHERE id=?";
    cursor.execute(query, (randID,));
    randQuote= cursor.fetchall();

    query = "UPDATE Quotes SET used=1 WHERE id=?";
    cursor.execute(query, (randID,));

    connection.commit()
    connection.close()

    return randQuote;

def main():
    print("Downloading picture")
    pictureBytes = getNonExistantPerson();
    fileName = "images/" + str(datetime.now()) + ".jpg"
    savePicture(pictureBytes, fileName);
    print("Analyzing emotions")
    analyze = DeepFace.analyze(fileName)
    dominantEmotion=analyze['dominant_emotion']
    print("Dominant emotion: " + dominantEmotion)

    print("Getting random quote")
    randomQuote = getRandomQuote()[0][0]
    print("Printing random quote on image")
    my_image = Image.open(fileName)
    title_font = ImageFont.truetype('fonts/ComicSansMS3.ttf', 40)
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((15, 15), randomQuote, (255, 255, 255), font=title_font) #(237, 230, 211)
    my_image.save(fileName[:-4]+"_text.jpg")


main();

# analyze={'emotion': {'angry': 5.725119045507654e-07, 'disgust': 9.583050847315866e-15, 'fear': 5.003701009087536e-07, 'happy': 99.38417673110962, 'sad': 9.116245536233691e-07, 'surprise': 9.39774125185977e-06, 'neutral': 0.6158128380775452}, 'dominant_emotion': 'happy', 'region': {'x': 137, 'y': 188, 'w': 727, 'h': 727}, 'age': 32, 'gender': 'Woman', 'race': {'asian': 5.955861914763716e-08, 'indian': 5.5438975632426946e-08, 'black': 3.7364089686825475e-11, 'white': 99.98656511306763, 'middle eastern': 0.0058048186474479735, 'latino hispanic': 0.007629213359905407}, 'dominant_race': 'white'}
