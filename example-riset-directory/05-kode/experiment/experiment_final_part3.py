
"""
experiment_final_part3.py
Bagian 3:
- Rule-Based Scheduler
- Adaptive Scheduler
Melanjutkan experiment_final_part2.py
"""

import pandas as pd
from pathlib import Path

INPUT_FILE="output/experiment_part2.csv"
OUTPUT_DIR=Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

def rule_scheduler(df):
    decisions=[]
    eff=[]
    for _,r in df.iterrows():
        if r["SOC"] < 30:
            d="Emergency"
        elif r["Solar"] < 250:
            d="Battery Mode"
        elif r["Load_Wh"] > r["PV_Energy_Wh"]:
            d="Saving Mode"
        else:
            d="Normal Mode"
        decisions.append(d)

        if r["Load_Wh"]>0:
            eff.append(min(100,(r["PV_Energy_Wh"]/r["Load_Wh"])*100))
        else:
            eff.append(100)

    df["Rule_Decision"]=decisions
    df["Rule_Efficiency"]=eff
    return df

def adaptive_scheduler(df):
    decisions=[]
    eff=[]
    scores=[]

    for _,r in df.iterrows():
        solar_score=min(r["Solar"]/10,100)
        soc_score=r["SOC"]
        load_score=max(0,100-r["Load_Wh"])
        temp_score=max(0,100-abs(r["Temperature"]-28)*5)

        score=0.40*soc_score+0.30*solar_score+0.20*load_score+0.10*temp_score

        if score>=80:
            d="Normal Operation"
            factor=0.95
        elif score>=60:
            d="Adaptive Saving"
            factor=0.85
        elif score>=40:
            d="Priority Pump"
            factor=0.75
        else:
            d="Emergency Mode"
            factor=0.60

        if r["Load_Wh"]>0:
            efficiency=min(100,(r["PV_Energy_Wh"]/(r["Load_Wh"]*factor))*100)
        else:
            efficiency=100

        scores.append(round(score,2))
        decisions.append(d)
        eff.append(round(efficiency,2))

    df["Adaptive_Score"]=scores
    df["Adaptive_Decision"]=decisions
    df["Adaptive_Efficiency"]=eff
    df["Improvement_%"]=df["Adaptive_Efficiency"]-df["Rule_Efficiency"]
    return df

def summary(df):
    print("="*60)
    print("BAGIAN 3 - SCHEDULER")
    print("="*60)
    print("Rule Efficiency     :",round(df["Rule_Efficiency"].mean(),2),"%")
    print("Adaptive Efficiency :",round(df["Adaptive_Efficiency"].mean(),2),"%")
    print("Improvement         :",round(df["Improvement_%"].mean(),2),"%")
    print("="*60)

def main():
    print("Membaca output Bagian 2...")
    df=pd.read_csv(INPUT_FILE)

    print("Menjalankan Rule-Based Scheduler...")
    df=rule_scheduler(df)

    print("Menjalankan Adaptive Scheduler...")
    df=adaptive_scheduler(df)

    csv=OUTPUT_DIR/"experiment_part3.csv"
    xlsx=OUTPUT_DIR/"experiment_part3.xlsx"
    df.to_csv(csv,index=False)
    df.to_excel(xlsx,index=False)

    summary(df)
    print("Output:",csv)
    print("Output:",xlsx)
    print("Bagian 3 selesai.")

if __name__=="__main__":
    main()
