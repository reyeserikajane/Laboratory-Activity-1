# Computational Implementation (Δ/C) - React to changing temperature
import random

def monitor_temperature():
    for _ in range(10):
        temp = random.randint(20, 100)  # Simulated sensor input
        print(f"Current Temperature: {temp}°C")
        if temp > 80:
            print("⚠️  ALERT: Overheating detected!")
        elif temp < 30:
            print("✅ Temperature is low. System running efficiently.")
        else:
            print("ℹ️  Normal operating temperature.")

# Example usage
monitor_temperature()
