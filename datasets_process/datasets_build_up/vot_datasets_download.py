import os
import requests
from urllib.parse import urlparse, urljoin

def is_absolute_url(url):
    return bool(urlparse(url).netloc)

def join_url(url_base, url_path):
    if is_absolute_url(url_path):
        return url_path
    return urljoin(url_base, url_path)

VOT_DATASETS = {
    "vot2013" : "http://data.votchallenge.net/vot2013/dataset/description.json",
    "vot2014" : "http://data.votchallenge.net/vot2014/dataset/description.json",
    "vot2015" : "http://data.votchallenge.net/vot2015/dataset/description.json",
    "vot-tir2015" : "http://www.cvl.isy.liu.se/research/datasets/ltir/version1.0/ltir_v1_0_8bit.zip",
    "vot2016" : "http://data.votchallenge.net/vot2016/main/description.json",
    "vot-tir2016" : "http://data.votchallenge.net/vot2016/vot-tir2016.zip",
    "vot2017" : "http://data.votchallenge.net/vot2017/main/description.json",
    "vot-st2018" : "http://data.votchallenge.net/vot2018/main/description.json",
    "vot-lt2018" : "http://data.votchallenge.net/vot2018/longterm/description.json",
    "vot-st2019" : "http://data.votchallenge.net/vot2019/main/description.json",
    "vot-lt2019" : "http://data.votchallenge.net/vot2019/longterm/description.json",
    "vot-rgbd2019" : "http://data.votchallenge.net/vot2019/rgbd/description.json",
    "vot-rgbt2019" : "http://data.votchallenge.net/vot2019/rgbtir/meta/description.json",
    "vot-st2020" : "https://data.votchallenge.net/vot2020/shortterm/description.json",
    "vot-rgbt2020" : "http://data.votchallenge.net/vot2020/rgbtir/meta/description.json",
    "vot-st2021": "https://data.votchallenge.net/vot2021/shortterm/description.json",
    "test" : "http://data.votchallenge.net/toolkit/test.zip",
    "segmentation" : "http://box.vicos.si/tracking/vot20_test_dataset.zip",
    "vot-lt2022": "https://data.votchallenge.net/vot2022/lt/description.json"
}
stack = "vot-lt2022"
url = VOT_DATASETS[stack]
base_url = url.rsplit('/', 1)[0] + "/"
try:
    meta = requests.get(url).json()
except requests.exceptions.RequestException as e:
    raise Exception("Unable to read JSON file {}".format(e))

for sequence in meta["sequences"]:
    seq_url = sequence["annotations"]["url"]
    download_url = join_url(base_url, seq_url)
    print(f'Download annotations at: {download_url}')
    for cname, channel in sequence["channels"].items():
        channel_url = join_url(base_url, channel["url"])
        print(f'Download {cname} zip at: {channel_url}')
    print("===========================================")
