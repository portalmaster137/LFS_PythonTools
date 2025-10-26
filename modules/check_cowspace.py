import os
import subprocess

def check_cowspace(required_mb):
    """
    Check if running in LiveISO and if there's enough cowspace available.
    
    Args:
        required_mb (int): Required space in megabytes
    
    Returns:
        tuple: (is_liveiso, has_enough_space, available_mb)
    """
    # Check if we're in a LiveISO by looking for /cow directory
    is_liveiso = os.path.exists('/run/archiso/cowspace')
    
    if not is_liveiso:
        return (False, False, 0)
    
    try:
        # Get available space in /cow
        df = subprocess.run(['df', '/run/archiso/cowspace', '--output=avail'], 
                          capture_output=True, 
                          text=True)
        
        # Skip header line and convert to int
        available_kb = int(df.stdout.strip().split('\n')[1])
        available_mb = available_kb // 1024
        
        has_enough_space = available_mb >= required_mb
        
        return (True, has_enough_space, available_mb)
        
    except Exception as e:
        return (True, False, 0)