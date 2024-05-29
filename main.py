import requests

api_key = ''
model = 'gpt-4'
conversation = [
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": ""  # prompt gpt here if desired
            },
        ]
    }
]


def add_to_history(content: str, user: str) -> None:
    new_message = {
        'role': user,  # user or system
        'content': [
            {
                'type': 'text',
                'text': content
            }
        ]
    }
    conversation.append(new_message)


def chat(my_message: str) -> str:
    add_to_history(my_message, 'user')
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": model,
        "messages": conversation,
        "max_tokens": 4096
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    try:
        add_to_history(response.json()['choices'][0]['message']['content'], 'assistant')
        return response.json()['choices'][0]['message']['content']
    except KeyError:
        print('uh oh', response.json())
        return ''


def main():
    while True:
        user = input()
        print(chat(user))


if __name__ == '__main__':
    main()
