class Price:
    def __init__(self, amount: int, currency: str) -> None:
        self.price = amount
        self.currency = currency

    def __add__(self, other) -> float | str:
        if not self.have_rate() or not other.have_rate():
            return "No currency exchange rate available."
        else:
            if self.currency == other.currency:
                return float(self.price + other.price)
            else:
                result = self.price + other.conversion(self.currency)
                return round(result, 2)

    def __sub__(self, other) -> float | str:
        if not self.have_rate() or not other.have_rate():
            return "No currency exchange rate available."
        else:
            if self.currency == other.currency:
                return float(self.price - other.price)
            else:
                result = self.price - other.conversion(self.currency)
                return round(result, 2)

    def have_rate(self) -> bool:
        if self.currency in currencies:
            return True
        else:
            return False

    def get_rate(self, currency, from_usd=False):
        if currency == "USD" and from_usd:
            return 1
        else:
            for rate in rates:
                if not from_usd:
                    if (
                        rate.get("from_curr") == self.currency
                        and rate.get("to_curr") == currency
                    ):
                        return rate.get("rate")
                else:
                    if (
                        rate.get("from_curr") == "USD"
                        and rate.get("to_curr") == currency
                    ):
                        return rate.get("rate")

    def conversion(self, end_currency):
        if self.currency == "USD":
            rate = self.get_rate(end_currency, from_usd=True)
            return self.price * rate
        else:
            rate = self.get_rate("USD")
            middle_price = self.price * rate
            reverse_rate = self.get_rate(end_currency, from_usd=True)
            return middle_price * reverse_rate


rates = [
    {"from_curr": "UAH", "to_curr": "USD", "rate": 0.034},
    {"from_curr": "UAH", "to_curr": "EUR", "rate": 0.032},
    {"from_curr": "USD", "to_curr": "UAH", "rate": 29.54},
    {"from_curr": "USD", "to_curr": "EUR", "rate": 0.96},
    {"from_curr": "EUR", "to_curr": "USD", "rate": 1.04},
    {"from_curr": "EUR", "to_curr": "UAH", "rate": 30.81},
]

currencies = set([entry.get("from_curr") for entry in rates])

p1 = Price(100, "EUR")
p2 = Price(200, "UAH")


def main():
    print(p1 + p2)


if __name__ == "__main__":
    main()
