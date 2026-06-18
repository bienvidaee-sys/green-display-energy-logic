# Energy Saving Simulation for Public Displays
# This script compares energy consumption between 24/7 "Always-On" mode 
# and "Sensor-Based Intelligent Standby" mode.

def calculate_savings(power_kw=0.5, days=365, price_per_kwh=3.5, activity_rate=0.3):
    """
    power_kw: Power consumption of the device in kW
    days: Duration of the simulation in days
    price_per_kwh: Cost of electricity per kWh
    activity_rate: Percentage of time (0.0 to 1.0) the display is active due to detected motion
    """
    total_hours = days * 24
    
    # Traditional Mode: Always ON (24/7)
    trad_energy = total_hours * power_kw
    trad_cost = trad_energy * price_per_kwh
    
    # Green Mode: Active when motion detected, Low-power standby when idle
    active_hours = total_hours * activity_rate
    standby_hours = total_hours * (1 - activity_rate)
    standby_power = power_kw * 0.05  # Assume standby consumes only 5% of full power
    
    green_energy = (active_hours * power_kw) + (standby_hours * standby_power)
    green_cost = green_energy * price_per_kwh
    
    # Display Results
    print(f"--- Annual Energy & Cost Analysis ---")
    print(f"Traditional Mode: {trad_energy:.0f} kWh, Cost: ${trad_cost:.2f}")
    print(f"Green Mode:       {green_energy:.0f} kWh, Cost: ${green_cost:.2f}")
    print(f"Total Saved:      ${(trad_cost - green_cost):.2f} ({(1 - green_cost/trad_cost)*100:.1f}% reduction)")

if __name__ == "__main__":
    calculate_savings()