import discord

intends = discord.Intents.default()
intends.message_content = True
client = discord.Client(intents=intends)

morse_to_alpha = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '-----': '0', '--..--': ',', '.-.-.-': '.', '..--..': '?',
    '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')',
    '.--.-.': '@', '.----.': "'", '-.-.--': '!'
}

alpha_to_morse = {v: k for k, v in morse_to_alpha.items()}


@client.event
async def on_message(message: discord.Message):

    if message.content.startswith("$help"):
        await message.reply("**My commands**\n"
                            "`$frommorse` and `$tomorse`")

    if message.content.startswith("$frommorse"):
        morse = message.content.split(" ", 1)
        if len(morse) < 2:
            if not message.reference:
                return
            morse = ["", (await message.channel.fetch_message(message.reference.message_id)).content]
        morse = morse[1].split("/")
        text = ""
        for mor in morse:
            chars = mor.upper().split(" ")
            for char in chars:
                char = char.strip()
                if char in morse_to_alpha:
                    text += morse_to_alpha[char]
            text += " "
        if text == "":
            await message.reply("no content")
            return
        await message.reply(text)

    if message.content.startswith("$tomorse"):
        morse = message.content.split(" ", 1)
        if len(morse) < 2:
            if not message.reference:
                return
            morse = ["", (await message.channel.fetch_message(message.reference.message_id)).content]
        morse = morse[1].upper().strip()
        text = ""
        for mor in morse:
            if mor == " ":
                text += " / "
            mor = mor.strip()
            if mor in alpha_to_morse:
                text += alpha_to_morse[mor] + " "
        if text == "":
            await message.reply("no content")
            return
        await message.reply(text)


client.run(open('token.txt', mode='r').read())
