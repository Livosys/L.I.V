from fastapi.middleware.cors import CORSMiddleware

def apply_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "https://shix.livosys.se",
            "https://shix-aide.lovable.app",
            "https://id-preview-7f5f44a6-0e88-4f1a-8120-4ac3ee40225d.lovable.app"
        ],
        allow_credentials=True,
        allow_methods=["GET", "POST", "OPTIONS"],
        allow_headers=["*"],
    )
