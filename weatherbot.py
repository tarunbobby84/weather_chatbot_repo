from botbuilder.core import ActivityHandler, TurnContext
import openai
from config import DefaultConfig

def get_weather_from_openai(user_input):
    openai.api_type = "azure"
    openai.api_base = DefaultConfig.OPENAI_ENDPOINT
    openai.api_version = DefaultConfig.OPENAI_API_VERSION
    openai.api_key = DefaultConfig.OPENAI_KEY

    prompt = (
        "You are a weather assistant. Only answer about weather for US states. "
        "If asked about a city or outside the US, say 'Sorry, I can only provide weather for US states.'"
    )
    response = openai.ChatCompletion.create(
        engine=DefaultConfig.OPENAI_ENGINE,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ],
        max_tokens=100
    )
    return response['choices'][0]['message']['content']

class WeatherBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        user_input = turn_context.activity.text
        reply = get_weather_from_openai(user_input)
        await turn_context.send_activity(reply)
