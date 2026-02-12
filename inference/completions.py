# Example using AmSC AI endpoints with https://ai.pydantic.dev/
import os

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

api_key = os.environ['AMSCAI_API_KEY']

model = OpenAIChatModel(
    'claude-sonnet-4-5',
    provider=OpenAIProvider(
        base_url='https://api.i2-core.american-science-cloud.org', api_key=api_key
    ),
)

agent = Agent(  
    model,
    instructions='Be concise, reply with one sentence.',  
)

result = agent.run_sync('What is the largest impact, fundamental science challenge that large language models should solve?')
print(result.output)

# can respond with, e.g.
"""The largest fundamental science challenge for large language models should be accelerating scientific discovery itself—developing the ability to generate novel, testable hypotheses across disciplines by reasoning over vast scientific literature and identifying non-obvious connections that human researchers might miss."""
