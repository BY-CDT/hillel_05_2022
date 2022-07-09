import asyncio


async def get_primes_amount(num: int) -> None:
    """Checks how many prime numbers are there in count from 1 to the supplied argument number."""
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


async def no_lock(num: int) -> None:
    """Calls asynchronously the get_primes_amount function. Allows multiple function calls to be executed
    asynchronously."""
    await get_primes_amount(num)


numbers = [40000, 40, 5, 1, 40000, 700]


def main():
    """Creating an event loop for the asynchronous execution. Feeds the provided list of numbers to the functions in
    order to get the count of prime numbers for each number provided from the list."""
    task = [no_lock(num) for num in sorted(numbers)]
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(asyncio.gather(*task))
    event_loop.close()


if __name__ == "__main__":
    main()
