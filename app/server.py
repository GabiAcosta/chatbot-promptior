from fastapi import FastAPI
from langserve import add_routes
from rag_conversation import chain as rag_conversation_chain


app = FastAPI()

add_routes(app, rag_conversation_chain, path="/rag-conversation")


@app.get("/")
def root():
    return {
        "message": "Welcome to the langserve server! More information and routes can be found at /docs. 🦜 🏓",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
