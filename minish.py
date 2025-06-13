#!/usr/bin/env python3
import os
import subprocess
import sys

VERSION = "0.1.0"
NAME = "minish"
HOME = os.path.expanduser("~")

# رنگ‌ها
GREEN = "\033[32m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"
BOLD = "\033[1m"

def get_prompt():
    cwd = os.getcwd()
    if cwd == HOME:
        return f"{CYAN}{BOLD}{NAME}>{RESET} "
    else:
        return f"{CYAN}{BOLD}{NAME} {BLUE}{cwd}{RESET}> "

def run_command(cmd): # type: ignore
    if cmd.startswith("cd"): # type: ignore
        parts = cmd.split(maxsplit=1) # type: ignore
        if len(parts) == 1: # type: ignore
            try:
                os.chdir(HOME)
            except Exception as e:
                print(f"{BOLD}Error changing directory:{RESET} {e}")
        else:
            path = parts[1].strip() # type: ignore
            try:
                os.chdir(os.path.expanduser(path)) # type: ignore
            except FileNotFoundError:
                print(f"{BOLD}No such directory:{RESET} {path}")
    elif cmd == "shinfo":
        show_shinfo()
    else:
        subprocess.run(cmd, shell=True) # type: ignore

def show_shinfo():
    art = f"""{GREEN}
┌────────────────┐
│   minish       │
└────────────────┘
{RESET}{BOLD}minish shell v{VERSION}{RESET}
Python {sys.version.split()[0]} • {os.name.upper()} platform
Author: Amirhossein
"""
    print(art)

def main():
    while True:
        try:
            prompt = get_prompt()
            cmd = input(prompt).strip()

            if not cmd:
                continue
            if cmd == "exit":
                break

            run_command(cmd)

        except KeyboardInterrupt:
            print()  # فقط خط جدید بده
        except EOFError:
            print("\nUse 'exit' to leave.")
            continue

if __name__ == "__main__":
    main()
