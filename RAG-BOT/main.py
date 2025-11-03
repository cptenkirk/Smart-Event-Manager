# main.py

from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from vector import retriever # Importiert den Retriever aus vector.py

# Die LLM-Instanz (wird im Code als 'llm' verwendet)
llm = OllamaLLM(model="llama3.1")

print()
print('Bot is running...')

# --- 1. Hilfsfunktion zur Formatierung der Dokumente ---
# Der Retriever gibt eine Liste von Dokumenten zurück. Das LLM benötigt einen String.
def format_docs(docs):
    # Wir fügen die page_content aller abgerufenen Dokumente zusammen
    return "\n\n".join(doc.page_content for doc in docs)

# --- 2. Prompt-Template definieren ---
# Verwende {context} als Platzhalter für den formatierten Text
template = """
Du bist ein hilfsbereiter Assistent, der Fragen des Benutzers auf der Grundlage des bereitgestellten Kontextes beantwortet.
Antworte kurz und prägnant.

Verwende den folgenden Kontext:
{context}

Frage: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# --- 3. Die korrigierte RAG-Kette definieren ---

# Die Kette wird einmal definiert und enthält die gesamte Logik (Retriever, Formatierung, Prompt, LLM)

rag_chain = (
    # Die Eingabe wird aufgeteilt in 'context' und 'question'
    {
        "context": retriever | format_docs, # 1. Retriever läuft, 2. Ergebnis wird formatiert
        "question": RunnablePassthrough()   # Die Benutzerfrage wird als 'question' weitergegeben
    }
    | prompt                            # Prompt-Template wird mit context und question befüllt
    | llm                               # Der fertige Prompt wird an das LLM gesendet
    | StrOutputParser()                 # Die Ausgabe des LLM wird in einen einfachen String umgewandelt
)


# --- 4. Interaktive Abfrage starten ---

while True:
    print("\n\n-----------------------------------------------------------------------")
    question = input("Ask a question (x to exit): ")
    print("\n\n")
    if question == "x":
        break

    # Wir rufen die Kette (rag_chain) nur einmal mit der Frage auf. 
    # Die Kette kümmert sich intern um den Retriever-Aufruf!
    print("... Antwort wird generiert ...")
    try:
        result = rag_chain.invoke(question) 
        print(result)
    except Exception as e:
        print(f"❌ FEHLER: {e}")
        print("Stelle sicher, dass der Ollama-Server läuft (Befehl: ollama serve).")
    
    print()