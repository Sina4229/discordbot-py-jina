from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

import discord, asyncio, pytz, datetime
from discord.ext import commands
import os

def main():
    prefix = '!'
    intents = discord.Intents.all()

    client = commands.Bot(command_prefix=prefix, intents = intents, help_command=None)

    @client.event
    async def on_ready(): # 봇이 실행되면 한 번 실행됨
        print("로그인 성공")
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Bot Made by. Sina#4229"))

    @client.event
    async def on_member_join(member):
        channel = client.get_channel(1076216516330127501)
        channel2 = client.get_channel(1076202522190033036)
        user = member.name
        embed = discord.Embed(title="입장로그", description= " ",timestamp=datetime.datetime.now(pytz.timezone('UTC')),color=0x00ff00)
        embed.add_field(name=" ", value=""".      /)⋈/) 
\n  (｡•ㅅ•｡)♡ 
┏--∪-∪━━━━━━━━━━━━━━━━━━┓ 
┊ ┊ ┊ ┊  ┊ 　　.　　　 *.    . ..  
┊ ┊ ┊ ┊                                         ┊ 
┊ ┊ ✫ ˚♡ ⋆｡ ❀  . .          .  . 
┊ ☪︎⋆ ⊹        .            .              . 
┊ . ˚      진아티콘  . . \n✧  ㅣ서버에 오신 것을 환영합니다. 
\n            .           .             . .           . .        . 
      ㅣ{} 님 서버에 입장하셨습니다. .  
 
1    ┊규칙 채널에서 먼저   
     규칙 내용을 읽어주신 뒤 , 
2    ┊{} 채널에서 인증  
     완료를 해주세요. 
\n      ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ""".format(user, channel2.mention))
        embed.set_footer(text="Bot Made by. Sina#4229")
        await channel.send(embed=embed)

    @client.event
    async def on_message(message):
        if message.content.startswith ("!인증 "):
            if message.author.guild_permissions.administrator:
                await message.channel.send(embed=discord.Embed(title="인증 시스템", description = "인증이 정상적으로 완료 되었습니다 !",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color = 0xff0000))

                user = message.mentions[0]

                embed = discord.Embed(title="인증 시스템", description="인증이 정상적으로 완료 되었습니다 !",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
                embed.add_field(name="인증 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
                embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
                embed.set_footer(text="Bot Made by. Sina#4229")
                await user.send (embed=embed)
                await message.author.send (embed=embed)
                role = discord.utils.get(message.guild.roles, name = '𝗡𝗲𝘁𝗶𝘇𝗲𝗻')
                await user.add_roles(role)

            else:
                await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0xff0000))
        
        elif message.content.startswith ("!청소 "):
            if message.author.guild_permissions.administrator:
                amount = message.content[4:]
                await message.delete()
                await message.channel.purge(limit=int(amount))

                embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
                embed.set_footer(text="Bot Made by. Sina#4229", icon_url="https://discordapp.com/channels/691615852620939274/703908401381376000/711859989177958410")
                await message.channel.send(embed=embed)
        
            else:
                await message.delete()
                await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))

        elif message.content.startswith ("!공지 "):
            await message.delete()
            if message.author.guild_permissions.administrator:
                notice = message.content[4:]
                channel = client.get_channel(1071265290807169085)
                embed = discord.Embed(title="지나티콘 공지", description="공지사항 내용은 항상 숙지 해주시기 바랍니다\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by.  Sina #4229 | 담당 관리자 : {}".format(message.author), icon_url="https://ibb.co/MhkJQ2b")
                embed.set_thumbnail(url="https://ibb.co/MhkJQ2b")
                await channel.send("@everyone", embed=embed)
                await message.author.send("**[ BOT 자동 알림 ]** | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
            else:
                await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

        elif message.content.startswith ("!kick "):
            if message.author.guild_permissions.administrator:
                member = message.guild.get_member(int(message.content.split(" ")[1]))
                await message.guild.kick(member, reason=' '.join(message.content.split(" ")[2:]))
            else:
                await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))
                
    client.run(TOKEN)

if __name__ == '__main__':
    main()

except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
