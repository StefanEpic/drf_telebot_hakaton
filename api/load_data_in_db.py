import json
import sqlite3

with open("videos.json", encoding="utf-8") as f:
    videos_data = json.load(f)

with open("emotions.json", encoding="utf-8") as f:
    emotions_data = json.load(f)

with open("food.json", encoding="utf-8") as f:
    food_data = json.load(f)

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

for video in videos_data:
    try:
        cursor.execute(""" INSERT INTO botapp_video (title, url) VALUES (?, ?) """, (video, videos_data[video]))
    except Exception as e:
        print(e)

for emotion in emotions_data:
    try:
        cursor.execute(
            """ INSERT INTO botapp_emotion (title, sticker_id) VALUES (?, ?) """, (emotion, emotions_data[emotion])
        )
    except Exception as e:
        print(e)

for food in food_data:
    try:
        cursor.execute(""" INSERT INTO botapp_food (title, sticker_id) VALUES (?, ?) """, (food, food_data[food]))
    except Exception as e:
        print(e)

conn.commit()
conn.close()
