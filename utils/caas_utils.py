from validate_email import validate_email


def remove_spaces_if_exist(entry):
    return entry.replace(" ", "")


def normalize_email(email):
    email = remove_spaces_if_exist(email)
    if validate_email(email):
        return email.lower()
    return False
