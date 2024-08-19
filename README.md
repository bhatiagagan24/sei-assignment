# sei-assignment
Take Home Assignment by Sei

Assignment - 
https://gist.github.com/ramkumarvenkat/b7026550e859f5881c937d9aaed8bc84

Written in Flask for quick development!

Endpoint - /check-compliance

Pass the url for examination as well as the OpenAI Chatgpt api token in the request body.


## Steps to run this Project - 

1. pip install -r requirements.txt
2. Run python3 api.py in the terminal
3. Open Postman or any other API Tool, and make a POST request to this endpoint `http://127.0.0.1:5000/create-compliance-report`
4. Request Body is as follows - 
{
	"url": "https://mercury.com/",
	"api_token": "<<Your Open AI API Token Here>>"
}
5. Curl Request - 

curl --request POST \
  --url http://127.0.0.1:5000/create-compliance-report \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/9.3.3' \
  --data '{
	"url": "https://mercury.com/",
	"api_token": "api_token_here"
}'