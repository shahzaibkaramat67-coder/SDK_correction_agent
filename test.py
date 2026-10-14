from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

base_url = os.getenv("FREELLMAPI_BASE_URL")
llm = os.getenv("FREELLMAPI_MODEL")
api_key = os.getenv("FREELLMAPI_API_KEY")

print("BASE URL:", base_url)
print("MODEL:", llm)
print("API KEY EXISTS:", bool(api_key))

client = OpenAI(base_url=base_url, api_key=api_key)

print("SENDING REQUEST...")

try:
    response = client.chat.completions.create(
        model=llm, messages=[{"role": "user", "content": "Say hello"}]
    )

    print("REQUEST SUCCESSFUL")
    print(response)

except Exception as e:
    print("REQUEST FAILED")
    print(type(e).__name__)
    print(repr(e))
