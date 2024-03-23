import decimal
import threading


def compute_pi(precision, start, end):
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
    return str(pi)


def main():
    while True:
        try:
            digits = int(input("Please enter the number of digits to compute (approximately): "))
            if digits <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a positive integer.")

    num_threads = 4
    precision_per_thread = digits // num_threads

    with open('Pi.txt', 'w') as f:
        threads = [threading.Thread(target=lambda: f.write(
            compute_pi(precision_per_thread, i * precision_per_thread, (i + 1) * precision_per_thread))) for i in
                   range(num_threads)]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    print("Calculation completed. Result saved in Pi.txt.")


if __name__ == "__main__":
    main()
