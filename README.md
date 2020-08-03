# RecyclingBot

## A simple bot written in discord.py for banning users in a cool and memey way

Ever wanted to get rid of a problem user in a really satisfying way?
Ever wanted to meme banning someone for the nth time?
Ever wanted to just add more visual power to yeeting someone off your server?

Then this is the bot for you!

## Dependencies
- [discord.py](https://discordpy.readthedocs.io/en/latest/api.html)
- [pywin32](https://pypi.org/project/pywin32/)
- [winshell](https://github.com/tjguk/winshell)

## Guide

1. First of all, you'll need to have a Discord Bot Application, you can get that [here](https://discord.com/developers/applications)
2. Secondly, invite the bot to your desired guild with ban permissions (don't forget to hoist the bot above members you want bannable)
  Link: https://discord.com/oauth2/authorize?client_id=CLIENT_ID_HERE&scope=bot&permissions=4 (remember to replace `CLIENT_ID_HERE`) with the bot's client id
3. Then, run `recyclingbot.py` and a first-time setup will begin
4. Next, Paste your bot's token and the guild you wish to operate on when prompted (This bot can only work in one guild at a time)
5. After that, the bot will start up. You won't need to re-do this setup when you run the bot in future, and you can update variables in the new `config.cfg` file.
6. Finally, drag the profile picture of the user you want to ban from the guild you entered earlier to your recycling bin.

And then watch as the magic happens!

### Bugs/limitations

- Right now, the bot will only work on the first 1000 users in a guild
- It doesn't work on default profile pics
- It may not work if the users profile pic is already in the recycling bin
- It can only ban members of the configured guild

Many of these limitations are insurmountable and unavoidable as, this isn't really something you're supposed to do with a Discord Bot and the Discord API doesn't really account for this use case.
