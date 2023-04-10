import json
import logging

import openai

from npc_creator.operations.return_types import Failure, Success


def ask_chatgpt(system_prompt, user_prompts):
    messages = [{'role': 'system', 'content': system_prompt}]
    messages += [{'role': "user", 'content': prompt} for prompt in user_prompts]

    logging.info(f'GPT Prompt: {messages}')
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
    except Exception as e:
        logging.info(f'GPT Error: {e}')
        return None

    logging.info(f'GPT Prompt: {completion}')
    return completion['choices'][0]['message']['content']


def ask_chatgpt_moderated(system_prompt, user_prompts):
    formatted_prompts = []
    for prompt in user_prompts:
        if type(prompt) is not str:
            prompt = '\n'.join([f'{key}: {value}' for key, value in prompt.items()])
        formatted_prompts.append(prompt)

    messages = [{'role': 'system', 'content': system_prompt}]
    messages += [{'role': "user", 'content': prompt} for prompt in formatted_prompts]

    logging.info(f'GPT Prompt: {messages}')
    if openai.Moderation.create(input='\n'.join(formatted_prompts))['results'][0]['flagged']:
        return Failure('input_was_flagged_by_gpt')

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
    except Exception as e:
        logging.info(f'GPT Error: {e}')
        return Failure('gpt_raised_an_error')

    content = completion['choices'][0]['message']['content']
    logging.info(f'GPT Prompt: {completion}')
    if openai.Moderation.create(input=content)['results'][0]['flagged']:
        return Failure('npc_was_flagged_by_gpt')
    return Success(content)
