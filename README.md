# AI-CrushesandCompliments-generator

ART INTEL FALL 2020      
By Estelle and Junior     

## Description
For the sound and text project, we drew inspiration from the ongoing class discussions on the advances of Natural Language Processing. In particular, how Language Models were able to generate new text that sounds like a human. These discussions made us think of how we could use such capabilities for creative purposes and we decided to finetune a <a href="https://openai.com/blog/gpt-2-1-5b-release/">GPT-2 model </a> using data scraped from NYUAD Crushes and Compliments, a public page where NYUAD students posts anonymous posts about anything and everything, but mostly to compliment somone. Using this data, we wanted to make an application that allows people to generate crushes and compliments posts based on some starting text. This projects is the fruition of our idea, and we hope you enjoy it. 

## Process and Implementation
These projects required us to do the 4 things below: 

### Scraping Facebook Data
We used the [facebook-scraper library](https://pypi.org/project/facebook-scraper/) to scrape data from the NYUAD Crushes and Compliments public page. To do so we run,
```
python3 data/cc_scraper.py
```

The scraped data can be found in *data/confessions.txt*.

### Finetuning GPT-2-Simple
We then finetuned [GPT-2-Simple](https://github.com/minimaxir/gpt-2-simple) (124M) with the scraped data from Facebook.To accomplish this, we used the Team Viewer to access the lab computers and run the training there as our laptops didnt have a GPU. This took a couple of hours and we achieved it with this command:
```
python3 script.py
```

The finetuned models can be found in *app/checkpoint/run1*.

### Generating Text with FineTuned Model
We created an API using [Flask](https://exploreflask.com/en/latest/)to generate text from the finetuned model and return it as a **json** response. To run the api locally:
```
python3 app/app.py
```

### Front-End
We then created a front-end webpage to take in input from the user and send it as a post api request to the api. To run it locally, first change the url on *line 119* of **app/templates/index.html** to the url (eg. localhost:8080) the api server is running on.


### Deploying GPT-2-Simple Text Generation API on Google Cloud Run
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

### Deploying Front-End on Heroku
The front-end website was deployed on Heroku and can be accessed from [here](http://nyuad-ccc.herokuapp.com/).

## Reflection and Evaluation

All in all, we were excited about the outcome of this project as it involved us getting our hands dirty in different technology stacks (ML traning using a remote GPU computer, front-end web development and api development and deployment). However, the application still has some issues. Sometimes,the generated texts based on some starting text comes back empty on the frontend, so maybe a better way to handle this edge case would have been more efficient. The application takes a while to generate text, so maybe a way to deploy the api and the front end in a single machine might solve this issue as currently the front end and the backend api run on two different machines. We are also worried about the people's privacy, as sometimes the generated text can provide shockingly realistic descriptions about people. As such, figuring out a way to protect's people's privacy in the application might be a good idea.
