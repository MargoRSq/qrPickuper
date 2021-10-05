from fastapi import FastAPI

app = FastAPI(title='instorify-api',
              version='1.0.0', docs_url="/docs")


@app.get("/urls/{id}")
async def get_sm(id: int):
    return {"urls": [
                     'https://t.me/iamsvyatoslav',
                     'https://www.instagram.com/vi_latyshev/',
                     'https://vk.com/inwhs'
                    ]}
