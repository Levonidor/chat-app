from bot.bot.services.handlers import (
    MemoryStorage,
    router,
    Dispatcher,
    Bot,
    logging,
    asyncio,
)
from bot.bot.utils import get_token


BOT_TOKEN = get_token()


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
