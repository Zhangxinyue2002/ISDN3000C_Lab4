import socket
import time
import json

# --- TODO: Configure these values --- #
SERVER_IP = '192.168.127.10'  # The IP address of your RDK-X5
SERVER_PORT = 9999
REQUEST_MESSAGE = "GET_DATA" # The message your server expects
# --- END OF TODO --- #

def run_client():
    while True:
        print("-" * 30)
        print(f"Attempting to connect to {SERVER_IP}:{SERVER_PORT}...")
        try:
            print("Connected to the server.")
            # --- TODO: YOUR CODE GOES HERE --- #
            # 1. Create a socket object.
            # 2. Use a 'with' statement for automatic cleanup.
            # 3. Connect to the server.
            # 4. Send the REQUEST_MESSAGE, encoded to bytes.
            # 5. Receive the response from the server (e.g., up to 4096 bytes).
            # 6. Decode the response from bytes to a string.
            # 7. (Recommended) If you used JSON, parse the string into a dictionary.
            #    Example: data = json.loads(response_string)
            # 8. Print the received data in a user-friendly format.
            # --- END OF TODO --- #

        except ConnectionRefusedError:
            print("Connection failed. Is the server running?")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Wait for 60 seconds before the next request
        print("\nWaiting for 60 seconds...")
        time.sleep(60)

if __name__ == "__main__":
    run_client()
