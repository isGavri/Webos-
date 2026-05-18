if __name__== "__main__":
    import csv,random

    with open('Egg Grade Dataset.csv',newline='',encoding="utf-8-sig") as csvLectura:
        lectura = csv.DictReader(csvLectura,delimiter=',')
        filas =[]
       

        for row in lectura:
            row["Stain_Area"] = round(random.uniform(0.0,1.0),2)
            row["Eggshell_fissure"]=round(random.uniform(0, 150),0)
            row["Leaks_presence"]=random.choice(
                [True, False, False, False, False]
            )  # 20 % prob derrame
            row["Internal_immaculacy"]=random.choice([True, True, True, True, False])  # 20% prob sucio
            row["Specific_gravity"]=round(random.uniform(1.050,1.090),4)
            row["Motted_area"]=round(random.uniform(0.0,7.2),1)
            row["Internal_chamber_distance"]=round(random.uniform(3.1,7.3),1)
            row["Color_uniformity"]=round(random.uniform(0.0,5.9),1)
            row["Rugosity"]=round(random.uniform(0.1,10.5),1) # micrómetros
            row["Eggshell_thickness"]=round(random.uniform(0.30, 0.45),3)

            filas.append(row)
        columnas = ["Height","Diameter","Weight","Stain_Area","Eggshell_fissure","Leaks_presence","Internal_immaculacy","Specific_gravity","Motted_area","Internal_chamber_distance","Color_uniformity","Rugosity","Eggshell_thickness"]

    with open('Egg Grade Dataset Final.csv',mode="w",newline='') as csvEscritura:
        escritor = csv.DictWriter(csvEscritura, fieldnames=columnas,extrasaction="ignore")
        escritor.writeheader()
        escritor.writerows(filas)


