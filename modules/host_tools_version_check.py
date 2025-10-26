def do_version_check():
    # execute vercheck.sh and capture return code
    import subprocess
    try:
        result = subprocess.run(['./vercheck.sh'], capture_output=True, text=True)
        if result.returncode != 0:
            print("  [ERROR] Host tools version check failed:")
            print(result.stdout)
            print(result.stderr)
            return False
        else:
            print("  [OK] Host tools version check passed.")
            return True
    except Exception as e:
        print(f"  [ERROR] Exception occurred while checking host tools versions: {e}")
        return False
        