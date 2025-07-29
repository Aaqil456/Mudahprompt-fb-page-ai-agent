import os
from agent.easypeasy_client import query_easypeasy
from agent.gemini_translator import rewrite_with_gemini
from agent.facebook_poster import post_to_facebook
from prompts.question_generator import generate_question
from memory.memory_handler import is_duplicate, save_to_memory
from datetime import datetime

def main():
    question = generate_question()
    raw_answer = query_easypeasy(question)

    if not raw_answer or is_duplicate(raw_answer):
        print("Skipped: empty or duplicate content.")
        return

    fb_post = rewrite_with_gemini(raw_answer)
    post_to_facebook(fb_post)

    save_to_memory({
        "question": question,
        "answer": raw_answer,
        "translated_post": fb_post,
        "timestamp": datetime.now().isoformat()
    })

if __name__ == "__main__":
    main()

