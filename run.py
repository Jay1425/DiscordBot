from threading import Thread
from web import run_flask
from bot import run_bot

# Run Flask in a separate thread
flask_thread = Thread(target=run_flask)
flask_thread.start()

# Run the Discord bot (main thread)
run_bot()
