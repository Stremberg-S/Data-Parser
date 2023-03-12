import aiofiles as aiofiles
from Path import *


# FILE OPERATIONS
def read_file():
    with open(all_stores, "r") as file:
        return file.read()


async def write_to_file(content):
    async with aiofiles.open(all_stores, "a") as file:
        existing_content = read_file()
        if content not in existing_content or "SCRIPT" in content:
            await file.write(content + "\n")


# OTHER
def discount(old, new):
    x = (old - new) / old * 100
    return round(x, 2)
