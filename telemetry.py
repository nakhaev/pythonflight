#!/usr/bin/env python3
import asyncio
from mavsdk import System

PORT = "/dev/ttyACM0"  # заміни, якщо інший (наприклад /dev/ttyUSB0)

async def run():
    drone = System()
    try:
        attempt = 0
        await drone.connect(system_address=f"serial://{PORT}:115200")

        print("Очікуємо підключення...")
        async for state in drone.core.connection_state():
            if state.is_connected:
                print("✅ Підключено до автопілота")
                break

        # Телеметрія: позиція
        asyncio.create_task(print_position(drone))
        # Телеметрія: висота
        asyncio.create_task(print_altitude(drone))
        # Телеметрія: батарея
        asyncio.create_task(print_battery(drone))
        # Телеметрія: стан (ARM, режим, здоров’я сенсорів)
        asyncio.create_task(print_status(drone))
        # Телеметрія: режим польоту
        asyncio.create_task(print_flight_mode(drone))

        # тримати скрипт активним
        while attempt < 6:
            await asyncio.sleep(1)
            attempt += 1
    except Exception as e:
        print(f"Помилка: {e}")

async def print_position(drone):
    async for pos in drone.telemetry.position():
        print(f"📍 Lat={pos.latitude_deg:.6f}, Lon={pos.longitude_deg:.6f}")

async def print_altitude(drone):
    async for pos in drone.telemetry.position():
        print(f"Alt rel: {pos.relative_altitude_m:.1f} м")

async def print_battery(drone):
    async for batt in drone.telemetry.battery():
        print(f"🔋 {batt.remaining_percent*100:.1f}%  ({batt.voltage_v:.1f} V)")

async def print_status(drone):
    async for health in drone.telemetry.health():
        print(f"⚙️ Health: {health}")

async def print_flight_mode(drone):
    async for flight_mode in drone.telemetry.flight_mode():
        print(f"✈️ Flight mode: {flight_mode}")

if __name__ == "__main__":
    asyncio.run(run())
