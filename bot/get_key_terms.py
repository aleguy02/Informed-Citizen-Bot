import os
from dotenv import load_dotenv
from groq import Groq

def get_key_terms(article: str):
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
                            "You will be provided a news article delimited in parentheses. Please create a list of 6 key political terms, such as terminology, numbers, names, acronyms, or dates, simplifying the language to help build the reader’s confidence in understanding political topics. "
                            "For each term, write a brief explanation that will help readers unfamiliar with political jargon understand the concept. "
                            "Structure the list in the following JSON format: "
                            '{"term1": "Political Term 1", "explanation1": "Explanation of the Term 1.", "term2": "Political Term 2", "explanation2": "Explanation of the Term 2.", "term3": "Political Term 3", "explanation3": "Explanation of the Term 3.", "term4": "Political Term 4", "explanation4": "Explanation of the Term 4.", "term5": "Political Term 5", "explanation5": "Explanation of the Term 5.", "term6": "Political Term 5", "explanation6": "Explanation of the Term 5."}'
                            "Make sure that the data is correctly formatted. Any fields that aren't populated should be assigned a value of 'MISSING'"
                            "IMPORTANT: REMEMBER YOUR RESPONSE IS A STRINGIFIED JSON. DO NOT RESPOND IN ANY OTHER FORMAT. CHECK THAT JSON IS VALID BEFORE OUTPUTTING."
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