from Catalog import *
from datetime import datetime
import asyncio
import time

if __name__ == "__main__":
    asyncio.run(write_to_file("\tSCRIPT STARTED.. :)"))
    while True:
        TIMESTAMP = datetime.now().strftime("%d.%m.%Y %H:%M")
        try:
            asyncio.run(write_to_file("\t-- " + TIMESTAMP + " --"))

            # Jimms:
            asyncio.run(get_all_RTX4080())
            asyncio.run(get_all_RTX4090())
            asyncio.run(get_all_Intel_motherboards())
            asyncio.run(get_all_i7_processors())
            asyncio.run(get_all_i9_processors())
            asyncio.run((get_all_DDR5()))

            # Marimekko:
            asyncio.run(get_all_bags())

            time.sleep(600)
            asyncio.run(write_to_file("\n"))
        except KeyboardInterrupt:
            asyncio.run(write_to_file("\tSCRIPT STOPPED.. :("))
            break
