class Guitar:
    def play(self):
        print("playing the guitar")


def play_instrument(instrument):
    return instrument.play()


guitar = Guitar()
play_instrument(guitar)
