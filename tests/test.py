from cognxcore import CogniCore


api_key = input("Enter your API key: ")
ai = CogniCore(api_key)

prompt = input("Enter your prompt: ")
response = ai.generate_content(prompt)
print(response)
