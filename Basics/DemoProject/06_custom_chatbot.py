'''
Create a simple chatbot using OpenRouter API
This script uses the OpenRouter API to create a simple chatbot that can respond to user queries.
It supports multiple models, including DeepSeek R1 and Gemini 2.0 Flash Exp.
You can use this script to ask questions and get answers from the models.   
You can change the model by modifying the `model` variable in the `get_completion` function.

'''

from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1", # Base URL for OpenRouter API
  api_key="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", # Your OpenRouter API key
)

model_deepseek = "deepseek/deepseek-r1-0528:free" # Use this variable to use DeepSeek R1 model

model_gemini20 = "google/gemini-2.0-flash-exp:free" # Use this variable to use Gemini 2.0 Flash Exp model

# This helper function will make it easier to use prompts and look at the generated outputs.  
def get_completion(prompt, model="deepseek/deepseek-r1-0528:free"):
     messages = [{"role": "user", "content": prompt}]
     extra_headers={
                "HTTP-Referer": "https://github.com/riteshsingh84/", # Optional. Site URL for rankings on openrouter.ai.
                "X-Title": "MyChatBot", # Optional. Site title for rankings on openrouter.ai.
            }   
     
     response = client.chat.completions.create(
        extra_headers=extra_headers,
        extra_body={},
        model=model,
        messages=messages,
        temperature=0     
        )
     return response.choices[0].message.content


# Ask the user for prompt
prompt = input("Enter your question: ")

# Get response from the model
response = get_completion(prompt, model=model_gemini20)  # Change to model_deepseek to use deepseek-r1-0528

print(response)