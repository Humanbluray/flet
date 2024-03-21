import os
from supabase import create_client, Client
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()

# Initialization. with the .env file
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


# CRUD operations ___________________________________
# READ___________________________________________________________
data = supabase.table("todos").select("*").execute()
print(data)
data = supabase.table("todos").select("id, name").execute()
print(data)

# read with filters (filter equlals)
# see others filters in the API description secxtion JAVASCRIPT
# data = supabase.table('todos').select('id, name').eq('name', 'item 1').execute()
# print(data)
#
# # INSERT OR CREATE _________________________________________________________________
# # data = supabase.table('todos').insert({'name': 'item 4'}).execute()
# created_at = str(datetime.utcnow() - timedelta(hours=2))
# new_task = supabase.table('todos').insert({'name': 'item 5', "created_at": created_at}).execute()
#
#
# # UPDATE _____________________________________________________________________
# # updated_task = supabase.table("todos").update({"name": "Todo Task number 2"}).eq("id", 2).execute()
# #
# #
# # # DELETE ___________________________________________________________________________
# # deleted_task = supabase.table('todos').delete().eq('id', 1).execute()


# datas = supabase.table('todos').select('id, name').execute()
# for data in datas:
#     if data[0] == 'data':
#         for row in data[1]:
#             print(row)
#


# AUTHENTIFICATIONS ___________________________________________________________________
