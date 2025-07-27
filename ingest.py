import os
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

PDF_FOLDER = "pdfs"
VECTOR_FOLDER = "vectorstore"
CHUNK_SIZE = 500  # words per chunk
CHUNK_OVERLAP = 100

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

def split_into_chunks(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def main():
    all_chunks = []
    sources = []

    print("🔍 Scanning PDFs...")
    for filename in os.listdir(PDF_FOLDER):
        if not filename.endswith(".pdf"):
            continue
        path = os.path.join(PDF_FOLDER, filename)
        text = extract_text_from_pdf(path)
        chunks = split_into_chunks(text)
        all_chunks.extend(chunks)
        sources.extend([filename] * len(chunks))

    print(f"✅ Found {len(all_chunks)} text chunks")

    print("📐 Generating embeddings...")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(all_chunks)

    print("💾 Storing in FAISS...")
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    faiss.write_index(index, os.path.join(VECTOR_FOLDER, "store.faiss"))
    with open(os.path.join(VECTOR_FOLDER, "chunks.pkl"), "wb") as f:
        pickle.dump(all_chunks, f)

    with open(os.path.join(VECTOR_FOLDER, "sources.pkl"), "wb") as f:
        pickle.dump(sources, f)

    print("🎉 Done! Your agent's brain is ready.")
  

if __name__ == "__main__":
    main()

