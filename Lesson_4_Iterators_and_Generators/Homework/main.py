result = []
FILE_NAME = "rockyou.txt"

with open(FILE_NAME, encoding="latin-1") as data:
    while True:
        word = data.readline()
        if not word:
            break
        else:
            if "user" in word:
                prompt = input(f"add {word} to the list? Y/N ").upper()
                if prompt == "Y":
                    result.append(word.replace("\n", ""))
                else:
                    continue

print(f"\n{len(result)} words were added.\n")
print(*result, sep=",")
