import io

checked_measurements = []
last_read = 0
increased = 0
first_record = 0
with open("./medidas.txt", "r") as measurements:
    for m in measurements:
        measure = int(m)
        if(first_record == 0):
            checked_measurements.append(f"{measure} (N/A no previous measurement)")
            print(f"{measurements} (N/A no previous measurement)")
            first_record += 1
        else:
            if(measure > last_read):
                checked_measurements.append(f"{measure} (increased)")
                print(f"{measure} (increased)")
                increased += 1
            elif(measure < last_read):
                checked_measurements.append(f"{measure} (decreased)")
                print(f"{measure} (decreased)")
            else:
                checked_measurements.append(f"{measure} (stay)")
                print(f"{measure} (stay)")
        last_read = measure

with open("./medidas_checked.txt", "w") as mc:
    for line in checked_measurements:
        mc.write(f"{line}\n")

print(f"el número de incrementos es de..: {increased}")