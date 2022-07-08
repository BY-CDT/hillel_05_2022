import asyncio


async def get_primes_amount(num: int):
    results = 0
    for item in range(1, num + 1):
        counter = 0
        for divider in range(1, item + 1):
            if item % divider == 0:
                counter += 1
            if counter > 2:
                break
        if counter < 3:
            results += 1
    print(f"There are {results} prime numbers in {num}.")


async def no_lock(num):
    print(f"No_lock started {num}")
    await get_primes_amount(num)
    print(f"No_lock end {num}")


numbers = [40000, 40, 5, 1, 40000, 700]


def main():
    task = [no_lock(num) for num in sorted(numbers)]
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(asyncio.gather(*task))
    event_loop.close()


if __name__ == "__main__":
    main()
