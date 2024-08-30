from db_config import Message
from read_all import display_all_message


def update_message():
    display_all_message()

    msg = Message.get_by_id(1)
    msg.user = "Tom Cruise"
    msg.save()

    display_all_message()


if __name__ == "__main__":
    update_message()
