# 
# https://docs.python-telegram-bot.org/en/v21.0.1/index.html
# 
# 1. Uzinstalē bibliotēku
# > pip3 install python-telegram-bot
# 
# 2. Uztaisi jaunu Telegram botu un saņem "token" - https://core.telegram.org/bots/features#creating-a-new-bot
#
# 3. Samaini kodā YOUR_TOKEN ar savu token
# 
# 4. Palaid kodu un ieraksti čatā /start
# 
# 5. Apskaties citas komandas - /hello un /echo
#
# 6. Izmantojot kodu no iepriekšēja piemēra (1_faker.py), izveido jaunu komandu /fakeperson, kura uzģenerē personas vārdu, uzvārdu ar telefona numuru, adresi un personas kodu
# 
# 7. Izmantojot kodu no iepriekšēja piemēra (2_chuck_norris.py), izveido jaunu komandu /chuck, kura uzģenerē jaunu joku par programmetājiem

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from faker import Faker
import requests
fake = Faker()

# izveido bota pieslēgumu Telegram
app = ApplicationBuilder().token("6691028918:AAH3jpjCFissGPDD8C2mFXyxRHSZjt4p95M").build()

# komanda /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm test bot. Type /hello or /echo")

# komanda /hello
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")

# komanda /echo
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("I hear: " + update.message.text)

async def faker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(fake.name() + fake.address() + fake.phone_number() + fake.ssn())

async def chuck(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    r = requests.get('https://api.chucknorris.io/jokes/random?category=dev')
    R = r.json()
    await update.message.reply_text("\n" + R["value"])

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_photo("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivnHQJRh38vYp6EsJ9GN_SIBw0TpEwYDbuGirJBIOVKS_7j9j6LpzCWJs5cwliqV8pUQknknzkt0VscAr3mcGpQhJ4YxYLgd2q8YhgzBcYWryq8zDaQ3Bp1LVjaUxy2fD3Pjkeok4oLtQ/s1600/catblog1.jpg")

# savieno čata komandu ar funkciju
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("echo", echo))
app.add_handler(CommandHandler("faker", faker))
app.add_handler(CommandHandler("chuck", chuck))
app.add_handler(CommandHandler("test", test))


# sāk bota darbību
app.run_polling()