import sklearn.decomposition as PCA
import matplotlib.pyplot as plt
import seaborn as sns


def pca_ratio(df):
    sns.set_style("darkgrid")
    pca = PCA()
    X_pca = pca.fit_transform(df)
    total = pca.explained_variance_ratio_.cumsum()
    percent = df.shape[1] - len(total[total <=.95])
    print(percent,total[percent])
    plt.plot(range(len(pca.explained_variance_ratio_.cumsum())),pca.explained_variance_ratio_.cumsum())
