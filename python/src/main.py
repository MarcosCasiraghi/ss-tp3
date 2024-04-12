from src.animation import animate
from src.util import get_all_files

if __name__ == "__main__":
    animate(get_all_files('../output-files/particle')[-1], get_all_files('../output-files/static')[-1], 10000)