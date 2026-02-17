import os
import sys
import subprocess
import shutil

def is_venv():
    flag = False
    try:
        path = os.environ["VIRTUAL_ENV"]
        if path.endswith('src/ex00/mutteria'):
            flag=True
    except KeyError:
        pass
    finally:
        return flag

def main():
    if not is_venv():
        print("ERROR: Please activate virtual environment first!", file=sys.stderr)
        sys.exit(1)
    
    packages_to_install = ["beautifulsoup4", "pytest"]
    print(f"Installing: {', '.join(packages_to_install)}")
    
    subprocess.check_call([
        sys.executable, "-m", "pip", "install"
    ] + packages_to_install)
    
    print("\nAll installed packages:")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "freeze"],
        capture_output=True,
        text=True
    )
    
    packages = sorted(result.stdout.strip().split('\n'))
    for pkg in packages:
        if pkg:
            print(pkg)
    
    with open("requirements.txt", "w") as f:
        f.write(result.stdout)
    
    print(f"\nSaved to requirements.txt")
    
    # Создаем архив окружения
    venv_path = sys.prefix
    archive_name = "venv_archive.zip"
    shutil.make_archive("venv_archive", 'zip', venv_path)
    print(f"Created archive: {archive_name}")

if __name__ == "__main__":
    main()