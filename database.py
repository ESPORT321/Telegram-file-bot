from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)

db = client["TelegramFileBot"]

users = db["users"]
files = db["files"]
banned = db["banned"]
settings = db["settings"]
