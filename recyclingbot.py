import os, sys, time, asyncio, winshell, discord, json, requests
bot = discord.Client()
try:
    config = json.loads((open('config.cfg','r')).read())
except:
    print('Config missing or damaged, entering first-time setup.')
    config = {}
    config['token'] = input('Please paste your bot token here: ')
    config['guild'] = input('Please paste your chosen guild ID here: ')
    (open('config.cfg','w')).write(json.dumps(config))
def rbinexec():
    rbin = winshell.recycle_bin()
    rcontents = []
    for x in rbin:
        y=(x.original_filename()).rsplit("\\")
        rcontents.append(y[len(y)-1])
    rlen = len(rcontents)
    while True:
        rcontentsnew = []
        for x in rbin:
            y=(x.original_filename()).rsplit("\\")
            rcontentsnew.append(y[len(y)-1])
        if len(rcontentsnew) > rlen:
            print("file added!")
            for x in rcontentsnew:
                if x not in rcontents:
                    print(x)
                    if (x.startswith("a_") and len(x) == 34) or (len(x) == 32):
                        print("Is discord image!")
                        configa = json.loads((open('config.cfg','r')).read())
                        if x in configa['pfpdata']:
                            r = requests.put('https://discord.com/api/v7/guilds/'+str(config['guild'])+'/bans/'+((configa['pfpdata'])[x]),headers = {'Authorization':'Bot '+str(config['token'])})
                            r.raise_for_status()
            rcontents = rcontentsnew
        rlen = len(rcontentsnew)
        time.sleep(1)
@bot.event
async def on_ready():
    print("Connected to Discord, fetching guild users...")
    config['pfpdata'] = {}
    g = await bot.fetch_guild(int(config['guild']))
    mbs = await g.query_members(query="",limit=1000)
    for m in mbs:
        if m.avatar:
            (config['pfpdata'])[m.avatar] = str(m.id)
    (open('config.cfg','w')).write(json.dumps(config))
    print("Done!")
    await bot.loop.run_in_executor(None, rbinexec)
bot.run(config['token'])