import random


class juegoAhorcado:
    """
    .. include:: ./README.md
    """
    """
    Esta clase permite crear objetos para poder jugar al ahorcado
    """
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

    tematica = 'FRUTAS MARCAS JUEGOS'.split()
    tematica_azar = random.choice(tematica)

    if tematica_azar == 'FRUTAS':
        palabras_tematica = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO ' \
                            'LIMA LIMON MANDARINA NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA '.split()
    elif tematica_azar == 'MARCAS':
        palabras_tematica = 'FORD AUDI TOYOTA VOLKSWAGEN FERRARI TESLA PEUGEOT SEAT'.split()
    elif tematica_azar == 'JUEGOS':
        palabras_tematica = 'MINECRAFT GTAV ROBLOX VALORANT LOL COUNTER ROCKET'.split()

    def jugar(self):
        """
        Esta función es la que utiliza las otras funciones para poder jugar, es la "base del juego".
        """
        letras_incorrectas = []
        letras_correctas = []
        palabra_adivinar = random.choice(self.palabras_tematica)
        nombre = input("Dime tu nombre")
        while True:
            self.dibujar(letras_incorrectas, letras_correctas, palabra_adivinar)
            self.contarIntentos(letras_incorrectas)
            nueva_letra = self.DIMELETRA(letras_incorrectas + letras_correctas, palabra_adivinar)

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
        """
        Esta función printea el muñeco colgado e indica la tematica y las letras incorrectas dichas.
        :param letras_incorrectas: letras incorrectas anteriormente dichas
        :param letras_correctas: letras correctas anteriormente dichas
        :param palabra_adivinar: palabra que se debe adivinar
        """
        print(self.ESTADOS[len(letras_incorrectas)])
        print('La categoría es: ', self.tematica_azar)
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

    def DIMELETRA(self, letras_dichas, palabra_adivinar):
        """
        Esta función pide al jugador una letra por teclado para adivinar la palabra
        :param letras_dichas: letras correctas e incorrectas anteriormente dichas
        :param palabra_adivinar: palabra que se debe adivinar
        :return: adivina(letra introducida por el usuario)
        """
        while True:
            print('Adivina una letra.')
            adivina = input('> ').upper()
            if (adivina == 'TERMINAR'):
                print(self.ESTADOS[6])
                print(f"La palabra era {palabra_adivinar}")
                break
            elif len(adivina) != 1:
                print('Introduce una única letra.')
            elif adivina in letras_dichas:
                print('Esa letra ya la sabías. Elige otra vez.')
            elif not adivina.isalpha():
                print('Introduce una LETRA.')

            else:
                return adivina

    def contarIntentos(self, letras_incorrectas):
        """
        Funcion para visualizar el numero de intentos restantes
        :param letras_incorrectas: letras incorrectas anteriormente dichas
        """
        print(-(len(letras_incorrectas) - len(self.ESTADOS) - 1) - 2)


if __name__ == '__main__':
    juego1 = juegoAhorcado()
    juego1.jugar()
