import pandas as pd
import os
import sys
from auditor.logic import calculate_six_sigma_metrics

# Specification Limits
USL = 103.0
LSL = 97.0
TARGET = 100.0
MIN_CPK_THRESHOLD = 1.33  # Four Sigma Quality gate

def run_verification():
    input_file = "data/raw_measurements.csv"
    output_file = "data/quality_audit_results.csv"
    
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} not found.")
        sys.exit(1)
        
    df = pd.read_csv(input_file)
    measurements = df["measurement"].values
    
    metrics = calculate_six_sigma_metrics(measurements, USL, LSL, TARGET)
    
    results_df = pd.DataFrame([metrics])
    
    # Add status
    passed = metrics["cpk"] >= MIN_CPK_THRESHOLD
    results_df["status"] = "PASSED" if passed else "FAILED"
    results_df["threshold"] = MIN_CPK_THRESHOLD
    
    # Ensure directory exists
    if not os.path.exists("data"):
        os.makedirs("data")
        
    results_df.to_csv(output_file, index=False)
    
    print("\n" + "="*40)
    print("📊 SIX SIGMA QUALITY AUDIT REPORT")
    print("="*40)
    print(f"Mean:         {metrics['mean']:.4f}")
    print(f"Std Dev:      {metrics['std']:.4f}")
    print(f"Cp:           {metrics['cp']:.4f}")
    print(f"Cpk:          {metrics['cpk']:.4f}")
    print(f"Sigma Level:  {metrics['sigma_level']:.2f}")
    print(f"Status:       {'✅ PASSED' if passed else '❌ FAILED'}")
    print("="*40 + "\n")
    
    if not passed:
        print(f"Failure: Cpk {metrics['cpk']:.4f} is below threshold {MIN_CPK_THRESHOLD}")
        # According to the policy, we should notify "Purmamarca" and stop the line
        # In a real pipeline, the exit code 1 handles "stop_the_line"
        sys.exit(1)
    
    print("Audit successful. Final report saved to data/quality_audit_results.csv")
    sys.exit(0)

if __name__ == "__main__":
    run_verification()
