# RecyclingBot

## A simple Discord.py bot for banning users in a cool way

Ever wanted to get rid of a problem user in a really satisfying way?
Ever wanted to meme banning someone for the nth time?
Ever wanted to just add more visual power to yeeting someone off your server?

This is the script for you!

## Dependencies
- [discord.py](https://discordpy.readthedocs.io/en/latest/api.html)
- [pywin32](https://pypi.org/project/pywin32/)
- [winshell](https://github.com/tjguk/winshell)

## How to use

1. First, you'll need to make a bot application for Discord, you can do that [here](https://discord.com/developers/applications)
2. Secondly, inivte the bot to your desired guild with ban permissions (don't forget to hoist the bot above members you want bannable)
3. Next, put `recyclingbot.py` in a folder somewhere.
4. Then, run `recyclingbot.py` and a first-time setup will begin
5. After that, Paste your bot's token and the guild you wish to operate on when prompted (This bot can only work in one guild at a time)
6. Penultiamtely, the bot will run. You won't need to re-do this setup when you run the bot in future, and you can update vars in the new `config.cfg` file made.
7. Finally, drag the profile picture of the person you want to ban from your selected guild to the desktop, then to your recycling bin.

And then you can watch as the magic happens!

### Bugs/limitations

- Right now, the bot will only work on the first 1000 users in a guild
- It won't update when users join or edit their profile pic
- It doesn't work on default profile pics
- It may not work if the users profile pic is already in the recycling bin
- It can only ban members of the configured guild

Many of these limitations are insurmountable and unavoidable as this, really isn't something you're supposed to do with a Discord bot and the Discord API doesn't really account for this use case.
