import asyncio
from bleak import BleakScanner

async def is_device_in_range(target_name):
    print("Scanning for Bluetooth devices...")
    devices = await BleakScanner.discover()

    for device in devices:
        print(f"Found: {device.name} ({device.address})")
        if device.name and target_name.lower() in device.name.lower():
            print(f"Device {target_name} is in range!")
            return True

    print(f"Device {target_name} is not in range.")
    return False

target_device_name = "Calvin’s iPhone (2)"
found = False
while found != True:
    if found != True:
        found = asyncio.run(is_device_in_range(target_device_name))
