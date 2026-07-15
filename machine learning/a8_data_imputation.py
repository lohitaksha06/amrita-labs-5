import numpy as np
def load_data_with_missing():
    np.random.seed(42)
    n = 100
    age = np.random.randint(20, 80, n).astype(float)
    tsh = np.random.uniform(0.1, 10.0, n)
    t3 = np.random.uniform(0.5, 3.5, n)
    tt4 = np.random.uniform(40, 180, n)
    age[0:5] = [200, 300, -5, 250, -10]
    tsh[0:3] = [50, 80, 100]
    sex = np.random.choice(["F", "M"], n)
    diagnosis = np.random.choice(["hyperthyroid", "hypothyroid", "negative"], n)
    age[[10, 20, 30, 40]] = np.nan
    tsh[[15, 25, 35]] = np.nan
    t3[[12, 22]] = np.nan
    tt4[[18]] = np.nan
    sex[[5, 15, 25]] = None
    diagnosis[[8, 28]] = None
    return {
        "age": age, "tsh": tsh, "t3": t3, "tt4": tt4,
        "sex": sex, "diagnosis": diagnosis
    }
def impute_with_mean(data):
    non_null = data[~np.isnan(data)]
    mean_val = np.mean(non_null)
    filled = data.copy()
    filled[np.isnan(filled)] = mean_val
    return filled, mean_val
def impute_with_median(data):
    non_null = data[~np.isnan(data)]
    median_val = np.median(non_null)
    filled = data.copy()
    filled[np.isnan(filled)] = median_val
    return filled, median_val

def impute_with_mode(data):
    valid = [x for x in data if x is not None]
    unique, counts = np.unique(valid, return_counts=True)
    mode_val = unique[np.argmax(counts)]
    filled = []
    for val in data:
        if val is None:
            filled.append(mode_val)
        else:
            filled.append(val)
    return filled, mode_val


if __name__ == "__main__":
    data = load_data_with_missing()
    print("===== DATA IMPUTATION =====")
    print()
    before_null = np.isnan(data["age"]).sum()
    filled_age, age_median = impute_with_median(data["age"])
    after_null = np.isnan(filled_age).sum()
    print(f"age (has outliers -> use median):")
    print(f"  before: {before_null} missing")
    print(f"  median used: {age_median:.2f}")
    print(f"  after: {after_null} missing (all filled)")
    print()
    t3_clean = data["t3"][~np.isnan(data["t3"])]
    q1 = np.percentile(t3_clean, 25)
    q3 = np.percentile(t3_clean, 75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    t3_outliers = t3_clean[(t3_clean < lower) | (t3_clean > upper)]
    before_null = np.isnan(data["t3"]).sum()
    if len(t3_outliers) == 0:
        filled_t3, t3_mean = impute_with_mean(data["t3"])
        print(f"t3 (no outliers -> use mean):")
        print(f"  mean used: {t3_mean:.2f}")
    else:
        filled_t3, t3_median = impute_with_median(data["t3"])
        print(f"t3 (has {len(t3_outliers)} outliers -> use median):")
        print(f"  median used: {t3_median:.2f}")
    print(f"  before: {before_null} missing, after: {np.isnan(filled_t3).sum()} missing")
    print()
    before_null = sum(1 for x in data["sex"] if x is None)
    filled_sex, sex_mode = impute_with_mode(data["sex"])
    after_null = sum(1 for x in filled_sex if x is None)
    print(f"sex (categorical -> use mode):")
    print(f"  mode used: '{sex_mode}'")
    print(f"  before: {before_null} missing, after: {after_null} missing")
    print()

    before_null = sum(1 for x in data["diagnosis"] if x is None)
    filled_diag, diag_mode = impute_with_mode(data["diagnosis"])
    after_null = sum(1 for x in filled_diag if x is None)
    print(f"diagnosis (categorical -> use mode):")
    print(f"  mode used: '{diag_mode}'")
    print(f"  before: {before_null} missing, after: {after_null} missing")
