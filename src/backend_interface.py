import subprocess
import json
import os

def run_backend_search(directory, query):
    exe_path = "backend.exe"

    if not os.path.exists(exe_path):
        return [{"name": "Error", "path": "backend.exe не знайдено!", "size": 0}]

    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    try:

        result = subprocess.run(
            [exe_path, directory, query],
            capture_output=True, text=True, encoding='cp1251', errors='ignore',startupinfo=startupinfo)

        raw_json = result.stdout.strip()
        if raw_json:
            return json.loads(raw_json)
        return []

    except Exception:
        return []