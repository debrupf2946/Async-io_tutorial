import asyncio as ai
import time

start=time.time()

async def fetch_file():
    await ai.sleep(1)
    print("file is fetched")
    
async def main():
    print("start main")
    await ai.gather(fetch_file(),
              fetch_file(),
              fetch_file())
    print("main compleated")
    
ai.run(main())

end=time.time()

print("execution time is",(end-start))
    