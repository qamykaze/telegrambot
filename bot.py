import telebot

bot = telebot.TeleBot("1319930270:AAELlfB3meE5E4MmWowZ0A7Su4YVXywMhfc")

#Comandos que responden mensajes simples
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['kali'])
def send_welcome(message):
    bot.reply_to(message, '''
            You are a beginner. I don't care that you've been using Ubuntu for two months or shit like that, you're a beginner. If you weren't a beginner, someone wouldn't have sent you this, so shut the fuck up and read this.

Kali Linux has a fuckton of problems.
Limited repositories, a modified kernel and many other fun things that will hurt your user experience like Adebowale does with sister's nice arse. Heck, it even used to have root by default, which is the fastest way to have your sistem broken.

Those are things that are made to make this distro useful as virtual machine tool for experienced people who knows how to solve the shitton of problems that Kali will throw at them.

If the bootloader breaks, the package manager gives problems or the graphics drivers stop working no one will help you. Or if they do, they are not people you should be speaking to because they don't want you to learn shit. And you know why?

Because you fucking wanted it! You installed an unstable, insecure distro, full of problems because you wanted to be a hackerboi!

Install a distro meant to be used by beginners like Ubuntu and its spins and derivates, Fedora, OpenSUSE and many others. You can install the tools you need for your pentesting studies on them too.
            ''')

@bot.message_handler(commands=['cyberpunk'])
def send_welcome(message):
    bot.reply_to(message, "https://www.youtube.com/watch?v=ykV6z7TN4F4")



bot.polling()
















