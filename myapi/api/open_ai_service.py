import openai

openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"

def open_ia_response(prompt):
    response = openai.ChatCompletion.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": 
                f"{prompt} Tu réponds en français"
            }
        ]
        
    )
    
    return response["choices"][0]["message"]["content"]

