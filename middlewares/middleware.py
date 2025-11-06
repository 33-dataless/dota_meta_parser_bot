from aiogram import BaseMiddleware
from aiogram.types import Update
from typing import Callable, Dict, Any, Awaitable
from database.messages import messages

class DataBaseMiddleWare(BaseMiddleware):
    async def __call__(
            self, 
            handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: Dict[str, Any]
    ) -> Any:
        if event.message:
            user_id = event.message.from_user.id
            name_user = event.message.from_user.first_name
            text_user = event.message.text
            messages(user_id=user_id, message=text_user, name=name_user)
        return await handler(event, data)