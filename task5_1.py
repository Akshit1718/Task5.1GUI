import RPi.GPIO as GPIO
import tkinter as tk
GPIO.setmode(GPIO.BCM)
LED_PINS = {'red': 17, 'green': 27, 'blue': 22}

# Set all LEDs to OFF
for led_pin in LED_PINS.values():
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.output(led_pin, GPIO.LOW)

# Function to control required LED to be ON
def activate_led(led_color):
    for led_pin in LED_PINS.values():
        GPIO.output(led_pin, GPIO.LOW)
    GPIO.output(LED_PINS[led_color], GPIO.HIGH)

# Function to close the GUI window
def shutdown():
    GPIO.cleanup()  # Clean up GPIO settings
    w.destroy()  # Close the Tkinter window

# Create the main Tkinter window
w = tk.Tk()
w.title("Select LED")
w.geometry("300x100")

# Track which LED is currently selected
active_led = tk.StringVar(value='red')

# Create radio buttons for LED color choices
tk.Radiobutton(w, text="Red LED", variable=active_led, value='red', command=lambda: activate_led('red')).pack(anchor=tk.W)
tk.Radiobutton(w, text="Green LED", variable=active_led, value='green', command=lambda: activate_led('green')).pack(anchor=tk.W)
tk.Radiobutton(w, text="Blue LED", variable=active_led, value='blue', command=lambda: activate_led('blue')).pack(anchor=tk.W)

# Button to exit the program 
tk.Button(w, text="Exit", command=shutdown).pack()

# Start the Tkinter event loop
w.mainloop()
