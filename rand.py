import random
import secrets
import string

# Standard random string
length = 1000
random_string = "".join(random.choices(string.ascii_letters + string.digits, k=length))
print(random_string)

# Cryptographically secure random string
secure_string = "".join(
    secrets.choice(string.ascii_letters + string.digits) for _ in range(length)
)
