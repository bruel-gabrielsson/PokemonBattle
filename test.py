from ai21 import AI21Client
from ai21.models.chat import ChatMessage

KEY = 'v7uBaXL8sXKB4SmHsrxIOa14sYsWPcT9'

client = AI21Client(api_key=KEY)  # or pass it in directly

response = client.chat.completions.create(
    model='jamba-large',
    messages=[ChatMessage(role='user', content='Hello, please provide a brief explanation of what AI21 does, in 100 words or less')]
)



print(response)

# def battle()