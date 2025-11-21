# Impact Listener

`impact-listener` is an event-driven microservice designed to listen for "impact" domain events, process them, and emit or store the processed data. This makes it easy to build reactive systems that respond to domain events in real time.

---

## Table of Contents

- [Features](#features)  
- [Architecture](#architecture)  
- [Tech Stack](#tech-stack)  
- [Directory Structure](#directory-structure)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Running](#running)  
- [Configuration](#configuration)  
- [Usage](#usage)  
- [Event Flow](#event-flow)  
- [Testing](#testing)  
- [Docker Support](#docker-support)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)

---

## Features

- Listens for domain events (e.g., via HTTP/webhook, message queue, or other event source)  
- Validates and transforms incoming payloads  
- Allows custom handler logic for different event types  
- Optionally forwards processed events to downstream systems  
- Lightweight, modular, and extensible  

---

## Architecture

┌────────────────────────────┐
│ Event Source / Broker │
│ (Kafka, Webhook, MQ etc.) │
└──────────────┬─────────────┘
│
▼
┌───────────────────────┐
│ Impact Listener │
│ - Receives events │
│ - Validates payload │
│ - Applies business logic│
│ - Emits or stores data │
└──────────────┬────────┘
│
▼
┌────────────────────────┐
│ Downstream / Storage │
│ (DB, other service, log)│
└────────────────────────┘

yaml

---

## Tech Stack

- Python (or your language of choice)  
- Lightweight HTTP server or consumer library  
- Configurable event handler modules  
- (Optional) Docker for containerization  

---

## Directory Structure

Here is a sample structure for the listener service:

impact-listener/
├── main.py # Entry point, starts listener
├── handlers/ # Logic for different event types
├── config/ # Configuration files / environment settings
├── utils/ # Utility functions (parsing, validation, logging)
├── requirements.txt # Required Python packages
└── Dockerfile # Dockerfile to build container

yaml

---

## Getting Started

### Prerequisites

- Python 3.7+  
- `pip`  
- (Optional) Docker  

### Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/simpsonorg/impact-listener.git
   cd impact-listener
(Optional) Create and activate a virtual environment:

bash
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
pip install -r requirements.txt
Running
To run the listener locally:

bash
python main.py
Make sure your event source (e.g., webhook, broker) is correctly configured to send to this service.

Configuration
Use configuration (via environment variables or config files) for:

Event source endpoint or broker URL

Logging level

Handler options (e.g., which handlers to enable)

Retry or error policies

Example (env variables):

ini
Copy code
EVENT_SOURCE_URL=https://my-webhook-endpoint
LOG_LEVEL=INFO
Usage
Start the listener

Send domain event payloads from your event source

The service will dispatch them to the appropriate handler

Processed data can be logged, stored, or forwarded

Event Flow
Example of an "impact" event payload:

json
Copy code
{
  "eventId": "evt-12345",
  "type": "IMPACT_CREATED",
  "timestamp": "2025-11-21T10:00:00Z",
  "data": {
    "source": "systemA",
    "impactScore": 85,
    "details": "High impact detected"
  }
}
Handlers in handlers/ will read this, apply logic, and produce output or side-effects.

Testing
Write unit tests for individual handlers

Test payload validation logic

Use a test client / mock event source to simulate event delivery

If using HTTP endpoint, test with curl or Postman

Example (pytest-style):

python
Copy code
def test_handle_impact_created():
    from handlers.impact import handle_impact_created
    event = { "type": "IMPACT_CREATED", "data": { "impactScore": 90 } }
    result = handle_impact_created(event)
    assert result["status"] == "processed"
Docker Support
Build Docker image:

bash
docker build -t impact-listener .
Run container:

bash
docker run -e EVENT_SOURCE_URL=https://source \
           -e LOG_LEVEL=DEBUG \
           -p 8000:8000 \
           impact-listener
Contributing
Contributions are welcome! Here’s how you can contribute:

Fork the repository

Create a new branch: git checkout -b feature/your-handler

Implement logic or tests

Commit changes: git commit -m "Add handler for new event type"

Push and open a Pull Request

License
This project is licensed under the Citi License.
