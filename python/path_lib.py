from os import chdir
from pathlib import Path


def main() -> None:
    print(f"Current working directory: {Path.cwd()}")
    print(f"Home directory: {Path.home()}")

    path_1 = Path("/usr/bin/pythonista")
    path_2 = Path("/usr/bin/python")
    path_3 = Path("/usr") / "bin" / "python"
    print(path_1.exists())
    print(path_2.exists())
    print(path_3.exists())

    path_4 = Path.cwd() / "settings.yml"
    # with the context manager
    with path_4.open() as file:
        print(file.read())
    # with a method of the Path class
    print(path_4.read_text())

    # resolving a relative path to absolute
    path_5 = Path("settings.yml")
    print(path_5)
    print(path_5.resolve())
    full_path = path_5.resolve()

    # getting the parent of a path
    print(f"Parent: {full_path.parent}")
    print(f"Parent: {full_path.parent.parent}")
    print(f"Parent: {full_path.parent.parent.parent}")

    # getting the name of a file given a full path
    print(f"Name: {full_path.name}")

    # getting the stem of the file given a full path
    print(f"Stem: {full_path.stem}")

    # getting the suffix (file extension) given a full path
    print(f"Suffix: {full_path.suffix}")

    # check whether is a file or directory
    print(f"Is a directory?: {full_path.is_dir()}")
    print(f"Is a file?: {full_path.is_file()}")

    # creating a file
    new_file = Path.cwd() / "new_file.txt"
    new_file.touch()

    # writing to a file
    new_file.write_text("Hello")

    # deleting a file
    new_file.unlink()

    # creating a new directory
    new_dir = Path.cwd() / "new_dir"
    new_dir.mkdir()

    # changing to a given directory
    chdir(new_dir)
    print(f"Current working directory: {Path.cwd()}")

    # deleting a directory
    new_dir.rmdir()


if __name__ == "__main__":
    main()
