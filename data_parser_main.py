import asyncio
from datetime import datetime

from Catalog.Jimms.graphic_cards import get_all_RTX4080, get_all_RTX4090
from Catalog.Jimms.monitors import get_all_monitors
from Catalog.Jimms.motherboards import get_all_Intel_motherboards
from Catalog.Jimms.processors import (get_all_i7_processors,
                                      get_all_i9_processors)
from Catalog.Jimms.ram import get_all_DDR5
from Catalog.Marimekko.bags import get_all_bags
from data_parser_utils import sleep_for_10_minutes, write_to_file
from path import JIMMS, MARIMEKKO


async def run_jimms_tasks():
    """
    Runs a series of asynchronous tasks to gather information from
        various sources.

    """
    await asyncio.gather(
        get_all_RTX4080(),
        get_all_RTX4090(),
        get_all_Intel_motherboards(),
        get_all_i7_processors(),
        get_all_i9_processors(),
        get_all_DDR5(),
        get_all_monitors()
    )


async def run_marimekko_tasks():
    """
    Runs a series of asynchronous tasks to gather information from
        various sources.

    """
    await asyncio.gather(
        get_all_bags()
    )


async def main():
    """
    Main entry point for running the script that performs periodic tasks.

    """
    while True:
        timestamp = datetime.now().strftime("%d.%m.%Y %H:%M")

        try:
            await write_to_file(JIMMS, f"\t-- {timestamp} --")
            await run_jimms_tasks()

            await write_to_file(MARIMEKKO, f"\t-- {timestamp} --")
            await run_marimekko_tasks()

            await sleep_for_10_minutes()

        except KeyboardInterrupt:
            await write_to_file(MARIMEKKO, "\tSCRIPT STOPPED.. :(")
            break


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
