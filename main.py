import telebot
from telebot import types

# Define the token from BotFather
TOKEN = '7229956147:AAFOrAr2PyJGh-pHHfBbSZy1GdBnptetfiQ'
bot = telebot.TeleBot(TOKEN)
url = "https://mhmdtaqi-code.github.io/farsaweb"



j1= """مرحبا! إذا تحب تشارك ويانه وتكون جزء من فريق فرصة التطوعي، تقدر تقدم طلبك بسهولة. كل اللي تحتاجه هو شغف للتطوع ورغبة بخدمة المجتمع. 
اليك اليلنك :
https://mhmdtaqi-code.github.io/farsaweb/


 يحتوي على استمارة الانضمام. ننتظرك بفريقنا!

إليك شروط التطوع لفريق فرصة:

الشغف والاهتمام: يكون عندك اهتمام حقيقي بالتطوع ورغبة في تطوير نفسك وخدمة المجتمع.

البيئة السليمة: نحرص على خلق بيئة عمل إيجابية، لذلك نتوقع من كل المتطوعين الالتزام بالاحترام والتعاون مع باقي أعضاء الفريق"""

# Define the questions and answers
questions = {
    "كيف يتم تحديد الأولويات وتوزيع المهام داخل الفريق": "الإجابة: نقوم بتحديد الأولويات من خلال تقييم احتياجات المجتمع والأهداف الاستراتيجية للمشروع. بعد ذلك، نوزع المهام بناءً على مهارات وخبرات الأعضاء، ونتأكد من أن كل شخص متأكد من دوره ومهامه",
    "ما هي التحديات الرئيسية التي واجهتكم في عملكم التطوعي، وكيف تعاملتم معها؟": "الإجابة: واجهنا تحديات مثل نقص الموارد والتنسيق بين الأعضاء. تعاملنا مع هذه التحديات من خلال تحسين استراتيجيات التخطيط وتوفير التدريب اللازم للأعضاء وتوسيع شبكة علاقاتنا للحصول على دعم إضافي.",
    "ما هو الدور الذي يلعبه كل عضو في الفريق وكيف يساهم في تحقيق الأهداف؟": "الإجابة: كل عضو يلعب دوراً مهماً بناءً على خبراته ومهاراته. مثلاً، البعض يتولى القيادة والتنسيق، بينما يتعامل آخرون مع الجوانب الفنية أو العلاقات العامة. كل دور يكمل الآخر ويساهم في تحقيق الأهداف الجماعية.",
    "كيف يتم التعامل مع النزاعات أو الخلافات بين أعضاء الفريق؟": "الإجابة: نستخدم أسلوب الحوار المفتوح لمعالجة النزاعات. نقوم بترتيب اجتماعات خاصة لحل المشاكل وتعزيز التفاهم بين الأعضاء. الهدف هو الوصول إلى حل يرضي جميع الأطراف ويعزز العمل الجماعي"
}

general_questions = {
    'كيف يمكنني معرفة المزيد عن الدورات؟': f"الجواب: سيتم الإعلان عن الدورات عبر حساباتنا الرسمية.  {url}                                                   Instagram:@foors_aa",
    'هل هناك حد أدنى للعمر للانضمام الينا؟': "الجواب: لا يوجد، الجميع مرحب بهم",
    'هل أحتاج إلى مؤهلات معينة للمشاركة؟': "الجواب: لا , نرحب بكل من لديه الرغبة في التطوع",
    'هل أحتاج إلى معدات خاصة للتطوع؟': "الجواب: لا، سنوفر لك كل ما تحتاجه",
    'هل هناك رسوم للانضمام؟': "الجواب: لا، الانضمام إلى فريق فرصة مجاني بالكامل. نحن نعتمد على الجهود التطوعية والروح الجماعية",
    'كيف ستفيدني المشاركة؟': "الجواب: ستطور مهاراتك وتساهم في خدمة المجتمع.",
    'ما هي القيم التي يعمل بها الفريق؟': "الجواب: التعاون، التطور، والمسؤولية المجتمعية"
}

# Define the welcome message handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton('ماهي فرصه')
    btn2 = types.KeyboardButton('للتطوع مع فرصه')
    btn3 = types.KeyboardButton('بعض الاسئله')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "اختر زر:", reply_markup=markup)

# Define the message handler for options
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'ماهي فرصه':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn1 = types.KeyboardButton('موقعنا')
        btn2 = types.KeyboardButton('عنا')
        btn3 = types.KeyboardButton('رجوع')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "اختر خياراً من القائمة التالية:", reply_markup=markup)
    elif message.text == 'للتطوع مع فرصه':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        btn1 = types.KeyboardButton('رجوع')
        markup.add(btn1)
        bot.send_message(message.chat.id, j1, reply_markup=markup)
    elif message.text == 'بعض الاسئله':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        for question in general_questions.keys():
            markup.add(types.KeyboardButton(question))
        for question in questions.keys():
            markup.add(types.KeyboardButton(question))
        markup.add(types.KeyboardButton('رجوع'))
        bot.send_message(message.chat.id, "اختر سؤالاً من القائمة التالية:", reply_markup=markup)
    elif message.text in questions:
        bot.send_message(message.chat.id, questions[message.text])
    elif message.text in general_questions:
        bot.send_message(message.chat.id, general_questions[message.text])
    elif message.text == 'موقعنا':
        bot.send_message(message.chat.id, f"{url}")
    elif message.text == 'عنا':
        bot.send_message(message.chat.id, "فرصة هو فريق تطوعي يهدف إلى تمكين الشباب وتطوير مهاراتهم من خلال تنظيم دورات تعليمية وفعاليات مجتمعية تهدف إلى نشر الوعي وتعزيز التعاون. نؤمن بأن التعليم هو القوة التي تصنع مستقبلًا أفضل")
    elif message.text == 'رجوع':
        send_welcome(message)

bot.polling()
