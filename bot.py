import discord
from discord.ext import commands
import sqlite3
import asyncio
import config

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)

# SQLite veritabanı 
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL DEFAULT 0
    )
""")
conn.commit()

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} olarak giriş yaptı!')

# Yeni bir görev ekler
@bot.command()
async def add_task(ctx, *, description):
    cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
    conn.commit()
    await ctx.send(f"✅ Görev eklendi: {description}")


# Belirtilen Id ye sahip görevi siler
@bot.command()
async def delete_task(ctx, task_id: int):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    await ctx.send(f"🗑 Görev silindi: ID {task_id}")

# Tüm görevleri gösterme
@bot.command()
async def show_tasks(ctx):
    cursor.execute("SELECT id, description, completed FROM tasks")
    tasks = cursor.fetchall()
    if not tasks:
        await ctx.send("📭 Hiç görev yok.")
    else:
        response = "\n".join([f"🔹 **ID {task[0]}** - {task[1]} {'✅' if task[2] else '❌'}" for task in tasks])
        await ctx.send(response)



@bot.command()
async def complete_task(ctx, task_id: int):
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    await ctx.send(f"✅ Görev tamamlandı: ID {task_id}")

bot.run(config.BOT_TOKEN) 
