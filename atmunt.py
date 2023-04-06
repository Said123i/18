import math

DecreChar = 0.03 #Уменьшение характеристик каждый ход
DecreType = 0.05 #Уменьшение характеристик в зависимости от типа питомца

#Объявление класса Tpet. В нем прописываются все характеристики питомца
def GameStart():
    class Tpet():
        def __init__(self,Type,name):
            self.type = type
            self.name = name
            self.photo = ''
            self.thirs = 0.8 + DecreChar
            self.weight = 0.8 + DecreChar
            self.heppiness = 0.8 + DecreChar
            self.years = 1
            self.game = True

            def food(seif):
                if (pet.weight < 9.75) and (pet.weight > 0):
                    pet.weight = pet.weight+0.25
                    pet.thirst = pet.thirst-0.06
                else: print('Не голоден.')

            def water(self):
                if (pet.thirst < 9.75) and (pet.thirst >0):
                    pet.thirst = pet.thirst+0.25
                    pet.weight=pet.weight -0.07
                else: print(' Не хочеть пить.')

            def play(self):
                if (pet.heppiness < 9.75) and (pet.heppiness > 0):
                        pet.heppiness = pet.heppiness + 0.25
                        pet.thirst = pet.thirst - 0.07
        def ignore(self):
            pet.weight = pet.weight
            pet.thirst = pet.thirst
            pet.heppiness = pet.heppiness


        def LeaveGame(self):
            print('')
            print('Спасибо за игру.')
            print('')
            pet.game = False

    def ChooseAction(action):
            if action == '1':
                pet.food()
            elif action == '2':
                pet.weight()
            elif action == '3':
                pet.play()
            elif action == '4':
                pet.ignor()
            elif action == '5':
                pet.LeaveGame()
            else: print('Недопустимое действие.')

    print('Выберите имя своему питомцу:')
    name = input()
    print('')
    check = False
    while check == False:
            print('Выберите тип питомца: 1:собака 2:кошка 3:крыса')
            type = input()
            pet = Tpet(type,name)
            if type == '1':
                photo == '(V._.V)'
                check = True
            elif type == '2':
                    photo = '(^._.^)'
                    check = True
            elif type == '3':
                    photo = '<:3 )~'
                    check = True
            else: print('Тип недоступеню')
            print('')
    pet = Tpet(type,name)
    pet.photo = photo
    pet.years=1
    pet.thirst=8.00 + DecreChar
    pet.weight=8.00 + DecreChar
    pet.heppiness=8.00 + DecreChar
    while (pet.game == True) and ((pet.weight >0) and (pet.thirst >0) and (pet.heppiness >0 )and (pet.years <13)) :
        pet.years = pet.years + 0.25
        pet.weight = pet.weight - DecreChar
        pet.thirst = pet.thirst - DecreChar
        pet.heppiness = pet.heppiness - DecreChar
        if pet.type == '1':
            pet.heppiness = pet.heppiness - DecreType
        elif pet.type == '2':
