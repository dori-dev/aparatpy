"""scraper module for aparatpy project
"""
from typing import List
import re
import requests
from bs4 import BeautifulSoup
from aparatpy.exceptions import QualityError


class Scraper:
    """scrap the video page
    """

    def __init__(self, url, quality):
        self.url = url
        self.quality = quality

    def get_all_links(self) -> List[str]:
        """get all links for download video

        Returns:
            list[str]: list of video links
        """
        result = requests.get(self.url)
        content = BeautifulSoup(result.text, 'html.parser')
        video_links = content.find_all('a', href=re.compile("https://.*.mp4"))
        links = [link['href'] for link in video_links]
        return links

    def get_link(self) -> str:
        links = self.get_all_links()
        available_qualities = self.get_qualities(links)
        if self.quality not in available_qualities:
            raise QualityError(f"Sorry, this quality({self.quality}p) is not available,"
                               f"\navailable qualities are: {available_qualities}")

        return links[available_qualities.index(self.quality)]

    @staticmethod
    def get_qualities(links: List[str]) -> List[str]:
        """get all available qualities for video

        Args:
            links (List[str]): list of video links

        Returns:
            List[str]: list of available_qualities
        """
        quality_re = re.compile(".*(-[0-9]{3,4}p).mp4.*")
        available_qualities = []
        for link in links:
            available_qualities.append(re.findall(quality_re, link)[0][1:-1])

        return available_qualities


if __name__ == "__main__":
    scraper = Scraper("https://www.aparat.com/v/u4AkE", "360")
    print(scraper.get_link())
