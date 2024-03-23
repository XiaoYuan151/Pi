import decimal
import threading


def compute_pi(precision, start, end, result):
    decimal.getcontext().prec = precision + 2  # Set precision (additional 2 for rounding)

    C = 426880 * decimal.Decimal(10005).sqrt()
    K = decimal.Decimal(6)
    M = decimal.Decimal(1)
    X = decimal.Decimal(1)
    L = decimal.Decimal(13591409)
    S = L

    for i in range(start, end):
        L += 545140134
        X *= -262537412640768000
        M *= K ** 3
        S += decimal.Decimal(M * L) / X
        K += 12

    pi = C / S
    result[start:end] = str(pi)[start:end]


def main():
    while True:
        try:
            digits = int(input("Please enter the number of digits to compute (approximately): "))
            if digits <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a positive integer.")

    while True:
        try:
            num_threads = int(input("Please enter the number of threads to use (default is 64): ") or "64")
            if num_threads <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a positive integer.")

    precision_per_thread = digits // num_threads

    results = [''] * digits

    threads = []
    for i in range(num_threads):
        start = i * precision_per_thread
        end = (i + 1) * precision_per_thread if i < num_threads - 1 else digits
        thread = threading.Thread(target=compute_pi, args=(digits, start, end, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    pi_str = ''.join(results)
    with open('Pi.txt', 'w') as f:
        f.write(pi_str)
    print("Calculation completed. Result saved in Pi.txt.")


if __name__ == "__main__":
    main()
