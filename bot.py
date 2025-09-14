import discord
from discord.ext import commands
from discord.ui import View, Button, Modal, TextInput

# Configurações
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# IDs fixos (altere pelos do seu servidor)
GUILD_ID = 1412843906156204076  # ID do servidor
CATEGORY_TICKETS = None  # se tiver uma categoria específica, coloque o ID aqui
ROLE_MM = None  # coloque o ID do cargo Middleman

# Evento inicial
@bot.event
async def on_ready():
    print(f"🤖 Bot conectado como {bot.user}")

# Comando para abrir ticket
@bot.command()
async def ticket(ctx):
    modal = PixValueModal()
    await ctx.send("📩 Para abrir um ticket, primeiro informe o valor do Pix.", view=None)
    await ctx.send_modal(modal)


# Modal para capturar valor do Pix
class PixValueModal(Modal, title="Abrir Ticket"):
    pix_value = TextInput(label="Valor do Pix", placeholder="Ex: 50.00", required=True)

    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild
        category = guild.get_channel(CATEGORY_TICKETS) if CATEGORY_TICKETS else None

        # Cria o canal de ticket
        ticket_channel = await guild.create_text_channel(
            name=f"ticket-{interaction.user.name}",
            category=category,
            overwrites={
                guild.default_role: discord.PermissionOverwrite(view_channel=False),
                interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True),
            },
        )

        await ticket_channel.send(
            f"🎫 Ticket criado por {interaction.user.mention}\n💸 Valor Pix informado: **R${self.pix_value.value}**",
            view=ClaimView()
        )

        await interaction.response.send_message(
            f"✅ Ticket criado com sucesso: {ticket_channel.mention}", ephemeral=True
        )


# Botão para MM reivindicar
class ClaimView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(ClaimButton())


class ClaimButton(Button):
    def __init__(self):
        super().__init__(label="🎯 Reivindicar", style=discord.ButtonStyle.primary)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"⚡ {interaction.user.mention} reivindicou este ticket!",
            allowed_mentions=discord.AllowedMentions(users=True)
        )


# Rodar bot
bot.run("SEU_TOKEN_AQUI")
