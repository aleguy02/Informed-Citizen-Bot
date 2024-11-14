import os
from dotenv import load_dotenv
from groq import Groq

def create_summary(article: str):
    load_dotenv()

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )
    chat_completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": ("You are now an assistant whose goal to make political discussions more accessible to readers, especially those who are not familiar with political jargon. "
                            "You will be provided a news article delimited in parentheses. Please create a concise summary of the article to help build the reader’s confidence in understanding political topics. Your summary should be unbiased and focus on key information"
                            f"Here is the article's contents: ({article})")
            }
        ],
        temperature=0.5,
        max_tokens=2048,
        top_p=1,
        stream=False,
        stop=None,
    )

    return chat_completion.choices[0].message.content