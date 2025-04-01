from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "who is current Prime Minister of India?"}
  ]
)

print(completion.choices[0].message.content)
