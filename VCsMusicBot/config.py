from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN", "1653789420:AAG24i9nE699rwpF6sMlY74-SlkgW1zap0Y")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ZauteKm")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/b99c523f09e87933846e9.png")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "VCsMusicPlayer")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "tgVCSets")
PROJECT_NAME = getenv("PROJECT_NAME", "VCsMusicBot")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/LushaiMusic/VCsMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
