import os
from dotenv import load_dotenv
from groq import Groq
import json
import redis


load_dotenv()

# Groq-based function
def create_summary_and_key_terms(article: str):

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )
    chat_completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": ("You are now an assistant whose goal to make political discussions more accessible to readers, especially those who are not familiar with political jargon. "
                            "You will be provided a news article's content delimited in parentheses. Please create a concise summary of the article and a list of key political terms, such as terminology, numbers, names, acronyms, or dates, simplifying the language to help build the reader’s confidence in understanding political topics. "
                            "**Instructions**: "
                            "1. **Summarize**: Please create a 1-paragraph summary of the article to help build the reader’s confidence in understanding political topics. Your summary should be unbiased and focused on key information"
                            "2. **Summary**: After reading the article, write a concise, 1-paragraph summary of the main ideas. The summary should be neutral, clear, and provide an overview of the political issue or event discussed in the article. "
                            "3. **Key Terms**: Please create a list of 6 key political terms, such as terminology, numbers, names, acronyms, or dates, simplifying the language to help build the reader’s confidence in understanding political topics. For each term, write a brief explanation that will help readers unfamiliar with political jargon understand the concept. "
                            "4. **Format**: Structure the data in the following JSON format: "
                            '{ "summary": "Your 1-paragraph summary here", "key_terms": [{"term": "Political Term 1", "explanation": "Explanation of Political Term 1."}, {"term": "Political Term 2", "explanation": "Explanation of Political Term 2."}, {"term": "Political Term 3", "explanation": "Explanation of Political Term 3."}, {"term": "Political Term 4", "explanation": "Explanation of Political Term 4."}, {"term": "Political Term 5", "explanation": "Explanation of Political Term 5."}, {"term": "Political Term 6", "explanation": "Explanation of Political Term 6."}] }'
                            "5. **Verification**: Make sure that the data is correctly formatted."
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


# Format terms function
def format_terms(chat_completion_str: str):
    try:
        chat_completion_str = chat_completion_str.strip()
        start_index = chat_completion_str.find("{")
        end_index = chat_completion_str.rfind("]") + 1
        chat_completion_str = chat_completion_str[start_index:end_index] + "}"
        chat_completion_str_dict = json.loads(chat_completion_str) 

        summary = chat_completion_str_dict["summary"]
        terms_as_string = ""

        i = 1
        for item in chat_completion_str_dict["key_terms"]:
            terms_as_string += (f"{i}. {item['term']}: {item['explanation']}\n")
            i += 1
        
        return {"summary": summary, "terms" : terms_as_string}
    except Exception as e:
        print(f"Error occured in format_terms: {e}")
        return 0
    

# Redis-based function
def get_article_data():  # relative imports are hell on earth so I'm just handling redis<->bot logic in here
    r = redis.Redis(
        host = os.getenv("REDIS_HOST"),
        port = os.getenv("REDIS_PORT"),
        db = 0,
        password = os.getenv("REDIS_PASSWORD"),
        decode_responses=True
        )
    
    article_data = r.hgetall("article_data")
    if not article_data:
        print("No values at key")
        return 0 # 0 will be treated as an error code in bot.py
    
    return {
                "headline": article_data["headline"],
                "article": article_data["article"],
                "url": article_data["url"]
            }