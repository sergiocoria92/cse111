import math

def storage_efficiency(radius, height):
    # Cálculo del volumen
    volume = math.pi * radius ** 2 * height
    # Cálculo del área superficial
    surface_area = 2 * math.pi * radius * (height + radius)
    # Eficiencia de almacenamiento (volumen dividido por el área superficial)
    return volume / surface_area

def main():
    names = []  # Lista para los nombres
    radii = []  # Lista para los radios
    heights = []  # Lista para las alturas
    costs = []  # Lista para los costos
    
    # Pedir 12 nombres, radios, alturas y costos
    for i in range(12):
        names.append(input(f"Enter name {i+1}: "))
        radii.append(float(input(f"Enter radius for {names[-1]}: ")))
        heights.append(float(input(f"Enter height for {names[-1]}: ")))
        costs.append(float(input(f"Enter cost for {names[-1]}: ")))

    # Calcular y mostrar la eficiencia de almacenamiento para cada uno
    for i in range(12):
        efficiency = storage_efficiency(radii[i], heights[i])
        print(f"{names[i]}: Storage Efficiency = {efficiency:.2f}")

if __name__ == "__main__":
    main()
