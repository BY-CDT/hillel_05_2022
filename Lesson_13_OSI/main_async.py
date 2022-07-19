from asyncio import gather, run
from random import randint
from time import perf_counter

from aiohttp import ClientSession

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
MAX_POKEMON = 400
SIZE = 100


def get_random_id() -> str:
    """Generates a random id in range from 1 to max set value."""
    return str(randint(1, MAX_POKEMON + 1))


async def get_pokemon(id_: str):
    """Makes a request to a specified URL (Base + Random ID). Converts response to json and return the name of the
    pokemon."""
    url = BASE_URL + id_
    async with ClientSession() as session:
        async with session.get(url) as request:
            result = await request.json()
            return result["name"]


async def get_random_pokemon():
    """Calls get_random_id function. Supplies received ID as a parameter to a get_pokemon function."""
    random_id = get_random_id()
    return await get_pokemon(random_id)


async def main():
    """Counts execution time. Get names of the random pokemons in the specified range."""
    start_time = perf_counter()
    tasks = [get_random_pokemon() for _ in range(SIZE)]
    results = await gather(*tasks)
    finish_time = perf_counter()

    print(*results, sep="\n")
    print(f"\n{'=' * 30}\n\nTotal time: {finish_time - start_time}")


if __name__ == "__main__":
    run(main())
