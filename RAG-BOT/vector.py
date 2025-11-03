# vector.py

from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from docx import Document as DocxDocument
import os
from langchain_ollama.llms import OllamaLLM 


def get_full_docx_text(filename):
    """Extrahiert den gesamten Fließtext aus einer DOCX-Datei."""
    doc = DocxDocument(filename)
    fullText = []
    
    
    for para in doc.paragraphs:
        fullText.append(para.text)
        
    return '\n'.join(fullText)


docx_file_path = r"C:\Users\admin\Desktop\datafeeding\INTRO.docx"
try:
    full_text_content = get_full_docx_text(docx_file_path)
except Exception as e:
    print(f"FEHLER: Konnte DOCX-Datei nicht lesen: {e}")
    # Fallback für leeres Dokument, um den Start zu ermöglichen
    full_text_content = "Kein Dokumenteninhalt gefunden."

# Erstellung der Dokumentenliste mit dem gesamten Text
documents = [
    Document(
        page_content=full_text_content,
        metadata={"source": docx_file_path}
    )
]

# --- 3. Initialisierung und Indizierung ---
embeddings = OllamaEmbeddings(model="llama3.1")
llm = OllamaLLM(model="llama3.1") # LLM für die Nutzung in main.py exportieren

db_location = "chroma_db"

# Überprüfen, ob der Vektorspeicher bereits existiert
# Wenn der Ordner nicht existiert, müssen wir die Dokumente hinzufügen.
add_documents = not os.path.exists(db_location) 

# Chroma-Instanz erstellen/laden
vector_store = Chroma(
    collection_name="reviews_collection",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents: 
    print(f"Erstelle Vektorspeicher in '{db_location}' und füge Dokumente hinzu...")
    
    # Fügt das EINE Dokument (aus dem DOCX-Text) hinzu.
    vector_store.add_documents(documents=documents)
    
    # Erstellt den Ordner, um anzuzeigen, dass der Index existiert
    if not os.path.exists(db_location):
        os.makedirs(db_location)
else:
    print(f"Lade bestehenden Vektorspeicher aus '{db_location}'...")

# --- 4. Retriever exportieren ---
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)