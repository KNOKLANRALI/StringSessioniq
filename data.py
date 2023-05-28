from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🔥 اضغط هنا للاستخراج 🔥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠  رجوع 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("✨ قناتنا ✨", url="https://t.me/iqthon")],
    ]

    START = """
Hey {}

اهلا بك {}

بوت ستخراج كود تيرمكس و كود بايروجرام

By @iqthon
شرح استخدام هنا @YZZZY
    """

    
