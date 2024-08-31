import os
from groq import Groq

# Directly set the API key
gro_api_key = "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"

def generate_summary(news_body):
    # Pass the API key to the Groq client
    client = Groq(api_key=gro_api_key)
    
    chat_completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {
                "role": "system",
                "content": "You are expert in news summarization in Bengali. Please summarize the following news article in top 3-5 bullet points in Bengali."
            },
            {
                "role": "user",
                "content": news_body
            }
        ],
        temperature=0,
        max_tokens=32768,
        top_p=1,
        stream=False,
        stop=None,
    )
    return chat_completion.choices[0].message.content
