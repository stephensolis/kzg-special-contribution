import glob
import hashlib
import os
import sys

if len(sys.argv) != 2:
    print('usage: get-entropy.py <path to mounted comma drive>')
    sys.exit(1)

base_path = sys.argv[1] + '/0/realdata/'

if not os.path.isdir(base_path):
    print("[!] Couldn't open data directory.")
    sys.exit(1)

drives = set()
for path in os.listdir(base_path):
    if path[0].isdigit():
        path_parts = path.split('--')
        drives.add(path_parts[0] + '--' + path_parts[1])

latest_drive = sorted(drives, reverse=True)[0]
print('[i] Found latest drive: {}.'.format(latest_drive))

num_segments = len(glob.glob(base_path + latest_drive + '*'))
print('[i] Latest drive has {} segments.'.format(num_segments))

entropy = hashlib.sha256()
for i in range(num_segments):
    log_path = base_path + latest_drive + '--' + str(i) + '/rlog'
    print('[+] Hashing segment {}/{}... '.format(i + 1, num_segments), end='', flush=True)
    with open(log_path, 'rb') as f:
        entropy.update(f.read())
    print('done.')

print()
print('[*] Entropy: ' + entropy.hexdigest())
