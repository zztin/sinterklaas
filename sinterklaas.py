import argparse
import random
import os

def assign_gifts(names, k=3, max_attempts=10000):
    n = len(names)
    if n < k + 1:
        raise ValueError("Not enough people to assign gifts.")
    
    for _ in range(max_attempts):
        gives = {name: [] for name in names}
        receives_count = {name: 0 for name in names}
        
        valid = True
        for giver in names:
            choices = [x for x in names if x != giver]
            random.shuffle(choices)
            selected = []
            for c in choices:
                if receives_count[c] < k:
                    selected.append(c)
                    receives_count[c] += 1
                    if len(selected) == k:
                        break
            if len(selected) < k:
                valid = False
                break
            gives[giver] = selected
        
        if valid and all(receives_count[x] == k for x in names):
            return gives
    
    raise RuntimeError("Failed to generate a valid assignment.")

def write_assignments(assignments, outdir):
    os.makedirs(outdir, exist_ok=True)
    for giver, receivers in assignments.items():
        filepath = os.path.join(outdir, f"{giver}.txt")
        with open(filepath, "w") as f:
            for r in receivers:
                f.write(r + "\n")

def check_self_giving(giver, receiver, filename):
    if giver == receiver:
        print(f"Error: {giver} gives to themselves in {filename}")
        return False
    return True


import os

def check_gift_counts_and_self(names, folder, k=3):
    counts = {name: 0 for name in names}
    valid = True

    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            giver = filename.replace(".txt", "")
            path = os.path.join(folder, filename)

            with open(path, "r") as f:
                for line in f:
                    receiver = line.strip()

                    # Count appearances
                    if receiver in counts:
                        counts[receiver] += 1
                    else:
                        print(f"Warning: Unknown name in file {filename}: {receiver}")
                        valid = False

                    # Call the helper
                    if not check_self_giving(giver, receiver, filename):
                        valid = False

    # Check counts
    for name, count in counts.items():
        if count != k:
            print(f"{name} appears {count} times (expected {k})")
            valid = False

    if valid:
        print("All checks passed.")

    return counts



def main():
    parser = argparse.ArgumentParser(description="Gift assignment generator")
    parser.add_argument("--names", nargs="+", required=True, help="List of participant names")
    parser.add_argument("--k", type=int, default=3, help="How many gifts each person gives")
    parser.add_argument("--outdir", type=str, default="gift_results", help="Output directory")
    parser.add_argument("--check", action="store_true", help="Check counts after generating")
    
    args = parser.parse_args()
    
    assignments = assign_gifts(args.names, k=args.k)
    write_assignments(assignments, args.outdir)
    
    print(f"Assignments written to {args.outdir}")

    if args.check:
        check_gift_counts_and_self(args.names, args.outdir, args.k)

if __name__ == "__main__":
    main()

