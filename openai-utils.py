from openai import OpenAI

class OpenApiClient:
    def __init__(self, api_key):
        self.model = 'gpt-4o-mini'
        self.role = 'user'
        return self.__init_client(api_key=api_key)
    def __init_client(self, api_key):
        client = client = OpenAI(api_key=api_key)
        return client
    def get_prompt(self):
        return '''
            Assume you are a compliance officer and given this list of compliance checks, please provide a list of changes required 
            in the website text given at the bottom to make it compliant 
            '''

client = OpenAI(
    # Defaults to os.environ.get("OPENAI_API_KEY")
)

chat_completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello world"}]
)