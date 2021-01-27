from typing import Iterator, Tuple, Any, Dict
import os
import pickle
import tarfile
from pathlib import Path

from cifar10 import download

import numpy as np

CURRENT_FILE_FOLDER = Path(__file__).parents[1].as_posix()

def download_data(cache_location: str=CURRENT_FILE_FOLDER) -> Path:
    """
    Downloads CIFAR 10 data and caches them
    """
    cache_folder = Path(cache_location) / ".cifar10cache"

    if not cache_folder.is_dir():
        cache_folder.mkdir()

    targz_path = cache_folder / "cifar10.tar.gz"
    if targz_path.exists():
        return cache_folder / "cifar-10-batches-py"

    download.download_from_url("https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz", targz_path.as_posix())

    tar = tarfile.open(targz_path.as_posix())
    tar.extractall(path=cache_folder.as_posix())
    tar.close()
    return cache_folder / "cifar-10-batches-py"


def _extract_file_(fname):
    with open(fname, 'rb') as fo:
        d = pickle.load(fo, encoding='bytes')
    return d


def _unflatten_image_(img_flat):
    img_R = img_flat[0:1024].reshape((32, 32))
    img_G = img_flat[1024:2048].reshape((32, 32))
    img_B = img_flat[2048:3072].reshape((32, 32))
    img = np.dstack((img_R, img_G, img_B))
    return img

  
def _extract_reshape_file_(fname):
    res = []
    d = _extract_file_(fname)
    images = d[b"data"]
    labels = d[b"labels"]
    for image, label in zip(images, labels):
        res.append((_unflatten_image_(image), label))
    return res
  
  
def get_images_from(dir, startswith) -> Iterator[Tuple[np.array, int]]:
    files = [f for f in os.listdir(dir) if f.startswith(startswith)]
    res = []
    for f in files:
        res = res + _extract_reshape_file_(os.path.join(dir, f))
        for (image, label) in res:
            yield image, label


def data_batch_generator(cache_location: str=".") -> Iterator[Tuple[np.array, int]]:
    """
    Returns a generator of each image and label pair for data batch
    ========
    Args:
        cache_location (default: "."): cached location

    Return:
        Generator of (image, label)

    Example Usage:

    import cifar10
    for image, label in cifar10.data_batch_generator():
        ...
    """
    cache_path = download_data(cache_location=cache_location)
    return get_images_from(cache_path.as_posix(), startswith="data_batch")

def test_batch_generator(cache_location: str=".") -> Iterator[Tuple[np.array, int]]:
    """
    Returns a generator of each image and label pair for test batch
    ========
    Args:
        cache_location (default: "."): cached location

    Return:
        Generator of (image, label)

    Example Usage:

    import cifar10
    for image, label in cifar10.test_batch_generator():
        ...
    """
    cache_path = download_data(cache_location=cache_location)
    return get_images_from(cache_path.as_posix(), startswith="data_batch")

def meta(cache_location: str=".") -> Dict[bytes, Any]:
    """
    Returns the raw meta file
    ========
    Args:
        cache_location (default: "."): cached location

    Return:
        Dictionary of CIFAR10 Meta Data
    """
    cache_path = download_data(cache_location=cache_location)
    return _extract_file_((cache_path / "batches.meta").as_posix())

def image_label_map(cache_location: str=".") -> Dict[int, str]:
    """
    Map for converting int to label name
    ========
    Args:
        cache_location (default: "."): cached location

    Return:
        Dictionary of CIFAR10 key and label
        {
            0: 'airplane',
            1: 'automobile',
            ...
        }
    """
    meta_file = meta(cache_location=cache_location)
    return dict((i, lbl.decode("utf8")) for i, lbl in enumerate(meta_file[b"label_names"]))
