#!/usr/bin/env python3
import asyncio
from mavsdk import System
from mavsdk.offboard import OffboardError

PORT = "/dev/ttyACM0"  # заміни, якщо інший

async def main():
    # Підключення до серійного порту через mavsdk_server (вбудовано в пакет)
    drone = System()
    try:
        await drone.connect(system_address=f"serial://{PORT}:57600")
            # Чекаємо підключення
        async for state in drone.core.connection_state():
            if state.is_connected:
                print("✅ Connected")
                break
        
        #Переконайся, що GPS/армінг дозволені (для стенду можна вимкнути arm checks в параметрах, але краще мати RC failsafe)
        print("Arming…")
        await drone.action.arm()
        await asyncio.sleep(2)
        await drone.action.disarm()

        # print("Takeoff to 2m…")
        # await drone.action.takeoff()
        # await asyncio.sleep(5)

        # print("Landing…")
        # await drone.action.land()
        # await asyncio.sleep(5)
        
    except Exception as e:
        print(f"Failed: {e}")
        print("Trying 115200 baud...")


    print("Done.")

if __name__ == "__main__":
    asyncio.run(main())
