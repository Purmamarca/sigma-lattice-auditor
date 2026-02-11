import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Parameters for Kaizen Continuous Improvement (Ref: Pages 247-254)
num_iterations = 150
baseline_date = datetime(2026, 2, 1)

def generate_kaizen_data():
    data = []
    # Modeling "Continuous Improvement": 
    # Variance and Waste should decrease over time as Kaizen is applied.
    for i in range(num_iterations):
        timestamp = baseline_date + timedelta(days=i * 0.5)
        
        # Muda (Waste) reduction simulation
        improvement_factor = np.exp(-i / 100) 
        waste_hrs = np.random.gamma(2, 8) * improvement_factor
        
        # Standardized Work Stability (Target 8.5h)
        process_hrs = np.random.normal(8.5, 1.2 * improvement_factor)
        
        total_time = waste_hrs + process_hrs
        
        data.append({
            "Kaizen_ID": f"KZN-{2026}-{i:03}",
            "Timestamp": timestamp.isoformat(),
            "Waste_Muda_Hrs": round(waste_hrs, 2),
            "Value_Add_Hrs": round(process_hrs, 2),
            "Total_Lead_Time": round(total_time, 2),
            "PCE_Percent": round((process_hrs / total_time) * 100, 2),
            "Sigma_Stability": "Stable" if abs(process_hrs - 8.5) < 2.4 else "Outlier"
        })
    return pd.DataFrame(data)

if __name__ == "__main__":
    # Ensure directory exists
    os.makedirs("methodology/kaizen_events", exist_ok=True)
    df = generate_kaizen_data()
    df.to_csv("methodology/kaizen_events/continuous_improvement_log.csv", index=False)
    print("Kaizen data logs generated in methodology/kaizen_events/")
