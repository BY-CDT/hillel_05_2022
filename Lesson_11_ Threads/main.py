from random import randint
from statistics import mean as avg
from threading import Thread

numbers_list = []


def num_list() -> None:
    """Generating a random list of 10_000 numbers in range from 1 to 1_000."""
    [numbers_list.append(randint(1, 1000)) for _ in range(1, 10_001)]


def is_prime(num: int) -> bool:
    """Checking if a number is a prime. (Not equal to 1 and could be divided equally only by 1 and itself)"""
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if counter < 3 and num != 1:
        return True
    else:
        return False


def prime_counter(numbers: list) -> None:
    """Counts the total number of prime numbers in the list."""
    count = 0
    for num in numbers:
        if is_prime(num):
            count += 1
    print(f"There are {count} prime numbers in the generated list.")


def get_average(numbers: list) -> None:
    """Calculating the average number for a list of numbers."""
    print(f"The average is: {round(avg(numbers), 2)}.")


def main():
    """Generates a list of numbers and prints the number of prime numbers in that list as well as the average for the
    numbers in the list. Has 3 threads. The first thread generates a list, thread two and three are waiting till the
    list will be ready to process."""
    generating_list = Thread(target=num_list)
    counting_prime = Thread(target=prime_counter, kwargs={"numbers": numbers_list})
    average_num = Thread(target=get_average, kwargs={"numbers": numbers_list})

    # The first option of the program execution
    generating_list.start()
    generating_list.join()
    counting_prime.start()
    average_num.start()

    # The second option of the program execution.
    # But in this iteration thread three is waiting on the thread two to be finished
    # threads = [generating_list, counting_prime, average_num]
    # for thread in threads:
    #     thread.start()
    #     thread.join()


if __name__ == "__main__":
    main()
