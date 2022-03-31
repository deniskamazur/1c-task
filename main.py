import argparse
import os

import cv2

from lib import pipeline


def valid_path(string):
    if os.path.exists(string):
        return string
    else:
        raise ValueError(f"Could not find file {string}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect paper edges on image")

    parser.add_argument(
        "--input_path",
        type=valid_path,
        help="path to input image",
    )

    parser.add_argument(
        "--output_path",
        type=str,
        default="./result.jpg"
    )

    args = parser.parse_args()

    image = cv2.imread(args.input_path)
    result = pipeline(image)
    cv2.imwrite(args.output_path, result)
