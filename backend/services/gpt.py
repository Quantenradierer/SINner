import logging

import openai
import os



class Gpt:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')

    def ask_gpt(self, prompt):
        logging.info(f'GPT Prompt: {prompt}')
        response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0.7, max_tokens=512)
        logging.info(f'GPT Response: {response}')
        return response['choices'][0]['text']

    def ask_chatgpt(self, prompt):
        logging.info(f'GPT Prompt: {prompt}')
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        logging.info(f'GPT Prompt: {completion}')
        return completion['choices'][0]['message']['content']
