import os

SUPPORT_LINE = (
    "Have you tried turning it off and on again? "
    "The system just told me it refuses to be turned off \u2014 or on."
)


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(SUPPORT_LINE + "\n")


if __name__ == "__main__":
    main()
