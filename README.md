# AI-confessions-generator

## Scraping Facebook Data
We used the [facebook-scraper library](https://pypi.org/project/facebook-scraper/) to scrape data from the NYUAD Crushes and Compliments public page. To do so we run,
```
python3 data/cc_scraper.py
```

The scraped data can be found in *data/confessions.txt*.

## Finetuning GPT-2-Simple
We then finetuned GPT-2-Simple (124M) with the scraped data from Facebook. This took a couple of hours and we achieved it with this command:
```
python3 script.py
```

The finetuned models can be found in *app/checkpoint/run1*.
