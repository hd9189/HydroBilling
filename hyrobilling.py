from matplotlib.legend import Legend
import pandas as pd
from matplotlib import pyplot as plt

def billing():
    df = pd.read_csv('Hydro_Billing.csv')
    ax = df.plot.bar(
    # ax = df.plot.line(
        x='From (yyyy-mm-dd)',
        y='Amount Due',
        rot = 45,
        legend=False
    )
    ax.set_title('Hydrobill', fontsize=16)
    ax.set_xlabel('Date (yyyy-mm-dd)', fontsize=14)
    ax.set_ylabel('Amount ($)', fontsize=14)
    plt.show()

billing()