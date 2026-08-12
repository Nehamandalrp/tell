from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# ============================================================
# CONFIGURATION
# ============================================================

BOT_TOKEN = "8990029460:AAHWuEoKynKu8t-yvDpeoXewkTXz1pqjJJw"

# Telegram username WITHOUT @
YOUR_USERNAME = "Raniivideo"

# ============================================================
# CUSTOM DETAILS - EDIT THESE
# ============================================================

CATEGORY_DETAILS = {
    "category_1": {
        "name": " C-----p",
        "text": "My Custom Text for Category 1",
    },
    "category_2": {
        "name": "ᴍ0ᴍ s0ɴ",
        "text": "My Custom Text for Category 2",
    },
    "category_3": {
        "name": "scʜʟ ᴠɪᴅᴇᴏ",
        "text": "My Custom Text for Category 3",
    },
    "category_4": {
        "name": "ʀ@2ᴘ€",
        "text": "My Custom Text for Category 4",
    },
    "category_5": {
        "name": "ꜰᴀɪᴍʟʏ sᴘ",
        "text": "My Custom Text for Category 5",
    },
    "category_6": {
        "name": "ʙʀᴏ ss",
        "text": "My Custom Text for Category 6",
    
    }
    
}

BINANCE_DETAILS = """
💳 Binance

(My Binance Details)

Example:
Binance ID: YOUR_BINANCE_ID
Email: YOUR_EMAIL
"""

PAYPAL_DETAILS = """
💳 PayPal

(My PayPal Details)

PayPal:
YOUR_PAYPAL_EMAIL
"""

REMITLY_DETAILS = """
💳 Remitly

(My Remitly Details)

Name:
YOUR_NAME

Country:
YOUR_COUNTRY

Other details:
YOUR_REMITLY_DETAILS
"""

QR_DETAILS = """
💳 QR Payment

(My QR Code or QR Details)

Please scan the QR code to make payment.
"""

UPI_DETAILS = """
💳 UPI

(My UPI Details)

UPI ID:
YOUR_UPI_ID
"""

REVOLUT_DETAILS = """
💳 Revolut

(My Revolut Details)

Revolut:
YOUR_REVOLUT_DETAILS
"""

CRYPTO_DETAILS = """
💳 USDT / Bitcoin / Crypto

USDT Address:
YOUR_USDT_ADDRESS

Network:
YOUR_NETWORK

Bitcoin Address:
YOUR_BITCOIN_ADDRESS

Ethereum Address:
YOUR_ETHEREUM_ADDRESS

Network Details:
YOUR_NETWORK_DETAILS
"""

PACKAGE_DETAILS = """
📦 All Package

(My Package Details)

Package 1:
YOUR PACKAGE DETAILS

Package 2:
YOUR PACKAGE DETAILS

Package 3:
YOUR PACKAGE DETAILS
"""


# ============================================================
# KEYBOARDS
# ============================================================

def main_menu_keyboard():
    keyboard = [
        
        [
            InlineKeyboardButton("1️⃣ C-----p", callback_data="category_1"),
            InlineKeyboardButton("2️⃣ ᴍ0ᴍ s0ɴ", callback_data="category_2"),
        ],
        [
            InlineKeyboardButton("3️⃣ scʜʟ ᴠɪᴅᴇᴏ", callback_data="category_3"),
            InlineKeyboardButton("4️⃣ ʀ@2ᴘ€", callback_data="category_4"),
        ],
        [
            InlineKeyboardButton("5️⃣ ꜰᴀɪᴍʟʏ sᴘ", callback_data="category_5"),
            InlineKeyboardButton("6️⃣ ʙʀᴏ ss", callback_data="category_6"),
        ],
        [
            InlineKeyboardButton("📦 All Package", callback_data="all_package"),
        ],
        [
            InlineKeyboardButton("☎️ Helpline", callback_data="helpline"),
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
            InlineKeyboardButton("✅ Binance", callback_data="payment_binance"),
            InlineKeyboardButton("✅ PayPal", callback_data="payment_paypal"),
        ],
        [
            InlineKeyboardButton("✅ Remitly", callback_data="payment_remitly"),
            InlineKeyboardButton("✅ QR", callback_data="payment_qr"),
        ],
        [
            InlineKeyboardButton("✅ UPI", callback_data="payment_upi"),
            InlineKeyboardButton("✅ Revolut", callback_data="payment_revolut"),
        ],
        [
            InlineKeyboardButton(
                "✅ USDT / Bitcoin / Crypto",
                callback_data="payment_crypto"
            )
        ],
        [
            InlineKeyboardButton("⬅️ Back", callback_data="back_category"),
            InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu"),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def payment_page_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("⬅️ Back", callback_data="payment_menu"),
            InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu"),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


def helpline_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


# ============================================================
# /START
# ============================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = (
        
        "Which Category Do You Want?\n"
        
    )

    await update.message.reply_text(
        text,
        reply_markup=main_menu_keyboard()
    )


# ============================================================
# MAIN CALLBACK HANDLER
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

        text = (
            
            "Which Category Do You Want?\n"
            
        )

        await query.edit_message_text(
            text=text,
            reply_markup=main_menu_keyboard()
        )

        return

    # --------------------------------------------------------
    # CATEGORY
    # --------------------------------------------------------

    if data in CATEGORY_DETAILS:

        category = CATEGORY_DETAILS[data]

        text = (
            f"📢 {category['name']}\n\n"
            f"{category['text']}\n\n"
            f"Telegram Link:\n"
            f"https://t.me/{YOUR_USERNAME}"
        )

        # Save selected category so Back can return here
        context.user_data["selected_category"] = data

        await query.edit_message_text(
            text=text,
            reply_markup=category_keyboard()
        )

        return

    # --------------------------------------------------------
    # PAYMENT MENU
    # --------------------------------------------------------

    if data == "payment_menu":

        text = (
            "💳 Select Your Payment Method"
        )

        await query.edit_message_text(
            text=text,
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
            f"{category['text']}\n\n"
            f"Telegram Link:\n"
            f"https://t.me/{YOUR_USERNAME}"
        )

        await query.edit_message_text(
            text=text,
            reply_markup=category_keyboard()
        )

        return

    # --------------------------------------------------------
    # BINANCE
    # --------------------------------------------------------

    if data == "payment_binance":

        await query.edit_message_text(
            text=BINANCE_DETAILS,
            reply_markup=payment_page_keyboard()
        )

        return

    # --------------------------------------------------------
    # PAYPAL
    # --------------------------------------------------------

    if data == "payment_paypal":

        await query.edit_message_text(
            text=PAYPAL_DETAILS,
            reply_markup=payment_page_keyboard()
        )

        return

    # --------------------------------------------------------
    # REMITLY
    # --------------------------------------------------------

    if data == "payment_remitly":

        await query.edit_message_text(
            text=REMITLY_DETAILS,
            reply_markup=payment_page_keyboard()
        )

        return

    # --------------------------------------------------------
    # QR
    # --------------------------------------------------------

    if data == "payment_qr":

        await query.edit_message_text(
            text=QR_DETAILS,
            reply_markup=payment_page_keyboard()
        )

        return

    # --------------------------------------------------------
    # UPI
    # --------------------------------------------------------

    if data == "payment_upi":

        await query.edit_message_text(
            text=UPI_DETAILS,
            reply_markup=payment_page_keyboard()
        )

        return

    # --------------------------------------------------------
    # REVOLUT
    # --------------------------------------------------------

    if data == "payment_revolut":

        await query.edit_message_text(
            text=REVOLUT_DETAILS,
            reply_markup=payment_page_keyboard()
        )

        return

    # --------------------------------------------------------
    # CRYPTO
    # --------------------------------------------------------

    if data == "payment_crypto":

        await query.edit_message_text(
            text=CRYPTO_DETAILS,
            reply_markup=payment_page_keyboard()
        )

        return

    # --------------------------------------------------------
    # ALL PACKAGE
    # --------------------------------------------------------

    if data == "all_package":

        text = PACKAGE_DETAILS

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
            text=text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

        return

    # --------------------------------------------------------
    # HELPLINE
    # --------------------------------------------------------

    if data == "helpline":

        text = (
            "❓ Need Help?\n\n"
            "Contact:\n"
            f"https://t.me/{YOUR_USERNAME}"
        )

        await query.edit_message_text(
            text=text,
            reply_markup=helpline_keyboard()
        )

        return


# ============================================================
# ERROR HANDLER
# ============================================================

async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE
):

    print(
        f"Error: {context.error}"
    )


# ============================================================
# RUN BOT
# ============================================================

def main():

    if BOT_TOKEN == "YOUR_BOT_TOKEN":
        print("❌ Please add your Bot Token in BOT_TOKEN.")
        return

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    # /start
    app.add_handler(
        CommandHandler("start", start)
    )

    # All inline buttons
    app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    # Error handler
    app.add_error_handler(error_handler)

    print("🤖 Bot is running...")

    # Polling
    app.run_polling()


if __name__ == "__main__":
    main()