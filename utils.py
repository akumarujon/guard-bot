def is_msg_from_admin(chat_id, user_id, bot):
    status = ['creator','administrator']

    member_status = bot.get_chat_member(chat_id,user_id)

    return member_status.status in status

def is_bot_admin(chat_id, user_id, bot):
    status = ['administrator']

    member_status = bot.get_chat_member(chat_id, user_id)

    return member_status.status in status