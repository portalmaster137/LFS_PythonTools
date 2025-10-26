def do_version_check():
    # execute vercheck.sh and capture return code
    import subprocess
    try:
        result = subprocess.run(['./vercheck.sh'], capture_output=True, text=True)
        #check for any "ERROR" in stdout or stderr
        if "ERROR" in result.stdout or "ERROR" in result.stderr:
            print("  [ERROR] Host tools version check failed. Please update the required tools.")
            print(result.stdout)
            print(result.stderr)
            return False
        else:
            print("  [OK] All host tools meet the required versions.")
            return True
    except Exception as e:
        print(f"  [ERROR] Failed to execute version check script: {e}")
        return False

        