import random
import string


def code_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=8):
    new_code = code_generator(size=size)
    class_url = instance.__class__
    code_exists = class_url.objects.filter(shortcode=new_code).exists()
    if code_exists:
        return create_shortcode(instance, size=size)
    return new_code
