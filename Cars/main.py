# main.py

from General.Cars.Car import Car # Importation de la classe Car depuis le module Car.py

def main():
    car = Car()  # Crée une instance de la classe Car
    car.start()  # Démarre la voiture
    car.drive(50)  # La voiture roule sur 50 kilomètres
    car.refuel(20)  # On ajoute 20 unités de carburant
    car.drive(100)  # La voiture roule sur 100 kilomètres
    print(f"Mileage: {car.mileage}, Fuel: {car.fuel}")  # Affiche les résultats

if __name__ == "__main__":  # Exécute la fonction main uniquement si ce fichier est exécuté directement
    main()









    #Le fichier main.py sert à
#Exécuter et organiser le code de manière logique et ordonnée.
#Tester le projet et vérifier son bon fonctionnement.
#Démarrer l'application de façon centralisée.