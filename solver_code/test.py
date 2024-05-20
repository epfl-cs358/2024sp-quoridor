import serial
import time

# Open serial port
ser = serial.Serial('COM4', 9600)

try:
    while True:
        # Read bytes from Arduino
        if ser.readable:
            received_bytes = ser.readline()
            
            # Check if any bytes were received
            if received_bytes:
                print("Received from Arduino:", received_bytes)
            
                # # Send response to Arduino
                time.sleep(3)
                response_message = "Message received: "
                sent_message = False
                while(not(sent_message)):
                    if(ser.writable):
                        ser.write(response_message.encode())
                        sent_message = True
                        print("Message sent")
        # Wait for a moment before sending next message
        time.sleep(1)
finally:
    ser.close()