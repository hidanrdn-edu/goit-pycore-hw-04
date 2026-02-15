import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)


def display_directory_structure(path, prefix=""):
    try:
        path_obj = Path(path)
        if not path_obj.exists():
            print(f"{Fore.RED}Error: Path does not exist: {path}{Style.RESET_ALL}")
            return
        
        if not path_obj.is_dir():
            print(f"{Fore.RED}Error: Path is not a directory: {path}{Style.RESET_ALL}")
            return
        
        try:
            items = sorted(path_obj.iterdir(), key=lambda x: (not x.is_dir(), x.name))
        except PermissionError:
            print(f"{Fore.RED}Error: Permission denied to access {path}{Style.RESET_ALL}")
            return

        if prefix == "":
            print(f"{Fore.CYAN}{path_obj.name}/{Style.RESET_ALL}")
        
        for index, item in enumerate(items):
            is_last_item = index == len(items) - 1
            
            connector = "└── " if is_last_item else "├── "
            extension = "    " if is_last_item else "│   "
            

            if item.is_dir():
                print(f"{prefix}{connector}{Fore.CYAN}{item.name}/{Style.RESET_ALL}")
                next_prefix = prefix + extension
                display_directory_structure(item, next_prefix)
            else:
                print(f"{prefix}{connector}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
    
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")


def main():
    try:
        directory_path = sys.argv[1]
    except IndexError:
        print(f"{Fore.YELLOW}Usage: python Task3.py <directory_path>{Style.RESET_ALL}")
        sys.exit(1)
    
    display_directory_structure(directory_path)


if __name__ == "__main__":
    main()
