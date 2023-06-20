import asyncio, json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from EdgeGPT.EdgeUtils import Query, Cookie
from datetime import datetime

cookies = json.loads(open("cookies.json", encoding="utf-8").read())

async def main():

    bot = await Chatbot.create(cookies = cookies)

    while True:

        prompt = input('Write your prompt: ')
        time_prompt = datetime.now().strftime("%H:%M:%S")

        if prompt.lower() != 'exit':

            response = await bot.ask(prompt = prompt, conversation_style = ConversationStyle.creative, simplify_response = True)
            time_response = datetime.now().strftime("%H:%M:%S")
            conversation = f"{time_prompt} Prompt:\n\n{prompt}\n\n{time_response} Response:\n\n{response['text']}\n\n"
            with open("conversation.md", "a", encoding="utf-8") as file: file.write(conversation)

        else: 
            await bot.close()
            break

if __name__ == "__main__":
    asyncio.run(main())
