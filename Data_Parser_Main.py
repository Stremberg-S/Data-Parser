from datetime import datetime

from Catalog import *

if __name__ == "__main__":
    while True:
        TIMESTAMP = datetime.now().strftime("%d.%m.%Y %H:%M")

        # Jimms:
        try:
            asyncio.run(write_to_file(JIMMS, "\t-- " + TIMESTAMP + " --"))

            asyncio.run(get_all_RTX4080())
            asyncio.run(get_all_RTX4090())
            asyncio.run(get_all_Intel_motherboards())
            asyncio.run(get_all_i7_processors())
            asyncio.run(get_all_i9_processors())
            asyncio.run(get_all_DDR5())
            asyncio.run(get_all_monitors())
        except KeyboardInterrupt:
            asyncio.run(write_to_file(JIMMS, "\tSCRIPT STOPPED.. :("))
            break

        # Marimekko:
        try:
            asyncio.run(write_to_file(MARIMEKKO, "\t-- " + TIMESTAMP + " --"))

            asyncio.run(get_all_bags())
        except KeyboardInterrupt:
            asyncio.run(write_to_file(MARIMEKKO, "\tSCRIPT STOPPED.. :("))
            break

        try:
            asyncio.run(sleep_for_10_minutes())
        except KeyboardInterrupt:
            break
