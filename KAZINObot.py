from telegram.ext import Application, CommandHandler
import random
ForTest = 0
Balance = 0
Cars = []
Guns = []
# Вітається
async def start(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text="<b>Вітаємо тебе в нашому казино🙌🏻!</b>\n \nЩоб дізнатись список наявних команд, введіть /menu \nЩоб отримати подарунок для новачка, введіть /bonus", parse_mode="HTML")

# Показує список команд
async def menu(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text="<b>| 🚀 КОМАНДИ ДЛЯ ПОЧАТКУ РОБОТИ 🚀 |</b> \n  \n1. /start - розпочати роботу бота \n2. /menu - список команд \n3. /support - підтримка\n \n<b>| 🪙 КОМАНДИ ДЛЯ РОБОТИ З БАЛАНСОМ 🪙 |</b>\n \n1. /balance - показати мій баланс\n2. /bonus - отримати бонус\n3. /cars - переглянути список своїх автомобілів\n4. /guns - переглянути список моєї зброї\n \n<b>| 🎰 ІГРОВІ КОМАНДИ 🎰 |</b>\n \n1. /games - дізнатись список ігр, що доступні на данний момент\n \n<b>| 💶КОМАНДИ ДЛЯ ВИТРАТИ ГРОШЕЙ💶 |</b>\n \n1. /market - переглянути асоримент товарів для покупки.\n2. /sell_market -  продати непотрібні товари\n", parse_mode="HTML")

# Показує ваш баланс
async def balance(update, context):
    global Balance
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text=f"Ваш баланс складає {Balance}💰")


# Показує список ігор
async def games(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text="<b>| КОЛЕСО ФОРТУНИ |</b>\n \nПрокрутіть колесо фортуни! Воно дає змогу отримати до 500💰, або втратити їх!\nВведіть /game1 щоб почати🚀\n \n<b>| МОНЕТКА | </b>\n \nВведіть вашу ставку, оберіть сторону монетки та отримайте подовоєну сумму2️⃣! \nВведіть /game2 щоб почати🚀\n\n<b>| РУЛЕТКА |</b>\n \nВведіть сумму ставки, число. Якщо на барабані🎰 буде парне число, та ваше число також буде таким то ви отримаєте трійний виграш3️⃣! Але якщо ваше число буде непарним, то ви втратите двійну ставку2️⃣. Так само з непарними.\nВведіть /game3 щоб почати🚀\n \n<b>| КУБИК |</b>\n \nПоставте ставку та виберіть число, що на вашу думку випаде на кубику. Якщо вам пощастить, ви отримаєте вашу ставку помножену на цифру, що впиала на кубику🎲\nВведіть /game4 щоб почати🚀", parse_mode="HTML")

#Подарунок для початку
async def bonus(update, context):
    global ForTest
    global Balance
    chat = update.effective_chat
    if ForTest<1:
        Balance += 2000
        await context.bot.send_message(chat_id=chat.id, text="<b>Вітаю! ви отримали 500 бонусних 💰</b>\nБудьте обережні, їх можна отримувати лише 1 раз", parse_mode="HTML")
        ForTest += 1

    elif ForTest>=1:
        await context.bot.send_message(chat_id=chat.id, text= "Ви вже отримували бонус❌")

#підтримка
async def support(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text= "Всі питання, що виникли задавайте за цим номером телефону: +380(67)3757121")

#Магазин
async def shops(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text= "<b>Виберіть магазин в який хочете завітати:</b>\n\n<b>Автосалон</b>\nЩоб переглянути асортимент, введіть: /shop auto\n\n<b>Магазин зброї</b>\nЩоб переглянути асортимент, введіть: /shop gun", parse_mode="HTML")

#Асортимент магазинів
async def shop_choise(update, context):
    chat = update.effective_chat
    choise = (context.args[0])
    if choise == "auto":
        await context.bot.send_message(chat_id=chat.id, text= "<b>| НАШ АСОРТИМЕНТ |</b>\n \n<b>Мопед Дренчик --- 500💰</b>\nЩоб купити, введіть: /buy 1\n \n<b>ЛуАЗ 969 --- 1000💰</b>\nЩоб купити, введіть: /buy 2\n \n<b>BMW M5 E60 --- 15000💰</b>\nЩоб купити, введіть: /buy 3\n \n<b>McLaren 750s --- 60000💰</b>\nЩоб купити, введіть: /buy 4\n \n<b>Rolls Royse Cullinan --- 99000💰</b>\nЩоб купити, введіть: /buy 5", parse_mode="HTML")
        return
    if choise == "gun":
        await context.bot.send_message(chat_id=chat.id, text= "<b>| НАШ АСОРТИМЕНТ |</b>\n \n<b>Самопал --- 300💰</b>\nЩоб купити,введіть: /buy 6\n \n<b>Glock 19--- 1500💰</b>\nЩоб купити, введіть: /buy 7\n \n<b>FN SCAR--- 7800💰</b>\nЩоб купити, введіть: /buy 8\n \n<b>GBU 57 A/B --- 100000💰</b>\nЩоб купити, введіть: /buy 9\n \n<b>Водородна бомба --- 1000000💰</b>\nЩоб купити, введіть: /buy 10", parse_mode="HTML")
        return
    else:
        await context.bot.send_message(chat_id=chat.id, text= "Недоступна команад")

#Основна команда для покупки
async def buy(update, context):
    global Cars
    global Guns
    global Balance
    chat = update.effective_chat
    choise = int(context.args[0])
    if choise == 1:
        if Balance >= 500:
            Cars.append("Мопед Дренчик")
            await context.bot.send_message(chat_id=chat.id, text= f"Вітаємо з покупкою <b>Мопед Дренчик</b>, тепер ваш автопарк: {Cars}", parse_mode="HTML")
            Balance -= 500
            return
        elif Balance < 500:
            await context.bot.send_message(chat_id=chat.id, text= "у вас недостатньо коштів на рахунку❌")
            return
    if choise == 2:
        if Balance >= 1000:
            Cars.append("ЛуАЗ 969")
            await context.bot.send_message(chat_id=chat.id, text= f"Вітаємо з покупкою <b>ЛуАЗ 969</b>, тепер ваш автопарк: {Cars}", parse_mode="HTML")
            Balance -= 1000
            return
        elif Balance < 1000:
            await context.bot.send_message(chat_id=chat.id, text= "у вас недостатньо коштів на рахунку❌")
            return
    if choise == 3:
        if Balance >= 15000:
            Cars.append("BMW M5 E60")
            await context.bot.send_message(chat_id=chat.id, text= f"Вітаємо з покупкою <b>BMW E60</b>, тепер ваш автопарк: {Cars}", parse_mode="HTML")
            Balance -= 15000
            return
        elif Balance < 15000:
            await context.bot.send_message(chat_id=chat.id, text= "у вас недостатньо коштів на рахунку❌")
            return
    if choise == 4:
        if Balance >= 60000:
            Cars.append("McLaren 750s")
            await context.bot.send_message(chat_id=chat.id, text= f"Вітаємо з покупкою <b>McLaren 750s</b>, тепер ваш автопарк: {Cars}", parse_mode="HTML")
            Balance -= 60000
            return
        elif Balance < 60000:
            await context.bot.send_message(chat_id=chat.id, text= "у вас недостатньо коштів на рахунку❌")
            return
    if choise == 5:
        if Balance >= 99000:
            Cars.append("Rolls Royce Cullinan")
            await context.bot.send_message(chat_id=chat.id, text= f"Вітаємо з покупкою <b>Rolls Royce Cullinan</b>, тепер ваш автопарк: {Cars}", parse_mode="HTML")
            Balance -= 99000
            return
        elif Balance < 99000:
            await context.bot.send_message(chat_id=chat.id, text= "у вас недостатньо коштів на рахунку❌")
            return
    if choise == 6:
        if Balance >= 300:
            Guns.append("Самопал")
            await context.bot.send_message(chat_id=chat.id, text= f"Вітаємо з покупкою <b>Самопал</b>, тепер ваш арсенал: {Guns}", parse_mode="HTML")
            Balance -= 300
            return
        elif Balance < 300:
            await context.bot.send_message(chat_id=chat.id, text= "у вас недостатньо коштів на рахунку❌")
            return
    if choise == 7:
        if Balance >= 1500:
            Guns.append("Glock 19")
            await context.bot.send_message(chat_id=chat.id, text= f"Вітаємо з покупкою <b>Glock 19</b>, тепер ваш арсенал: {Guns}", parse_mode="HTML")
            Balance -= 1500
            return
        elif Balance < 1500:
            await context.bot.send_message(chat_id=chat.id, text= "у вас недостатньо коштів на рахунку❌")
            return
    if choise == 8:
        if Balance >= 7800:
            Guns.append("FN SCAR")
            await context.bot.send_message(chat_id=chat.id, text= f"Вітаємо з покупкою <b>FN SCAR</b>, тепер ваш арсенал: {Guns}", parse_mode="HTML")
            Balance -= 7800
            return
        elif Balance < 7800:
            await context.bot.send_message(chat_id=chat.id, text= "у вас недостатньо коштів на рахунку❌")
            return
    if choise == 9:
        if Balance >= 100000:
            Guns.append("GBU 57 A/B")
            await context.bot.send_message(chat_id=chat.id, text= f"Вітаємо з покупкою <b>GBU 57 A/B</b>, тепер ваш арсенал: {Guns}", parse_mode="HTML")
            Balance -= 100000
            return
        elif Balance < 100000:
            await context.bot.send_message(chat_id=chat.id, text= "у вас недостатньо коштів на рахунку❌")
            return
    if choise == 10:
        if Balance >= 1000000:
            Guns.append("Водородна бомба")
            await context.bot.send_message(chat_id=chat.id, text= f"Вітаємо з покупкою <b>Водородна бомба</b>, тепер ваш арсенал: {Guns}.\n(Ідея від розробника: влупіть нею по кремлю)", parse_mode="HTML")
            Balance -= 1000000
            return
        elif Balance < 1000000:
            await context.bot.send_message(chat_id=chat.id, text= "у вас недостатньо коштів на рахунку❌")
            return
            
    else:
        await context.bot.send_message(chat_id=chat.id, text= "Недоступна команад")

#Продаж
async def shop_sell(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text= "<b>Виберіть тип товару який ви хочете продати</b>\n \n<b>Автомобіль</b>\nВведіть: /item_sell auto\n \n<b>Зброя</b>\nВведіть: /item_sell guns", parse_mode="HTML")

#Асссортимент для продажу
async def item_sell(update, context):
    chat = update.effective_chat
    choise = (context.args[0])
    if choise == "auto":
        await context.bot.send_message(chat_id=chat.id, text= "<b>| ПРОДАЖ |</b>\n \n<b>Мопед дренчик --- 450💰</b>\nЩоб продати, введіть /sell 1\n \n<b>ЛуАЗ 969 ---  900💰</b>\nЩоб продати, введіть /sell 2\n \n<b>BMW M5 E60 --- 11500💰</b>\nЩоб продати, введіть /sell 3\n \n<b>McLaren 750s --- 50000💰</b>\nЩоб продати, введіть /sell 4\n \n<b>Rolls Roice --- 82000💰</b>\nЩоб продати, введіть /sell 5", parse_mode="HTML")
        return
    if choise == "guns":
        await context.bot.send_message(chat_id=chat.id, text= "<b>| ПРОДАЖ |</b>\n \n<b>Самопал --- 280💰</b>\nЩоб продати, введіть /sell 6\n \n<b>Glock 19 ---  1350💰</b>\nЩоб продати, введіть /sell 7\n \n<b>FN SCAR --- 6300💰</b>\nЩоб продати, введіть /sell 8\n \n<b>GBU 57 A/B --- 80000💰</b>\nЩоб продати, введіть /sell 9\n \n<b>Водородна бомба --- 800000💰</b>\nЩоб продати, введіть /sell 10", parse_mode="HTML")
        return
    else:
        await context.bot.send_message(chat_id=chat.id, text= "Недоступна команад")
#Основна команда для продажу
async def sell(update, context):
    global Balance
    chat = update.effective_chat
    choise = int(context.args[0])
    if choise == 1:
        if "Мопед Дренчик" in Cars:
            Balance += 450
            await context.bot.send_message(chat_id=chat.id, text= "Ви успішно продали <b>Мопед Дренчик</b>", parse_mode="HTML")
            return
        elif "Мопед Дренчик" not in Cars:
            await context.bot.send_message(chat_id=chat.id, text= "У вас немає цього автомобіля❌")
            return
    if choise == 2:
        if "ЛуАЗ 969" in Cars:
            Balance += 900
            await context.bot.send_message(chat_id=chat.id, text= "Ви успішно продали <b>ЛуАЗ 969</b>", parse_mode="HTML")
            return
        elif "ЛуАЗ 969" not in Cars:
            await context.bot.send_message(chat_id=chat.id, text= "У вас немає цього автомобіля❌")
            return
    if choise == 3:
        if "BMW M5 E60" in Cars:
            Balance += 11500
            await context.bot.send_message(chat_id=chat.id, text= "Ви успішно продали <b>BMW M5 E60</b>", parse_mode="HTML")
            return
        elif "BMW M5 E60" not in Cars:
            await context.bot.send_message(chat_id=chat.id, text= "У вас немає цього автомобіля❌")
            return
    if choise == 4:
        if "McLaren 750s" in Cars:
            Balance += 50000
            await context.bot.send_message(chat_id=chat.id, text= "Ви успішно продали <b>McLaren 750s</b>", parse_mode="HTML")
            return
        elif "McLaren 750s" not in Cars:
            await context.bot.send_message(chat_id=chat.id, text= "У вас немає цього автомобіля❌")
            return
    if choise == 5:
        if "Rolls Royce Cullinan" in Cars:
            Balance += 82000
            await context.bot.send_message(chat_id=chat.id, text= "Ви успішно продали <b>Rolls Royce Cullinan</b>", parse_mode="HTML")
            return
        elif "Rolls Royce Cullinan" not in Cars:
            await context.bot.send_message(chat_id=chat.id, text= "У вас немає цього автомобіля❌")
            return
    if choise == 6:
        if "Самопал" in Guns:
            Balance += 280
            await context.bot.send_message(chat_id=chat.id, text= "Ви успішно продали <b>Самопал</b>", parse_mode="HTML")
            return
        elif "Самопал" not in Guns:
            await context.bot.send_message(chat_id=chat.id, text= "У вас немає цього автомобіля❌")
            return
    if choise == 7:
        if "Glock 19" in Guns:
            Balance += 1350
            await context.bot.send_message(chat_id=chat.id, text= "Ви успішно продали <b>Glock 19</b>", parse_mode="HTML")
            return
        elif "Glock 19" not in Guns:
            await context.bot.send_message(chat_id=chat.id, text= "У вас немає цього автомобіля❌")
            return
    if choise == 8:
        if "FN SCAR" in Guns:
            Balance += 6300
            await context.bot.send_message(chat_id=chat.id, text= "Ви успішно продали <b>FN SCAR</b>", parse_mode="HTML")
            return
        elif "FN SCAR" not in Guns:
            await context.bot.send_message(chat_id=chat.id, text= "У вас немає цього автомобіля❌")
            return
    if choise == 9:
        if "GBU 57 A/B" in Guns:
            Balance += 80000
            await context.bot.send_message(chat_id=chat.id, text= "Ви успішно продали <b>GBU 57 A/B</b>", parse_mode="HTML")
            return
        elif "GBU 57 A/B" not in Guns:
            await context.bot.send_message(chat_id=chat.id, text= "У вас немає цього автомобіля❌")
            return
    if choise == 10:
        if "Водородна бомба" in Guns:
            Balance += 800000
            await context.bot.send_message(chat_id=chat.id, text= "Ви успішно продали <b>Водородна бомба</b>", parse_mode="HTML")
            return
        elif "Водородна бомба" not in Guns:
            await context.bot.send_message(chat_id=chat.id, text= "У вас немає цього автомобіля❌")
            return
    else:
        await context.bot.send_message(chat_id=chat.id, text= "Недоступна команад")

#Переглянути мій автопарк
async def my_cars(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text= f"<b>Ваш автопарк: {Cars}</b>", parse_mode="HTML")

#Переглянути мій арсенал
async def my_guns(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text= f"<b>Ваш арсенал: {Guns}</b>", parse_mode="HTML")

# Гра 1, колесо фортуни
async def game1(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text="<b>|🎰КОЛЕСО ФОРТУНИ🎰|</b>\n \nВведіть /spin щоб прокрутити колесо", parse_mode="HTML")

#Команда для прокруту колеса
async def spin(update, context):
    global Balance
    chat = update.effective_chat
    wheel = ["-50", "-100", "-200", "-300", "-500", "50", "100", "200", "300", "500"]
    winnings = random.choice(wheel)
    Balance += int(winnings)
    await context.bot.send_message(chat_id=chat.id, text=f"Ви зробили оберт колеса фортуни та отримали {winnings}💰\nВаш новий баланс: {Balance}💰")

#гра 2, монетка
async def game2(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text="<b>|🪙МОНЕТКА🪙|</b>\n \nВведіть /flip, сумму ставки та значення (Орел або Решка) щоб підкинути її\nПриклад правильного вводу команди: /flip 200 орел", parse_mode="HTML")

#команда для підкиду монетки
async def flip_da_coin(update, context):
    global Balance
    chat = update.effective_chat
    user_choice = context.args[1].lower()
    money_choice = int(context.args[0])

    if money_choice > Balance:
        await context.bot.send_message(chat_id=chat.id, text= "У вас недостатньо коштів на рахунку❌")
        return
    if money_choice < 0:
        await context.bot.send_message(chat_id=chat.id, text= "Ви не можете поставити відємне число як ставку❌")
    if user_choice not in ["орел", "решка"]:
        await context.bot.send_message(chat_id=chat.id, text="<b>Невірний вибір</b>\nВведіть /flip, сумму ставки та значення(Орел або Решка)", parse_mode="HTML")
        return

    flip_result = random.choice(["Орел", "Решка"])
    winnings = money_choice*2

    if flip_result.lower() == user_choice:
        Balance-=money_choice
        Balance += winnings
        await context.bot.send_message(chat_id=chat.id, text=f"<b>Результат підкидання:</b> {flip_result} \n<b>Оновлений баланс:</b> {Balance}💰 \n<b>Ваш виграш:</b> {winnings}💰", parse_mode="HTML")
    else:
        Balance -= money_choice
        await context.bot.send_message(chat_id=chat.id, text=f"<b>Результат підкидання:</b> {flip_result} \n<b>Оновлений баланс:</b> {Balance}💰 \n<b>Програні гроші:</b> {money_choice}💰", parse_mode="HTML")

#Гра 3, рулетка
async def game3(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text="<b>|🎟РУЛЕТКА🎟|</b>\n \nВведіть команду /bet та сумму ставки, після цього число від 1 до 36\nПриклад правильного вводу команди: /bet 200 13", parse_mode="HTML")

#Команда для рулетки
async def bet(update, context):
    global Balance
    chat = update.effective_chat
    bet_amount = int(context.args[0])
    num_chose = int(context.args[1])
    if num_chose <= 36 and num_chose >= 1:
        if bet_amount > Balance:
            await context.bot.send_message(chat_id=chat.id, text=" У вас недостатньо коштів на рахунку❌")
            return
        result = random.choice(["Парне", "Непарне"])
        winning = bet_amount * 3
        if result == "Парне":
            if num_chose % 2 == 0:
                Balance-=bet_amount
                Balance+=winning
                await context.bot.send_message(chat_id=chat.id, text=f"<b>Результат:</b> {result} \n<b>Оновлений баланс:</b> {Balance}💰 \n<b>Ваш виграш:</b> {winning}💰", parse_mode="HTML")
            elif num_chose % 2 != 0:
                Balance -= bet_amount*2
                await context.bot.send_message(chat_id=chat.id, text=f"<b>Результат:</b> {result} \n<b>Оновлений баланс:</b> {Balance}💰 \n<b>Програні гроші:</b> {bet_amount*2}💰", parse_mode="HTML")
        elif result == "Непарне":
            if num_chose % 2 != 0:
                Balance-=bet_amount
                Balance+=winning
                await context.bot.send_message(chat_id=chat.id, text=f"<b>Результат:</b> {result} \n<b>Оновлений баланс:</b> {Balance}💰 \n<b>Ваш виграш:</b> {winning}💰", parse_mode="HTML")
            elif num_chose % 2 == 0:
                Balance -= bet_amount*2
                await context.bot.send_message(chat_id=chat.id, text=f"<b>Результат:</b> {result} \n<b>Оновлений баланс:</b> {Balance}💰 \n<b>Програні гроші:</b> {bet_amount*2}💰", parse_mode="HTML")
    elif num_chose>36:
        await context.bot.send_message(chat_id=chat.id, text= "Число занадто велике")
    elif num_chose<1:
        await context.bot.send_message(chat_id=chat.id, text= "Число занадто мале")
# Game 4: Dice Roll
async def game4(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text="<b>|🎲КИДОК КУБИКА🎲|</b>\n \nВведіть команду /roll, сумму стави, та цифрцу від 1 до 6 для кидка кубика\nПриклад правильного вводу команди: /roll 200 5", parse_mode="HTML")

async def roll(update, context):
    global Balance
    chat = update.effective_chat
    roll_amount = int(context.args[0])
    if roll_amount > Balance:
        await context.bot.send_message(chat_id=chat.id, text="У вас недостатньо коштів на рахунку❌")
        return
    dice_roll = random.randint(1, 6)
    user_choice = int(context.args[1])
    winnings = 0
    if user_choice < 1:
        await context.bot.send_message(chat_id=chat.id, text="Число має бути від 1 до 6, ваше число занадто мале", parse_mode="HTML")
        return
    if user_choice > 6:
        await context.bot.send_message(chat_id=chat.id, text="Число має бути від 1 до 6, ваше число занадто велике", parse_mode="HTML")
        return
    if user_choice >= 1 or user_choice <= 6:
        if user_choice == dice_roll:
            Balance -= roll_amount
            winnings = user_choice * roll_amount
            Balance += winnings
            await context.bot.send_message(chat_id=chat.id, text=f"<b>Ваш результат:</b> {dice_roll} \n<b>Оновлений баланс:</b> {Balance}💰\n<b>Ваш виграш:</b> {winnings}💰", parse_mode="HTML")
            return
        elif user_choice != dice_roll:
            Balance -= roll_amount
            await context.bot.send_message(chat_id=chat.id, text=f"<b>Ваш результат:</b> {dice_roll} \n<b>Оновлений баланс:</b> {Balance}💰\n<b>Програні гроші:</b> {roll_amount}💰", parse_mode="HTML")

application = Application.builder().token("6049849076:AAEwFmrJukP72pDpMBenN4rT9FDfM5UXeLI").build()
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("menu", menu))
application.add_handler(CommandHandler("balance", balance))
application.add_handler(CommandHandler("games", games))
application.add_handler(CommandHandler("game1", game1))
application.add_handler(CommandHandler("spin", spin))
application.add_handler(CommandHandler("game2", game2))
application.add_handler(CommandHandler("flip", flip_da_coin))
application.add_handler(CommandHandler("game3", game3))
application.add_handler(CommandHandler("bet", bet))
application.add_handler(CommandHandler("game4", game4))
application.add_handler(CommandHandler("roll", roll))
application.add_handler(CommandHandler("bonus", bonus))
application.add_handler(CommandHandler("support", support))
application.add_handler(CommandHandler("market", shops))
application.add_handler(CommandHandler("shop", shop_choise))
application.add_handler(CommandHandler("buy", buy))
application.add_handler(CommandHandler("sell_market", shop_sell))
application.add_handler(CommandHandler("item_sell", item_sell))
application.add_handler(CommandHandler("sell", sell))
application.add_handler(CommandHandler("cars", my_cars))
application.add_handler(CommandHandler("guns", my_guns))
application.run_polling()
