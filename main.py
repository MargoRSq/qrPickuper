from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='instorify-api',
              version='1.0.0', docs_url="/docs")

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/urls/{id}")
async def get_sm(id: int):
    return {"urls": [
                     'https://t.me/iamsvyatoslav',
                     'https://www.instagram.com/vi_latyshev/',
                     'https://vk.com/inwhs'
                    ]}
