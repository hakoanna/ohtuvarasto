from varasto import Varasto

def main():
    mehua = Varasto(100.0)

    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")
    print("rivi 10")
    print("rivi 11")

if __name__ == "__main__":
    main()
