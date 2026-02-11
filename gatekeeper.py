import pandas as pd
import os
import sys
from auditor.logic import calculate_six_sigma_metrics

# Specification Limits
USL = 103.0
LSL = 97.0
TARGET = 100.0
MIN_CPK_THRESHOLD = 1.33  # Four Sigma Quality gate

def run_gatekeeper():
    input_file = "data/raw_measurements.csv"
    output_file = "data/quality_audit_results.csv"
    
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} not found.")
        sys.exit(1)
        
    df = pd.read_csv(input_file)
    measurements = df["measurement"].values
    
    metrics = calculate_six_sigma_metrics(measurements, USL, LSL, TARGET)
    cpk = metrics["cpk"]
    
    # Export CPK for the pipeline webhook
    # In Antigravity/Bolt environments, we often use GitHub Actions style output or env files
    if "GITHUB_ENV" in os.environ:
        with open(os.environ["GITHUB_ENV"], "a") as f:
            f.write(f"MEASURED_CPK={cpk:.4f}\n")
    
    # Also print for logs
    print(f"MEASURED_CPK={cpk:.4f}")
    
    results_df = pd.DataFrame([metrics])
    passed = cpk >= MIN_CPK_THRESHOLD
    results_df["status"] = "PASSED" if passed else "FAILED"
    results_df["threshold"] = MIN_CPK_THRESHOLD
    
    if not os.path.exists("data"):
        os.makedirs("data")
        
    results_df.to_csv(output_file, index=False)
    
    print("\n" + "="*40)
    print("🛡️ GATEKEEPER SERVICE: QUALITY GATE")
    print("="*40)
    print(f"Mean:         {metrics['mean']:.4f}")
    print(f"Cpk:           {cpk:.4f}")
    print(f"Sigma Level:  {metrics['sigma_level']:.2f}")
    print(f"Status:       {'✅ PASSED' if passed else '❌ FAILED'}")
    print("="*40 + "\n")
    
    if not passed:
        print(f"CRITICAL FAILURE: Process stability (Cpk {cpk:.4f}) is below threshold ({MIN_CPK_THRESHOLD}).")
        print("Terminating pipeline immediately...")
        sys.exit(1)
    
    print("Quality gate passed. Proceeding with pipeline...")
    sys.exit(0)

if __name__ == "__main__":
    run_gatekeeper()
