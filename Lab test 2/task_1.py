def convert(amount, ccy, fetch_rate):

    return amount * fetch_rate(ccy)
def stub_fetch_rate(ccy):
    rates = {
        'USD': 83.0,
        'EUR': 90.0,
        'INR': 1.0
    }
    return rates.get(ccy, 1.0)

if __name__ == "__main__":

    

    # Example of dependency injection for testability (already used above with stub_fetch_rate)
    def test_convert_with_stub():
        # This test does not require network and is fully reproducible
        assert convert(100, 'USD', stub_fetch_rate) == 8300.0
        assert convert(50, 'EUR', stub_fetch_rate) == 4500.0
        assert convert(200, 'INR', stub_fetch_rate) == 200.0
        assert convert(10, 'JPY', stub_fetch_rate) == 10.0  # fallback to 1.0

    # Example of monkeypatching for testability
    class DummyFetchRate:
        def __init__(self, rate):
            self.rate = rate
        def __call__(self, ccy):
            return self.rate

    def test_convert_with_monkeypatch():
        dummy_rate = DummyFetchRate(42.0)
        assert convert(2, 'USD', dummy_rate) == 84.0

    # Run tests
    test_convert_with_stub()
    test_convert_with_monkeypatch()
    # INSERT_YOUR_CODE
   
    # INSERT_YOUR_CODE
    # Take dynamic input for amount and currency code, then convert and print result
    amount = float(input("Enter amount: "))
    ccy = input("Enter currency code: ")
    result = convert(amount, ccy, stub_fetch_rate)
    print(f"convert({amount},'{ccy}') with rate {stub_fetch_rate(ccy)} => {result}")