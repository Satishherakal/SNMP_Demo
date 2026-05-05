from groq import Groq
import re
import platform
import socket
import psutil
import time

# 🔑 Put your Groq API key here
client = Groq(api_key="YOUR_GROQ_API_KEY")


# 🔹 STEP 1: LLM → OID (simulation)
def get_oid_from_llm(query):
    prompt = f"""
    Convert the following user query into a valid SNMP OID.
    Only return the OID number.

    Examples:
    system uptime → 1.3.6.1.2.1.1.3.0
    system name → 1.3.6.1.2.1.1.5.0
    system description → 1.3.6.1.2.1.1.1.0

    Query: {query}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message.content

    # Extract only OID
    match = re.search(r'(\d+(\.\d+)+)', text)
    return match.group(1) if match else None


# 🔹 STEP 2: Simulated SNMP GET using local system data
def get_local_data(query):
    query = query.lower()

    if "name" in query:
        return socket.gethostname()

    elif "uptime" in query:
        uptime_seconds = time.time() - psutil.boot_time()
        return f"{int(uptime_seconds)} seconds"

    elif "system" in query or "os" in query:
        return platform.system() + " " + platform.release()

    elif "cpu" in query:
        return f"{psutil.cpu_percent()}%"

    elif "memory" in query:
        mem = psutil.virtual_memory()
        return f"{mem.percent}% used"

    else:
        return "Sorry, I cannot fetch that."


# 🔹 MAIN PROGRAM
if __name__ == "__main__":
    query = input("Ask your network query: ")

    # LLM generates OID
    oid = get_oid_from_llm(query)

    if oid:
        print("✅ Generated OID:", oid)
    else:
        print("⚠️ Could not generate OID")

    # Get local system data
    result = get_local_data(query)

    print("📡 Result:", result)