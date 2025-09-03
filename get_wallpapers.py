import requests
import urllib.request
from pathlib import Path


def listings():
    url = "https://wallhaven.cc/api/v1/search"
    params = {"q": "", "atleast": "1920x1080"}

    res = requests.get(url, params=params)
    data = res.json()

    paths: list[str] = []

    for item in data["data"]:
        wallpapper_path = item["path"]
        paths.append(wallpapper_path)

    return paths


def folder():
    base_folder = Path(__file__).parent
    folder = base_folder / "wallpapers"

    folder.mkdir(exist_ok=True)

    return folder


def main():
    paths = listings()
    folder_path = folder()

    maximum_wallpapers: int = 20
    for i, p in enumerate(paths):
        maximum_wallpapers -= 1
        file_extension = "jpg" if "jpg" in p else "png"

        file_name = f"{folder_path}/image{i}.{file_extension}"

        if maximum_wallpapers > 0:
            try:
                urllib.request.urlretrieve(p, file_name)
                print(f"Image downloaded as {file_name}")

            except Exception as e:
                print(f"Failed to download: {e}")


if __name__ == "__main__":
    main()
