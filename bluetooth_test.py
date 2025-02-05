import asyncio
from bleak import BleakClient, BleakScanner

IPHONE_BLE_ADDRESS = "XX:XX:XX:XX:XX:XX" 
CHARACTERISTIC_UUID = "00001801-0000-1000-8000-00805f9b34fb"

async def run():
    print("Scanning for devices...")
    devices = await BleakScanner.discover()

    for device in devices:
        print(f"Found device: {device.name} ({device.address})")
        if device.address == IPHONE_BLE_ADDRESS:
            print(f"Found iPhone, connecting to {device.name}...")
            async with BleakClient(device.address) as client:
                print(f"Connected: {client.is_connected}")
                try:
                    value = await client.read_gatt_char(CHARACTERISTIC_UUID)
                    print(f"Received data: {value}")
                except Exception as e:
                    print(f"Error reading characteristic: {e}")
                break 
        else:
            print(f"Skipping device: {device.name}")

asyncio.run(run())
