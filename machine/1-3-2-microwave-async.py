import asyncio
import time

async def cook(food, t):
    print(f'{time.ctime()} - Microwave ({food}): Cooking {t} seconds...')
    await asyncio.sleep(t)
    print(f'{time.ctime()} - Microwave ({food}): Finished cooking')
    return f'{food} is completed'

async def main():
    coros = [cook('Rice', 5), cook('Noodle', 3), cook('Curry', 1)]
    results = await asyncio.wait(coros, return_when='FIRST_COMPLETED')
    print(f'Completed task: {len(results[0])}')
    for completed_task in results[0]:
        print(f' - {completed_task.result()}')
    print(f'Uncompleted task: {len(results[1])}')

if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time() - t1
    print(f'Executed in {t2:0.2f} seconds.')