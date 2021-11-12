import random, string
import discord
from discord.ext import commands
import asyncio
from captcha.image import ImageCaptcha
from discord.utils import get

intents = discord.Intents().all()

bot = commands.Bot(command_prefix ="!", case_insensitive=True, intents = intents)

@bot.event
async def on_ready():
  print("Bot is ready.")

@bot.command()
async def verify(ctx):
  member = ctx.message.author
  role = discord.utils.get(member.guild.roles, name="Member") //Change the name to your own verified role.
  if role in member.roles:
    await ctx.send("You already have a member role.")
    return
    
   
  //Change this channel id to your own verification channel. You can remove this code if you want it to be accessible everywhere
  verifychannel = 899596792054837278
  
  if ctx.channel.id != verifychannel:
    await ctx.send("You can't use the verify command here, please go to #verify.")
    return
  
  print(ctx.channel.id)

  genword = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

  image = ImageCaptcha(width = 280, height = 90)

  captcha_text = gebword

  data = image.generate(captcha_text)

  image.write(captcha_text,"Captcha.png")

  print(captcha_text)

  file=discord.File("./Captcha.png")
  embed=discord.Embed(title="Verification", description="Please type out the word in this image. **ITS CASE SENSITIVE**")

  await ctx.send(embed=embed, file=file)

  def checkuser(m):
    return m.author.id == ctx.author.id

  try:
    VerifyMessage = await bot.wait_for('message', check=checkuser, timeout=30.0)

    if VerifyMessage.content == captcha_text
      member = ctx.message.author
      role = discord.utils.get(member.guild.roles, name="Member")
      await ctx.send("Great Job! You solved the captcha.")

      await member.add_roles(role)
    else:
        await ctx.send("Invalid captcha answer, Please try again.")
  except asyncio.TimeoutError:
    await ctx.send('You took to long to solve the captcha, please do the command again or dm an online moderator if you cant solve the captcha')

//Change this TOKEN var to your own discord token bot.
bot.run(TOKEN)
