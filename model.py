import ollama
file_path = 'transcript.txt'
with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
response=ollama.chat(model='llama3',messages=[
    {
        'role':'user',
        'content':f'{content},Summarize this text and give me description of it without losing topics in the provided text.'
    },
])
print(response['message']['content'])