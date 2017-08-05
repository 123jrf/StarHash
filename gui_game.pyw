import os, packet, random, ships, winsound
from tkinter import *
from PIL import Image, ImageTk
#import render

soundfx = False

if soundfx:
    winsound.PlaySound("resources/starhash.wav", winsound.SND_FILENAME)

class Application(Frame):
    """An application for the game gui."""
    widgets = []

    def __init__(self, master):
        """Create the gui."""
        super().__init__(master)
        self.master = master
        self.grid()

        # Load images
        self.images = [
            ImageTk.PhotoImage(Image.open("resources/titlescreen.bmp")),
            ImageTk.PhotoImage(Image.open("resources/passplay.bmp"))
            ]
        
        self.title_screen()

    def clear(self):
        """Clear ALL the widgets."""
        for widget in self.widgets:
            widget.destroy()

    def title_screen(self):
        self.clear()
        self.master.geometry("405x300")

        # Title image
        title_image = Label(image = self.images[0])
        title_image.grid(row = 0, column = 0)
        self.widgets.append(title_image)

        space1 = Label(text = "")
        space1.grid(row = 1, column = 0)
        self.widgets.append(space1)

        # Pass and play
        button_pass = Button(text = "Pass n' Play")
        button_pass.grid(row = 2, column = 0)
        button_pass['command'] = self.pass_play_menu
        self.widgets.append(button_pass)

        pass_lbl = Label(text = "Share this computer with a friend.")
        pass_lbl.grid(row = 3, column = 0)
        self.widgets.append(pass_lbl)

        space2 = Label(text = "")
        space2.grid(row = 4, column = 0)
        self.widgets.append(space2)

        # Online multiplayer
        button_online = Button(text = "Online Multiplayer")
        button_online.grid(row = 5, column = 0)
        self.widgets.append(button_online)

        online_lbl = Label(text = "Play with someone on the internets!")
        online_lbl.grid(row = 6, column = 0)
        self.widgets.append(online_lbl)

    def pass_play_menu(self):
        self.clear()
        self.master.geometry("405x300")

        # Title image
        title_image = Label(image = self.images[1])
        title_image.grid(row = 0, column = 0, columnspan = 3)
        self.widgets.append(title_image)

        # Back to title screen
        back_button = Button(text = "Back to Title Screen")
        back_button['command'] = self.title_screen
        back_button.grid(row = 1, column = 0, sticky = W)
        self.widgets.append(back_button)

        space1 = Label(text = "")
        space1.grid(row = 2, column = 0)
        self.widgets.append(space1)

        rspace = Label(text = "\t\t\tlong")
        rspace.grid(row = 2, column = 3)
        self.widgets.append(rspace)

        # Player 1 Name Entry
        player1n = Label(text = "Player 1's Name:")
        player1n.grid(row = 3, column = 0)
        self.widgets.append(player1n)
        
        self.player1n = Entry()
        self.player1n.grid(row = 3, column = 1, sticky = W)
        self.widgets.append(self.player1n)

        # Player 1 Seed Entry
        player1s = Label(text = "Player 1's Seed:")
        player1s.grid(row = 4, column = 0)
        self.widgets.append(player1s)
        
        self.player1s = Entry()
        self.player1s.grid(row = 4, column = 1, sticky = W)
        self.widgets.append(self.player1s)

        space2 = Label(text = "")
        space2.grid(row = 5, column = 0)
        self.widgets.append(space2)

        # Player 2 Name Entry
        player2n = Label(text = "Player 2's Name:")
        player2n.grid(row = 6, column = 0)
        self.widgets.append(player2n)
        
        self.player2n = Entry()
        self.player2n.grid(row = 6, column = 1, sticky = W)
        self.widgets.append(self.player2n)

        # Player 2 Seed Entry
        player2s = Label(text = "Player 2's Seed:")
        player2s.grid(row = 7, column = 0)
        self.widgets.append(player2s)
        
        self.player2s = Entry()
        self.player2s.grid(row = 7, column = 1, sticky = W)
        self.widgets.append(self.player2s)

        space3 = Label(text = "")
        space3.grid(row = 8, column = 0)
        self.widgets.append(space3)

        # Start button
        back_button = Button(text = "Play!")
        back_button['command'] = self.pass_play
        back_button.grid(row = 9, column = 1, sticky = N)
        self.widgets.append(back_button)

    def pass_play(self):
        self.ship1 = ships.Ship()
        self.ship1.generate(self.player1s.get())
        self.ship1.name = self.player1n.get()
        if not self.ship1.name.strip():
            self.ship1.name = "Player 1"

        self.ship2 = ships.Ship()
        self.ship2.generate(self.player2s.get())
        self.ship2.name = self.player2n.get()
        if not self.ship2.name.strip():
            self.ship2.name = "Player 2"

        self.clear()
        self.master.geometry("894x500")

        player1 = Label(text = self.ship1.name + "'s Ship:")
        player1.grid(row = 0, column = 0)
        self.widgets.append(player1)

        player2 = Label(text = self.ship2.name + "'s Ship:")
        player2.grid(row = 0, column = 2)
        self.widgets.append(player2)

        # Ship info texts
        for ship in (self.ship1, self.ship2):
            ship.status = Text(width = 30, height = 30, wrap = WORD)
            ship.status.insert(0.0, ship.__str__())
            self.widgets.append(ship.status)
            
        self.ship1.status.grid(row = 1, column = 0, rowspan = 2)
        self.ship2.status.grid(row = 1, column = 2, rowspan = 2)

        # Battle text
        self.battle = Text(width = 50, height = 15, wrap = WORD)
        self.battle.grid(row = 1, column = 1, sticky = S)
        self.widgets.append(self.battle)

        # Next Round Button
        self.round = Button(text = "Next Round!", command = self.pass_round)
        self.round.grid(row = 2, column = 1)
        self.widgets.append(self.round)

    def pass_round(self):
        """A round in pass and play."""
        damage = self.ship2.defend(self.ship1.attack())
        if damage > 0:
            self.battle.insert(END, self.ship1.name + " hits " + \
                               self.ship2.name + " for " + \
                               str(round(damage, 1)) + " damage!\n")
        else:
            self.battle.insert(END, self.ship1.name + " missed!\n")

        damage = self.ship1.defend(self.ship2.attack())
        if damage > 0:
            self.battle.insert(END, self.ship2.name + " hits " + \
                               self.ship1.name + " for " + \
                               str(round(damage, 1)) + " damage!\n\n")
        else:
            self.battle.insert(END, self.ship2.name + " missed!\n\n")

        self.ship1.status.delete(0.0, END)
        self.ship1.status.insert(0.0, self.ship1.__str__())
        self.ship2.status.delete(0.0, END)
        self.ship2.status.insert(0.0, self.ship2.__str__())

        if self.ship1.defense <= 0 and self.ship2.defense <= 0:
            self.battle.insert(END, "Both ships were destroyed. It's a draw!")
            self.round.destroy()
            self.round = Button(text = "Back to menu",
                                command = self.pass_play_menu)
            self.round.grid(row = 2, column = 1)
            self.widgets.append(self.round)
            #winsound.PlaySound("resources/draw.wav", winsound.SND_FILENAME)
            
        elif self.ship1.defense > 0 and self.ship2.defense <= 0:
            self.battle.insert(END, self.ship1.name + " wins!")
            self.round.destroy()
            self.round = Button(text = "Back to menu",
                                command = self.pass_play_menu)
            self.round.grid(row = 2, column = 1)
            self.widgets.append(self.round)
            winsound.PlaySound("resources/player1.wav", winsound.SND_FILENAME)
                
        elif self.ship2.defense > 0 and self.ship1.defense <= 0:
            self.battle.insert(END, self.ship2.name + " wins!")
            self.round.destroy()
            self.round = Button(text = "Back to menu",
                                command = self.pass_play_menu)
            self.round.grid(row = 2, column = 1)
            self.widgets.append(self.round)
            winsound.PlaySound("resources/player2.wav", winsound.SND_FILENAME)
        
root = Tk()
root.title("StarHash")
root.geometry("405x300")
app = Application(root)
root.mainloop()
