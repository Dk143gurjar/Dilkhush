import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "12138418"))
    API_HASH = os.environ.get("API_HASH", "f7c60f0f506a54d27df6bc32a1bbe785")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5386526071:AAEGHSYlwWIxJnzzVZHY6Jh6_2IHXUMEWnE")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQA_t-EvvjEkPu_61mBM5OS6rPFCrZT1zxHyzPtK3sLP9H6SJTI9DMXfdGHcKaEsUehnnileRi3-RHnWYpuTeZ0De5fa7BzOpHY9JDXhRr-Ufc8USi2itTOtNYmc8E-D4VuCc9rhX5jiTW_T32YrNWl_AYGbIX7N2_gs7Mq3fuU2oIL8SbZZZrIj4S554FHYEhfAhPz5TyBgWqPnq0L2A4jkZu7UM2bujyqZOTZWD2omfgERWQjd8KJ1CvtamVxyEktb-hQRvrnc-Pbsc0loStlaOcVulOzyOdHTMIavasV8AeuB0SRAC9rWuHv0LLevf5SCtuvEUaY67Q-3D10XkGclai1HpAA")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "dkmusic5bot")
    SUPPORT = os.environ.get("SUPPORT", "dk_music1")
    CHANNEL = os.environ.get("CHANNEL", "education_quiz_hub")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1781352356"))
