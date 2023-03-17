import logging
import openai


def ask_gpt(prompt):
    logging.info(f'GPT Prompt: {prompt}')
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0.7, max_tokens=512)
    logging.info(f'GPT Response: {response}')
    return response['choices'][0]['text']
