import discord
from dotenv import load_dotenv
import os
import openai


load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

token = os.getenv("TOKEN")

chat =""

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global chat
        chat += f"{message.author}: {message.content}"
        print(f'Message from {message.author}: {message.content}')

        if self.user != message.author:
            if self.user in message.mentions:
                print(chat)

                await message.channel.typing()
                channel = message.channel
                print("in open")
                response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            # {"role": "system", "content": "You are a sarcastic chat bot which replies with 'Moye Moyeeee' on every chats and also greets user with moye moyeeeeee....!!!. '\n' If users asks to complete any code you should sarcastically insult the user about the questions he asks. '\n' also include dark humor when any user ask any simple question to you and give some good slang reply if he asks you complex question"},
                            {"role": "system", "content": "You are a helpful assistant. To Answer Questions asked by user"},
                            # {"role": "user", "content": message.content}
                            {"role": "user", "content": message.content}
                            # {
                            # "role" : "assistant",
                            # "content": message.content  
                            # }
                        ],
                        temperature=1,
                        max_tokens=300,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                messageToSend = response.choices[0]['message']['content']
                print("messgaeto send",messageToSend)
                await channel.send(messageToSend)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
