class Pharmacy:
    def __init__(self, name):
        self.name = name
        self.boxOffice = 100000
        self.listOfPrice = {}

    def drug_Append(self, drug):
        self.listOfPrice[drug.name] = {
            'price': drug.cost,
            'count': 0,
            'term': drug.term,
            'company': drug.company,
            'effect': drug.effect
        }

    def drug_ToSell(self, nameDrug, amountDrug):
        if nameDrug in self.listOfPrice:
            if self.listOfPrice[nameDrug]['count'] >= amountDrug:
                self.boxOffice += self.listOfPrice[nameDrug]['price'] * amountDrug
                self.listOfPrice[nameDrug]['count'] -= amountDrug
                print(f"{amountDrug} dona {nameDrug} sotildi!")
            else:
                print(f"{nameDrug} dan yetarlicha mavjud emas!")
        else:
            print(f"{nameDrug} mavjud emas!")

    def drug_Dell(self):
        for drug, info in list(self.listOfPrice.items()):
            if info['term'] < 2024:
                del self.listOfPrice[drug]
                print(f"{drug} yaroqlilik muddati o'tgan va o'chirildi!")

    def restock_drug(self, nameDrug, amountDrug):
        if nameDrug in self.listOfPrice:
            self.listOfPrice[nameDrug]['count'] += amountDrug
            print(f"{amountDrug} dona {nameDrug} qayta zaxiraga qo'shildi!")
        else:
            print(f"{nameDrug} mavjud emas!")

class Drugs(Pharmacy):
    def __init__(self, name, cost, term, company, effect):
        super().__init__(name)
        self.cost = cost
        self.term = term
        self.company = company
        self.effect = effect


drug1 = Drugs('Aspirin', 2000, 2026, 'Bayer', 'headache')
drug2 = Drugs('Ibuprofen', 15000, 2025, 'Advil', 'pain relief')
drug3 = Drugs('Paracetamol', 10000, 2023, 'Tylenol', 'fever')
drug4 = Drugs('Amoxicillin', 25000, 2024, 'Pfizer', 'antibiotic')
drug5 = Drugs('Loratadine', 17000, 2027, 'Claritin', 'allergy')


pharmacy = Pharmacy("Central Pharmacy")

pharmacy.drug_Append(drug1)
pharmacy.drug_Append(drug2)
pharmacy.drug_Append(drug3)
pharmacy.drug_Append(drug4)
pharmacy.drug_Append(drug5)

# sklad
pharmacy.restock_drug('Aspirin', 10)
pharmacy.restock_drug('Ibuprofen', 5)
pharmacy.restock_drug('Paracetamol', 8)
pharmacy.restock_drug('Amoxicillin', 3)
pharmacy.restock_drug('Loratadine', 12)

print("\n")
# sell
pharmacy.drug_ToSell('Aspirin', 3)
pharmacy.drug_ToSell('Ibuprofen', 2)

print("\n")

# dell
pharmacy.drug_Dell()

# Hozirgi holati
print("\nFarmatsiya kassasi:", pharmacy.boxOffice,"\n")

print("Dori ro'yxati:\n")

for key , value in pharmacy.listOfPrice.items():
    print(key,value)



        
        
       