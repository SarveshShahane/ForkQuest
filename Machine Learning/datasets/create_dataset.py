from sklearn.datasets import make_blobs, make_regression
import pandas as pd

def create_dataset(n_samples=100, n_features=2, information=2, std=1.0, random_state=42, type="classification"):
    """
    Create a synthetic dataset using make_blobs.

    Parameters:
    n_samples (int): The total number of samples.
    n_features (int): The number of features for each sample.
    information (int): The number of centers to generate in case of classification and the numbers of informative features in case of regression.
    std (float): The standard deviation of the generated sample.
    random_state (int): Determines random number generation for dataset creation.

    Returns:
    X (array): The generated samples.
    y (array): The integer labels for cluster membership of each sample.
    """

    if(type == "classification"):
        X, y = make_blobs(n_samples=n_samples, n_features=n_features, centers=information, 
        cluster_std=std, random_state=random_state)
    elif(type == "regression"):  
        X, y = make_regression(n_samples=n_samples, n_features=n_features, n_informative=information, noise=std, random_state=random_state)
    else:
        raise ValueError("Type must be either 'classification' or 'regression'")
    
    return X, y

if __name__ == "__main__":

    # Creating Classification dataset
    X, y = create_dataset(1000, 3, 2, 1, 37, "classification")
    # print("Features:\n", X)
    # print("Labels:\n", y)

    df = pd.DataFrame(X, columns=[f'feature_{i+1}' for i in range(X.shape[1])])
    df['label'] = y

    # print(df.head())
    df.to_csv('classification_dataset1.csv', index=False)
    print("Dataset saved to 'classification_dataset1.csv'")
    

    # Creating Regression dataset
    X, y = create_dataset(1000, 3, 2, 10, 37, "regression")
    # print("Features:\n", X)
    # print("Labels:\n", y)

    df = pd.DataFrame(X, columns=[f'feature_{i+1}' for i in range(X.shape[1])])
    df['target'] = y    
    # print(df.head())
    df.to_csv('regression_dataset1.csv', index=False)
    print("Dataset saved to 'regression_dataset1.csv'")
