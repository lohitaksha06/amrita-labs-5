import numpy as np
def load_full_vectors():
    np.random.seed(42)
    vec1 = np.array([55, 4.2, 1.8, 120, 1.2, 95, 1, 0, 0, 0])
    vec2 = np.array([42, 7.8, 1.2, 155, 0.9, 130, 0, 1, 0, 1])
    return vec1, vec2
def cosine_similarity(v1, v2):
    dot_product = 0
    for i in range(len(v1)):
        dot_product = dot_product + v1[i] * v2[i]
    norm1 = 0
    for val in v1:
        norm1 = norm1 + val ** 2
    norm1 = np.sqrt(norm1)
    norm2 = 0
    for val in v2:
        norm2 = norm2 + val ** 2
    norm2 = np.sqrt(norm2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot_product / (norm1 * norm2)
if __name__ == "__main__":
    v1, v2 = load_full_vectors()
    print("patient 1 - full feature vector:")
    print("  [age, tsh, t3, tt4, t4u, fti, sex, sick, pregnant, surgery]")
    print(f"  {v1}")
    print()
    print("patient 2 - full feature vector:")
    print(f"  {v2}")
    print()

    cos_sim = cosine_similarity(v1, v2)
    print(f"dot product  = {np.dot(v1, v2):.2f}")
    print(f"||v1||       = {np.linalg.norm(v1):.2f}")
    print(f"||v2||       = {np.linalg.norm(v2):.2f}")
    print()
    print(f"cosine similarity = {cos_sim:.4f}")
    print()
    print("cosine similarity ranges from -1 (opposite) to +1 (identical).")
    print(f"a value of {cos_sim:.4f} means these two patients are "
          f"{'quite similar' if cos_sim > 0.8 else 'moderately similar' if cos_sim > 0.5 else 'not very similar'}.")
