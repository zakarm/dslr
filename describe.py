import pandas as pd
from typing import Dict
import sys
import logging
from colorama import Fore, Style, init

init(autoreset=True)

class Describe:
    def __init__(self) -> None:
        self.count: float = 0
        self.mean: float = 0
        self.std: float = 0
        self.min: float = 0
        self.twenty_five: float = 0
        self.fifty: float = 0
        self.seventy_five: float = 0
        self.max: float = 0

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()

def check_args() -> None:
    if len(sys.argv) != 2:
        logger.error(Fore.RED + "Usage: python describe.py <file>")
        exit(1)
    logger.info(Fore.GREEN + "[Info] - Processing...")
    file = sys.argv[1].split(".")
    if len(file) < 1 and file[1] != "csv":
        logger.error(Fore.RED + "Extension not supported. Please provide a <file>.csv")
        exit(1)
    logger.info(Fore.GREEN + "[Info] - Reading file...")

def describe(df: pd.DataFrame) -> Dict[str, Describe]:
    datas: Dict[str, Describe] = {}
    for i in df.columns:
        if df[i].dtype == "int64" or df[i].dtype == "float64":
            datas[i] = Describe()
            datas[i].count = df[i].count()
            datas[i].mean = df[i].mean()
            datas[i].std = df[i].std()
            datas[i].min = df[i].min()
            datas[i].twenty_five = df[i].quantile(0.25)
            datas[i].fifty = df[i].quantile(0.50)
            datas[i].seventy_five = df[i].quantile(0.75)
            datas[i].max = df[i].max()
    return datas

def main() -> None:
    check_args()
    df = pd.read_csv(sys.argv[1])
    logger.info(Fore.YELLOW + "[Info] - Calculating statistics...")
    datas = describe(df)

    df_datas = pd.DataFrame({
        col: {
            "count": descr.count,
            "mean": descr.mean,
            "std": descr.std,
            "min": descr.min,
            "25%": descr.twenty_five,
            "50%": descr.fifty,
            "75%": descr.seventy_five,
            "max": descr.max
        }
        for col, descr in datas.items()
    }).T

    print(Fore.CYAN + str(df_datas))

if __name__ == "__main__":
    main()
