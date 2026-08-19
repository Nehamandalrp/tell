from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import os
from threading import Thread
from flask import Flask

# Dummy Web Server (Render ko 24/7 active rakhne ke liye)
web_app = Flask("")


@web_app.route("/")
def home():
    return "Bot is running 24/7!"


def run_web():
    port = int(os.environ.get("PORT", 8080))
    web_app.run(host="0.0.0.0", port=port)


def keep_alive():
    t = Thread(target=run_web)
    t.daemon = True
    t.start()
# ============================================================
# CONFIGURATION
# ============================================================

BOT_TOKEN = "8990029460:AAFo8NpBUU6nOCmp5-YR1jyI52e3vi6QP2s"

# Admin ka numeric Telegram Chat ID
ADMIN_CHAT_ID = 8200494184


# ============================================================
# CATEGORY DETAILS
# ============================================================

CATEGORY_DETAILS = {
    "category_1": {
        "name": "C------P",
        "photo": "Qr.jpg",
        "text": "🔥300+ 𝗠𝗘𝗗𝗜𝗔 / 700+  𝗠𝗘𝗗𝗜𝗔.\n🔥 𝗟𝗜𝗙𝗘𝗧𝗜𝗠𝗘 𝗠𝗘𝗠𝗕𝗘𝗥𝗦𝗛𝗜𝗣 \n✅ ꜱᴍᴀʟʟ ᴘᴀᴄᴋ 𝗥𝗦 • 299₹/-\n✅ ʙɪɢ ᴘᴀᴄᴋ 𝗥𝗦 • 499₹/-\nɪɴᴛᴇʀɴᴀᴛɪᴏɴᴀʟ ᴘʀɪᴄᴇ 👇\n✅ ꜱᴍᴀʟʟ  PACK •  15$\n✅ ʙɪɢ ᴘᴀᴄᴋ •  25$\n  \n Demo link - https://t.me/+KiUcrvqVKZNkOTg1  ",
        
    },
    "category_2": {
        "name": "ᴍᴏᴍ sᴏɴ",
        "text": "🔥300+ 𝗠𝗘𝗗𝗜𝗔 / 700+  𝗠𝗘𝗗𝗜𝗔.\n🔥 𝗟𝗜𝗙𝗘𝗧𝗜𝗠𝗘 𝗠𝗘𝗠𝗕𝗘𝗥𝗦𝗛𝗜𝗣 \n\n✅ ꜱᴍᴀʟʟ ᴘᴀᴄᴋ 𝗥𝗦 • 299₹/-\n✅ ʙɪɢ ᴘᴀᴄᴋ 𝗥𝗦 • 499₹/-\nɪɴᴛᴇʀɴᴀᴛɪᴏɴᴀʟ ᴘʀɪᴄᴇ 👇\n✅ ꜱᴍᴀʟʟ  PACK •  15$\n✅ ʙɪɢ ᴘᴀᴄᴋ •  25$ \n  \n Demo link - https://t.me/+KiUcrvqVKZNkOTg1 ",
    },
    "category_3": {
        "name": "ʀ@2ᴘ€",
        "text": "🔥300+ 𝗠𝗘𝗗𝗜𝗔 / 700+  𝗠𝗘𝗗𝗜𝗔.\n🔥 𝗟𝗜𝗙𝗘𝗧𝗜𝗠𝗘 𝗠𝗘𝗠𝗕𝗘𝗥𝗦𝗛𝗜𝗣 \n\n✅ ꜱᴍᴀʟʟ ᴘᴀᴄᴋ 𝗥𝗦 • 299₹/-\n✅ ʙɪɢ ᴘᴀᴄᴋ 𝗥𝗦 • 499₹/-\nɪɴᴛᴇʀɴᴀᴛɪᴏɴᴀʟ ᴘʀɪᴄᴇ 👇\n✅ ꜱᴍᴀʟʟ  PACK •  15$\n✅ ʙɪɢ ᴘᴀᴄᴋ •  25$–– \n  \n Demo link - https://t.me/+KiUcrvqVKZNkOTg1 ",
    },
    "category_4": {
        "name": "ᴅᴇꜱɪ ᴍᴍꜱ",
        "text": "🔥300+ 𝗠𝗘𝗗𝗜𝗔 / 700+  𝗠𝗘𝗗𝗜𝗔.\n🔥 𝗟𝗜𝗙𝗘𝗧𝗜𝗠𝗘 𝗠𝗘𝗠𝗕𝗘𝗥𝗦𝗛𝗜𝗣 \n\n✅ ꜱᴍᴀʟʟ ᴘᴀᴄᴋ 𝗥𝗦 • 299₹/-\n✅ ʙɪɢ ᴘᴀᴄᴋ 𝗥𝗦 • 499₹/-\nɪɴᴛᴇʀɴᴀᴛɪᴏɴᴀʟ ᴘʀɪᴄᴇ 👇\n✅ ꜱᴍᴀʟʟ  PACK •  15$\n✅ ʙɪɢ ᴘᴀᴄᴋ •  25$\n  \n Demo link - https://t.me/+KiUcrvqVKZNkOTg1 ",
    },
    "category_5": {
        "name": "sᴄʜᴏᴏʟ ᴠɪᴅᴇᴏ",
        "text": "🔥300+ 𝗠𝗘𝗗𝗜𝗔 / 700+  𝗠𝗘𝗗𝗜𝗔.\n🔥 𝗟𝗜𝗙𝗘𝗧𝗜𝗠𝗘 𝗠𝗘𝗠𝗕𝗘𝗥𝗦𝗛𝗜𝗣 \n\n✅ ꜱᴍᴀʟʟ ᴘᴀᴄᴋ 𝗥𝗦 • 299₹/-\n✅ ʙɪɢ ᴘᴀᴄᴋ 𝗥𝗦 • 499₹/-\nɪɴᴛᴇʀɴᴀᴛɪᴏɴᴀʟ ᴘʀɪᴄᴇ 👇\n✅ ꜱᴍᴀʟʟ  PACK •  15$\n✅ ʙɪɢ ᴘᴀᴄᴋ •  25$ \n  \n Demo link - https://t.me/+KiUcrvqVKZNkOTg1 ",
    },
    "category_6": {
        "name": "ꜰᴀɪᴍʟʏ sᴘʏ",
        "text": "🔥300+ 𝗠𝗘𝗗𝗜𝗔 / 700+  𝗠𝗘𝗗𝗜𝗔.\n🔥 𝗟𝗜𝗙𝗘𝗧𝗜𝗠𝗘 𝗠𝗘𝗠𝗕𝗘𝗥𝗦𝗛𝗜𝗣 \n \n✅ ꜱᴍᴀʟʟ ᴘᴀᴄᴋ 𝗥𝗦 • 299₹/-\n✅ ʙɪɢ ᴘᴀᴄᴋ 𝗥𝗦 • 499₹/-\nɪɴᴛᴇʀɴᴀᴛɪᴏɴᴀʟ ᴘʀɪᴄᴇ 👇\n✅ ꜱᴍᴀʟʟ  PACK •  15$\n✅ ʙɪɢ ᴘᴀᴄᴋ •  25$ \n  \n Demo link - https://t.me/+KiUcrvqVKZNkOTg1 ",
    },
}


# ============================================================
# PAYMENT DETAILS
# ============================================================

BINANCE_DETAILS = """
💳 Binance

UID:
1176282510

Username:
sanjudox

Step 1️⃣ Send Payment

Step 2️⃣ Send Payment Screenshot For Verification

Step 3️⃣ Wait For Reply
"""

PAYPAL_DETAILS = """
💳 PayPal

PayPal:
Username - @Rajkamalhero  
Step 1️⃣ Send Payment

Step 2️⃣ Send Payment Screenshot For Verification

Step 3️⃣ Wait For Reply
"""

REMITLY_DETAILS = """
💳 Remitly to UPI 

I give u UPI- sanjubaba-international@cnrb

Step 1️⃣ Send Payment

Step 2️⃣ Send Payment Screenshot For Verification

Step 3️⃣ Wait For Reply



"""

QR_DETAILS = """
💳 QR Payment
"""

UPI_DETAILS = """
💳 UPI

UPI ID:
sanjubaba-international@cnrb 
"""

REVOLUT_DETAILS = """
💳 Revolut

@Raniivideo Dm me 
"""

CRYPTO_DETAILS = """
💳 USDT / Bitcoin / Crypto

⭐ USDT Address  with Network 🛜 

ETH -   0x22c9fe0319ddad833f3fe13fb942140aa79dff34
SOL -     F7ANEJ8vfyFhR4VEnmobyeBPWqeJEWTLbWUgD8dr2UNe
TRX -   TBGsETLni6zfKbqhWLNanJ8DtswXgMcXoq 


Bitcoin Address:
⭐ BITCOIN Address  with Network 🛜 


BTC -   15cxVVopFtrG3wxsjJEYj5LTEFFyb6sQ7P
ETH -     0x22c9fe0319ddad833f3fe13fb942140aa79dff34 
BSC -   0x22c9fe0319ddad833f3fe13fb942140aa79dff34


"""

PACKAGE_DETAILS = """
📦 All Package \n
\n⭐ᴄʜɪʟᴅ (ᴄʜᴀɴɴᴇʟ+ ꜰɪʟᴇ) \n⭐ᴍᴏᴍ ꜱᴏɴ ( ɢʀᴏᴜᴘ+ ꜰɪʟᴇ) \n⭐ʀ@ᴘᴇ ( ꜰɪʟᴇ ) \n⭐ꜱɪꜱ ʙʀᴏᴛʜᴇʀ ( ɢʀᴏᴜᴘ) \n⭐ᴠɪʀᴀʟ ᴍᴍꜱ  ( ɢʀᴏᴜᴘ) \n⭐ᴅᴇꜱɪ ᴍᴍꜱ ( ɢʀᴏᴜᴘ) \n⭐ᴅᴇꜱɪ ( ɢʀᴏᴜᴘ) \n⭐ ꜰᴀɪᴍʟʏ ꜱᴘʏ (ɢʀᴏᴜᴘ) \n⭐ ꜱᴄʜᴏᴏʟ ᴠɪᴅᴇᴏ (ɢʀᴏᴜᴘ) \n⭐ ᴄᴘ ɢᴜʏ (ɢʀᴏᴜᴘ) \n⭐ ᴛᴀᴍɪʟ (ɢʀᴏᴜᴘ) \n⭐ ʟᴇꜱʙɪᴀɴ (ɢʀᴏᴜᴘ) \n⭐ ꜰʟᴀꜱʜɪɴɢ  (ɢʀᴏᴜᴘ) \n⭐ ꜱɴᴀᴘ ɢꜰ ʙꜰ(ɢʀᴏᴜᴘ) \n⭐  ᴄᴄᴛᴠ ᴄᴀᴍ  (ɢʀᴏᴜᴘ) \n⭐ ɪɴᴅɪᴀɴ ʙʜᴀʙʜɪ  (ɢʀᴏᴜᴘ) \n⭐ ᴅᴀʀᴋ ᴡᴇʙ \n⭐ ꜰᴏᴏᴛ ᴊᴏʙ \n⭐ʙʟᴏᴡ ᴊᴏʙ/ꜱᴜᴄᴋɪɴɢ \n⭐ʀᴜꜱꜱɪᴀɴ (ɢʀᴏᴜᴘ)

\n ᴘʀɪᴄᴇ - 1999₹ 🪙  @Raniivideo 
\n ɪɴᴛᴇʀɴᴀᴛɪᴏɴᴀʟ ᴘʀɪᴄᴇ - 99$💰

\n 500 ɢʙ ᴍᴇɢᴀ ʟɪɴᴋ ꜰʀᴇᴇ📍
\nIf Are you interested \n 👇


"""


# ============================================================
# KEYBOARDS
# ============================================================

def main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "C------P",
                callback_data="category_1"
            ),
            InlineKeyboardButton(
                "ᴍᴏᴍ sᴏɴ",
                callback_data="category_2"
            ),
        ],
        [
            InlineKeyboardButton(
                "ʀ@2ᴘ€",
                callback_data="category_3"
            ),
            InlineKeyboardButton(
                "ᴅᴇꜱɪ ᴍᴍꜱ",
                callback_data="category_4"
            ),
        ],
        [
            InlineKeyboardButton(
                "sᴄʜᴏᴏʟ ᴠɪᴅᴇᴏ",
                callback_data="category_5"
            ),
            InlineKeyboardButton(
                "ꜰᴀɪᴍʟʏ sᴘʏ",
                callback_data="category_6"
            ),
        ],
        [
            InlineKeyboardButton(
                "📦 All Package",
                callback_data="all_package"
            )
        ],
        [
            InlineKeyboardButton(
                "☎️ Helpline",
                callback_data="helpline"
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def category_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "💳 How To Send Payment",
                callback_data="payment_menu"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 Main Menu",
                callback_data="main_menu"
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def payment_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "✅ Binance",
                callback_data="payment_binance"
            ),
            InlineKeyboardButton(
                "✅ PayPal",
                callback_data="payment_paypal"
            ),
        ],
        [
            InlineKeyboardButton(
                "✅ Remitly",
                callback_data="payment_remitly"
            ),
            InlineKeyboardButton(
                "✅ QR",
                callback_data="payment_qr"
            ),
        ],
        [
            InlineKeyboardButton(
                "✅ UPI",
                callback_data="payment_upi"
            ),
            InlineKeyboardButton(
                "✅ Revolut",
                callback_data="payment_revolut"
            ),
        ],
        [
            InlineKeyboardButton(
                "✅ USDT / Bitcoin / Crypto",
                callback_data="payment_crypto"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="back_category"
            ),
            InlineKeyboardButton(
                "🏠 Main Menu",
                callback_data="main_menu"
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def payment_page_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "📸 Send Payment Screenshot For verification",
                url="https://t.me/Raniivideo"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="payment_menu"
            ),
            InlineKeyboardButton(
                "🏠 Main Menu",
                callback_data="main_menu"
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


# ============================================================
# START
# ============================================================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    text = "Which Category Do You Want?"

    await update.message.reply_text(
        text,
        reply_markup=main_menu_keyboard()
    )


# ============================================================
# CALLBACK HANDLER
# ============================================================

async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query

    await query.answer()

    data = query.data

    # --------------------------------------------------------
    # MAIN MENU
    # --------------------------------------------------------

    if data == "main_menu":

        await query.edit_message_text(
            "Which Category Do You Want?",
            reply_markup=main_menu_keyboard()
        )

        return

    # --------------------------------------------------------
    # CATEGORY
    # --------------------------------------------------------

    if data in CATEGORY_DETAILS:

        category = CATEGORY_DETAILS[data]

        context.user_data["selected_category"] = data

        text = (
            f"📢 {category['name']}\n\n"
            f"{category['text']}"
        )

        await query.edit_message_text(
            text,
            reply_markup=category_keyboard()
        )

        return

    # --------------------------------------------------------
    # PAYMENT MENU
    # --------------------------------------------------------

    if data == "payment_menu":

        await query.edit_message_text(
            "💳 Select Your Payment Method",
            reply_markup=payment_keyboard()
        )

        return

    # --------------------------------------------------------
    # BACK TO CATEGORY
    # --------------------------------------------------------

    if data == "back_category":

        category_id = context.user_data.get(
            "selected_category",
            "category_1"
        )

        category = CATEGORY_DETAILS[category_id]

        text = (
            f"📢 {category['name']}\n\n"
            f"{category['text']}"
        )

        await query.edit_message_text(
            text,
            reply_markup=category_keyboard()
        )

        return

    # --------------------------------------------------------
    # QR PAYMENT
    # --------------------------------------------------------

    if data == "payment_qr":

        caption = (
            "💳 QR Payment\n\n"
            "Step 1️⃣ Send Payment\n\n"
            "Step 2️⃣ Send Payment Screenshot For Verification\n\n"
            "Step 3️⃣ Wait For Reply"
        )

        await query.message.delete()

        with open("Qr.jpg", "rb") as qr:
            await context.bot.send_photo(
                chat_id=query.from_user.id,
                photo=qr,
                caption=caption,
                reply_markup=payment_page_keyboard()
            )

        return

    # --------------------------------------------------------
    # OTHER PAYMENT METHODS
    # --------------------------------------------------------

    payment_details = {
        "payment_binance": BINANCE_DETAILS,
        "payment_paypal": PAYPAL_DETAILS,
        "payment_remitly": REMITLY_DETAILS,
        "payment_upi": UPI_DETAILS,
        "payment_revolut": REVOLUT_DETAILS,
        "payment_crypto": CRYPTO_DETAILS,
    }

    if data in payment_details:

        await query.edit_message_text(
            payment_details[data],
            reply_markup=payment_page_keyboard()
        )

        return

    # --------------------------------------------------------
    # ALL PACKAGE
    # --------------------------------------------------------

    if data == "all_package":

        keyboard = [
            [
                InlineKeyboardButton(
                    "💳 How To Send Payment",
                    callback_data="payment_menu"
                )
            ],
            [
                InlineKeyboardButton(
                    "🏠 Main Menu",
                    callback_data="main_menu"
                )
            ],
        ]

        await query.edit_message_text(
            PACKAGE_DETAILS,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

        return

    # --------------------------------------------------------
    # HELPLINE
    # --------------------------------------------------------

    if data == "helpline":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🏠 Main Menu",
                    callback_data="main_menu"
                )
            ]
        ]

        await query.edit_message_text(
            "❓ @raniivideo , @sanju100K \n\n"
            "Please contact our support team. And Wait For Reply ",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

        return


# ============================================================
# SCREENSHOT HANDLER
# ============================================================

async def receive_screenshot(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if not context.user_data.get("waiting_for_screenshot"):
        return

    user = update.effective_user

    if user.username:
        username_text = f"🔗 Username: @{user.username}"
    else:
        username_text = "🔗 Username: Not Available"

    caption = (
        "📸 NEW PAYMENT SCREENSHOT\n\n"
        f"👤 Name: {user.full_name}\n"
        f"🆔 User ID: {user.id}\n"
        f"{username_text}"
    )

    if update.message.photo:

        await context.bot.send_photo(
            chat_id=ADMIN_CHAT_ID,
            photo=update.message.photo[-1].file_id,
            caption=caption
        )

        await update.message.reply_text(
            "✅ Screenshot received successfully.\n"
            "Your payment will be verified."
        )

    elif update.message.document:

        await context.bot.send_document(
            chat_id=ADMIN_CHAT_ID,
            document=update.message.document.file_id,
            caption=caption
        )

        await update.message.reply_text(
            "✅ Payment proof received successfully."
        )

    else:

        await update.message.reply_text(
            "❌ Please send a screenshot/image."
        )

        return

    context.user_data["waiting_for_screenshot"] = False


# ============================================================
# ERROR HANDLER
# ============================================================

async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE
):

    print(f"Error: {context.error}")


# ============================================================
# RUN BOT
# ============================================================

def main():

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    app.add_handler(
        MessageHandler(
            filters.PHOTO | filters.Document.IMAGE,
            receive_screenshot
        )
    )

    app.add_error_handler(error_handler)

    print("🤖 Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    keep_alive()
    main()
