import pandas as pd
import numpy as np
import os

def generate_synthetic_data(filename="data/raw_measurements.csv", n_samples=1000):
    if not os.path.exists("data"):
        os.makedirs("data")
        
    # Parameters for a "good" process
    # Target: 100, Std Dev: 0.5
    # Spec Limits: [98.5, 101.5]
    # This should give Cpk ~ 1.0 (if mean is 100)
    # For Six Sigma (Cpk=2.0), we need Std Dev = 0.25 (3*0.25 = 0.75; 1.5/0.75 = 2.0)
    
    mean = 100.0
    std_dev = 1.0 # Let's make it slightly worse than Six Sigma to test the "fail" threshold later if needed
    
    data = np.random.normal(mean, std_dev, n_samples)
    
    df = pd.DataFrame({
        "sample_id": range(1, n_samples + 1),
        "measurement": data
    })
    
    df.to_csv(filename, index=False)
    print(f"Generated {n_samples} samples in {filename}")

if __name__ == "__main__":
    generate_synthetic_data()
