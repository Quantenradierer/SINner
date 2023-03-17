import logging
import openai


def ask_chatgpt(prompt):
    logging.info(f'GPT Prompt: {prompt}')

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
    except Exception as e:
        logging.info(f'GPT Error: {e}')
        return None

    logging.info(f'GPT Prompt: {completion}')
    return completion['choices'][0]['message']['content']