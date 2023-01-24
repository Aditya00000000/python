import discord
import chat_bot

async def send_message(message,user_message,is_private):
    try:
        responses  = chat_bot.responses(user_messages)
        await responses.author.send(responses) if is_private else await responses.author.send(responses)
    expect: Exception as  e:
        print(e)