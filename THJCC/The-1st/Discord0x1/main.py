import discord
import json

bot = discord.Bot(intents = discord.Intents.all())
with open("token.json","r") as file:
    token = json.load(file)

@bot.event
async def on_ready():
    print(f">>{bot.user} is ON!!<<")
    bot.add_view(roleView())

#ctf
@bot.slash_command(description="")
async def ls(ctx):
    await ctx.respond(f"""```
{ctx.author.name}@thjcc:~/$ ls
meow.txt woof.txt scint.url flag.txt scaict.url scist.url 5eCR3t_fi1e
```""",ephemeral=True)
    

@bot.slash_command(description="")
async def cat(ctx,file:str):
    if file == "flag.txt":
        await ctx.respond(":b: :three: :regional_indicator_r: :exclamation: :regional_indicator_j: :zero: :one: :regional_indicator_n:(2/3) ",ephemeral=True)
    elif file == "5eCR3t_fi1e":
        await ctx.respond("請專心解題目！！https://youtu.be/0GzLgn2fgcI?si=OaS3euomCrluowP5",ephemeral=True)
    elif file == "meow.txt":
        await ctx.respond(f"""```
{ctx.author.name}@thjcc:~/$ cat meow.txt
      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)   
```""",ephemeral=True)
        
    elif file == "woof.txt":
        await ctx.respond(f"""```
{ctx.author.name}@thjcc:~/$ cat woof.txt
   / \__
  (    @\___
  /         O wooof!
 /   (_____/
/_____/
```""",ephemeral=True)
    elif file == "scint.url":
        await ctx.respond(f"""```
{ctx.author.name}@thjcc:~/$ cat scint.url
https://scint.org/
```""",ephemeral=True)
    elif file == "scaict.url":
        await ctx.respond(f"""```
{ctx.author.name}@thjcc:~/$ cat scaict.url
https://scaict.org/
```""",ephemeral=True)   
    elif file == "scist.url":
        await ctx.respond(f"""```
{ctx.author.name}@thjcc:~/$ cat scist.url
https://scist.org/
```""",ephemeral=True)
        
    else:
        await ctx.respond(f"""```
{ctx.author.name}@thjcc:~/$ cat {file}
cat: {file}: No such file or directory
```""",ephemeral=True)



bot.run(token["token"])
