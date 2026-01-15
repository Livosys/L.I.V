from fastapi.middleware.cors import CORSMiddleware

def lock_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["https://shix.livosys.se"],
        allow_credentials=True,
        allow_methods=["POST","GET"],
        allow_headers=["Authorization","Content-Type"]
    )
