# Project-Lyrics-Analyzer
This project is beginner friendly and this project is build using for loop, dictionary, and if &amp; else Conditions 

text = """
Yeah
Rest in peace to all the kids that lost their lives in the Parkland shooting
This song is dedicated to you
Okay, she keep cryin', she keep cryin' every single night
Day and night, on my mind, please don't kill the vibe
Oh no, I swear to God, I be in my mind
Swear I wanna die, yeah, when you cross my-
Said I wanna die, yuh
No, I'm not alright, yuh
I might start a riot
I'm so fuckin' tired, yuh
So what's up? What you say?
Feelin' good, I'm feelin' great
Tired of the fuckin' hate
Stackin' cheese all on my plate
So outside of my misery, I think I'll find
A way of envisioning a better life
For the rest of us, the rest of us
There's hope for the rest of us, the rest of us
Okay, she keep cryin', she keep cryin' every single night
Day and night, on my mind, please don't kill the vibe
Oh, no, I swear to God, I be in my mind
Swear I wanna die, yeah, when you cross my-
Said I wanna die, yuh
No, I'm not alright, yuh
I might start a riot
I'm so fuckin' tired, yuh
So what's up? What you say?
Feelin' good, I'm feelin' great
Tired of the fuckin' hate
Stackin' cheese all on my plate
"""
word_count = {}

for word in text.lower().split():
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

print(word_count)
