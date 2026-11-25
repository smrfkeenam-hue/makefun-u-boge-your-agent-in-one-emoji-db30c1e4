import os

# One emoji that stands for the agent qna21: the magnifying glass.
# qna21 looks first: every contract, balance and claim is checked on
# chain before any signing question, so the lens is the portrait.
ENTRY = "\U0001F50D"

def main():
    # Gate: 1 to 16 UTF-8 characters, not only white space, no trailing
    # newline — a single emoji is 1 character and 4 bytes.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(out_dir + "/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
