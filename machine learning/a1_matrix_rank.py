import numpy as np
def load_purchase_data():
    data = np.array([
     [2, 1.5, 3, 150],
     [5, 2.0, 4, 280],
     [1, 0.5, 1, 70],
    [3, 2.5, 2, 200],
    [4, 1.0, 5, 250],
    [2, 3.0, 3, 230],
    [6, 1.8, 4, 310],
    [1, 2.0, 2, 140],
    [3, 1.2, 5, 210],
    [4, 2.5, 3, 260]
])
    X = data[:, :3]
    y = data[:, 3]
    return X, y

def compute_cost_using_pseudo_inverse(X, y):
    X_pinv = np.linalg.pinv(X)
    cost = np.dot(X_pinv, y)
    return cost
if __name__ == "__main__":
    X, y = load_purchase_data()
    print("Feature Matrix X (Candies, Mangoes, Milk Packets):")
    print(X)
    print("\nOutput vector y (Payment in Rs):")
    print(y)
    print()
    num_features = X.shape[1]
    print(f"[THINKING] dimenionality of vector space: {num_features}")
    print("  -> each observation is a vector in 3D space (Candies, Mangoes, Milk)")
    num_vectors = X.shape[0]
    print(f"[THINKING] number of vectors in this space: {num_vectors}")
    rank = np.linalg.matrix_rank(X)
    print(f"[CODING] rank of feature matrix X: {rank}")
    print("  -> rank tells us how many features are linearly independent")
    cost = compute_cost_using_pseudo_inverse(X, y)
    print(f"\n[CODING] cost per unit of each product:")
    print(f"  cost of 1 Candy  = Rs {cost[0]:.2f}")
    print(f"  cost of 1 Kg Mangoes = Rs {cost[1]:.2f}")
    print(f"  cost of 1 Milk Packet = Rs {cost[2]:.2f}")
