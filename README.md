# sei-assignment
Take Home Assignment by Sei

![image](https://github.com/user-attachments/assets/f11bcc01-bd61-4ce3-9911-4664e0fe7a5b)


Assignment - 
https://gist.github.com/ramkumarvenkat/b7026550e859f5881c937d9aaed8bc84

Written in Flask for quick development!

Endpoint - /check-compliance [http://127.0.0.1:5000/create-compliance-report]

Pass the url for examination as well as the OpenAI Chatgpt api token in the request body.

## Improvements - 
This ia a prototype and not even a MVC. We can definitely optimize a lot of things including the introduction of caching, and using 
a database. We can cache the scraped webpages as well as the openai API responses.

We further need to have better exception handling in place, and this API synchronous as of now. We can greatly increase the performance by making it asynchronous. 

We can also make the code a lot more extensible, but then again this is a prototype.
Also due to security concerns with my API Key, I've made it accoridng to BYOK Model so that folks at Sei can test it using their own key. 

Please Note that I'm using a paid Open AI account.


## Steps to run this Project - 

1. Init virtual env using the following commands -
   python3 -m venv venv
   source ./venv/bin/activate  
2. pip install -r requirements.txt
3. Run python3 api.py in the terminal
4. Open Postman or any other API Tool, and make a POST request to this endpoint `http://127.0.0.1:5000/create-compliance-report`
5. Request Body is as follows - 
{
	"url": "https://mercury.com/",
	"api_token": "<<Your Open AI API Token Here>>"
}
6. Curl Request - 

curl --request POST \
  --url http://127.0.0.1:5000/create-compliance-report \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/9.3.3' \
  --data '{
	"url": "https://mercury.com/",
	"api_token": "api_token_here"
}'



