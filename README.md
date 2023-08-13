# Trivia Bot
This is a Discord bot that gives trivia questions, with a leaderboard!

## Running the Bot
Clone the repository using `git clone`.

Run:
```
pip install -r requirements.txt
```

Go to Upstash (https://upstash.com/) and create a new Redis database.

Make an environment file called `.env` in the following format:
```
DISCORD_TOKEN="enter token for discord bot"
DB_URL="enter upstash db url"
DB_PORT="enter upstash db port"
DB_PASSWORD="enter upstash db password"
```

Then run:
```
python main.py
```

Note: the token for the discord bot can be recieved through the Discord developer portal!

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
python main.py
```

## Tools
This program uses:

* Discord.py - Interfacing with Discord and creating a Discord Bot
* Redis - Leaderboard system
* Upstash - Serverless redis database
