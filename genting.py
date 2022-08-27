#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
# A Powerful Music Bot Property Of Dk music group

# Kanged By © @Dk143gurjar
# Rocks © @Dk_music_Shayri
# Owner Dilkhush 
# Dk gurjar
# All rights reserved. Yukki


import asyncio

from pyrogram import Client as c

API_ID = input("\nEnter Your API_ID:\n > ")
API_HASH = input("\nEnter Your API_HASH:\n > ")

print("\n\n Enter Phone number when asked.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    print("\nHERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n")
    print(f"\n{ss}\n")


asyncio.run(main())
