# TextDiffDE
GermanTextDifficulty

## Find the CEFR level of a German text.
This project is based on the Flesch Reading Ease paradigm, where the length of words and sentences tends to be correlated with the complexity of written English. 

Can be used to get an idea of the level of your own written German, or the level of a text that you want to study.

## Creation 
I created a corpus from a mish-mash of pre-graded German texts from all over the internet in the public domain, then calculated the average sentence- and word-length for each level of the Common European Framework of Reference (CEFR). There are six leves A1 and A2 are the Beginner (or breakthrough) levels, B1 and B2 are the Intermediate (independent user) levels, and C1 and C2 are the Advanced (mastery) levels.

I then pinned these numbers to a Python data array which could be used as a measure against the average word and sentence lengths in a user-entered text.

The program is pretty stock standard Python. It shouldn't require any additional libraries to run. 

## Instructions for use
1. Download **main.py** and **input_text.txt** to a local folder on your computer.

2. Replace the text in **input_text.txt** with your own German text. Don't worry too much about spaces or punctuation.

3. Open a prompt/terminal, and navigate to the directorz where you saved the two files.

4. Type: *python3 main.py*

5. Mach Spaß!
