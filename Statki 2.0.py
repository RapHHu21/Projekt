import random
import tkinter as tk


class Plansza(tk.Tk):

    def __init__(self):
        super().__init__()

        self.x = 'light blue'
        self.geometry('1200x900+350+50')
        self.title('Statki')

        self.typ_pracy_gracz = 'normal'
        self.typ_pracy_bot = 'disabled'
        self.cheatmode_col = 'light blue'

        self.tablica_wyk_guzior_gracz = []
        self.tablica_wyk_guzior_on_bot = []
        self.tablica_wykorzystanych_guzik_strzal_bot = []
        self.tablica_statkow_gracz = []
        self.tablica_statkow_bot = []

        self.hitpoints_gracz = 8
        self.hitpoints_bot = 8
        self.licznik_onclick = -8
        self.statki_na_planszy = 0
        self.licznik_petla = -1

        self.return_value = True

        self.text_fazy = 'wybierz pozycje statkow'
        self.text_komunikat = '1: wybierz 3-polowy statek'

        napis_1 = tk.Label(self, text='plansza przeciwnika', pady=10)
        napis_1.grid(row=0, column=4, columnspan=3)
        napis_2 = tk.Label(self, text='twoja plansza', pady=10)
        napis_2.grid(row=0, column=17, columnspan=3)
        self.napis_fazy = tk.Label(self, text=f"{self.text_fazy}")
        self.napis_fazy.grid(row=0, column=11, columnspan=3)
        self.napis_komunikat = tk.Label(self, text=f"{self.text_komunikat}")
        self.napis_komunikat.grid(row=12, column=11, columnspan=3)

        plansza_bot_pink = 10
        columns_1 = 10
        self.btn_bot = [[None] * plansza_bot_pink for _ in range(columns_1)]

        for plansza_1 in range(plansza_bot_pink):
            for col_bot in range(columns_1):
                self.btn_bot[plansza_1][col_bot] = tk.Button(self, text=f"{plansza_1 + 1},{col_bot + 1}", width=5,
                                                             height=2, bg=self.x,
                                                             state=self.typ_pracy_bot, command=lambda r=col_bot,
                                                             c=plansza_1: self.button_click_bot(
                        r + 1, c + 1))
                self.btn_bot[plansza_1][col_bot].grid(row=plansza_1 + 2, column=col_bot, sticky='nsew')

        plansza_gap_black = 10
        columns_gap = 10
        self.btn_gap = [[None] * plansza_gap_black for _ in range(columns_gap)]

        for plansza_gap_black in range(10):
            for column_gap in range(3):
                self.btn_gap[plansza_gap_black][column_gap] = tk.Button(self, width=6, height=2, state='disabled',
                                                                        bg='black')
                self.btn_gap[plansza_gap_black][column_gap].grid(row=plansza_gap_black + 2, column=11 + column_gap,
                                                                 sticky='nsew')

        plansza_gracz_pink = 10
        columns_2 = 10
        self.btn_gracz = [[None] * plansza_gracz_pink for l in range(columns_2)]

        for plansza_2 in range(plansza_gracz_pink):
            for col_gracz in range(columns_2):
                self.btn_gracz[plansza_2][col_gracz] = tk.Button(self, text=f"{'s'},{'s'}", width=5, height=2,
                                                                bg=self.x, state=self.typ_pracy_gracz,
                                                                command=lambda r=col_gracz,
                                                                c=plansza_2: self.button_click_gracz(r + 1, c + 1))
                self.btn_gracz[plansza_2][col_gracz].grid(row=plansza_2 + 2, column=col_gracz + 14, sticky='nsew')

        self.btn_koniec = tk.Button(self, width=6, height=2, state='normal', bg='#ff3333', text='OFF',
                                    command=lambda: self.zamknij())
        self.btn_koniec.grid(row=13, column=0, sticky='nsew')
        self.napis_koniec = tk.Label(self, text='kliknij aby wylaczyc gre')
        self.napis_koniec.grid(row=13, column=1, columnspan=3)

        self.cheat_button = tk.Button(self, width=6, height=2, state='normal', bg='#ff3333', text='CHT', command=lambda: self.cheat_mode())
        self.cheat_button.grid(row=14, column=0, sticky='nsew')
        self.napis_cheat = tk.Label(self, text='kliknij aby wlaczyc Cheat Mode')
        self.napis_cheat.grid(row=14, column=1, columnspan=4)

    def cheat_mode(self):
        self.cheatmode_col = 'red'
        self.cheat_button.config(state='disabled')

    def button_click_gracz(self, row, column):
        if self.licznik_onclick < 0:

            if len(self.tablica_statkow_gracz) < 2:
                self.text_komunikat = '1: wybierz 3-polowy statek'
            elif 3 <= len(self.tablica_statkow_gracz) <= 5:
                self.text_komunikat = '2: wybierz 3-polowy statek'
            elif len(self.tablica_statkow_gracz) > 5:
                self.text_komunikat = '3: wybierz 2-polowy statek'

            if self.statek(row - 1, column - 1):
                self.licznik_onclick += 1
                self.tablica_statkow_gracz.append([row - 1, column - 1])
                self.btn_gracz[column - 1][row - 1].config(bg='yellow', state='disabled')

        if len(self.tablica_statkow_gracz) == 8 and self.licznik_onclick == 0:
            self.text_komunikat = ''
            self.statki_bota()

        self.licznik_petla += 1

        if self.licznik_onclick < 0:
            self.typ_pracy_gracz = 'disabled'
            self.typ_pracy_bot = 'disabled'
            self.text_fazy = 'wybierz pozycje statkow'
            self.tablica_wyk_guzior_gracz.append([row - 1, column - 1])

        else:
            self.typ_pracy_gracz = 'disabled'
            self.typ_pracy_bot = 'normal'
            self.text_fazy = 'oddaj strzal'

        for i in range(0, 10):
            for j in range(0, 10):
                if self.licznik_onclick >= 0:
                    if [i, j] not in self.tablica_wyk_guzior_on_bot:
                        self.btn_bot[i][j].config(state='normal')
                    else:
                        self.btn_bot[i][j].config(state='disabled')

                    self.btn_gracz[i - 1][j - 1].config(state='disabled')

        self.napis_fazy.config(text=self.text_fazy)
        self.napis_komunikat.config(text=self.text_komunikat)

    def button_click_bot(self, column, row):

        if self.hitpoints_bot > 0 and self.hitpoints_gracz > 0:
            self.tablica_wyk_guzior_on_bot.append([row - 1, column - 1])

            if self.licznik_onclick % 2 == 0 and self.licznik_onclick >= 0:
                self.typ_pracy_bot = 'normal'

            for i in range(0, 10):
                for j in range(0, 10):
                    self.btn_gracz[i][j].config(state='disabled')
                    if [i, j] not in self.tablica_wyk_guzior_on_bot:
                        self.btn_bot[i][j].config(state='disabled')
                    if [i, j] in self.tablica_statkow_bot:
                        self.btn_bot[i][j].config(bg=self.cheatmode_col)
                    if [i,j] in self.tablica_statkow_bot and [i,j] in self.tablica_wyk_guzior_on_bot:
                        self.btn_bot[i][j].config(bg='green')

            if [row-1, column-1] not in self.tablica_statkow_bot:
                self.btn_bot[row - 1][column - 1].config(bg='blue')

            self.czy_trafiony_bot(row - 1, column - 1)

            self.licznik_onclick += 1
            self.button_strzal_on_gracz()

    def button_strzal_on_gracz(self):

        if self.hitpoints_bot > 0 and self.hitpoints_gracz > 0:
            wspolrzedna_X_strzalu = random.randint(0, 9)
            wspolrzedna_Y_strzalu = random.randint(0, 9)

            if self.licznik_onclick >= 0:
                if [wspolrzedna_X_strzalu, wspolrzedna_Y_strzalu] not in self.tablica_wykorzystanych_guzik_strzal_bot:
                    self.tablica_wykorzystanych_guzik_strzal_bot.append([wspolrzedna_X_strzalu, wspolrzedna_Y_strzalu])
                    self.button_click_gracz(wspolrzedna_X_strzalu, wspolrzedna_Y_strzalu)
                    for i in range(0, 10):
                        for j in range(0, 10):
                            self.btn_gracz[wspolrzedna_Y_strzalu][wspolrzedna_X_strzalu].config(bg='black')
                    self.czy_trafiony_gracz(wspolrzedna_Y_strzalu, wspolrzedna_X_strzalu)
                else:
                    self.button_strzal_on_gracz()

    def statek(self, pozycja_X, pozycja_Y):
        # sprawdzanie poprawnosci ulozonych statkow

        tablica_wewn_statek = self.tablica_statkow_gracz
        dlugosc_tablica = len(tablica_wewn_statek)

        if 1 <= dlugosc_tablica < 3:
            statek_1 = tablica_wewn_statek[0]
            if dlugosc_tablica >= 2:
                statek_2 = tablica_wewn_statek[1]
        elif 4 <= dlugosc_tablica < 6:
            statek_1 = tablica_wewn_statek[3]
            if dlugosc_tablica >= 5:
                statek_2 = tablica_wewn_statek[4]
        elif dlugosc_tablica >= 7:
            statek_1 = tablica_wewn_statek[6]

        if 1 <= dlugosc_tablica < 9 and dlugosc_tablica % 3 != 0:

            if statek_1[0] == pozycja_X:
                if abs(statek_1[1] - pozycja_Y) == 1:
                    if dlugosc_tablica != 1 and dlugosc_tablica != 4 and dlugosc_tablica != 7:
                        self.return_value = False
                    else:
                        self.return_value = True
                        return self.return_value
                else:
                    self.return_value = False
                if 2 <= dlugosc_tablica < 4 or 5 <= dlugosc_tablica < 7:
                    if statek_2[0] == pozycja_X:
                        self.return_value = True
                        if dlugosc_tablica == 2 or dlugosc_tablica == 5:
                            if abs(statek_1[1] - pozycja_Y) == 1 and abs(statek_2[1] - pozycja_Y) == 2:
                                self.return_value = True
                            elif abs(statek_1[1] - pozycja_Y) == 2 and abs(statek_2[1] - pozycja_Y) == 1:
                                self.return_value = True
                            else:
                                self.return_value = False
                    else:
                        self.return_value = False
                        return self.return_value

            elif statek_1[1] == pozycja_Y:
                if abs(statek_1[0] - pozycja_X) == 1:
                    if dlugosc_tablica != 1 and dlugosc_tablica != 4 and dlugosc_tablica != 7:
                        self.return_value = False
                    else:
                        self.return_value = True
                        return self.return_value
                else:
                    self.return_value = False

                if 2 <= dlugosc_tablica < 4 or 5 <= dlugosc_tablica < 7:
                    if statek_2[1] == pozycja_Y:
                        self.return_value = True
                        if dlugosc_tablica == 2 or dlugosc_tablica == 5:
                            if abs(statek_1[0] - pozycja_X) == 1 and abs(statek_2[0] - pozycja_X) == 2:
                                self.return_value = True
                            elif abs(statek_1[0] - pozycja_X) == 2 and abs(statek_2[0] - pozycja_X) == 1:
                                self.return_value = True
                            else:
                                self.return_value = False
                    else:
                        self.return_value = False
                        return self.return_value

            else:
                self.return_value = False

            return self.return_value
        elif dlugosc_tablica % 3 == 0:
            return True

    def statki_bota(self):
        losowa_1 = random.randint(0, 100)
        losowa_2 = random.randint(0, 100)
        losowa_3 = random.randint(0, 100)

        # statek 1
        if losowa_1 < 50:
            pozycja_y_1 = random.randint(0, 9)
            pozycja_x_1 = random.randint(0, 7)

            i = 0
            while i < 3:
                self.tablica_statkow_bot.append([pozycja_x_1 + i, pozycja_y_1])
                i += 1
        else:
            pozycja_y_1 = random.randint(0, 7)
            pozycja_x_1 = random.randint(0, 9)
            i = 0
            while i < 3:
                self.tablica_statkow_bot.append([pozycja_x_1, pozycja_y_1 + i])
                i += 1

        # statek 2
        if losowa_2 < 50:
            pozycja_x_2 = random.randint(0, 7)
            pozycja_y_2 = random.randint(0, 9)

            def statek2(wsp_x, wsp_y):

                if pozycja_y_1 <= wsp_y >= pozycja_y_1 and abs(wsp_x - pozycja_x_1) >= 3:
                    i = 0
                    while i < 3:
                        self.tablica_statkow_bot.append([wsp_x + i, wsp_y])
                        i += 1
                else:
                    statek2(random.randint(0, 7), random.randint(0, 9))

            statek2(pozycja_x_2, pozycja_y_2)

        else:
            pozycja_x_2 = random.randint(0, 9)
            pozycja_y_2 = random.randint(0, 7)

            def statek2(wsp_x, wsp_y):

                if pozycja_x_1 <= wsp_x >= pozycja_x_1 and abs(wsp_y - pozycja_y_1) >= 3:
                    i = 0
                    while i < 3:
                        self.tablica_statkow_bot.append([wsp_x, wsp_y + i])
                        i += 1
                else:
                    statek2(random.randint(0, 9), random.randint(0, 7))

            statek2(pozycja_x_2, pozycja_y_2)

        # statek 3
        if losowa_3 < 50:
            pozycja_x_3 = random.randint(0, 9)
            pozycja_y_3 = random.randint(0, 7)

            def statek3(wsp_x, wsp_y):
                if ([wsp_x, wsp_y] in self.tablica_statkow_bot) or ([wsp_x, wsp_y + 1] in self.tablica_statkow_bot):
                    statek3(random.randint(0, 9), random.randint(0, 7))
                else:
                    self.tablica_statkow_bot.append([wsp_x, wsp_y])
                    self.tablica_statkow_bot.append([wsp_x, wsp_y + 1])
                    return

            statek3(pozycja_x_3, pozycja_y_3)

        else:
            pozycja_x_3 = random.randint(0, 7)
            pozycja_y_3 = random.randint(0, 9)

            def statek3(wsp_x, wsp_y):
                if ([wsp_x, wsp_y] in self.tablica_statkow_bot) or ([wsp_x + 1, wsp_y] in self.tablica_statkow_bot):
                    statek3(random.randint(0, 7), random.randint(0, 9))
                else:
                    self.tablica_statkow_bot.append([wsp_x, wsp_y])
                    self.tablica_statkow_bot.append([wsp_x + 1, wsp_y])
                    return

            statek3(pozycja_x_3, pozycja_y_3)

    def czy_trafiony_bot(self, wsp_x, wsp_y):
        if self.hitpoints_bot > 0 and self.hitpoints_gracz > 0:
            if [wsp_x, wsp_y] in self.tablica_statkow_bot:
                self.hitpoints_bot -= 1
                if self.hitpoints_bot == 0:
                    self.koniec_gry()

    def czy_trafiony_gracz(self, wsp_x, wsp_y):
        if self.hitpoints_bot > 0 and self.hitpoints_gracz > 0:
            if [wsp_y, wsp_x] in self.tablica_statkow_gracz:
                self.hitpoints_gracz -= 1
                self.btn_gracz[wsp_x][wsp_y].config(bg='red')
            if self.hitpoints_gracz == 0:
                self.koniec_gry()

    def koniec_gry(self):
        for i in range(0, 10):
            for j in range(0, 10):
                self.btn_bot[i][j].config(bg='black', text='', state='disabled')
                self.btn_gracz[i][j].config(bg='black', text='', state='disabled')

        if self.hitpoints_bot == 0:

            # plansza_bota, litera W
            for i in range(5, 10):
                if i % 2 == 1:
                    self.btn_bot[4][i].config(bg='green', state='disabled')
                    self.btn_bot[5][i].config(bg='green', state='disabled')
                else:
                    self.btn_bot[6][i].config(bg='green', state='disabled')

            # plansza_gap litera I
            for i in range(0, 2):
                if i == 1:
                    self.btn_gap[4][i].config(bg='green', state='disabled')
                    self.btn_gap[5][i].config(bg='green', state='disabled')
                    self.btn_gap[6][i].config(bg='green', state='disabled')

            # plansza_gracza, litera N
            pixel = 0
            for i in range(0, 5):
                if i ==0 or i == 4:
                    self.btn_gracz[4][i].config(bg='green', state='disabled')
                    self.btn_gracz[5][i].config(bg='green', state='disabled')
                    self.btn_gracz[6][i].config(bg='green', state='disabled')
                else:
                    self.btn_gracz[4 + pixel][i].config(bg='green', state='disabled')
                    pixel += 1

        elif self.hitpoints_gracz == 0:

            # litera L
            for i in range(5, 7):
                if i == 5:
                    self.btn_bot[4][i].config(bg='red', state='disabled')
                    self.btn_bot[5][i].config(bg='red', state='disabled')
                    self.btn_bot[6][i].config(bg='red', state='disabled')
                else:
                    self.btn_bot[6][i].config(bg='red', state='disabled')

            # plansza_bota, litera O
            for i in range(8, 10):
                if i == 8:
                    self.btn_bot[4][i].config(bg='red', state='disabled')
                    self.btn_bot[5][i].config(bg='red', state='disabled')
                    self.btn_bot[6][i].config(bg='red', state='disabled')
                else:
                    self.btn_bot[4][i].config(bg='red', state='disabled')
                    self.btn_bot[6][i].config(bg='red', state='disabled')

            # plansza_gap, litera O,S
            for i in range(0,3):
                if i == 0:
                    self.btn_gap[4][i].config(bg='red', state='disabled')
                    self.btn_gap[5][i].config(bg='red', state='disabled')
                    self.btn_gap[6][i].config(bg='red', state='disabled')
                elif i == 2:
                    self.btn_gap[6][i].config(bg='red', state='disabled')

            # plansza_gracz, litera S,T
            for i in range(0,6):
                if i == 0 or i == 4:
                    self.btn_gracz[4][i].config(bg='red', state='disabled')
                    self.btn_gracz[5][i].config(bg='red', state='disabled')
                    self.btn_gracz[6][i].config(bg='red', state='disabled')
                elif i != 2:
                    self.btn_gracz[4][i].config(bg='red', state='disabled')

    def zamknij(self):
        self.destroy()

plansza = Plansza()
plansza.mainloop()
