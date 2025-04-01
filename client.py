from openai import OpenAI

client = OpenAI(api_key="your own key"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "who is current Prime Minister of India?"}
  ]
)

print(completion.choices[0].message.content)
