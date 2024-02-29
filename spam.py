import requests
import concurrent.futures

class LinkOpener:
    def __init__(self):
        self.link_entries = []

    def add_link(self, url, count):
        for _ in range(count):
            self.link_entries.append(url)

    def open_link(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # يتم رفع الاستثناء في حالة حدوث خطأ في الطلب
            return f"Successfully opened: {url}"
        except requests.exceptions.RequestException as e:
            return f"Failed to open {url}. Error: {e}"

    def open_links(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(self.open_link, self.link_entries)
            for result in results:
                print(result)

if __name__ == "__main__":
    link_opener = LinkOpener()

    # Adding the data you requested
    link_opener.add_link("https://smmegytop.com/ref/v6lym", 1000000)

    # Opening the links
    link_opener.open_links()
