# IoT Gateway with AI Chat Capabilities

## Project Overview
This is an IoT gateway server that integrates DeepSeek AI for intelligent chat responses and fortune-based message generation. The server is built using Python socket programming and can handle multiple client connections simultaneously, providing responses with ASCII art visualization using Pokemon characters.

## Features
- Multi-threaded server for concurrent client connections
- DeepSeek AI integration for intelligent chat responses
- ASCII art output using Pokemon characters
- Secure API key management using environment variables

## Prerequisites
- Python 3.8+
- Pokemonsay for ASCII art generation
- DeepSeek API key (More details in later section)

## Installation

### 1. System Dependencies
Install the required system packages:

# Install Pokemonsay (https://github.com/possatti/pokemonsay)


### 2. Python Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
We provided a `.env` file in the project root and simplely add your DeepSeek API key:
Here is a free DeepSeek API website, its only for personal use: (https://github.com/chatanywhere/GPT_API_free?tab=readme-ov-file)
```
DEEPSEEK_API_KEY="your-api-key-here"
```

## Project Structure
- `deepseek_pokemon.py`: Main server implementation with DeepSeek AI -- Run this on the RDK platform.
- `monitoring_client.py`: Network monitoring client template
- `requirements.txt`: Python package dependencies
- `.env`: Deepseek API key configuration

## Usage

### Server Setup
Run the server on RDK:
```bash
# Start AI chat server
python deepseek_pokemon.py
```

### Client Connection
1. Update SERVER_IP in client files to match your RDK-X5 IP (default: '192.168.127.10')
2. Run the client:
```bash
python "monitoring_client.py"
```

## Network Settings
- Server Host: 0.0.0.0 (all interfaces)
- Default Port: 9999
- Protocol: TCP/IP (IPv4)

## Network Setup and Data Format

### Network Configuration
- RDK Platform (Server):
  - IP Address: 192.168.127.10
  - Port: 9999
  - Network Interface: All interfaces (0.0.0.0)
  - Connection Type: TCP/IP

- Client Side:
  - Connects to RDK's IP (192.168.127.10)
  - Uses same port (9999)
  - Supports multiple simultaneous connections

### Data Format
- Client to Server:
  - Plain text messages encoded in UTF-8
  - Maximum message size: 1024 bytes
  - No special formatting required

- Server to Client:
  - AI responses formatted with Pokemon ASCII art
  - UTF-8 encoded responses
  - Response includes:
    - AI-generated text (via DeepSeek API)
    - ASCII art visualization
  - Maximum response size: 4096 bytes

## Security Notes
- Keep your DeepSeek API key confidential
- The `.env` file is excluded from version control
- Use secure network configurations in production