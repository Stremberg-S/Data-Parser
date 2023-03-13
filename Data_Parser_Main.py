from Catalog import *
from datetime import datetime
import asyncio

if __name__ == "__main__":
    while True:
        TIMESTAMP = datetime.now().strftime("%d.%m.%Y %H:%M")

        # Jimms:
        try:
            asyncio.run(write_to_file(jimms, "\t-- " + TIMESTAMP + " --"))

            asyncio.run(get_all_RTX4080())
            asyncio.run(get_all_RTX4090())
            asyncio.run(get_all_Intel_motherboards())
            asyncio.run(get_all_i7_processors())
            asyncio.run(get_all_i9_processors())
            asyncio.run((get_all_DDR5()))
        except KeyboardInterrupt:
            asyncio.run(write_to_file(jimms, "\tSCRIPT STOPPED.. :("))
            break

        # Marimekko:
        try:
            asyncio.run(write_to_file(marimekko, "\t-- " + TIMESTAMP + " --"))

            asyncio.run(get_all_bags())
        except KeyboardInterrupt:
            asyncio.run(write_to_file(marimekko, "\tSCRIPT STOPPED.. :("))
            break

        try:
            asyncio.run(sleep_for_10_minutes())
        except KeyboardInterrupt:
            break
