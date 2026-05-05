# SNMP Demo Project 📡

A Python-based demonstration of using Large Language Models (LLMs) to bridge natural language queries with network management protocols like SNMP.

## 🚀 Overview

This project showcases a simple pipeline where:
1. **User Query**: A user asks a network-related question in plain English (e.g., "What is the system uptime?").
2. **LLM Reasoning**: The query is sent to a Groq-powered LLM (Llama 3.1) to translate the request into a standard **SNMP Object Identifier (OID)**.
3. **Data Retrieval**: The program then simulates an SNMP GET request by fetching real-time telemetry from the local system (CPU, Memory, Uptime, etc.) based on the identified query.

## ✨ Features

- **Natural Language Processing**: Translates human language into technical OIDs using Groq AI.
- **System Telemetry**: Real-time retrieval of:
  - System Uptime
  - OS Description
  - CPU Usage
  - Memory Statistics
  - Hostname
- **Simulated SNMP Logic**: Demonstrates how an AI agent can interact with network devices.

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.x
- [Groq API Key](https://console.groq.com/keys)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Satishherakal/SNMP_Demo.git
   cd SNMP_Demo
   ```
2. Install dependencies:
   ```bash
   pip install groq psutil
   ```

3. Update your API Key:
   Open `main.py` and replace `YOUR_GROQ_API_KEY` with your actual Groq key.

## 🏃 Usage

Run the main script:
```bash
python main.py
```

Enter a query when prompted:
- *"What is the CPU usage?"*
- *"Tell me the system name"*
- *"Show me the memory status"*

## 📂 Project Structure

- `main.py`: Core logic for LLM interaction and system data fetching.
- `SNMP_Program.zip`: Compressed version of the source code.

---
*Created for SNMP Lab demonstration purposes.*
