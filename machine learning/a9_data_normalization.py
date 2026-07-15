import numpy as np

# synthetic thyroid data for normalization

def load_data():
    np.random.seed(42)
    n = 50
    age = np.random.randint(20, 80, n).astype(float)
    tsh = np.random.uniform(0.1, 10.0, n)
    t3 = np.random.uniform(0.5, 3.5, n)
    tt4 = np.random.uniform(40, 180, n)
    fti = np.random.uniform(50, 200, n)
    return {"age": age, "tsh": tsh, "t3": t3, "tt4": tt4, "fti": fti}
def min_max_normalize(data):
    min_val = np.min(data)
    max_val = np.max(data)
    if max_val == min_val:
        return np.zeros_like(data), min_val, max_val
    normalized = (data - min_val) / (max_val - min_val)
    return normalized, min_val, max_val
def z_score_normalize(data):
    mean_val = np.mean(data)
    std_val = np.std(data)
    if std_val == 0:
        return np.zeros_like(data), mean_val, std_val
    normalized = (data - mean_val) / std_val
    return normalized, mean_val, std_val
if __name__ == "__main__":
    data = load_data()
    print("===== DATA NORMALIZATION / SCALING =====")
    print()

    print("original data ranges:")
    for attr in data:
        vals = data[attr]
        print(f"  {attr}: min={np.min(vals):.2f}, max={np.max(vals):.2f}, "
              f"mean={np.mean(vals):.2f}, std={np.std(vals):.2f}")
    print()

    print("which attributes need normalization?")
    print("  -> all numeric attributes have diffrent scales so yes.")
    print("     age(20-80), tsh(0.1-10), t3(0.5-3.5), tt4(40-180), fti(50-200)")
    print("     without scaling, tt4 and fti would dominate the distance")
    print()

    print("--- min-max normalization (scales to [0,1]) ---")
    for attr in data:
        norm_vals, mn, mx = min_max_normalize(data[attr])
        print(f"  {attr}: min={np.min(norm_vals):.2f}, max={np.max(norm_vals):.2f}, "
              f"range=[{mn:.2f}-{mx:.2f}]")
    print()

    print("--- z-score normalization (mean=0, std=1) ---")
    for attr in data:
        norm_vals, mn, sd = z_score_normalize(data[attr])
        print(f"  {attr}: mean={np.mean(norm_vals):.2f}, std={np.std(norm_vals):.2f}, "
              f"original_mean={mn:.2f}, original_std={sd:.2f}")
    print()

    print("--- summary ---")
    print("min-max: good when data is bounded and you want [0,1] range.")
    print("z-score: good when data has outliers and you want mean=0, std=1.")
    print("both preserve relative relationships between data points.")
