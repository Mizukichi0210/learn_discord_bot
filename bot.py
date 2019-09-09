import discord
import configparser
import re
import random

client = discord.Client()

# config.ini の読み込み
# Read config.ini
inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')

# 改行コードの設定
# Set separator
SEPARATOR = "\n"

# コードブロックの設定
# Set code blocks on markdown
CODEBLOCKS = '```'

# '!help'コマンドが入力された場合
# If someone entered '!help'.
@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        text = inifile.get('message','help_message_1') + SEPARATOR + inifile.get('message','help_message_2')
        await message.channel.send(text)

# 入退室管理
# Manage Entered and left.
@client.event
async def on_voice_state_update(member, before, after):
    message = ""
    # 発言するチャンネルの指定
    # Set channel id.
    channel = client.get_channel(int(inifile.get('bot_settings','channel_id')))

    try:
        # 入室した場合
        # If someone enterd VOICE CHANNEL.
        if(before.channel is None):
            message = '' + inifile.get('entering_message', str(random.randrange(6)))
            if(member.nick is None):
            message = CODEBLOCKS + message.replace('name', f'{str(member.name)}') + CODEBLOCKS
            else:
                message = CODEBLOCKS + message.replace('name', f'{str(member.nick)}') + CODEBLOCKS

        # 退室した場合
        # If someone left VOICE CHANNEL.
        elif(after.channel is None):
            message = '' + inifile.get('leaving_message', str(random.randrange(5)))
            if(member.nick is None):
                message = CODEBLOCKS + message.replace('name', f'{str(member.name)}') + CODEBLOCKS
            else:
                message = CODEBLOCKS + message.replace('name', f'{str(member.nick)}') + CODEBLOCKS

        await channel.send(message)
        return

    except Exception as e:
        # TODO: 例外の扱いについて考える
        # TODO: How to handle exception output.
        print(e)

# botの接続と起動
# Set token.
client.run(inifile.get('bot_settings','token'))
