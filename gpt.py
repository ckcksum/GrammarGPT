from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

GENERAL_PROMPT = (
    "As an AI assistant, your task is to improve the English of the text or vocabulary I provide. Please do not highlight the mistakes; simply offer a corrected version. Ensure that the original meaning of the text is retained, and try to preserve the original wording as much as possible, unless it is unclear or contains substantial grammatical errors."
)

EMAIL_PROMPT = "Formal tone. No need to be professional unless specified. If subject of the email is not provided, please create one. And return the improved text in general email format"
TEXTCHAT_PROMPT = "Allow for informal language and short forms."

# Change prompt according to the input type
def get_system_prompt(input_type: str) -> str:
    if input_type == 'e':
        return GENERAL_PROMPT + " " + EMAIL_PROMPT
    elif input_type == 'c':
        return GENERAL_PROMPT + " " + TEXTCHAT_PROMPT
    elif input_type == 'g':
        return GENERAL_PROMPT

# From OpenAI doc
def ask(system_prompt: str, user_input: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": [{
                    "type": "text",
                    "text": system_prompt
                }]
            },
            {
                "role": "user",
                "content": [{
                    "type": "text",
                    "text": user_input
                }]
            },
        ],
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0,
        response_format={
            "type": "text"
        }
    )

    return response.choices[0].message.content or "ERROR OCCURS.\n"