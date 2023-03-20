import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title='keycap-store'
)

if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)