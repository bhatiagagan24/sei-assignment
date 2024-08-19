from utils import load_website_content
from openaiUtils import OpenApiClient

def get_compliance_analysis_results(url, api_key):
    website_text = load_website_content(url)
    llm_client = OpenApiClient(api_key=api_key)
    return llm_client.get_response(website_text=website_text)
