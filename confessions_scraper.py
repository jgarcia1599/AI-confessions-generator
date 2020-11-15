'''
Script to scrape data from NYUAD Confessions and save it as a txt file

Usage:

python3 confessions_scraper.py

'''


from facebook_scraper import get_posts
import emoji


filename = 'confessions.txt'
def give_emoji_free_text(text):
    allchars = [str for str in text]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.split() if not any(i in str for i in emoji_list)])

    return clean_text
for post in get_posts('NYUAD-Crushes-and-Compliments-1185494961476520', pages=200):
    # remove emojis from text
    clean_text = give_emoji_free_text(post['text'])
    print(clean_text)
    # save cleantext in .txt file
    with open(filename, 'a') as f:
        print(give_emoji_free_text(clean_text),file=f)

