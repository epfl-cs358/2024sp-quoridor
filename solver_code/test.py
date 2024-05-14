import serial
import time

# Open serial port
ser = serial.Serial('COM4', 9600, timeout=1)

try:
    while True:
        # Read bytes from Arduino
        received_bytes = ser.readline()
        
        # Check if any bytes were received
        if received_bytes:
            print("Received from Arduino:", received_bytes)
            # Convert bytes to string (assuming ASCII encoding)
            # received_message = received_bytes.decode().strip()
            
            # # Print received message
            # print("Received from Arduino:", received_message)
            
            # # Send response to Arduino
            response_message = "Message received: "
            # ser.write(response_message.encode())
        
        # Wait for a moment before sending next message
        time.sleep(1)
finally:
    ser.close()