import asyncio
import time

start=time.time()

async def get_movie_tickits():
    await asyncio.sleep(3)
    print("movie tickets")
    
async def like_ig():
    await asyncio.sleep(1)
    print("liked instagram")
    
async def main():
    task1=asyncio.create_task(get_movie_tickits())
    task2=asyncio.create_task(like_ig())
    await task1
    
asyncio.run(main())

end=time.time()

print("time of execution",(end-start))
    