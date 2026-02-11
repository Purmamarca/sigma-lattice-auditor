import numpy as np
from scipy import stats

def calculate_six_sigma_metrics(data, usl, lsl, target=None):
    """
    Calculate Six Sigma quality metrics: Cp, Cpk, and Sigma Level.
    """
    mean = np.mean(data)
    std = np.std(data, ddof=1)
    
    if std == 0:
        return {
            "mean": mean,
            "std": std,
            "cp": float('inf'),
            "cpk": float('inf'),
            "sigma_level": float('inf')
        }
    
    cp = (usl - lsl) / (6 * std)
    cpk = min((usl - mean) / (3 * std), (mean - lsl) / (3 * std))
    
    # Sigma level is usually calculated as Z-score
    # We take the minimum distance to the nearest spec limit in units of std dev
    sigma_level = min((usl - mean) / std, (mean - lsl) / std)
    
    return {
        "mean": float(mean),
        "std": float(std),
        "cp": float(cp),
        "cpk": float(cpk),
        "sigma_level": float(sigma_level)
    }
