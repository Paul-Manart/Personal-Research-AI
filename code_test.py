import asyncio, json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from EdgeGPT.EdgeUtils import Query, Cookie

cookies = json.loads(open("bing_cookies_e.json", encoding="utf-8").read())  # might omit cookies option

async def main():
    bot = await Chatbot.create() # Passing cookies is "optional", as explained above

    prompt = input('Write your prompt: ')
    response = await bot.ask(prompt=prompt, conversation_style=ConversationStyle.creative, simplify_response=True)

    # Save the text as Markdown
    with open("output.md", "w", encoding="utf-8") as file:
        file.write(response['text'])

    # print(f'{10-i} messages left.\n')
    print(json.dumps(response['text'], indent=2)) # Returns
    
    await bot.close()

if __name__ == "__main__":
    asyncio.run(main())
