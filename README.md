<h2>Entwicklung eines KI-gestützten Informations- und Buchungsportals mit RAG-Infrastruktur</h2>

Dieses Projekt ist mein offizielles Abschlussprojekt zur IHK-Prüfung als Fachinformatiker für Anwendungsentwicklung. Es kombiniert moderne Webtechnologien mit einer leistungsfähigen Retrieval Augmented Generation (RAG) Architektur.



## 📌 Projekt-Übersicht
Dieses System automatisiert den Zugriff auf interne Wissensdatenbanken und koppelt diese mit einer Buchungslogik. 
Kern ist eine **RAG-Infrastruktur (Retrieval Augmented Generation)**, die Halluzinationen des LLMs minimiert.

## 🏗 System-Architektur
Die Anwendung ist modular aufgebaut:
- **Orchestrierungs-Layer:** n8n (Workflow-Automatisierung & Error Handling)
- **AI-Engine:** Google Gemini Pro via API
- **Vector-Storage:** ChromaDB zur semantischen Indizierung von PDF/Text-Daten
- **Integration:** REST-Schnittstellen zur Anbindung an Drittsysteme

## 🛠 Software Engineering Aspekte
- **Anforderungsmanagement:** Erstellung von Lasten- und Pflichtenheft gemäß IHK-Standard.
- **Datenmodellierung:** Entwurf von Vektor-Einbettungen (Embeddings) und Metadaten-Strukturen.
- **DevOps:** Containerisierung der Komponenten mittels Docker für konsistente Entwicklungsumgebungen.

## 🛠 Tech Stack & Infrastructure
- **Frontend:** Responsive Web-Interface (optimiert für Kiosk-Modus auf Raspberry Pi)
- **Orchestrierung:** n8n (Self-hosted auf VServer via Docker)
- **KI-Modell:** Google Gemini Pro via REST-API
- **Datenbank:** Vektorbasierter Speicher für Kontext-Relevanz
- **Reverse Proxy:** Nginx Proxy Manager für SSL & Security
