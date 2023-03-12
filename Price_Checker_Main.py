from Catalog.Graphic_Cards import *
from Catalog.Motherboards import *
from Catalog.Processors import *
from Catalog.RAM import *
from datetime import datetime
import asyncio
import time

if __name__ == "__main__":
    asyncio.run(write_to_file("\tSCRIPT STARTED.. :)"))
    while True:
        TIMESTAMP = datetime.now().strftime("%d.%m.%Y %H:%M")
        try:
            asyncio.run(write_to_file("\t-- " + TIMESTAMP + " --"))
            # RTX 4080:
            asyncio.run(get_all_RTX4080())
            # RTX 4090:
            asyncio.run(get_all_RTX4090())
            # Motherboards:
            asyncio.run(get_all_Intel_motherboards())
            # i7:
            asyncio.run(get_all_i7_processors())
            # i9:
            asyncio.run(get_all_i9_processors())
            # DDR5:
            asyncio.run((get_all_DDR5()))

            time.sleep(600)
            asyncio.run(write_to_file("\n"))
        except KeyboardInterrupt:
            asyncio.run(write_to_file("\tSCRIPT STOPPED.. :("))
            break
