'''
Script to scrape data from NYUAD Confessions and save it as a txt file
Usage:
python3 confessions_scraper.py
'''


from facebook_scraper import get_posts
import emoji
import io
import re

filename = 'confessions.txt'
def process_text(text):
    allchars = [str for str in text]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.split() if not any(i in str for i in emoji_list)])
    processed_text = ''
    try:
        processed_text = re.split('"', clean_text)[1]       
    except:
        pass
    return processed_text

posts = []
for post in get_posts('NYUAD-Crushes-and-Compliments-1185494961476520', pages=400):
    # remove emojis from text
    clean_text = process_text(post['text'])
    
    if clean_text != '':
        posts.append(clean_text)
    # save cleantext in .txt file
with io.open(filename, 'w', encoding="utf-8") as out_file:
#     print(give_emoji_free_text(clean_text),file=f)
    for post in posts:
        out_file.write(post + '\n\n\n\n\n')