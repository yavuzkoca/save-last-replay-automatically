import time
import shutil
import os
from watchfiles import watch, Change
MIN_FILE_SIZE = 200

timestamp = time.time()

app_data_folder_path = os.getenv('APPDATA')
replays_folder = app_data_folder_path + '\\My The Lord of the Rings, The Rise of the Witch-king Files\\Replays'

last_replay_file = replays_folder + '\\Last Replay.BfME2Replay'
target_file = replays_folder + '\\' + str(int(timestamp)) + '.BfME2Replay'

for changes in watch(replays_folder):
    for change_type, path in changes:
        if (change_type != Change.modified):
            continue
        if (path != last_replay_file):
            continue
        if (os.path.getsize(last_replay_file) <= MIN_FILE_SIZE):
            continue
        shutil.copy(last_replay_file, target_file)
