import re

MAIN_FILE = "main.py"

with open(MAIN_FILE, "r") as f:
    content = f.read()

# Add import if missing
if "from ai_chat.chat_rag import router as chat_rag_router" not in content:
    content = (
        "from ai_chat.chat_rag import router as chat_rag_router\n" +
        content
    )

# Inject router include if missing
if "app.include_router(chat_rag_router, prefix=\"/ai\")" not in content:
    # Add call after first occurrence of app = FastAPI()
    content = re.sub(
        r"(app\s*=\s*FastAPI\s*\(\s*\

cd /home/shix.livosys.se/backend

# Backup of main.py
cp main.py main_backup_before_rag_ai.py

# Ensure ai_chat exists
mkdir -p ai_chat

# Patch main.py automatically
cat << 'EOF' > patch_main.py
import re

MAIN_FILE = "main.py"

with open(MAIN_FILE, "r") as f:
    content = f.read()

# Add import if missing
if "from ai_chat.chat_rag import router as chat_rag_router" not in content:
    content = (
        "from ai_chat.chat_rag import router as chat_rag_router\n" +
        content
    )

# Inject router include if missing
if "app.include_router(chat_rag_router, prefix=\"/ai\")" not in content:
    # Add call after first occurrence of app = FastAPI()
    content = re.sub(
        r"(app\s*=\s*FastAPI\s*\(\s*\))",
        r"\1\napp.include_router(chat_rag_router, prefix=\"/ai\")",
        content
    )

with open(MAIN_FILE, "w") as f:
    f.write(content)

print("✔ main.py patched successfully!")
print("✔ Backup saved as main_backup_before_rag_ai.py")
