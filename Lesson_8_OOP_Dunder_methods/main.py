currencies = [
    {"from": "USD", "to": "UAH", "rate": 29.54},
    {"from": "UAH", "to": "USD", "rate": 0.034},
    {"from": "EUR", "to": "USD", "rate": 1.04},
]


class Price:
    def __init__(self, price: int, currency: str) -> None:
        self.price = price
        self.currency = currency

    def __add__(self, other) -> tuple:
        if self.currency == other.currency:
            result = self.price + other.price, self.currency
        else:
            result = self.conversion() + other.conversion(), "UAH"
        return result

    def __sub__(self, other) -> float:
        if self.currency == other.currency:
            result = self.price - other.price, self.currency
        else:
            result = self.conversion() - other.conversion(), "UAH"
        return result

    def conversion(self):
        if self.currency == "UAH":
            result = self.price
        elif self.currency == "USD":
            result = self.conversion_2_uah()
        else:
            to_usd = Price(self.conversion_1_usd(), "USD")
            result = to_usd.conversion_2_uah()
        return result

    def exchange_rate(self, currency_to):
        rate = "No rate available."
        for exchange_rate in currencies:
            if all(
                (
                    exchange_rate.get("from") == self.currency,
                    exchange_rate.get("to") == currency_to,
                )
            ):
                rate = exchange_rate.get("rate")
                break
            else:
                continue
        return rate

    def conversion_1_usd(self):
        rate = self.exchange_rate("USD")
        if isinstance(rate, str):
            result = rate
        else:
            result = self.price * rate
        return result

    def conversion_2_uah(self):
        rate = self.exchange_rate("UAH")
        if isinstance(rate, str):
            result = rate
        else:
            result = self.price * rate
        return result


product_a = Price(100, "UAH")
product_b = Price(200, "USD")
product_c = Price(100, "EUR")


def main():
    print(product_b + product_b)
    exit()


if __name__ == "__main__":
    main()
