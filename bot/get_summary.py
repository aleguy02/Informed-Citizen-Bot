import os
from dotenv import load_dotenv
from groq import Groq

def create_summary(article_data: dict):
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
                            "You will be provided a news article's headline delimited in square braces and its article content delimited in parentheses. Please create a concise summary of the article and a list of key political terms, simplifying the language to help build the reader’s confidence in understanding political topics. "
                            "**Instructions**: "
                            "1. **Unbiased Analysis**: You must analyze the article critically, without showing bias toward any political ideology. Your summary and key terms should be neutral and fact-based. "
                            "2. **Focus on Key Information**: When processing the article, identify the most important points, including major events or actions described, names of key individuals or organizations, dates or timelines, and important political terms and concepts "
                            "3. **Summary**: After reading the article, write a concise, 1-paragraph summary of the main ideas. The summary should be neutral, clear, and provide an overview of the political issue or event discussed in the article. "
                            "4. **Key Terms**: Identify 6 political terms or concepts that are central to the article. Identify and extract key ideas, including significant words, numbers, names, and dates. For each term, write a brief explanation that will help readers unfamiliar with political jargon understand the concept. Each explanation should focus on breaking down the meaning in an accessible way. "
                            "5. **Format**: Structure the data in the following JSON format: "
                            '{ "summary": "Your 1-paragraph summary here", "key_terms": [{"term": "Political Term 1", "explanation": "Explanation of the term."}, {"term": "Political Term 2", "explanation": "Explanation of the term."}, {"term": "Political Term 3", "explanation": "Explanation of the term."}, {"term": "Political Term 4", "explanation": "Explanation of the term."}, {"term": "Political Term 5", "explanation": "Explanation of the term."}] }'
                            "5. **Verification**: Verify that the data is correctly formatted. Any fields that aren't populated should be assigned a value of 'MISSING'"
                            "IMPORTANT: REMEMBER YOUR RESPONS IS A STRINGIFIED JSON. DO NOT RESPOND IN ANY OTHER FORMAT. CHECK THAT JSON IS VALID BEFORE OUTPUTTING."
                            f"Here is the article's headline and contents: [{article_data['headline']}], ({article_data['article']})")
            }
        ],
        temperature=0.5,
        max_tokens=2048,
        top_p=1,
        stream=False,
        stop=None,
    )

    return chat_completion.choices[0].message.content