# Trivia Bot
This is a Discord bot that gives trivia questions, with a leaderboard!

## Development
Clone the repository using `git clone`.

Run:
```
pip install -r requirements.txt
```

You need to also set up a redis database which can be done using Docker and Docker Compose:
```
docker-compose up -d
```

Make an environment file called `.env` with token `DISCORD_TOKEN`:
```
DISCORD_TOKEN="enter your discord token here"
```

Then, run the python program:
```
python3 main.py
```

## Tools
This program uses:

* Discord.py - Interfacing with Discord and creating a Discord Bot
* Redis - Leaderboard system
