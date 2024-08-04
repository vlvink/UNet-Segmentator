import pandas as pd
import os


def make_dataframe(img_path: str,
                   mask_path: str) -> pd.DataFrame:
    """Function makes a pandas dataframe of paths: images_paths and it's masks_paths.
    :param img_path: Path to image
    :param mask_path: Path to mask
    :return df:
    """
    images_paths = sorted(os.listdir(img_path))
    masks_paths = sorted(os.listdir(mask_path))

    df = pd.DataFrame({
        "images_paths": images_paths,
        "masks_paths": masks_paths
    })

    return df
