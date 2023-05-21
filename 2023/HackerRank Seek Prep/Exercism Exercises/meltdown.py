"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000:
        return True
    return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power/theoretical_max_power) * 100
    if efficiency >= 80:
        return 'green'
    elif efficiency >= 60:
        return 'orange'
    elif efficiency >= 30:
        return 'red'
    else:
        return 'black'
    


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    dangerNumber = temperature * neutrons_produced_per_second
    thresholdThreshold = threshold * 0.1
    
    if dangerNumber < (threshold * 0.9):
        return 'LOW'
    elif  threshold - thresholdThreshold <= dangerNumber <= threshold + thresholdThreshold:
        return 'NORMAL'
    else:
        return 'DANGER'
        
        

    
