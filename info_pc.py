import psutil

cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
cpu_freq = psutil.cpu_freq(percpu=True)

print("CPU: ")
for i, (percent, freq) in enumerate(zip(cpu_percent, cpu_freq), start=1):
    print(f"Core {i}: {percent}%, Frequency: {freq.current}Mhz")
    
virtual_mem = psutil.virtual_memory()
swap = psutil.swap_memory()

print("\nMemory: ")
print(f"Total: {virtual_mem.total / (1024 **3):.2f}Gb")
print(f"Used: {virtual_mem.used / (1024 **3):.2f}Gb")   
print(f"Swap Total: {swap.total / (1024 **3):.2f}Gb")
print(f"Swap Used: {swap.used / (1024 **3):.2f}Gb")

network = psutil.net_io_counters()
print("\nNetwork: ")
print(f"Bytes Received: {network.bytes_recv}")
print(f"Bytes Sent: {network.bytes_sent}")

try:
    temperatures = psutil.sensors_temperatures()
    if temperatures:
        print("\nTemperatures: ")
        for name, entries in temperatures.items():
            for entry in entries:
                print(f"{name}: {entry.current}°C")
    else:
        print("No temperatures found")
except AttributeError:
    print("No temperatures found")
    
battery = psutil.sensors_battery()
if battery:
    plugged = "Plugged In" if battery.power_plugged else "Not Plugged In"
    print(f"\nBattery: {plugged}, {battery.percent}%")
else:
    print("\nNo battery found")
    
disk = psutil.disk_usage("/")
print("\nDisk: ")
print(f"Total: {disk.total / (1024 **3):.2f}Gb")
print(f"Used: {disk.used / (1024 **3):.2f}Gb")
print(f"Free: {disk.free / (1024 **3):.2f}Gb")