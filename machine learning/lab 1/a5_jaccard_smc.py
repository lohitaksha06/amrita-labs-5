import numpy as np
def load_thyroid_vectors():
    np.random.seed(42)
    vec1 = np.array([1, 0, 0, 1, 0, 1, 0, 0, 1, 0])
    vec2 = np.array([1, 0, 1, 0, 0, 1, 1, 0, 0, 0])
    return vec1, vec2
def calc_frequencies(v1, v2):
    f11 = 0
    f10 = 0
    f01 = 0
    f00 = 0
    for i in range(len(v1)):
        if v1[i] == 1 and v2[i] == 1:
            f11 = f11 + 1
        elif v1[i] == 1 and v2[i] == 0:
            f10 = f10 + 1
        elif v1[i] == 0 and v2[i] == 1:
            f01 = f01 + 1
        else:
            f00 = f00 + 1
    return f11, f10, f01, f00

def jaccard_coefficient(f11, f10, f01):
    denom = f01 + f10 + f11
    if denom == 0:
        return 0.0
    return f11 / denom
def smc_coefficient(f11, f10, f01, f00):
    denom = f00 + f01 + f10 + f11
    if denom == 0:
        return 0.0
    return (f11 + f00) / denom
if __name__ == "__main__":
    v1, v2 = load_thyroid_vectors()
    print("first patient binary vector:")
    print(v1)
    print("\nsecond patient binary vector:")
    print(v2)
    print()

    f11, f10, f01, f00 = calc_frequencies(v1, v2)
    print(f"f11 (both 1):    {f11}")
    print(f"f10 (1,0):       {f10}")
    print(f"f01 (0,1):       {f01}")
    print(f"f00 (both 0):    {f00}")
    print()

    jc = jaccard_coefficient(f11, f10, f01)
    smc_val = smc_coefficient(f11, f10, f01, f00)
    print(f"jaccard coefficient (JC)  = {jc:.4f}")
    print(f"simple matching coeff (SMC) = {smc_val:.4f}")
    print()

    print("--- comparison ---")
    print(f"JC ({jc:.4f}) is lower than SMC ({smc_val:.4f}) because JC ignores (0,0) matches.")
    print("JC is better when (0,0) matches are not meaningful (e.g., absence of a disease).")
    print("SMC is better when (0,0) matches are equally informative as (1,1) matches.")
