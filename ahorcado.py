import random


class juegoAhorcado:
    ESTADOS = [
        r"""
         +--+
         |  |
            |
            |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
            |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
         |  |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
        /|  |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
        /|\ |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
        /|\ |
        /   |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
        /|\ |
        / \ |
            |
        ====="""]

    SALVADO = [
        r"""
         +--+
            |
            |
        \O/ |
         |  |
        / \ |
        ====="""]

    tematica = 'FRUTAS'
    palabras_tematica = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON MANDARINA NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA '.split()

    def jugar(self):

        letras_incorrectas = []
        letras_correctas = []
        palabra_adivinar = random.choice(self.palabras_tematica)
        nombre = input("Dime tu nombre")
        while True:
            self.dibujar(letras_incorrectas, letras_correctas, palabra_adivinar)
            self.contarIntentos(letras_incorrectas)
            nueva_letra = self.DIMELETRA(letras_incorrectas + letras_correctas)

            if nueva_letra in palabra_adivinar:

                letras_correctas.append(nueva_letra)

                ganar = True
                for letras_secretas in palabra_adivinar:
                    if letras_secretas not in letras_correctas:
                        ganar = False
                        break
                if ganar:
                    print(self.SALVADO[0])
                    print('¡Bien hecho! la palabra secreta es :', palabra_adivinar)
                    print(f'Has ganado, {nombre}!')
                    break

            else:
                letras_incorrectas.append(nueva_letra)

                if len(letras_incorrectas) == len(self.ESTADOS) - 1:
                    self.dibujar(letras_incorrectas, letras_correctas, palabra_adivinar)
                    print('Demasiados intentos!')
                    print('La palabra era "{}"'.format(palabra_adivinar))
                    break

    def dibujar(self, letras_incorrectas, letras_correctas, palabra_adivinar):
        print(self.ESTADOS[len(letras_incorrectas)])
        print('La categoría es: ', self.tematica)
        print()

        print('Letras incorrectas: ', end='')
        for let in letras_incorrectas:
            print(let, end=' ')
        if len(letras_incorrectas) == 0:
            print('No hay letras incorrectas.')
        print()

        espacio_letras = ['_'] * len(palabra_adivinar)

        for i in range(len(palabra_adivinar)):
            if palabra_adivinar[i] in letras_correctas:
                espacio_letras[i] = palabra_adivinar[i]

        print(' '.join(espacio_letras))

    def DIMELETRA(self, letras_dichas):
        while True:
            print('Adivina una letra.')
            adivina = input('> ').upper()
            if len(adivina) != 1:
                print('Introduce una única letra.')
            elif adivina in letras_dichas:
                print('Esa letra ya la sabías. Elige otra vez.')
            elif not adivina.isalpha():
                print('Introduce una LETRA.')

            else:
                return adivina

    def contarIntentos(self, letras_incorrectas):
        print(-(len(letras_incorrectas) - len(self.ESTADOS) - 1)-2)

if __name__ == '__main__':
    juego1 = juegoAhorcado()
    juego1.jugar()
