from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Caculadora simples"}

@app.get("/soma")
def soma(num1: int, num2: int):
    return num1 + num2

@app.get("/subtracao")
def subtracao(num1: int, num2: int):
    return num1 - num2

@app.get("/multiplicacao")
def multiplicacao(num1: int, num2: int):
    return num1 * num2

@app.get("/divisao")
def divisao(num1: int, num2: int):
    return num1 / num2

