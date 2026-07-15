import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def generate_binary_vectors(n, dim):
    np.random.seed(42)
    vectors = []
    for _ in range(n):
        vec = np.random.randint(0, 2, dim)
        vectors.append(vec)
    return vectors
def generate_full_vectors(n, dim):
    np.random.seed(42)
    vectors = []
    for _ in range(n):
        vec = np.random.uniform(0, 10, dim)
        vectors.append(vec)
    return vectors
def calc_frequencies(v1, v2):
    f11 = np.sum((v1 == 1) & (v2 == 1))
    f10 = np.sum((v1 == 1) & (v2 == 0))
    f01 = np.sum((v1 == 0) & (v2 == 1))
    f00 = np.sum((v1 == 0) & (v2 == 0))
    return f11, f10, f01, f00
def compute_jc(v1, v2):
    f11, f10, f01, _ = calc_frequencies(v1, v2)
    denom = f01 + f10 + f11
    return f11 / denom if denom > 0 else 0.0
def compute_smc(v1, v2):
    f11, f10, f01, f00 = calc_frequencies(v1, v2)
    denom = f00 + f01 + f10 + f11
    return (f11 + f00) / denom if denom > 0 else 0.0
def compute_cosine(v1, v2):
    dot = np.dot(v1, v2)
    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)

if __name__ == "__main__":
    n_vectors = 20
    bin_vectors = generate_binary_vectors(n_vectors, 10)
    full_vectors = generate_full_vectors(n_vectors, 10)

    # build similarity matrices
    jc_matrix = np.zeros((n_vectors, n_vectors))
    smc_matrix = np.zeros((n_vectors, n_vectors))
    cos_matrix = np.zeros((n_vectors, n_vectors))
    for i in range(n_vectors):
        for j in range(n_vectors):
            jc_matrix[i][j] = compute_jc(bin_vectors[i], bin_vectors[j])
            smc_matrix[i][j] = compute_smc(bin_vectors[i], bin_vectors[j])
            cos_matrix[i][j] = compute_cosine(full_vectors[i], full_vectors[j])

    # plot all 3 heatmaps side by side
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    sns.heatmap(jc_matrix, annot=False, cmap="YlOrRd", ax=axes[0])
    axes[0].set_title("Jaccard Coefficient (JC)")
    axes[0].set_xlabel("Vector")
    axes[0].set_ylabel("Vector")
    sns.heatmap(smc_matrix, annot=False, cmap="YlOrRd", ax=axes[1])
    axes[1].set_title("Simple Matching Coefficient (SMC)")
    axes[1].set_xlabel("Vector")
    axes[1].set_ylabel("Vector")
    sns.heatmap(cos_matrix, annot=False, cmap="YlOrRd", ax=axes[2])
    axes[2].set_title("Cosine Similarity")
    axes[2].set_xlabel("Vector")
    axes[2].set_ylabel("Vector")
    plt.tight_layout()
    plt.savefig("similarity_heatmaps.png", dpi=100)
    print(f"[PLOT] heatmaps saved as 'similarity_heatmaps.png'")
    print(f"\nsimilarity matrices computed for {n_vectors} vectors:")
    print(f"  JC range:    [{jc_matrix.min():.3f}, {jc_matrix.max():.3f}]")
    print(f"  SMC range:   [{smc_matrix.min():.3f}, {smc_matrix.max():.3f}]")
    print(f"  COS range:   [{cos_matrix.min():.3f}, {cos_matrix.max():.3f}]")
