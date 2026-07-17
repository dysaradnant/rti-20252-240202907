
import pandas as pd
from pathlib import Path

INPUT_FILE="output/experiment_part1.csv"
OUTPUT_DIR=Path("output"); OUTPUT_DIR.mkdir(exist_ok=True)

PUMP_POWER=18.0; FAN_POWER=12.0; LED_POWER=24.0
BATTERY_CAPACITY_WH=240.0
SOC_INITIAL=100.0; SOC_MIN=20.0; SOC_MAX=100.0
CHARGE_EFF=0.95; DISCHARGE_EFF=0.95; SELF_DISCHARGE=0.0002

def clamp(v,a,b): return max(a,min(b,v))
def pump_duty(rh):
    return 1.0 if rh<=40 else 0.8 if rh<=50 else 0.6 if rh<=60 else 0.4 if rh<=70 else 0.2 if rh<=80 else 0.1
def fan_duty(t):
    return 1.0 if t>=35 else 0.8 if t>=33 else 0.6 if t>=31 else 0.4 if t>=29 else 0.2 if t>=27 else 0.0
def led_duty(s):
    return 1.0 if s<=100 else 0.8 if s<=300 else 0.6 if s<=500 else 0.3 if s<=700 else 0.0

def main():
    df=pd.read_csv(INPUT_FILE)
    pump=[];fan=[];led=[];load=[]
    for _,r in df.iterrows():
        p=PUMP_POWER*pump_duty(r["Humidity"]); f=FAN_POWER*fan_duty(r["Temperature"]); l=LED_POWER*led_duty(r["Solar"])
        pump.append(round(p,2)); fan.append(round(f,2)); led.append(round(l,2)); load.append(round(p+f+l,2))
    df["Pump_Wh"]=pump; df["Fan_Wh"]=fan; df["LED_Wh"]=led; df["Load_Wh"]=load
    soc=SOC_INITIAL; ch=[]; dis=[]; socs=[]
    for _,r in df.iterrows():
        pv=r["PV_Energy_Wh"]; ld=r["Load_Wh"]
        ce=max(0,pv-ld)*CHARGE_EFF; de=max(0,ld-pv)/DISCHARGE_EFF
        soc=clamp(soc-SELF_DISCHARGE*100+(ce-de)/BATTERY_CAPACITY_WH*100,SOC_MIN,SOC_MAX)
        ch.append(round(ce,2)); dis.append(round(de,2)); socs.append(round(soc,2))
    df["Charge_Wh"]=ch; df["Discharge_Wh"]=dis; df["SOC"]=socs
    df.to_csv(OUTPUT_DIR/"experiment_part2.csv",index=False)
    df.to_excel(OUTPUT_DIR/"experiment_part2.xlsx",index=False)
    print("Average Load:",round(df["Load_Wh"].mean(),2))
    print("Average SOC:",round(df["SOC"].mean(),2))
    print("Done")

if __name__=="__main__":
    main()
