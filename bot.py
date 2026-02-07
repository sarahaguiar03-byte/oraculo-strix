import os
import random
import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")


# -----------------------------
# Conteúdo do Oráculo
# -----------------------------

BOATOS_ENGRACADOS = [
    "🗞️ **Rubina está de olho em você.** Seu nome estará marcado no *Strixhaven Star* antes do almoço.",
    "🕵️ **Calyx foi pego espionando alunos de outras faculdades.** Detenção por **5 dias**! Dizem que ele tentou argumentar com ‘pesquisa acadêmica’.",
    "☕ O Firejolt Café está servindo um ‘espresso de concentração’. Quem tomou conseguiu decorar um grimório… por 12 minutos.",
    "📚 Alguém deixou um livro ‘auto-organizável’ na Bibliopex. Agora ele organiza *pessoas* também.",
    "🎭 Quentillius foi visto ensaiando um monólogo dramático para pedir… açúcar emprestado.",
    "🧪 Dina jura que não foi ela… mas um dos vasos do campus começou a recitar poesia sobre decomposição.",
    "💠 Zimone foi vista rabiscando equações no ar. As equações… responderam.",
    "✒️ Felisa publicou um verso tão afiado que cortou o silêncio da sala. Literalmente.",
    "🖋️ Grayson aplicou uma ‘crítica construtiva’ tão intensa que a lousa pediu desculpas primeiro.",
]

BOATOS_SOMBRIOS = [
    "🗞️ **Rubina está de olho em você.** Seu nome estará marcado no *Strixhaven Star*… e a tinta parece… fresca demais.",
    "🕯️ A Bibliopex tem uma prateleira que aparece só quando você está cansado. Quem pega um livro lá… sonha com páginas virando sozinhas.",
    "🧪 Dina comentou baixinho: ‘se a planta te responde… não responde de volta’.",
    "💠 Zimone calculou a probabilidade de você estar sendo observado: **alta**. Ela não explicou o porquê.",
    "✒️ Felisa encontrou uma frase perdida num pergaminho antigo… e ela parecia *descrever você*.",
    "🖋️ Grayson anda corrigindo redações que ninguém escreveu. E mesmo assim, ele dá nota.",
    "🎭 Quentillius ensaia no auditório vazio. Às vezes, a plateia aplaude… sem ter ninguém lá.",
]

BOATOS_ROMANTICOS = [
    "💌 Dizem que alguém deixou um bilhete anônimo no seu material. O papel cheira a Firejolt e destino.",
    "✨ Dina comentou que ‘até a natureza torce por certos encontros’. E olhou direto pra você.",
    "🎭 Quentillius foi visto sorrindo enquanto dobrava um papel… como quem guarda um segredo doce.",
    "💠 Zimone afirmou: ‘as variáveis finalmente alinharam’. E você foi a única variável que ela encarou.",
    "✒️ Felisa disse que seu nome ‘combina com rima’. Perigo: ela escreve bem demais.",
    "🖋️ Grayson fez uma observação rara: ‘algumas pessoas merecem finais felizes’. E ficou um segundo a mais olhando.",
]


EVENTOS_ENGRACADOS = [
    "🎲 **Evento:** Um professor abre a porta da sala e diz: ‘Hoje é prova surpresa.’ A turma inteira conjura a mesma expressão: *pânico elegante*.",
    "☕ **Evento:** No Firejolt, sua bebida vem com uma runa no copo. A runa… é um coração. (Ou um aviso. Difícil saber.)",
    "📚 **Evento:** Um livro tenta fugir da Bibliopex correndo em perninhas de papel. Você ganha XP se capturar. Você ganha trauma se perder.",
    "🎭 **Evento:** Quentillius desafia você para um ‘duelo artístico’. A plateia é involuntária. A vergonha também.",
    "🧪 **Evento:** Dina te oferece um ‘tônico revitalizante’. Ele funciona. Só que agora seu cabelo brilha no escuro por 24h.",
    "💠 **Evento:** Zimone pede ajuda com um cálculo. Você entende nada. Mesmo assim, ela diz: ‘perfeito’.",
    "✒️ **Evento:** Felisa lê um poema seu (que você não escreveu) e jura que sentiu sua ‘aura autoral’.",
    "🖋️ **Evento:** Grayson aparece do nada e te dá uma pena: ‘Escreva algo que valha a lembrança’. A pena… pesa como responsabilidade.",
]

EVENTOS_SOMBRIOS = [
    "🕯️ **Evento:** As luzes do corredor piscam e, por um segundo, as sombras formam o símbolo de uma faculdade que você não reconhece.",
    "📜 **Evento:** Um pergaminho cai do seu livro. Você nunca viu aquilo. Está endereçado a você. A caligrafia parece… familiar.",
    "🧪 **Evento:** Dina te alerta: ‘não pisa na linha de sal’. Você olha pro chão e percebe que ela já estava lá.",
    "💠 **Evento:** Zimone sussurra: ‘isso não deveria estar acontecendo’. O relógio do campus atrasa exatamente 13 segundos.",
    "🖋️ **Evento:** Grayson corrige um texto seu antes de você escrever. E a correção faz sentido demais.",
    "✒️ **Evento:** Felisa encontra uma palavra antiga presa no ar. Quando ela pronuncia, a temperatura cai. E alguém ri ao longe.",
    "🎭 **Evento:** Quentillius ensaia uma cena e, no fim, ele não lembra quem escreveu as falas. Só lembra que doeu.",
]

EVENTOS_ROMANTICOS = [
    "🌙 **Evento:** Você encontra um cantinho vazio no campus. De repente, alguém chega com dois cafés. ‘Achei que você ia estar aqui.’",
    "💌 **Evento:** Um bilhete desliza pela sua mesa durante a aula. Só diz: ‘Depois da aula. No Firejolt. Confia.’",
    "✨ **Evento:** Dina te entrega uma flor estranha e diz: ‘Ela desabrocha quando alguém pensa em você’. Ela já está aberta.",
    "🎭 **Evento:** Quentillius encosta ao seu lado e murmura: ‘Não é uma declaração… é um ensaio.’ Mas a voz dele treme.",
    "💠 **Evento:** Zimone te mostra um gráfico. O título é: ‘Probabilidade de eu estar feliz perto de você’. O pico é agora.",
    "✒️ **Evento:** Felisa escreve seu nome num papel e a tinta vira pequenas constelações. ‘Só pra ver se combinava.’",
    "🖋️ **Evento:** Grayson deixa um comentário num texto seu: ‘Continue’. Só isso. E você sente que significa muito.",
]


# Bilhetes: curtinhos, tipo “cartinha de sala de aula”
BILHETES_ENGRACADOS = [
    "📩 *‘Se eu sobreviver a essa aula, te encontro no Firejolt. Se eu não sobreviver, vinga meu nome.’*",
    "📩 *‘Você tá vendo isso? A lousa piscou. Se eu desaparecer, minha mochila é sua.’*",
    "📩 *‘Não olha agora. Tem um professor olhando. Ok, agora olha. Ele ainda tá olhando.’*",
    "📩 *‘Se eu te passar esse bilhete e você rir, eu finjo que foi magia.’*",
    "📩 *‘Dina disse que isso é seguro. Dina também disse que lesmas podem ser pets.’*",
    "📩 *‘Quentillius apostou que você ia sorrir lendo isso. Eu apostei que ia corar.’*",
]

BILHETES_SOMBRIOS = [
    "📩 *‘Não aceita nada que brilhe. Principalmente se chamar seu nome.’*",
    "📩 *‘Tem uma porta no corredor que não estava lá ontem. Se ela aparecer pra você… não entra sozinho.’*",
    "📩 *‘Zimone disse que a chance de dar errado é 1. E hoje o 1 tá muito perto.’*",
    "📩 *‘Grayson escreveu “cuidado” no meu caderno. Eu não lembro dele ter passado por aqui.’*",
    "📩 *‘Felisa achou uma palavra que não deveria existir. Ela tá tentando esquecer.’*",
    "📩 *‘Se alguém te chamar pelo nome completo… finge que não é você.’*",
]

BILHETES_ROMANTICOS = [
    "📩 *‘Se eu fingir que preciso de ajuda pra estudar, você finge que acredita?’*",
    "📩 *‘Encontro no Firejolt depois? Eu prometo não transformar isso num drama… muito.’*",
    "📩 *‘Dina disse que certas flores escolhem certas pessoas. Acho que eu escolhi você.’*",
    "📩 *‘Quentillius chama isso de ensaio, mas eu chamo de coragem.’*",
    "📩 *‘Zimone falou que eu fico estatisticamente mais feliz perto de você. Eu concordo com a ciência.’*",
    "📩 *‘Felisa escreveu meu coração em versos e deixou seu nome no meio.’*",
]


def pick_by_tone(eng, som, rom, tone: str) -> str:
    tone = (tone or "").lower().strip()
    if tone == "engraçado":
        return random.choice(eng)
    if tone == "sombrio":
        return random.choice(som)
    if tone == "romântico" or tone == "romantico":
        return random.choice(rom)
    # aleatório entre todos
    return random.choice(eng + som + rom)


# -----------------------------
# Bot + Slash Commands
# -----------------------------

class OraculoBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        if GUILD_ID:
            guild = discord.Object(id=int(GUILD_ID))
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
            print("✅ Comandos sincronizados no servidor (rápido).")
        else:
            await self.tree.sync()
            print("✅ Comandos sincronizados globalmente (pode demorar um pouco).")


bot = OraculoBot()


@bot.event
async def on_ready():
    print(f"🔮 Oráculo online como {bot.user} (ID: {bot.user.id})")


# Grupo: /oraculo ...
oraculo = app_commands.Group(name="oraculo", description="Oráculo de Strixhaven: boatos, eventos e bilhetes 🔮")
bot.tree.add_command(oraculo)


@oraculo.command(name="boato", description="Receba um boato do Strixhaven Star 🗞️")
@app_commands.describe(tom="Escolha: engraçado / sombrio / romântico (ou deixe vazio para aleatório)")
async def boato(interaction: discord.Interaction, tom: str | None = None):
    msg = pick_by_tone(BOATOS_ENGRACADOS, BOATOS_SOMBRIOS, BOATOS_ROMANTICOS, tom)
    await interaction.response.send_message(msg)


@oraculo.command(name="evento", description="Um mini-evento para movimentar a sessão 🎲")
@app_commands.describe(tom="Escolha: engraçado / sombrio / romântico (ou deixe vazio para aleatório)")
async def evento(interaction: discord.Interaction, tom: str | None = None):
    msg = pick_by_tone(EVENTOS_ENGRACADOS, EVENTOS_SOMBRIOS, EVENTOS_ROMANTICOS, tom)
    await interaction.response.send_message(msg)


@oraculo.command(name="bilhete", description="Um bilhetinho estilo sala de aula ✉️")
@app_commands.describe(tom="Escolha: engraçado / sombrio / romântico (ou deixe vazio para aleatório)")
async def bilhete(interaction: discord.Interaction, tom: str | None = None):
    msg = pick_by_tone(BILHETES_ENGRACADOS, BILHETES_SOMBRIOS, BILHETES_ROMANTICOS, tom)
    await interaction.response.send_message(msg)


if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError("❌ DISCORD_TOKEN não encontrado no .env")
    bot.run(TOKEN)
