import sys
import traceback
from aiohttp import web
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity
from weatherbot import WeatherBot
from config import DefaultConfig

APP_ID = ""      # Leave blank unless using Bot Channels Registration
APP_PASSWORD = ""

SETTINGS = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
ADAPTER = BotFrameworkAdapter(SETTINGS)
BOT = WeatherBot()

async def messages(req):
    body = await req.json()
    activity = Activity().deserialize(body)
    auth_header = req.headers.get('Authorization', '')
    response = await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)
    if response:
        return web.json_response(data=response.body, status=response.status)
    return web.Response(status=201)

APP = web.Application()
APP.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    try:
        web.run_app(APP, host="0.0.0.0", port=3978)
    except Exception as error:
        raise error
