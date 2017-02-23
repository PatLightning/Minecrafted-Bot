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

    if message.content.startswith('How many wood planks are in a wood block?'):
        Ugly = await client.send_message(message.channel, '3 wood planks')
        await asyncio.sleep(6)
        await client.edit_message(Ugly, '4 wood planks')


    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

@client.event
async def on_member_join(member):
    await client.send_message(member.server, 'Hello Minecrafter {}'.format(member.name))


@client.event
async def on_message_edit(before, after):
    await client.send_message(before.channel,'{} Changed a Mistake.'.format(before.author.name))



client.run('Mjg0MTk2NzQxNjU2MzQ2NjI0.C5AIfw.n2ElstrFkJmhI24FYG-KOwXdDU0')
