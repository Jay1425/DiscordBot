🤖 Discord Bot – Built by Jay Raychura
A powerful and customizable Discord bot developed using discord.py and Flask. This bot can handle server moderation, respond to commands, send automated replies, and includes a Flask web dashboard for real-time control.

🚀 Features
Slash Commands and Message Commands

Auto Responses

Moderation Tools (kick, ban, purge)

Fun Commands (jokes, memes, etc.)

Flask-based Web Dashboard

Easy to customize and expand

⚙️ Tech Stack
Python 3.11+

discord.py

Flask

Jinja2, HTML, Tailwind CSS

🔧 Setup Instructions
Clone the Repository:

git clone https://github.com/Jay1425/DiscordBot.git
cd DiscordBot
Create Virtual Environment:

python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
Install Requirements:

pip install -r requirements.txt
Create a .env File with the Following:

DISCORD_TOKEN=your_discord_bot_token
GUILD_ID=your_guild_id
FLASK_SECRET_KEY=your_flask_secret

Run the Bot and Flask Dashboard:

# In one terminal
python bot.py

# In another terminal
python app.py
```bash
DiscordBot/
│
├── bot.py                # Main Discord bot
├── app.py                # Flask dashboard
├── templates/            # HTML templates
├── static/               # CSS/JS (Tailwind)
├── .env                  # Environment config
├── requirements.txt      # Python packages
└── README.md             # Project info
```

👨‍💻 Made By
Jay Raychura
Email: jayraychura13@gmail.com
GitHub: https://github.com/Jay1425
Discord: @jayraychura

📄 License
MIT License – Free to use and modify.

🌟 Star This Repo
If this project helped you, give it a ⭐ on GitHub!