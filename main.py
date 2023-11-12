from statman import Statman
import time


def main():
    print('** example accessing stopwatch via Statman registry')
    Statman.stopwatch('sw1', autostart=True)

    time.sleep(10)

    Statman.stopwatch('sw1').stop()
    print(Statman.stopwatch('sw1').read(precision=1))


if __name__ == "__main__":
    main()
