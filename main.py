from fastapi import FastAPI
from app.routers.auth import router as auth
from app.routers.api import router as api
from app.models.database import Base,engine
from app.models.user import User
from app.models.invoice import Invoice 
from app.models.permission import Permission
from fastapi.middleware.cors import CORSMiddleware
from app.api.services.auth.auth import hash_password
from sqlalchemy import event

#Base.metadata.create_all(bind=engine)
origins = [
    "http://localhost:5173",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:2222",
    "http://app.superappcanari.com",
    "https://app.superappcanari.com",
    "app.superappcanari.com"
]
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


INITIAL_DATA = {
      'users': [
            {
                  'username': 'fahmi015',
                  'avatar': 'avatar1.png',
                  'first_name':'Mohcen',
                  'last_name':'Fahmi',
                  'password': hash_password('password')
            },
      ],
      'permissions':[
          {
              'name':'users'
          },
          {
              'name':'budgets'
          },
          {
              'name':'tasks'
          },
          {
              'name':'notes'
          },
          {
              'name':'calendar'
          },
      ]
}

def initialize_table(target, connection, **kw):
    tablename = str(target)
    if tablename in INITIAL_DATA and len(INITIAL_DATA[tablename]) > 0:
        connection.execute(target.insert(), INITIAL_DATA[tablename])

event.listen(User.__table__, 'after_create', initialize_table)


@app.on_event("startup")
def configure():
    print("create tables")
    Base.metadata.create_all(bind=engine)
    
app.include_router(auth)
app.include_router(api)
