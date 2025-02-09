if __name__ == "__main__":
    import uvicorn

    uvicorn.run("fastapi_backend_app:app", reload=False,
                port=8990, host="0.0.0.0")
