import openai

client = openai.OpenAI(
    api_key = "sk-poe-EMxz7iZtfIhucPR2sOk__qTB5FQr66sfEFkujGDqMaw",  # or os.getenv("POE_API_KEY")
    base_url = "https://api.poe.com/v1",
)

response = client.responses.create(
    model = "gpt-5.3-codex",
    input = "say hi"
)
print(*(tp for tp in response.__dict__.items()),sep="\n")
print(response.output_text)
