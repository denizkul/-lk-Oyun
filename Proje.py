import pygame

import random


pygame.init()


class Oyuncu:
    def __init__(self, can, OyuncuX, OyuncuY, Resim):
        self.can = can
        self.OyuncuX = OyuncuX
        self.OyuncuY = OyuncuY
        self.OyuncuResim = Resim

    def Cizim(self, Pencere):
        Pencere.blit(self.OyuncuResim, (self.OyuncuX, self.OyuncuY))

    def Kordinat(self, Genislik, Yukseklik):
        return pygame.Rect(self.OyuncuX, self.OyuncuY, Genislik, Yukseklik)

    def YerKordinat(self, Genislik, Yukseklik):
        return pygame.Rect(self.OyuncuX, self.OyuncuY + 100, Genislik, Yukseklik)

    def UstTaraf(self, Genislik):
        return pygame.Rect(self.OyuncuX, self.OyuncuY, Genislik, 1)


class Nesneler:
    def __init__(self, NesneX, NesneY, Resim, Hiz):
        self.NesneX = NesneX
        self.NesneY = NesneY
        self.Resim = Resim
        self.Hiz = Hiz

    def Cizim(self, Pencere):
        Pencere.blit(self.Resim, (self.NesneX, self.NesneY))

    def Kordinatlar(self, Genislik, Yukseklik):
        return pygame.Rect(self.NesneX, self.NesneY, Genislik, Yukseklik)

    def Hareket(self):
        self.NesneX -= self.Hiz
        return self.NesneX

    def AltTaraf(self, Genislik):
        return pygame.Rect(self.NesneX, (self.NesneY + self.NesneY), Genislik, 1)

    def HizArtir(self, artir):
        self.Hiz += artir


class BizimOyunumuz:
    def __init__(self):
        self.pencere_yuksekligi = 685
        self.pencere_genisligi = 928
        self.Pencere = pygame.display.set_mode((self.pencere_genisligi, self.pencere_yuksekligi))
        self.Arkaplan = pygame.image.load("Assets/Background.png").convert_alpha()
        pygame.display.set_caption("Coin Yakalama")

        self.kalp = pygame.image.load("Assets/S_ItemLightOutline_HeartRed_00.png").convert_alpha()
        self.kalp = pygame.transform.scale(self.kalp, (30, 24))

        self.SariKalp = pygame.image.load("Assets/S_ItemLightOutline_HeartGold_00.png").convert_alpha()
        self.SariKalp = pygame.transform.scale(self.SariKalp, (30, 24))

        self.KIksirResmi = pygame.image.load("Assets/S_ItemLightOutline_JarRed_00.png").convert_alpha()
        self.KIksirResmi = pygame.transform.scale(self.KIksirResmi, (30, 36))
        self.KIksirListesi = []
        self.KIksirSayisi = 3

        self.MIksirResmi = pygame.image.load("Assets/S_ItemLightOutline_JarBlue_00.png").convert_alpha()
        self.MIksirResmi = pygame.transform.scale(self.MIksirResmi, (30, 36))
        self.MIksirListesi = []
        self.MIksirSayisi = 2

        self.SIksirResmi = pygame.image.load("Assets/S_ItemLightOutline_JarGold_00.png").convert_alpha()
        self.SIksirResmi = pygame.transform.scale(self.SIksirResmi, (30, 36))
        self.SIksirListesi = []
        self.SIksirSayisi = 1

        self.OyuncuKare = pygame.image.load("Assets/kare.jpg").convert_alpha()
        self.OyuncuKare = pygame.transform.scale(self.OyuncuKare, (80, 80))
        self.DusmanKare = pygame.image.load("Assets/kare2.jpg").convert_alpha()
        self.DusmanKare = pygame.transform.scale(self.DusmanKare, (20, 20))

        self.SariAltin = pygame.image.load("Assets/S_ItemLightOutline_CoinGold_00.png").convert_alpha()
        self.SariAltin = pygame.transform.scale(self.SariAltin, (30, 36))

        self.YesilAltin = pygame.image.load("Assets/S_ItemLightOutline_CoinGreen_00.png").convert_alpha()
        self.YesilAltin = pygame.transform.scale(self.YesilAltin, (30, 36))

        self.MaviAltin = pygame.image.load("Assets/S_ItemLightOutline_CoinBlue_00.png").convert_alpha()
        self.MaviAltin = pygame.transform.scale(self.MaviAltin, (25, 30))

        self.KirmiziAltin = pygame.image.load("Assets/S_ItemLightOutline_CoinRed_00.png").convert_alpha()
        self.KirmiziAltin = pygame.transform.scale(self.KirmiziAltin, (30, 36))

        self.Altinlar = []
        self.AltinSayisi = 3

        self.DusmanListesi = []
        self.DusmanSayisi = 3

        self.Oyuncu = Oyuncu(3, 300, 520, self.OyuncuKare)
        self.OyunFont = pygame.font.SysFont("Arial", 40)
        self.SkorFont = pygame.font.SysFont("Arial", 30)
        self.Clock = pygame.time.Clock()
        self.Durum = "Oyun"
        self.Hizasgari = 1
        self.Hizlimit = 10
        self.Skor = 0

    def Cizim(self):
        self.Pencere.blit(self.Arkaplan, (0, 0))

        if self.Durum == "Oyun":

            self.Oyuncu.Cizim(self.Pencere)

            for KIksir in self.KIksirListesi:
                KIksir.Cizim(self.Pencere)

            for Dusman in self.DusmanListesi:
                Dusman.Cizim(self.Pencere)

            for MIksir in self.MIksirListesi:
                MIksir.Cizim(self.Pencere)

            for SIksir in self.SIksirListesi:
                SIksir.Cizim(self.Pencere)

            for Altin in self.Altinlar:
                Altin.Cizim(self.Pencere)

            if self.Oyuncu.can == 5:
                self.Pencere.blit(self.kalp, (self.KalpX, self.KalpY))
                self.Pencere.blit(self.kalp, (self.KalpX + 11, self.KalpY))
                self.Pencere.blit(self.kalp, (self.KalpX + 22, self.KalpY))
                self.Pencere.blit(self.SariKalp, (self.KalpX + 33, self.KalpY))
                self.Pencere.blit(self.SariKalp, (self.KalpX + 44, self.KalpY))

            elif self.Oyuncu.can == 4:
                self.Pencere.blit(self.kalp, (self.KalpX, self.KalpY))
                self.Pencere.blit(self.kalp, (self.KalpX + 11, self.KalpY))
                self.Pencere.blit(self.kalp, (self.KalpX + 22, self.KalpY))
                self.Pencere.blit(self.SariKalp, (self.KalpX + 33, self.KalpY))

            elif self.Oyuncu.can == 3:
                self.Pencere.blit(self.kalp, (self.KalpX, self.KalpY))
                self.Pencere.blit(self.kalp, (self.KalpX + 11, self.KalpY))
                self.Pencere.blit(self.kalp, (self.KalpX + 22, self.KalpY))

            elif self.Oyuncu.can == 2:
                self.Pencere.blit(self.kalp, (self.KalpX, self.KalpY))
                self.Pencere.blit(self.kalp, (self.KalpX + 11, self.KalpY))

            elif self.Oyuncu.can == 1:
                self.Pencere.blit(self.kalp, (self.KalpX, self.KalpY))
            self.Pencere.blit(self.MaviAltin, (8, 30))
            self.Pencere.blit(self.SkorFont.render("= " + str(self.Skor), True, (0, 0, 255)), (40, 30))
        elif self.Durum == "Bitti":
            self.Pencere.blit(self.OyunFont.render("CANIN KALMADI!", True, (0, 0, 0)), (200, 300))
            self.Pencere.blit(self.OyunFont.render("TEKRAR GİRMEK İÇİN Q'YE BASIN", True, (0, 0, 0)), (200, 350))
            self.Pencere.blit(self.SkorFont.render("Skorun: " + str(self.Skor), True, (0, 0, 0)), (30, 30))

        self.Clock.tick(60)
        pygame.display.update()

    def Oyun(self):

        def NesneOlustur(clas, liste, sayi, resim):
            if len(liste) != sayi:
                liste.append(clas(941, random.randint(50, 900), resim, random.randint(self.Hizasgari, self.Hizlimit)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Son"
        self.Tus = pygame.key.get_pressed()
        if self.Tus[pygame.K_ESCAPE]:
            return "Son"

        if self.Durum == "Oyun":
            self.KalpX = 30
            self.KalpY = 70

            if self.Tus[pygame.K_a]:
                if self.Tus[pygame.K_w]:
                    self.Oyuncu.OyuncuX -= 5
                    self.Oyuncu.OyuncuY -= 5
                elif self.Tus[pygame.K_s]:
                    self.Oyuncu.OyuncuX -= 5
                    self.Oyuncu.OyuncuY += 5
                else:
                    self.Oyuncu.OyuncuX -= 5

            elif self.Tus[pygame.K_d]:
                if self.Tus[pygame.K_w]:
                    self.Oyuncu.OyuncuY -= 5
                    self.Oyuncu.OyuncuX += 5
                elif self.Tus[pygame.K_s]:
                    self.Oyuncu.OyuncuY += 5
                    self.Oyuncu.OyuncuX += 5
                else:
                    self.Oyuncu.OyuncuX += 5

            elif self.Tus[pygame.K_s]:
                if self.Tus[pygame.K_d]:
                    self.Oyuncu.OyuncuY += 5
                    self.Oyuncu.OyuncuX += 5
                elif self.Tus[pygame.K_a]:
                    self.Oyuncu.OyuncuY += 5
                    self.Oyuncu.OyuncuX -= 5
                else:
                    self.Oyuncu.OyuncuY += 5

            elif self.Tus[pygame.K_w]:
                if self.Tus[pygame.K_a]:
                    self.Oyuncu.OyuncuY -= 5
                    self.Oyuncu.OyuncuX -= 5
                elif self.Tus[pygame.K_d]:
                    self.Oyuncu.OyuncuY -= 5
                    self.Oyuncu.OyuncuX += 5
                else:
                    self.Oyuncu.OyuncuY -= 5

            NesneOlustur(Nesneler, self.KIksirListesi, self.KIksirSayisi, self.KIksirResmi)

            NesneOlustur(Nesneler, self.DusmanListesi, self.DusmanSayisi, self.DusmanKare)

            NesneOlustur(Nesneler, self.MIksirListesi, self.MIksirSayisi, self.MIksirResmi)

            NesneOlustur(Nesneler, self.SIksirListesi, self.SIksirSayisi, self.SIksirResmi)

            if self.Skor <= 5:
                if len(self.Altinlar) != self.AltinSayisi:
                    self.Altinlar.append(Nesneler(941, random.randint(50, 900), self.SariAltin,
                                                       random.randint(self.Hizasgari, self.Hizlimit)))
            elif (self.Skor <= 10) and (self.Skor > 5):
                if len(self.Altinlar) != self.AltinSayisi:
                    self.Altinlar.append(Nesneler(941, random.randint(50, 900), self.YesilAltin,
                                                       random.randint(self.Hizasgari, self.Hizlimit)))
            else:
                if len(self.Altinlar) != self.AltinSayisi:
                    self.Altinlar.append(Nesneler(941, random.randint(50, 900), self.KirmiziAltin,
                                                       random.randint(self.Hizasgari, self.Hizlimit)))

            for Dusman in self.DusmanListesi:
                if Dusman.NesneX <= 0:
                    self.DusmanListesi.pop(self.DusmanListesi.index(Dusman))
                Dusman.Hareket()
                if (self.Oyuncu.Kordinat(100, 100)).colliderect(Dusman.Kordinatlar(20, 20)):
                    self.Oyuncu.can -= 1
                    self.DusmanListesi.pop(self.DusmanListesi.index(Dusman))

            for KIksir in self.KIksirListesi:
                if KIksir.NesneX <= 0:
                    self.KIksirListesi.pop(self.KIksirListesi.index(KIksir))
                KIksir.Hareket()
                if (self.Oyuncu.Kordinat(80, 80)).colliderect(KIksir.Kordinatlar(30, 36)):
                    self.KIksirListesi.pop(self.KIksirListesi.index(KIksir))
                    if self.Oyuncu.can < 3:
                        self.Oyuncu.can += 1

            for MIksir in self.MIksirListesi:
                if MIksir.NesneX <= 0:
                    self.MIksirListesi.pop(self.MIksirListesi.index(MIksir))
                MIksir.Hareket()
                if (self.Oyuncu.Kordinat(80, 80)).colliderect(MIksir.Kordinatlar(30, 36)):
                    self.Hizasgari += 1
                    self.Hizlimit += 1
                    self.MIksirListesi.pop(self.MIksirListesi.index(MIksir))

            for SIksir in self.SIksirListesi:
                if SIksir.NesneX <= 0:
                    self.SIksirListesi.pop(self.SIksirListesi.index(SIksir))
                SIksir.Hareket()
                if (self.Oyuncu.Kordinat(80, 80)).colliderect(SIksir.Kordinatlar(30, 36)):
                    if self.Oyuncu.can >= 3 and self.Oyuncu.can != 5:
                        self.Oyuncu.can += 1
                    self.SIksirListesi.pop(self.SIksirListesi.index(SIksir))

            for Coin in self.Altinlar:
                if Coin.NesneX <= -7:
                    self.Altinlar.pop(self.Altinlar.index(Coin))
                Coin.Hareket()
                if (self.Oyuncu.Kordinat(80, 80)).colliderect(Coin.Kordinatlar(32, 40)):
                    if Coin.Resim == self.SariAltin:
                        self.Skor += 1

                    elif Coin.Resim == self.YesilAltin:
                        self.Skor += 2

                    else:
                        self.Skor += 3
                    self.Altinlar.pop(self.Altinlar.index(Coin))

            if self.Oyuncu.can == 0:
                self.Durum = "Bitti"

        elif self.Durum == "Bitti":
            if self.Tus[pygame.K_q]:
                self.Durum = "Oyun"
                self.Oyuncu.can = 3
                for KIksir in self.KIksirListesi:
                    KIksir.NesneX = 941

                for MIksir in self.MIksirListesi:
                    MIksir.NesneX = 941

                for SIksir in self.SIksirListesi:
                    SIksir.NesneX = 941

                for Dusman in self.DusmanListesi:
                    Dusman.NesneX = 941

                self.Oyuncu.OyuncuX = 300
                self.Oyuncu.OyuncuY = 520

                self.Hizasgari = 1
                self.Hizlimit = 10

                self.Skor = 0

        self.Cizim()


Oyun = BizimOyunumuz()

while True:
    Durum = Oyun.Oyun()
    if Durum == "Son":
        break

pygame.quit()
