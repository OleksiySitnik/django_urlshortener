from string import ascii_letters, digits
from .models import Url

CHARS = ascii_letters + digits


def generate_key(alphabet=CHARS):
    last_id = Url.objects.last()
    print(last_id)

    length = len(alphabet)
    result = ''

    # while url_id:
    #     url_id, mod = divmod(url_id, length)
    #     result = alphabet[mod - 1] + result
    #
    # return result

if __name__ == "__main__":
    generate_key()

