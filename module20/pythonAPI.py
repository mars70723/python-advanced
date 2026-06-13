# {
#   "name": "Arianita",
#   "age": "23",
#   "address": {
#     "Country": "Kosova",
#     "City": "Prishtine",
#     "ZIP Code": "10000",
#     "Street": "Rruga B"
#   },
#   "contacts":[
#     {
#       "type": "email",
#       "value": "arianita@gmail.com"
#     },
#     {
#       "type": "phone",
#       "value": "+38344123456"
#     },
#     {
#       "type": "Linkedin",
#       "value": "Arianita"
#     }
#   ]
# }

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return {"message": "Hello World"}