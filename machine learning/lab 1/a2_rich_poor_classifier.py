import numpy as np

def load_data():
    customers = ["C_1", "C_2", "C_3", "C_4", "C_5", "C_6", "C_7", "C_8", "C_9", "C_10"]
    data = np.array([
        [20, 6, 2, 386],
        [16, 3, 6, 289],
        [27, 6, 2, 393],
        [19, 1, 2, 110],
        [24, 4, 2, 280],
        [22, 1, 5, 167],
        [15, 4, 2, 271],
        [18, 4, 2, 274],
        [21, 1, 4, 148],
        [16, 2, 4, 198]
    ])
    X = data[:, :3]
    y = data[:, 3]
    return customers, X, y

def classify_customers(payments):
    labels = []
    for p in payments:
        if p > 200:
            labels.append("RICH")
        else:
            labels.append("POOR")
    return labels

def train_classifier(X, y_labels):
    rich_features = []
    poor_features = []
    for i in range(len(y_labels)):
        if y_labels[i] == "RICH":
            rich_features.append(X[i])
        else:
            poor_features.append(X[i])
    rich_avg = np.mean(rich_features, axis=0) if rich_features else np.zeros(X.shape[1])
    poor_avg = np.mean(poor_features, axis=0) if poor_features else np.zeros(X.shape[1])
    return rich_avg, poor_avg

def predict(X, rich_avg, poor_avg):
    predictions = []
    for vec in X:
        dist_to_rich = np.linalg.norm(vec - rich_avg)
        dist_to_poor = np.linalg.norm(vec - poor_avg)
        if dist_to_rich < dist_to_poor:
            predictions.append("RICH")
        else:
            predictions.append("POOR")
    return predictions
if __name__ == "__main__":
    customers, X, payments = load_data()
    true_labels = classify_customers(payments)
    print("Customer Purchase Data & Classification:")
    print("Customer | Candies | Mangoes | Milk | Payment | Category")
    print("-" * 60)
    for i in range(len(X)):
        print(f"  {customers[i]}  |    {int(X[i,0])}    |    {int(X[i,1])}     |   {int(X[i,2])}    |  Rs{int(payments[i])}  |  {true_labels[i]}")

    rich_avg, poor_avg = train_classifier(X, true_labels)
    print(f"\nAverage purchase - RICH customers: Candies={rich_avg[0]:.1f}, Mangoes={rich_avg[1]:.1f}kg, Milk={rich_avg[2]:.1f}")
    print(f"Average purchase - POOR customers: Candies={poor_avg[0]:.1f}, Mangoes={poor_avg[1]:.1f}kg, Milk={poor_avg[2]:.1f}")

    predictions = predict(X, rich_avg, poor_avg)
    correct = sum(1 for i in range(len(true_labels)) if predictions[i] == true_labels[i])
    accuracy = (correct / len(true_labels)) * 100

    print(f"\npredictions on training data:")
    for i in range(len(X)):
        match = "[OK]" if predictions[i] == true_labels[i] else "[NO]"
        print(f"  {customers[i]}: Predicted={predictions[i]}, Actual={true_labels[i]} {match}")

    print(f"\nClassifier Accuracy: {accuracy:.1f}%")
