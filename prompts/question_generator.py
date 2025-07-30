import random

def generate_question():
    templates = [
        "Bagaimana {topic} boleh bantu dalam kehidupan harian?",
        "Apa manfaat {topic} untuk peniaga kecil?",
        "Kenapa {topic} penting dalam dunia hari ini?",
        "Terangkan penggunaan {topic} dalam bisnes moden.",
        "Apa kesilapan biasa bila guna {topic}?"
    ]

    topics = [
        "AI dalam perniagaan",
        "automasi kerja pejabat",
        "penggunaan chatbot",
        "pengurusan knowledge base",
        "AI untuk media sosial",
        "penghasilan kandungan AI",
        "agen AI pintar",
        "customer service automatik"
    ]

    template = random.choice(templates)
    topic = random.choice(topics)
    return template.format(topic=topic)
