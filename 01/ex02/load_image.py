import numpy as np
from PIL import Image


def ft_load(path: str):
    with Image.open(path) as im:
        print("The shape of image is:", np.array(im).shape)
        return np.array(im)


if __name__ == "__main__":
    import requests
    import io

    response = requests.get(
        "https://cdn.intra.42.fr/document/document/17375/landscape.jpg"
    )

    if response.status_code != 200:
        print("Failed to fetch image")
        exit(1)

    print(ft_load(io.BytesIO(response.content)))
