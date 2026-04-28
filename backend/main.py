from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserSignup(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

@app.post("/signup")
async def signup(user: UserSignup):
    # Mock signup logic
    print(f"Signing up user: {user.name} ({user.email})")
    return {"message": f"Successfully signed up {user.name}!"}

@app.post("/login")
async def login(user: UserLogin):
    # Mock login logic
    print(f"Logging in user: {user.email}")
    # Simple mock check
    if user.email == "error@example.com":
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Successfully signed in!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
