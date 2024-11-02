from django.db import models
import random
import string

# Function to generate a unique code for the room
def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break

    return code

# Room model
class Room(models.Model):  # Corrected models.Model
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True)  # Generates unique code
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)  # Corrected field name to guest_can_pause
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)  # Corrected field name to created_at



