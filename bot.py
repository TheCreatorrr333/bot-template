from imports import *

bot = lb.BotApp(
  token=tcr.get_token(),
  intents=hikari.Intents.ALL,
)



@bot.command
@lb.command('name', 'description')
@lb.implements(lb.SlashCommand)
async def cmd_botstatus(ctx: lb.SlashContext):
  await ctx.respond('UwU')






bot.run()
