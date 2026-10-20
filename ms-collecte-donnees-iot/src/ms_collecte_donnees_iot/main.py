from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def main():
    return {"Succes" : "Welcome To Novaria Collecte IoT"}