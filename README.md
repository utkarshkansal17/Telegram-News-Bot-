# Telegram-News-Bot
Chatbots are often touted as a revolution in the way users interact with technology and businesses. They have a fairly simple interface compared with traditional apps, as they only require users to chat, and the chatbots are supposed to understand and do whatever the user demands from them, at least in theory.

Many industries are shifting their customer service to chatbot systems. That’s because of the huge drop in the cost compared to actual humans, and also because of the robustness and constant availability. Chatbots deliver a degree of user support without substantial additional cost.

Today, chatbots are used in many scenarios, ranging from menial tasks such as displaying time and weather data to more complex operations such as rudimentary medical diagnosis and customer communication/support. You can devise a chatbot that will help your customers when they ask certain questions about your product, or you can make a personal assistant chatbot that can handle basic tasks and remind you when it’s time to head to a meeting or the gym.

There are a lot of options when it comes to where you can deploy your chatbot, and one of the most common uses are social media platforms, as most people use them on a regular basis. The same can be said of instant messaging apps, though with some caveats.

Telegram is one of the more popular IM platforms today, as it allows you to store messages on the cloud instead of just your device and it boasts good multi-platform support, as you can have Telegram on Android, iOS, Windows, and just about any other platform that can support the web version. Building a chatbot on Telegram is fairly simple and requires few steps that take very little time to complete. The chatbot can be integrated in Telegram groups and channels, and it also works on its own.

In this tutorial, we will be creating a Telegram bot that gives you an avatar image from Adorable Avatars. Our example will involve building a bot using Flask and deploying it on a free Heroku server.

To complete this tutorial, you will need Python 3 installed on your system as well as Python coding skills. Also, a good understanding of how apps work would be a good addition, but not a must, as we will be going through most of the stuff we present in detail. You also need Git installed on your system.

Of course, the tutorial also requires a Telegram account, which is free. You can sign up here. A Heroku account is required, too, and you can get it for free here.

#Bringing Your Telegram Bot to Life

To create a chatbot on Telegram, you need to contact the BotFather, which is essentially a bot used to create other bots.

The command you need is /newbot which leads to the following steps to create your bot:
Your bot should have two attributes: a name and a username. The name will show up for your bot, while the username will be used for mentions and sharing.

After choosing your bot name and username—which must end with “bot”—you will get a message containing your access token, and you’ll obviously need to save your access token and username for later, as you will be needing them.

