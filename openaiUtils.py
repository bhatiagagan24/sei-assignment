import os
import openai
import json

from openai import OpenAI

from utils import sanitize_url

compliance_check_map = {
    "stripe": "compliance-checks/stripe.json"
}


class OpenApiClient:
    def __init__(self, api_key):
        self.model = 'gpt-4-turbo'
        self.client = self.__init_client(api_key)

    def __init_client(self, api_key):
        self.client = OpenAI(api_key=api_key)
        return self.client

    # only loading stripe checks as of now, but we can configure
    # to load checks as required
    def __load_compliance_checks(self):
        file_path = compliance_check_map["stripe"]
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def __get_init_prompt(self):
        checks = self.__load_compliance_checks()
        return {
            "role": "system",
            "content": f'''
                Assume you are a compliance officer and this is the list of check 
                you need to perform on a bank's website {checks}
             '''
        }

    def __get_prompt(self, website_text):
        return {
            "role": "system",
            "content": f'''
                Given the website text below, analyse it and return what exactly is wrong, and how we can fix it, but do not return
                back the guidelines. just simply return what is wrong and how we can fix it. Return the response as list of objects.
                {website_text}
             '''
        }

    def get_response(self, website_text):
        init_message = self.__get_init_prompt()
        followup = self.__get_prompt(website_text=website_text)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                init_message,
                followup
            ],
            max_tokens=1500
        )
        return response.choices[0].message.content

