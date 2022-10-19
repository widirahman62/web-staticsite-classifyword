from fastapi import FastAPI, HTTPException
from typing import List 
from starlette.middleware.cors import CORSMiddleware 
from db import session 
from model import Words 



app = FastAPI(docs_url="/", redoc_url=None)

@app.get('/{word}')
async def index(word: str):
    data=session.query(Words).filter(Words.kata == word).first()
    # if data exist
    if data is not None:
        return data
    else:
        raise HTTPException(status_code=404, detail=f"Word {word} not found")

origins=[
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
