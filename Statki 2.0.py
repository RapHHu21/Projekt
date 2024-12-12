import random
import tkinter as tk



class Plansza(tk.Tk):

    def __init__(self):
        super().__init__()

        self.text_fazy = 'wybierz pozycje statkow'
        self.x = 'light blue'
        self.geometry('1200x900+350+50')
        self.title('piwo')
        self.licznik_onclick = -7
        self.typ_pracy_gracz = 'normal'
        self.typ_pracy_bot = 'disabled'
        self.tablica_wyk_guzior_gracz = []
        self.tablica_wyk_guzior_bot = []
        self.tablica_wykorzystanych_guzik_strzal_bot = []
        self.tablica_statkow_gracz = []
        self.statki_na_planszy = 0
        self.return_value = True
        self.licznik_petla = -1


        napis_1 = tk.Label(self, text='plansza przeciwnika', pady=10)
        napis_1.grid(row=0, column=4, columnspan=3)
        napis_2 = tk.Label(self, text='twoja plansza', pady=10)
        napis_2.grid(row=0, column=17, columnspan=3)
        self.napis_fazy = tk.Label(self, text=f"{self.text_fazy}")
        self.napis_fazy.grid(row=0, column=11, columnspan=3)



        plansza_bot_pink = 10
        columns_1 = 10
        self.btn_bot = [[None] * plansza_bot_pink for _ in range(columns_1)]

        for plansza_1 in range(plansza_bot_pink):
            for col_bot in range(columns_1):
                self.btn_bot[plansza_1][col_bot] = tk.Button(self, text=f"{plansza_1 + 1},{col_bot + 1}", width=5, height=2, bg=self.x,
                                                             state= self.typ_pracy_bot, command=lambda r=plansza_1,
                                                             c=col_bot: self.button_click_bot(r + 1, c + 1))
                self.btn_bot[plansza_1][col_bot].grid(row=plansza_1 + 2, column=col_bot, sticky='nsew')

        for row_gap in range(10):
            for column_gap in range(3):
                self.btn_gap = tk.Button(self, width=6, height=2, state='disabled', bg='#000000')
                self.btn_gap.grid(row=row_gap + 2, column=11 + column_gap,sticky='nsew')

        plansza_gracz_pink = 10
        columns_2 = 10
        self.btn_gracz = [[None] * plansza_gracz_pink for l in range(columns_2)]

        for plansza_2 in range(plansza_gracz_pink):
            for col_gracz in range(columns_2):
                self.btn_gracz[plansza_2][col_gracz] = tk.Button(self, text=f"{'s'},{'s'}", width=5, height=2, bg=self.x, state=self.typ_pracy_gracz,
                                                                 command=lambda r=plansza_2, c=col_gracz: self.button_click_gracz(r + 1, c + 1))
                self.btn_gracz[plansza_2][col_gracz].grid(row=plansza_2 + 2, column=col_gracz + 14, sticky='nsew')

    def button_click_gracz(self, row, column):

        self.tablica_wyk_guzior_gracz.append([row - 1, column - 1])
        print(self.tablica_wyk_guzior_gracz)

        if self.licznik_onclick <= 0:
            self.typ_pracy_gracz = 'disabled'
            self.typ_pracy_bot = 'disabled'
            self.text_fazy = 'wybierz pozycje statkow'
            self.tablica_statkow_gracz.append([row-1,column-1])

        else:
            self.typ_pracy_gracz = 'disabled'
            self.typ_pracy_bot = 'normal'
            self.text_fazy = 'oddaj strzal'



        for i in range (0,10):
            for j in range (0,10):
                if self.licznik_onclick >= 0:
                    if [i, j] not in self.tablica_wyk_guzior_bot:
                        self.btn_bot[i][j].config(state='normal')
                    else:
                        self.btn_bot[i][j].config(state='disabled')
                if self.licznik_onclick <= 0:
                    if [i,j] in self.tablica_wyk_guzior_gracz:
                        self.btn_gracz[i][j].config(state ='disabled', bg='red')
                if self.licznik_onclick >= 0:
                    self.btn_gracz[i - 1][j - 1].config(state='disabled')

        self.napis_fazy.config(text=self.text_fazy)


        print(self.typ_pracy_gracz)
        print(self.licznik_onclick)
        print(self.tablica_statkow_gracz, ' statki')


        if self.statek() == True:
            self.licznik_onclick += 1
        self.licznik_petla += 1
        print(self.licznik_onclick, ' funk2')
        print(self.licznik_petla, ' licznik 2')
    def button_click_bot(self, row, column):

        self.tablica_wyk_guzior_bot.append([row-1,column-1])
        self.btn_bot[row - 1][column - 1].config(bg='blue')

        if self.licznik_onclick % 2 == 0 and self.licznik_onclick >= 0:
            self.typ_pracy_bot = 'normal'

        print(self.tablica_wyk_guzior_bot, " guziki")
        for i in range (0,10):
            for j in range (0,10):
                self.btn_gracz[i][j].config(state='disabled')
                if [i,j] not in self.tablica_wyk_guzior_bot:
                    self.btn_bot[i][j].config(state='disabled')

        self.button_strzal_on_gracz()

        print(self.licznik_onclick, ' funk1')
        self.licznik_onclick +=1

    def button_strzal_on_gracz(self):

        wspolrzedna_X_strzalu = random.randint(0, 9)
        wspolrzedna_Y_strzalu = random.randint(0, 9)

        print(wspolrzedna_Y_strzalu)

        if self.licznik_onclick >= 0:
            print(wspolrzedna_X_strzalu)
            print(wspolrzedna_Y_strzalu)
            if [wspolrzedna_X_strzalu, wspolrzedna_Y_strzalu] not in self.tablica_wykorzystanych_guzik_strzal_bot:
                self.tablica_wykorzystanych_guzik_strzal_bot.append([wspolrzedna_X_strzalu, wspolrzedna_Y_strzalu])
                self.button_click_gracz(wspolrzedna_X_strzalu, wspolrzedna_Y_strzalu)
                for i in range(0, 10):
                    for j in range(0, 10):
                        self.btn_gracz[wspolrzedna_X_strzalu - 1][wspolrzedna_Y_strzalu - 1].config(bg='black')
            else:
                self.button_strzal_on_gracz()


    def statek(self):
        b = self.tablica_statkow_gracz
        c = self.licznik_petla

        if c <= 6:

            if len(b) > 1:
                if (b[0][0] == b[c][0]) or (b[0][1] == b[c][1]):
                    print('jest git')
                    self.return_value = True
                else:
                    self.return_value = False

            return self.return_value





if __name__ == "__main__":
    plansza = Plansza()
    plansza.mainloop()