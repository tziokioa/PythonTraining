# -*- coding: utf-8 -*-
import math

class Kruh:
    def obvodObsah(self):
        print ("Obvod kruhu:", 2 * math.pi * self.polomer)
        print ("Obsah kruhu:", math.pi * self.polomer**2)

kruh1 = Kruh()
kruh1.polomer=5
kruh1.obvodObsah()
