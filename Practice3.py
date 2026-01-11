import asyncio

async def slow_task(name, delay):
    print(f"Function {name} Started........")
    await asyncio.sleep(delay)
    print(f"Function {name} Finished.......")

async def main_timeout():
    try:
        # Run both tasks with a timeout
        await asyncio.wait_for(
            asyncio.gather(
                slow_task("A", 1.0),
                slow_task("B", 3.0)
            ),
            timeout=2.5
        )
    except asyncio.TimeoutError:
        print("Error Occurred: Timeout reached!")

# Run the main coroutine properly
asyncio.run(main_timeout())
