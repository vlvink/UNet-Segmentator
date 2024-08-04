import src

IMAGE_DATA_PATH = "data/raw/IMAGES"
MASK_DATA_PATH = "data/raw/MASKS"


if __name__ == "__main__":
    src.make_dataframe(IMAGE_DATA_PATH, MASK_DATA_PATH)

