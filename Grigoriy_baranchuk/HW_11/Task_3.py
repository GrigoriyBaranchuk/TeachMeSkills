import re

x = "'grigoriy_baranchuk@gmail.com"


def email_is_correct(email: str) -> bool:
    split_email = email.split("@")
    if email.count("@") != 1:
        return False
    else:
        pattern_email_name = r"[^\.][^@А-Яа-я]+[^\.]"
        pattern_hostname = r"[\w\d-]+\.[\w\d-]+"
        if (re.fullmatch(pattern_email_name, split_email[0]) and re.fullmatch(pattern_hostname, split_email[1]))\
                and len(split_email[1]) <= 63:
            return True
        else:
            return False


print(email_is_correct(x))
