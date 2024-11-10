import pandas as pd

class ColCount:
    def __init__(self, df: pd.DataFrame, col: str) -> None:
        self.count = sum(1 for _ in df[col].dropna())

    def __str__(self) -> str:
        return f"{self.count}"

    def __format__(self, format_spec: str) -> str:
        return f"{self.count:{format_spec}}"

class ColMean:
    def __init__(self, df: pd.DataFrame, col: str) -> None:
        values = df[col].dropna().tolist()
        self.mean = sum(values) / len(values) if values else 0

    def __str__(self) -> str:
        return f"{self.mean}"

    def __format__(self, format_spec: str) -> str:
        return f"{self.mean:{format_spec}}"

class ColStd:
    def __init__(self, df: pd.DataFrame, col: str) -> None:
        values = df[col].dropna().tolist()
        mean = sum(values) / len(values) if values else 0
        variance = sum((i - mean) ** 2 for i in values) / (len(values) - 1) if len(values) > 1 else 0
        self.std = variance ** 0.5

    def __str__(self) -> str:
        return f"{self.std}"

    def __format__(self, format_spec: str) -> str:
        return f"{self.std:{format_spec}}"

class ColMin:
    def __init__(self, df: pd.DataFrame, col: str) -> None:
        values = df[col].dropna().tolist()
        self.min = values[0] if values else None
        for i in values:
            if i < self.min:
                self.min = i

    def __str__(self) -> str:
        return f"{self.min}"

    def __format__(self, format_spec: str) -> str:
        return f"{self.min:{format_spec}}"

class ColQuantile:
    def __init__(self, df: pd.DataFrame, col: str, q: float) -> None:
        values = sorted(df[col].dropna().tolist())
        index = q * (len(values) - 1)
        if len(values) == 0:
            self.quantile = None
        elif index.is_integer():
            self.quantile = values[int(index)]
        else:
            lower = values[int(index)]
            upper = values[int(index) + 1]
            self.quantile = lower + (upper - lower) * (index % 1)

    def __str__(self) -> str:
        return f"{self.quantile}"

    def __format__(self, format_spec: str) -> str:
        return f"{self.quantile:{format_spec}}"

class ColMax:
    def __init__(self, df: pd.DataFrame, col: str) -> None:
        values = df[col].dropna().tolist()
        self.max = values[0] if values else None
        for i in values:
            if i > self.max:
                self.max = i

    def __str__(self) -> str:
        return f"{self.max}"

    def __format__(self, format_spec: str) -> str:
        return f"{self.max:{format_spec}}"