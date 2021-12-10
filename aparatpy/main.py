"""main of aparatpy project
"""
import requests
from scraper import Scraper
from exceptions import EmptyVideo


class Main:
    """Main Class
    """

    def __init__(self, url, quality):
        self.scraper = Scraper(url, quality)
        self.video_name = f"{url.split('/')[-1]}-{quality}.mp4"

    def download(self):
        """download video function
        """
        video_url = self.scraper.get_link()
        print("Downloading...")
        with open(self.video_name, 'wb') as video_file:
            result = requests.get(video_url, stream=True)
            total = int(result.headers.get('content-length'))
            if total is None:
                raise EmptyVideo("The video is empty!")
            download = 0
            for data in result.iter_content(chunk_size=2048):
                video_file.write(data)
                download += len(data)
                done = int(50 * download / total)
                print(f'\r[{"="*done}{" "*(50-done)}]', end="")
        print('\nVideo downloaded successfully!')


if __name__ == "__main__":
    main = Main("https://www.aparat.com/v/u4AkE", "360")
    main.download()
