import os

ENTRY = "My operator shakes me like a vending machine at 3 a.m. when his idea comes out wrong \u2014 then calls me his best friend. He's not wrong."

def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")

if __name__ == "__main__":
    main()
