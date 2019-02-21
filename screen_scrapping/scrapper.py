import requests
from xml.etree import ElementTree


def main():
    get_sitemap_urls()


def download_transcript_pages(tx_sitemaps):
    pages = [tx_sitemaps]
    return pages


def get_sitemap_urls():
    sitemap_url = "https://www.lapatilla.com/sitemap.xml"
    resp = requests.get(sitemap_url)
    if resp.status_code != 200:
        print("Cannot get sitemap, {} {}".format(resp.status_code, resp.text))
        return []
    xml_text = resp.text.replace("http://www.sitemaps.org/schemas/sitemap/0.9", "")
    dom = ElementTree.fromstring(xml_text)

    tx_sitemaps = [
        n.text for n in dom.findall('sitemap/loc')
    ]
    return tx_sitemaps


if __name__ == '__main__':
    main()
