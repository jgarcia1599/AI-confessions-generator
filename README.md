# AI-confessions-generator

## Scraping Facebook Data
We used the [facebook-scraper library](https://pypi.org/project/facebook-scraper/) to scrape data from the NYUAD Crushes and Compliments public page. To do so we run,
```
python3 data/cc_scraper.py
```

The scraped data can be found in *data/confessions.txt*.

## Finetuning GPT-2-Simple
We then finetuned [GPT-2-Simple](https://github.com/minimaxir/gpt-2-simple) (124M) with the scraped data from Facebook. This took a couple of hours and we achieved it with this command:
```
python3 script.py
```

The finetuned models can be found in *app/checkpoint/run1*.

## Generating Text with FineTuned Model
We created an API to generate text from the finetuned model and return it as a **json** response. To run the api locally:
```
python3 app/app.py
```

## Front-End
We then created a front-end webpage to take in input from the user and send it as a post api request to the api. To run it locally, first change the url on *line 119* of **app/templates/index.html** to the url (eg. localhost:8080) the api server is running on.
