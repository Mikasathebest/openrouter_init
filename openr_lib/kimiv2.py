from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

completion = client.chat.completions.create(
  extra_body={},
  model="moonshotai/kimi-k2:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion.choices[0].message.content)

# https://platform.openai.com/docs/guides/responses-vs-chat-completions?api-mode=responses
# Response has built-in tools and MCP support.
# response = client.responses.create(
#   model="moonshotai/kimi-k2:free",
#   input=[
#       {
#           "role": "user",
#           "content": "Write a one-sentence bedtime story about a unicorn."
#       }
#   ]
# )

# print(response)
