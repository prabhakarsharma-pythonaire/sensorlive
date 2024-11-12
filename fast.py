from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

# Define the root endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello, I'm Prabhakar!"}
