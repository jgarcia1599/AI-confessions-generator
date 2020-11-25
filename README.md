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


## Deploying GPT-2-Simple Text Generation API on Google Cloud Run
We deployed the GPT-2-Simple Text Generation API on Google Cloud Run following this [tutorial](https://github.com/minimaxir/gpt-2-cloud-run). The following are the commands we used:
Building the image:
```
docker build . -t gpt2
```

If you want to test the image locally with the same specs as Cloud Run, you can run:
```
docker run -p 8080:8080 --memory="2g" --cpus="1" gpt2
```

You can then visit/curl http://0.0.0.0:8080 to get generated text!


Now, create a project on Google Cloud Platform and get the *project-id*.

Then tag the image with the project-id you just retrieved:
```
docker tag gpt2 gcr.io/[PROJECT-ID]/gpt2
```

For this next step, you must grant Docker [permissions](https://cloud.google.com/container-registry/docs/advanced-authentication) to upload the image to the Google Container Registry:
```
docker push gcr.io/[PROJECT-ID]/gpt2
```

Once done, deploy the uploaded image to Cloud Run via the console. You'll likely encounter *Memory exceeded error* so make sure to set Memory Allocated to 2 GB and Maximum Requests Per Container to 1! Instructions to set memory [here](https://cloud.google.com/run/docs/configuring/memory-limits).

Now, get the url produced from your Google cloud deployment and use that in *app/templates/index.html* to send api requests.

## Deploying Front-End on Heroku
The front-end website was deployed on Heroku and can be accessed from [here](http://nyuad-ccc.herokuapp.com/).
