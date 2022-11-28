import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick

df = pd.read_csv('featured_articles2005-2009.csv')
title = "Length of Featured Wikipedia Articles"
xlabel = 'Character count of article'
ylabel = 'Frequency'

def make_histogram():
    df = pd.read_csv('featured_articles2005-2009.csv')
    q = df["Length"].quantile(0.975)
    p = df['Length'].quantile(0.025)
    new = df[(df["Length"] < q) & (df['Length'] > p)]

    plt.hist(new['Length'], weights=np.ones(len(new['Length']))/len(new['Length']), bins=10)
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    print(new['Length'].nlargest(n=10), new['Length'].nsmallest(n=10))
    plt.savefig('featured_hist.png')

make_histogram()
