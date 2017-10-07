import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for msg in client.logs_from(message.channel, limit=100):
            if msg.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    if message.content.startswith('How much of a minecrafter is Jarrod?'):
        Ugly = await client.send_message(message.channel, 'Not at all')
        await asyncio.sleep(10)
        await client.edit_message(Ugly, 'A huge minecrafter')


    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

@client.event
async def on_member_join(member):
    await client.send_message(member.server, 'Hello Minecrafter {}'.format(member.name))


@client.event
async def on_message_edit(before, after):
    if before.author.bot:
        return
    await client.send_message(before.channel,'{} Fucked up.'.format(before.author.name))

@client.event
async def on_reaction_remove(reaction, user):
    await client.send_message(reaction.message.channel,'uh oh {} '.format(user.name))







client.run('token')
