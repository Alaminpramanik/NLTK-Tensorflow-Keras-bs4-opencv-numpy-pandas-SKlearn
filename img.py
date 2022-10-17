from PIL import Image 
from io import BytesIO

@client.command()
async def wanted(ctx, user:discord.Member = None):
    if user:
        user=ctx.author
    wanted=image.open("https://instagram.fdac116-1.fna.fbcdn.net/v/t51.2885-19/103280599_561183587922801_1306027535501666726_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fdac116-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=yfsIcKEZRSAAX_bUuXZ&tn=AlQ0ngmckKNpnxVs&edm=AEF8tYYBAAAA&ccb=7-5&oh=00_AT_bcJn48ZjhrLHE4690q_Mj1B3kGEKSRN5rkR0Pr-sv7A&oe=633C0B1F&_nc_sid=a9513d")
    asset= ctx.author.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = image.open(data)