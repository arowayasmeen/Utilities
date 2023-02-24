import argparse
import os


def main(args):
    '''Brief Explanation of what the function does
    '''

    return

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--i",
        type=str,
        required=True,
        help="Input Directory"
    )

    ap.add_argument(
        "--o",
        type=str,
        required=True,
        help="Output Directory"
    )

    args = ap.parse_args()

    if not os.path.exists(args.o):
        print("Creating output directory as it does not exist.")
        os.makedirs(args.o, exist_ok=True)

    main(args)