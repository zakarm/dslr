import pandas as pd
from typing import Dict
import sys
import logging
from colorama import Fore, init
from utils.statistics_func import *

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
            datas[i].count = ColCount(df, i).count.__format__(".6f")
            datas[i].mean = ColMean(df, i).mean.__format__(".6f")
            datas[i].std = ColStd(df, i).std.__format__(".6f")
            datas[i].min = ColMin(df, i).min.__format__(".6f")
            datas[i].twenty_five = ColQuantile(df, i, 0.25).quantile.__format__(".6f")
            datas[i].fifty = ColQuantile(df, i, 0.50).quantile.__format__(".6f")
            datas[i].seventy_five = ColQuantile(df, i, 0.75).quantile.__format__(".6f")
            datas[i].max = ColMax(df, i).max.__format__(".6f")
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
    })

    print(Fore.CYAN + str(df_datas))

    logger.info(Fore.YELLOW + "----------------------------------------")
    logger.info(Fore.YELLOW + "[Info] - Pandas describe...")

    print(df.describe())

if __name__ == "__main__":
    main()
