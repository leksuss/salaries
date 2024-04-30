from fastapi import FastAPI


app = FastAPI()

@app.get('/calculate')
async def calculate(num1: int, num2: int):
    return {'result': num1 * num2}

@app.get('/custom')
def read_custom_message():
    return {'message': 'This is a custom message!'}