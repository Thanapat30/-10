#when do coroutines start running?
import asyncio
import time 

async def print_after(message, delay):
    #print a message after the sepcified delay (in seconds)
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message} ")

async def main():
    #Start coroutine twice (Hopefully they stary!)
    first_awaitabel = print_after("word!", 2)
    second_awaitbel = print_after("Hello", 1)
    #Wait for coroutines to finish
    await first_awaitabel
    await second_awaitbel

asyncio.run(main())