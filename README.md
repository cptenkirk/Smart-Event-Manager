<h2>Entwicklung eines KI-gestützten Informations- und Buchungsportals mit RAG-Infrastruktur</h2>

> 🎯 **IHK-Prüfungsstatus:** Dies ist mein offizielles Abschlussprojekt zur IHK-Prüfung als Fachinformatiker für Anwendungsentwicklung. Der **praktische Teil (Projektarbeit, Dokumentation, Präsentation und Fachgespräch) wurde im Juni 2026 erfolgreich bestanden**.

Dieses System kombiniert moderne Webtechnologien mit einer leistungsfähigen Retrieval Augmented Generation (RAG) Architektur auf einem eigenen vServer.





## 📌 Projekt-Übersicht
Dieses System automatisiert den Zugriff auf interne Wissensdatenbanken und koppelt diese mit einer Buchungslogik. 
Kern ist eine **RAG-Infrastruktur (Retrieval Augmented Generation)**, die Halluzinationen des LLMs minimiert.

## 🏗 System-Architektur
Die Anwendung ist modular aufgebaut:
- **Orchestrierungs-Layer:** n8n (Workflow-Automatisierung & Error Handling)
- **AI-Engine:** Ollama via API
- **Vector-Storage:** ChromaDB zur semantischen Indizierung von PDF/Text-Daten
- **Integration:** REST-Schnittstellen zur Anbindung an Drittsysteme

## 🛠 Software Engineering Aspekte
- **Anforderungsmanagement:** Erstellung von Lasten- und Pflichtenheft gemäß IHK-Standard.
- **Datenmodellierung:** Entwurf von Vektor-Einbettungen (Embeddings) und Metadaten-Strukturen.
- **DevOps:** Containerisierung der Komponenten mittels Docker für konsistente Entwicklungsumgebungen.

## 🛠 Tech Stack & Infrastructure
- **Frontend:** Responsive Web-Interface
- **Orchestrierung:** n8n (Self-hosted auf VServer via Docker)
- **KI-Modell:** Ollama via REST-API
- **Datenbank:** Vektorbasierter Speicher für Kontext-Relevanz
- **Reverse Proxy:** Nginx Proxy Manager für SSL & Security

## n8n-Backend Screenshots

- Vectoring

<img width="1908" height="914" alt="image" src="https://github.com/user-attachments/assets/cc2f4553-1737-44a7-9ef6-878a6eb356f3" />

- Ollama-Assistant

<img width="1913" height="919" alt="image" src="https://github.com/user-attachments/assets/3f9c954f-be7b-424e-bbde-69e442abf259" />

- Booking, Database, SMTP and Post

<img width="1912" height="916" alt="image" src="https://github.com/user-attachments/assets/80338a44-2f91-4bff-81f5-5689befd6347" />








