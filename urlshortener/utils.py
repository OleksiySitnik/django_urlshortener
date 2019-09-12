from string import ascii_letters, digits
from .models import Url

CHARS = ascii_letters + digits


def generate_key(alphabet=CHARS):
    last_id = len(Url.objects.all()) + 1

    print(last_id)

    length = len(alphabet)
    result = ''

    while last_id:
        last_id, mod = divmod(last_id, length)
        result = alphabet[mod - 1] + result

    return result



