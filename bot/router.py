# bot/router.py
def register_all_handlers(dp):
    from bot.handlers import start, info, news, feedback, admin
    start.register_handlers(dp)
    info.register_handlers(dp)
    news.register_handlers(dp)
    feedback.register_handlers(dp)
    admin.register_handlers(dp)
