import argparse
parser = argparse.ArgumentParser(prog="LFS Build Tool")
parser.add_argument('block_device')



def main():
    print("LFS Build Tool by porta.")
    print("STEP 1: Checking cowspace...")
    from modules.check_cowspace import check_cowspace
    is_liveiso, has_enough_space, available_mb = check_cowspace(4096)
    if is_liveiso:
        if has_enough_space:
            print(f"  [OK] Detected LiveISO with sufficient cowspace: {available_mb} MB available.")
        else:
            print(f"  [ERROR] Detected LiveISO but insufficient cowspace: {available_mb} MB available.")
            print("         At least 4096 MB is required to proceed.")
            return
    else:
        print("  [ERROR] Not running in LiveISO environment. Cannot proceed.")



if __name__ == "__main__":
    main()