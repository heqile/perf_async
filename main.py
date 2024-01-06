import asyncio
from contextlib import contextmanager
import time

@contextmanager
def profile(description):
    before = time.monotonic_ns()
    yield
    after = time.monotonic_ns()
    print(f"{description} - {(after - before)/1_000_000}")

async def func(delay):
    with profile(f"delay {delay * 1000} ms"):
        # await asyncio.sleep(0)
        time.sleep(0.01)
        await asyncio.sleep(delay)
        time.sleep(0.01)
    
async def main():
    with profile("total"):
        await asyncio.gather(func(0.01), func(0.01), func(0.01), func(0.01), func(0.01))
    
if __name__ == "__main__":
    asyncio.run(main())
