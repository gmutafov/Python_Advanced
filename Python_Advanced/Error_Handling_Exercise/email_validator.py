from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


VALID_DOMAINS = ('com', 'org', 'net', 'bg')
MIN_SYMBOLS = 4

pattern_name = r'\w+'

email = input()

while email != 'End':

    if email.count('@') > 1:
        raise MoreThanOneAtSymbolError("Email should contain only one @ symbol!")
    if '@' not in email:
        raise MustContainAtSymbolError(f"Must contain @!")
    if len(email.split('@')[0]) <= MIN_SYMBOLS:
        raise NameTooShortError("Name must be more than 4 characters")
    if email.split('.')[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + d for d in VALID_DOMAINS)}")
    if findall(pattern_name, email.split('@')[0])[0] != email.split('@')[0]:
        raise InvalidNameError("Name must contain only letters, digits and underscores!")

    print('Email is valid')

    email = input()