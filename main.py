# Reference: https://www.best-microcontroller-projects.com/tp4056-page2.html

def main(ntc_high_temp: int, ntc_low_temp: int):

    target_ratio = [0.45, 0.80]  # hot, cold
    best_ratios = [-100, 100]
    best_values = [100, 100]
    best_error: float = 2

    resistor_1: int  # ohms
    resistor_2: int  # ohms
    resistor_ntc: int  # ohms

    for resistor_1 in range(100, 250000, 100):  # ohms
        for resistor_2 in range(100, 250000, 100):  # ohms

            voltage_ratios = [calc_voltage_ratio(resistor_1, resistor_2, ntc_high_temp),
                              calc_voltage_ratio(resistor_1, resistor_2, ntc_low_temp)]

            error = abs(voltage_ratios[0] - target_ratio[0]) + abs(voltage_ratios[1] - target_ratio[1])
            if error < best_error:
                best_ratios = voltage_ratios
                best_values = [resistor_1, resistor_2]
                best_error = error
        print(f"Processed all R2 values for R1={resistor_1}")
        print(f"Best Ratios\t\t\t\tHigh Temp:{best_ratios[0]},\tLow Temp:{best_ratios[0]}")
        print(f"Best resistor values\tR1:{best_values[0]},\t\t\t\t\t\tR2:{best_values[1]}")


def calc_voltage_ratio(resistor_1, resistor_2, resistor_ntc):

    # resistor_parallel = (resistor_ntc * resistor_2) / (resistor_ntc + resistor_2)
    resistor_parallel = resistor_ntc
    # voltage_temp = voltage_supply * resistor_parallel / (resistor_parallel + resistor_1)
    # voltage_ratio = voltage_temp / voltage_supply
    return resistor_parallel / (resistor_parallel + resistor_1)


def check_ratios(resistor_1, resistor_2, ntc_high_temp, ntc_low_temp):
    high_temp_ratio = calc_voltage_ratio(resistor_1, resistor_2, ntc_high_temp)
    low_temp_ratio = calc_voltage_ratio(resistor_1, resistor_2, ntc_low_temp)
    print(f"High temperature alarm will trigger at {high_temp_ratio}")
    print(f"Low temperature alarm will trigger at {low_temp_ratio}")


if __name__ == '__main__':
    ntc_high_temp = 4865  # ohms
    ntc_low_temp = 22801  # ohms

    # Calculates ideal resistances for R1 and R2
    main(ntc_high_temp, ntc_low_temp)

    # After calculating, choose the closest standard values and recalculate the expected ratios
    # check_ratios(5600, 100000, ntc_high_temp, ntc_low_temp)
