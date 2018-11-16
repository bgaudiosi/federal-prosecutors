import requests
import zipfile
import argparse
from bs4 import BeautifulSoup
from time import sleep

_DOJ_BASE_LINK = "https://www.justice.gov"
_DOJ_FOIA_LINK = "https://www.justice.gov/usao/resources/foia-library/national-caseload-data"


live = True
def get_most_recent_link():
    global _DOJ_BASE_LINK
    global _DOJ_FOIA_LINK
    if (live):
        r = requests.get(_DOJ_FOIA_LINK)
        html = r.text
    else:
        f = open("doj.html")
        html = f.read()
        f.close()

    soup = BeautifulSoup(html, features="html.parser")
    uls = soup.find_all("ul")
    idx = 0
    for i in range(len(uls)):
        if "data files" in str(uls[i]):
            idx = i
            break

    # Now, find first one which is uncommented
    right_list = uls[idx]
    a = right_list.find_all("li")[0].find_all("a")[0]

    link = _DOJ_BASE_LINK + a['href']
    return link


def get_zip_links(link_to_zips):
    if (live):
        r = requests.get(link_to_zips)
        html = r.text
    else:
        f = open("doj2.html")
        html = f.read()
        f.close()

    soup = BeautifulSoup(html, features="html.parser")
    a_list = soup.find_all("a")

    # Find first disk
    links = []
    for a in a_list:
        if "Disk" in a.text:
            links.append(a['href'])

    return links


def download_files(select=None, wait_time=30, download_dir="data"):
    link_to_zips = get_most_recent_link()
    zip_links = get_zip_links(link_to_zips)
    if select == None:
        select = list(range(len(zip_links)))

    filenames = []
    for i in select:
        print("Downloading DISK" + str(i+1).zfill(2) + ".zip")
        if i >= len(zip_links) or i < 0:
            raise RuntimeError("Invalid download index " + str(i))
        r = requests.get(zip_links[i])
        filename = download_dir + "/DISK" + str(i+1).zfill(2) + ".zip"
        f = open(filename, 'wb')
        f.write(r.content)
        f.close()

        filenames.append(filename)

        if i == select[len(select)-1]:
            print("Download complete")
        else:
            print("Download complete. Sleeping for 30 seconds...")
            sleep(wait_time)

    return filenames


def unzip_files(files, extract_dir="data"):
    print("Unzipping files!")
    for f in files:
        print("Unzipping", f, "...")
        zip_ref = zipfile.ZipFile(f, 'r')
        zip_ref.extractall(extract_dir)
        zip_ref.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download files from the LIONS database')

    parser.add_argument('-d', '--download', action='store_true',
                        help='Download files only.')

    parser.add_argument('-z', '--zip', action='store_true',
                        help='Unzip files only')

    parser.add_argument('-s', '--select', nargs='*', type=int,
                        help='Select which disks to download.')

    args = parser.parse_args()

    # if neither flag is passed, assume true for both
    if not args.download and not args.zip:
        args.download = True
        args.zip = True

    if args.download:
        files = download_files(select=args.select)
    else:
        files = args.select

    if args.zip:
        unzip_files(files)
