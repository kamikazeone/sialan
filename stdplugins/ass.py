from telethon import events
import asyncio
from collections import deque
from userbot.events import register

@register(outgoing=True, pattern="^.ass")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("Assalamualaikum"))
	for _ in range(50):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
