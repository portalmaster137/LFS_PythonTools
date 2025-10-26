import argparse
parser = argparse.ArgumentParser(prog="LFS Build Tool")
parser.add_argument('block_device')



def main():
    print("LFS Build Tool by porta.")
    print("STEP 1: Checking cowspace...")
    from modules.check_cowspace import check_cowspace, resize_cowspace
    is_liveiso, has_enough_space, available_mb = check_cowspace(4096)
    if is_liveiso:
        if has_enough_space:
            print(f"  [OK] Detected LiveISO with sufficient cowspace: {available_mb} MB available.")
        else:
            print(f"  [ERROR] Detected LiveISO but insufficient cowspace: {available_mb} MB available.")
            print("         At least 4096 MB is required to proceed.")
            print("         attempting to resize cowspace to 4096 MB...") 
            resize_cowspace(4096)
            # Recheck cowspace after resizing
            is_liveiso, has_enough_space, available_mb = check_cowspace(4096)
            if has_enough_space:
                print(f"  [OK] Successfully resized cowspace: {available_mb} MB available.")
            else:
                return
    else:
        print("  [ERROR] Not running in LiveISO environment. Cannot proceed.")
        return
    
    print("STEP 2: Checking host tools versions...")
    from modules.host_tools_version_check import do_version_check
    if not do_version_check():
        return
    print("All checks passed. Proceeding with LFS build...")



if __name__ == "__main__":
    main()