import random
import matplotlib.pyplot as plt

class StockMarketSimulation:
    def __init__(self, initial_price, num_days, volatility):
        self.initial_price = initial_price
        self.num_days = num_days
        self.volatility = volatility
        self.prices = [initial_price]

    def simulate(self):
        for day in range(1, self.num_days):
            price_change = self.calculate_price_change()
            new_price = self.prices[-1] + price_change
            self.prices.append(new_price)

    def calculate_price_change(self):
        return random.uniform(-self.volatility, self.volatility)

    def plot_simulation(self):
        plt.plot(range(self.num_days), self.prices, label='Stock Price')
        plt.xlabel('Days')
        plt.ylabel('Price')
        plt.title('Stock Market Simulation')
        plt.legend()
        plt.show()

# Example usage
initial_price = 100
num_days = 365
volatility = 2

simulation = StockMarketSimulation(initial_price, num_days, volatility)
simulation.simulate()
simulation.plot_simulation()
