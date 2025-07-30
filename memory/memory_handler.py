import json
import os

MEMORY_FILE = "memory/memory.json"

def is_duplicate(answer: str) -> bool:
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            memory = json.load(f)
            return any(entry["answer"].strip() == answer.strip() for entry in memory)
    except:
        return False

def save_to_memory(entry: dict):
    try:
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                memory = json.load(f)
        else:
            memory = []
        memory.append(entry)
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(memory, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print("[Memory Save Error]", e)
