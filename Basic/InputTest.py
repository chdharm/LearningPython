def main():
    results = 0
    num = input()
    num1 = input()
    for i in range(0, num):
        if input() % num1 == 0:
            results += 1
    print results


if __name__ == "__main__":
    main()