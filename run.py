import asyncio
import random
import sys
from typing import Callable, Coroutine, Any

from loguru import logger
from loader import config, semaphore
from core.bot import Bot
from models import Account
from utils import setup
from database import initialize_database


async def run_module_safe(
    account: Account, process_func: Callable[[Bot], Coroutine[Any, Any, Any]]
) -> Any:
    async with semaphore:
        return await process_func(Bot(account))


async def process_farming(bot: Bot) -> None:
    await bot.process_farming()
    await bot.close_session()


async def run_module(accounts, process_func):
    tasks = [run_module_safe(account, process_func) for account in accounts]
    results = await asyncio.gather(*tasks)
    return results


async def run():
    await initialize_database()

    if not config.accounts_to_farm:
        logger.error("No accounts to farm")
        exit(1)

    random.shuffle(config.accounts_to_farm)
    while True:
        await run_module(config.accounts_to_farm, process_farming)

if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    setup()
    asyncio.run(run())
