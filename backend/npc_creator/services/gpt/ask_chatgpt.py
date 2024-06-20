import json
import logging
import os

import openai
from openai import OpenAI

from npc_creator.operations.return_types import Failure, Success


client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")


def ask_chatgpt_moderated(system_prompt, user_prompts, gpt, use_json=False):
    messages = [{"role": "system", "content": system_prompt}]
    messages += [{"role": "user", "content": prompt} for prompt in user_prompts]

    logging.info(f"GPT Prompt: {messages}")
    result = client.moderations.create(
        input="\n".join(
            user_prompts
            + [
                system_prompt,
            ]
        )
    )
    if result.results[0].flagged:
        logging.info(f"GPT Error: ", result)
        return Failure("input_was_flagged_by_gpt", result)

    kwargs = {}
    if use_json:
        kwargs = {"response_format": {"type": "json_object"}}

    try:
        completion = client.chat.completions.create(
            model=gpt, messages=messages, **kwargs
        )
    except Exception as e:
        logging.info(f"GPT Error: {e}")
        return Failure("gpt_raised_an_error", e)

    content = completion.choices[0].message.content
    logging.info(f"GPT Prompt: {completion}")

    result = client.moderations.create(input="\n".join([system_prompt, content]))
    if result.results[0].flagged:
        logging.info(f"GPT Error: ", result)
        return Failure("npc_was_flagged_by_gpt", result)

    if use_json:
        content = json.loads(content)

    return Success(content)
