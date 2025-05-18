import json
import os
from pathlib import Path
from termcolor import cprint, colored
from tkinter import Tk, filedialog


def url_to_utf16le_padded(url: str, target_length: int) -> bytes:
    encoded = url.encode('utf-16le') + b'\x00\x00'
    if len(encoded) > target_length:
        raise ValueError(f"URL too long ({len(encoded)} bytes), max allowed is {target_length}")
    return encoded.ljust(target_length, b'\x00')


def patch_dll(dll_path: Path, offset: int, url: str, total_bytes: int = 78):
    payload = url_to_utf16le_padded(url, total_bytes)
    with open(dll_path, 'r+b') as f:
        f.seek(offset)
        f.write(payload)
    cprint(f"Patched {dll_path} at offset {offset} with: {url}", "green")


def select_game_directory() -> Path:
    Tk().withdraw()
    folder = filedialog.askdirectory(title="Select Ortus Regni Game Directory")
    return Path(folder) if folder else None


def main():
    os.system('')
    if input(colored("Warning, are you sure you want to run? y for yes: ", "red")) != "y":
        cprint("Exiting...", "red")
        return
    with open("config.json", "r") as f:
        config = json.load(f)
        if "server" not in config:
            cprint("No server found in config.json", "red")
            return
        server_config = config["server"]

    game_dir = select_game_directory()
    if not game_dir:
        cprint("No folder selected. Exiting...", "red")
        return

    dll_path = game_dir / "OrtusRegni_Data" / "Managed" / "Assembly-CSharp.dll"
    if not dll_path.exists():
        cprint(f"DLL not found at: {dll_path}", "red")
        return

    offset = 2426953
    new_url = f"{server_config['protocol']}://{server_config['host']}:{server_config['port']}/api/"
    patch_dll(dll_path, offset, new_url)
    cprint(f"URL patched successfully {new_url}", "green")


if __name__ == "__main__":
    main()
