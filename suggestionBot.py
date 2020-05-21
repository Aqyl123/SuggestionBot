import discord
import asyncio

client = discord.Client()
token = 'YOUR TOKEN HERE'

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)

@client.event
async def on_message(message):
	channel = client.get_channel(YOUR CHANNEL ID)

	if message.channel.id == YOUR CHANNEL ID:
		if message.author.bot:
			await message.add_reaction("\u2705")
			await message.add_reaction("\u274C")

		if message.author.bot:
			return

		content = message.content

		await channel.send("**SUGGESTION** by {}\n\n".format(message.author.mention) + "`{}`\n\n".format(content) + "React :white_check_mark: for yes, or :x: for no.")

client.run(token)
