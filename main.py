import uvicorn
from create_app import app

if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=8001, reload=True)
