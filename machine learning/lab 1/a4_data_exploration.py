import numpy as np
def load_thyroid_data():
    np.random.seed(42)
    n = 100
    age = np.random.randint(20, 80, n).astype(float)
    tsh = np.random.uniform(0.1, 10.0, n)
    t3 = np.random.uniform(0.5, 3.5, n)
    tt4 = np.random.uniform(40, 180, n)
    t4u = np.random.uniform(0.5, 2.0, n)
    fti = np.random.uniform(50, 200, n)
    sex = np.random.choice(["F", "M"], n)
    sick = np.random.choice(["t", "f"], n, p=[0.2, 0.8])
    pregnant = np.random.choice(["t", "f"], n, p=[0.1, 0.9])
    surgery = np.random.choice(["t", "f"], n, p=[0.05, 0.95])
    diagnosis = np.random.choice(["hyperthyroid", "hypothyroid", "negative"], n, p=[0.1, 0.15, 0.75])
    for col_data in [age, tsh, t3, tt4, t4u, fti]:
        missing_idx = np.random.choice(n, size=int(n * 0.05), replace=False)
        for idx in missing_idx:
            col_data[idx] = np.nan
    return {
        "age": age, "tsh": tsh, "t3": t3, "tt4": tt4, "t4u": t4u, "fti": fti,
        "gender": sex, "sick": sick, "pregnant": pregnant, "surgery": surgery, "diagnosis": diagnosis
    }
if __name__ == "__main__":
    data = load_thyroid_data()

    print("===== THYROID DATA EXPLORATION =====")
    print(f"total records: {len(data['age'])}")
    print()

    print("--- attribute study ---")
    numeric_attrs = ["age", "tsh", "t3", "tt4", "t4u", "fti"]
    categorical_attrs = ["sex", "sick", "pregnant", "surgery", "diagnosis"]

    print("\nnumeric attributes:")
    for attr in numeric_attrs:
        vals = data[attr]
        non_null = vals[~np.isnan(vals)]
        print(f"  {attr}: range=[{np.min(non_null):.2f}, {np.max(non_null):.2f}], "
              f"mean={np.mean(non_null):.2f}, variance={np.var(non_null):.2f}")
    print()
    print("categorical attributes:")
    attr_types = {
        "sex": "nominal (binary)", "sick": "nominal (binary)",
        "pregnant": "nominal (binary)", "surgery": "nominal (binary)",
        "diagnosis": "nominal (multi-class)"
    }
    for attr in categorical_attrs:
        vals = data[attr]
        unique, counts = np.unique(vals, return_counts=True)
        print(f"  {attr}: type={attr_types[attr]}, values={dict(zip(unique, counts))}")
    print()
    print("--- encoding scheme ---")
    print("  sex:       label encoding (0/1)")
    print("  sick:      label encoding (0/1)")
    print("  pregnant:  label encoding (0/1)")
    print("  surgery:   label encoding (0/1)")
    print("  diagnosis: one-hot encoding (3 categories)")
    print()
    print("--- missing values ---")
    for attr in numeric_attrs:
        vals = data[attr]
        nan_count = np.isnan(vals).sum()
        if nan_count > 0:
            print(f"  {attr}: {nan_count} missing values ({nan_count/len(vals)*100:.1f}%)")
        else:
            print(f"  {attr}: no missing values")
    print()
    print("--- outliers (IQR method) ---")
    for attr in numeric_attrs:
        vals = data[attr]
        non_null = vals[~np.isnan(vals)]
        q1 = np.percentile(non_null, 25)
        q3 = np.percentile(non_null, 75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        outliers = non_null[(non_null < lower) | (non_null > upper)]
        print(f"  {attr}: {len(outliers)} outliers (bounds: [{lower:.2f}, {upper:.2f}])")
