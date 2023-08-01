import os
from pathlib import Path
import shutil

directory = 'E:/C#/Python/Barahlo/'

CATEGORIES = {
    "Videos": ['.avi', '.mp4', '.mov', '.mkv'],
    "Documents": ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    "Images": ['.jpeg', '.png', '.jpg', '.svg']
}

def normalize(filename):
    translit_map = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ie', 'ж': 'zh', 'з': 'z', 'и': 'y',
        'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's',
        'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ь': '', 'ю': 'iu',
        'я': 'ia',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D', 'Е': 'E', 'Є': 'Ye', 'Ж': 'Zh', 'З': 'Z', 'И': 'Y',
        'І': 'I', 'Ї': 'Yi', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S',
        'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ь': '', 'Ю': 'Yu',
        'Я': 'Ya'
    }
    
    valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    normalized = ''
    for char in filename:
        if char in valid_chars:
            normalized += char
        elif char in translit_map:
            normalized += translit_map[char]
        else:
            normalized += '_'
    return normalized

def process_file(file_path: Path):
    for category, extensions in CATEGORIES.items():
        if file_path.suffix.lower() in extensions:
            destination_folder = Path(directory) / category
            destination_path = destination_folder / normalize(file_path.stem) + file_path.suffix.lower()
            if not destination_folder.exists():
                destination_folder.mkdir()
            shutil.move(str(file_path), str(destination_path))
            break

def process_folder(folder_path: Path):
    for entry in folder_path.iterdir():
        if entry.is_file():
            process_file(entry)
        elif entry.is_dir() and entry.name not in ['archives', 'video', 'audio', 'documents', 'images']:
            process_folder(entry)

def create_categories(target_path: Path):
    for category in CATEGORIES.keys():
        folder_path = target_path / category
        if not folder_path.exists():
            folder_path.mkdir()

def main():
    target_path = Path(directory)
    create_categories(target_path)
    process_folder(target_path)
    print("Sorting completed!")

if __name__ == "__main__":
    main()
