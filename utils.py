from os import stat


def is_msg_from_admin(chat_id, user_id, bot):
    status = ['owner','administrator']

    member_status = bot.get_chat_member(chat_id,user_id)
    
    return member_status.status in status