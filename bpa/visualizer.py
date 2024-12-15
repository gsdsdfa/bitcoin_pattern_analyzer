import matplotlib.pyplot as plt

def plot_data(prices):
    plt.plot(prices)
    plt.title('Цена биткоина')
    plt.xlabel('Время')
    plt.ylabel('Цена (USD)')
    plt.show()