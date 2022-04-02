import os
from dotenv import load_dotenv

load_dotenv()

uname = os.getenv('USERNAME')
pword = os.getenv('PASSWORD')

print(uname, pword)