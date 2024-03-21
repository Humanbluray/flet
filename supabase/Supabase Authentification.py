import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()

# Initialization. with the .env file
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# sign up___________________________________________________________
email = "vantech.infos@gmail.com"
password = "pass1234"
session = supabase.auth.sign_up({"email": email, "password": password})

# sign in ______________________________________________________________
# email = "vante@gmail.com"
# password = "pass1234"
# try:
#     user = supabase.auth.sign_in_with_password({"email": email, "password": password})
# except Exception as ex:
#     print(ex)


