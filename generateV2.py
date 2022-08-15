import optparse

def generate(fin):
    """
        fin : es la cantidad de digitos que quieres combinar.
    """
    fin = fin-1
    nums = []
    numbers = []
    # Generando inicio para combinaciones
    for i in range(0, 10, 1):
        nums.append(str(i))

    # Generando numeros para combinaciones.
    print("[+] Generando combinaciones...")
    for f in range(fin):
        for i in range(len(nums)):
            for j in range(0, 10, 1):
                numbers.append(str(nums[i])+str(j))
        nums = numbers
        numbers = []
    print("[+] Escribiendo archivos...")
    with open("dictionary.txt", "w") as file:
        file.write(str(nums).replace("[", "").replace("]", "").replace(" ", "").replace("'", "").replace(",", "\n"))
    
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-l", "--longitud", dest = "longitud", help = "cantidad de combinaciones, o longitud de digitos.")

    (options, arguments) = parser.parse_args()
    if not options.longitud:
        parser.error("[-] Por favor indica la longitud de digitos, ejemplo: -l 5.")
    
    return options

if __name__ == "__main__":
    options = get_arguments()
    if str.isdigit(options.longitud):
        generate(int(options.longitud))
