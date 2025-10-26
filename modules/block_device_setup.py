def setup_block_device(block_device):
    print(f"Setting up block device: {block_device}")
    # use fdisk to create partitions, mkfs to format, and mount to mount them
    # block_device = '/dev/sdx'  # example block device
    import subprocess
    # create GPT partition table
    r = subprocess.run(['parted', block_device, 'mklabel', 'gpt'], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  [ERROR] Failed to create partition table: {r.stderr}")
        return
    # create swap partition, 4GB
    r = subprocess.run(['parted', block_device, 'mkpart', 'primary', 'linux-swap', '1MiB', '4097MiB'], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  [ERROR] Failed to create swap partition: {r.stderr}")
        return
    # create root partition, rest of the space
    r = subprocess.run(['parted', block_device, 'mkpart', 'primary', 'ext4', '4097MiB', '100%'], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  [ERROR] Failed to create root partition: {r.stderr}")
        return
    # format swap partition
    swap_partition = block_device + '1'
    r = subprocess.run(['mkswap', swap_partition], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  [ERROR] Failed to format swap partition: {r.stderr}")
        return
    subprocess.run(['swapon', swap_partition], capture_output=True, text=True)
    # format root partition
    root_partition = block_device + '2'
    r = subprocess.run(['mkfs.ext4', root_partition], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  [ERROR] Failed to format root partition: {r.stderr}")
        return
    
    # check for and make /mnt/lfs directory
    import os
    if not os.path.exists('/mnt/lfs'):
        os.makedirs('/mnt/lfs')
    # mount root partition
    r = subprocess.run(['mount', root_partition, '/mnt/lfs'], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  [ERROR] Failed to mount root partition: {r.stderr}")
        return
    print("  [OK] Block device setup complete.")
    

    pass