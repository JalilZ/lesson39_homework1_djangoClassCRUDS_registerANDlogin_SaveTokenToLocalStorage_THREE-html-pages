from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Student

admin.site.register(Student)




# username: jalil
# email: jalil@fake.com
# password: jalilpython

# Authentication1 (back-end server):
# http://127.0.0.1:8000/login/
# username: jalil
# password: jalilpython 
# >>>>>>>>>>>>>
# HTTP 200 OK
# Allow: POST, OPTIONS
# Content-Type: application/json
# Vary: Accept
#
# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NjI0MTA5MywiaWF0IjoxNjc4NDY1MDkzLCJqdGkiOiI2ZTM1NDA2NjQxMTU0NWYzOTYwMTc3NzU2MDQ2OTgxZCIsInVzZXJfaWQiOjF9.iLHiETPKNcFPNIUyztOoKQoNz3rirBI0eAD5HaUyAEU",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4NDY1OTkzLCJpYXQiOjE2Nzg0NjUwOTMsImp0aSI6ImRjNDY3MTEzNWJmZjQzNGFiZDViNzNiZjU2NmU5OGE1IiwidXNlcl9pZCI6MX0.oQ_DjAvxARrsQLuglsl1LZPxPQiYKqOr3jGY-qfliX4"
# }


# Authentication2 (THUNDER):
# see in obsidian lesson 38