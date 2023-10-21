import json
import logging
from datetime import datetime

import openai

from npc_creator.operations.return_types import Failure, Success


def ask_chatgpt_moderated(system_prompt, user_prompts, gpt='gpt-4'):
    messages = [{'role': 'system', 'content': system_prompt}]
    messages += [{'role': "user", 'content': prompt} for prompt in user_prompts]

    logging.info(f'GPT Prompt: {messages}')
    result = openai.Moderation.create(input='\n'.join(user_prompts))
    if result['results'][0]['flagged']:
        return Failure('input_was_flagged_by_gpt')

    try:
        completion = openai.ChatCompletion.create(
            model=gpt,
            messages=messages
        )
    except Exception as e:
        logging.info(f'GPT Error: {e}')
        return Failure('gpt_raised_an_error')

    content = completion['choices'][0]['message']['content']
    logging.info(f'GPT Prompt: {completion}')

    result = openai.Moderation.create(input=content)
    if result['results'][0]['flagged']:
        return Failure('npc_was_flagged_by_gpt')

    return Success(content)
