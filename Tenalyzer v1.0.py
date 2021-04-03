from tkinter import *
from tkinter import ttk
import time
from winsound import *
from pathlib import Path

#*||Program||*

#Font styles:
main_font = 'SimSun 30 bold'
sub_font = 'SimSun 20 bold'
sub_font2 = 'SimSun 11 bold'
sub_font3 = 'Arial 11 italic bold'
sub_font4 = 'Arial 9'


#background & foreground colors
active_BG = 'DarkGreen'
active_FG = 'white'
bg_1 = 'MediumSeaGreen'
bg_2 = 'palegreen'
bg_3 = 'SeaGreen'
bg_4 = 'LightGreen'
fg_1 = 'DarkGreen'
fg_2 = 'LightCyan'


#Frame & Mouse config
hand_cursor = 'hand2'
raised_relief = 'raised'
groove_relief = 'groove'
ridge_relief = 'ridge'


#Credits and Instructions
creators = ('Kanishka Yamani & Aranya Sharma\n\n')
instructions_text = ('Instructions:')
reference1 = 'Python: removing a TKinter frame, By: Aneurzym, Accessed: 1/08/2018\n<goo.gl/iqCzon>\n\n'
reference2 = 'The Tkinter PhotoImage Class, By: Effbot, Accessed: 5/08/2018\n<goo.gl/ZYDhLQ>\n\n'
reference3 = 'Structuring a Tkinter application, By: Bryan Oakley, Accessed 10/08/2018\n<goo.gl/Jxr47r>\n\n'
reference4 = 'Python absolute file path, By: Rudolf Olah, Accessed 10/08/2018\n<goo.gl/NP4Y6r>'
reference_text = ('Creators: ' + creators + 'References:\n\n' + reference1 + reference2 + reference3 + reference4)


#player1 (all variables apply to player 1)
status1 = False #True if first player wins the match or False if first player hasn't yet won / lost
points1 = 0 #Holds first player's points per game (15,30,40 etc..)
fouls1 = 0 #Holds first player's fouls throughout the entire game
total_fouls1 = 0 #Holds first player's total fouls throughout the entire match
lets1 = 0 #Holds first player's total lets throughout the entire match
serve_type1 = '' #Determines first player's serve outcome
score1 = 0 #Holds first player's score per game
games_won1 = 0 #Holds first player's games won throughout the entire set
total_games1 = 0 #Holds first player's total games won throughout the entire match
sets_won1 = 0 #Holds first player's sets won throughout the match
point_range1 = 0 #A range from 1-4 which allocates first player's points; 15/30/40
deuce1 = 0 #First player's points allocation during deuce
aces1 = 0 #Holds first player's total aces throughout the entire match


#player2 (all variables apply to player 2)
status2 = False #True if second player wins the match or False if second player hasn't yet won / lost
points2 = 0 #Holds second player's points per game (15,30,40,etc..)
fouls2 = 0 #Holds second player's fouls throughout the entire game
total_fouls2 = 0 #Holds second player's total fouls throughout the entire match
lets2 = 0 #Holds second player's lets throughout the entire match
serve_type2 = '' #Determines second player's serve outcome
score2 = 0 #Holds second player's score per game
games_won2 = 0 #Holds second player's games won throughout the entire match
total_games2 = 0 #Holds second player's total games won throughout the entire match
sets_won2 = 0 #Holds second player's sets won throughout the match
point_range2 = 0 #A range from 1-4 which allocates second player's points; 15/30/40
deuce2 = 0 #Second player's points allocation during deuce
aces2 = 0 #Holds second player's total aces throughout the entire match


#Nonspecific Variables
gender = '' #Determines number of sets according to gender/sex of players
arg_checker = '' #Checks previous frame to determine which labels/frames to remove
gender_checker = 0 #Checks if gender has been entered correctly
selection = '' #Serve type selection
first_server = 0 #determines who is currently serving
deuce_checker = 0 #checks if game isn't currently in a 'deuce' state
deuce = False #Boolean used to update the title text to say 'Deuce!' when in deuce state


#Path Locations
mypath = Path().absolute() #Returns the path of current python file
batpath = mypath / 'Misc\\server_tennis.png' #Appends extra path to locate file
ballpath = mypath / 'Misc\\serving1.png'
iconpath = mypath / 'Misc\\tennis_bats.ico'

#*||Functions||*

class tenalyzer_V1:

    def __init__(self, root):
        #Root Manipulation
        self.root = root
        self.root.grid_propagate(False)

        #Frames
        self.introframe_1 = Frame(root)
        self.introframe_1.config(bg=bg_3, width=540, height=100)
        self.introframe_1.grid(row=0)

        self.introframe_2 = Frame(root)
        self.introframe_2.config(bg=bg_1, width=540, height=300)
        self.introframe_2.grid(row=1)

        self.introframe_3 = Frame(root)
        self.introframe_3.config(bg=bg_3, width=540, height=50)
        self.introframe_3.grid(row=2)

        tennis_img = PhotoImage(file=batpath)
        tennis_img.zoom(5)
        self.img_label_1 = Label(root)
        self.img_label_1.config(bg=bg_2, width=535, height=295, image=tennis_img)
        self.img_label_1.image = tennis_img
        self.img_label_1.grid(row=1, sticky=NW)

        #Buttons
        self.button_1 = Button(root)
        self.button_1.grid(row=0)
        self.button_1.config(text='TENALYZER', bg=bg_2, activebackground=active_BG , fg=fg_1, activeforeground=active_FG, font=sub_font, width=14, bd=5, relief=raised_relief, cursor=hand_cursor, command=self.bridge)

        #Progressbar
        self.s = ttk.Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
        self.s.grid(row=2)

 
    def bridge(self):
        #Controls the loading bar
        for i in range (0,100):
            self.s['value']=self.s['value']+1
            self.root.update_idletasks()
            time.sleep(0.01)
        time.sleep(1)
        self.title_page()


    def title_page(self):
        #Variable Manipulation
        global status1, status2, points1, points2, fouls1, fouls2, lets1, lets2, serve_type1, serve_type2, score1, score2, games_won1, games_won2, sets_won1, sets_won2, gender, arg_checker, gender_checker, selection, first_server, point_range1, point_range2, total_fouls1, total_fouls2, deuce1, deuce2, deuce_checker, deuce, aces1, aces2, status1, status2, total_games1, total_games2
        status1 = False
        points1 = 0
        fouls1 = 0
        lets1 = 0
        serve_type1 = ''
        score1 = 0
        games_won1 = 0
        sets_won1 = 0
        status2 = False
        points2 = 0
        fouls2 = 0
        lets2 = 0
        serve_type2 = ''
        score2 = 0
        games_won2 = 0
        sets_won2 = 0
        gender = ''
        arg_checker = ''
        gender_checker = 0
        selection = ''
        first_server = 0
        point_range1 = 0
        point_range2 = 0
        total_fouls1 = 0
        total_fouls2 = 0
        deuce_checker = 0
        deuce = False
        aces1 = 0
        aces2 = 0
        status1 = ''
        status2 = ''
        total_games1 = 0
        total_games2 = 0

        #Grid Manipulation
        self.button_1.grid_forget()
        self.s.grid_forget()
        self.introframe_1.grid_forget()
        self.introframe_2.grid_forget()
        self.introframe_3.grid_forget()
        self.img_label_1.grid_forget()

        #Root Manipulation
        self.root.grid_propagate(False)
        
        #Frames
        self.frame_1 = Frame(root)
        self.frame_1.config(bg=bg_3, width=540, height=100)
        self.frame_1.grid(row=0)

        self.frame_2 = Frame(root)
        self.frame_2.config(bg=bg_1, width=540, height=100)
        self.frame_2.grid(row=1)

        self.frame_3 = Frame(root)
        self.frame_3.config(bg=bg_1, width=540, height=100)
        self.frame_3.grid(row=2)

        self.frame_4 = Frame(root)
        self.frame_4.config(bg=bg_1, width=540, height=100)
        self.frame_4.grid(row=3)

        self.frame_5 = Frame(root)
        self.frame_5.config(bg=bg_3, width=540, height=50)
        self.frame_5.grid(row=4)

        #Labels + Buttons
        self.label_1 = Label(root)
        self.label_1.grid(row=0)
        self.label_1.config(text='Tenalyzer v1.0', bg=bg_1, fg=fg_2, font=main_font, width=17, bd=10, relief=groove_relief)
        
        self.button_2 = Button(root)
        self.button_2.grid(row=1)
        self.button_2.config(text='START', bg=bg_2, activebackground=active_BG , fg=fg_1, activeforeground=active_FG, font=sub_font, width=14, bd=5, relief=raised_relief, cursor=hand_cursor, command=self.gender_page)
        
        self.button_3 = Button(root)
        self.button_3.grid(row=2)
        self.button_3.config(text='INSTRUCTIONS', bg=bg_2, activebackground=active_BG , fg=fg_1, activeforeground=active_FG, font=sub_font, width=14, bd=5, relief=raised_relief, cursor=hand_cursor, command=self.instructions_page)
        
        self.button_4 = Button(root)
        self.button_4.grid(row=3)
        self.button_4.config(text='CREDITS', bg=bg_2, activebackground=active_BG , fg=fg_1, activeforeground=active_FG, font=sub_font, width=14, bd=5, relief=raised_relief, cursor=hand_cursor, command=self.credits_page)

        self.button_5 = Button(root)
        self.button_5.grid(row=4)
        self.button_5.config(text='Exit', bg=bg_2, activebackground=active_BG , fg=fg_1, activeforeground=active_FG, font=sub_font2, width=16, bd=5, relief=raised_relief, cursor=hand_cursor, command=self.exit_command)

        #Logic
        if arg_checker == ('references'):
            self.references_label.grid_forget()
        elif arg_checker == ('main_prog'):
            self.main_frame1.grid_forget()
            self.main_frame2.grid_forget()
            self.main_frame3.grid_forget()
            self.main_frame4.grid_forget()
            self.main_frame5.grid_forget()
            self.main_frame6.grid_forget()


    def main_program(self):
        #Sound Manipulation
        self.sound1()
        
        #Variable Manipulation
        global points1, points2, games_won1, games_won2, sets_won1, sets_won2
        arg_checker = 'main_prog'

        #Grid Manipulation
        self.button_5.grid(row=4)
        
        #Frames
        self.main_frame1 = Frame(root)
        self.main_frame1.config(bg=bg_4, height=100, width=275)
        self.main_frame1.grid(row=1, columnspan=1, sticky=W)

        self.main_frame2 = Frame(root)
        self.main_frame2.config(bg=bg_4, height=100, width=275)
        self.main_frame2.grid(row=2, columnspan=1, sticky=W)

        self.main_frame3 = Frame(root)
        self.main_frame3.config(bg=bg_4, height=100, width=275)
        self.main_frame3.grid(row=3, columnspan=1, sticky=W)
        
        self.main_frame4 = Frame(root)
        self.main_frame4.config(bg=bg_2, height=100, width=275)
        self.main_frame4.grid(row=1, columnspan=1, sticky=E)

        self.main_frame5 = Frame(root)
        self.main_frame5.config(bg=bg_2, height=100, width=275)
        self.main_frame5.grid(row=2, columnspan=1, sticky=E)

        self.main_frame6 = Frame(root)
        self.main_frame6.config(bg=bg_2, height=100, width=275)
        self.main_frame6.grid(row=3, columnspan=1, sticky=E)

        #Labels + Buttons
        self.label_5 = Label(root) #grid_forget()
        self.label_5.grid(row=1, column=0, sticky=W, padx=50)
        self.label_5.config(text=name1_collect, bg=bg_1, fg=fg_2, font=sub_font4, width=23, height=1, bd=4, relief=groove_relief)

        self.label_6 = Label(root) #grid_forget()
        self.label_6.grid(row=2, column=0, sticky=W, padx=23)
        self.label_6.config(text='Points:' + str(points1), bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
        
        self.label_7 = Label(root) #grid_forget()
        self.label_7.grid(row=2, column=0, sticky=W, padx=167)
        self.label_7.config(text='Games:' + str(games_won1), bg=bg_1, fg=fg_2, font=sub_font4, width=9, height=1, bd=4, relief=groove_relief, anchor=W)

        self.label_8 = Label(root) #grid_forget()
        self.label_8.grid(row=2, column=0, sticky=W, padx=100)
        self.label_8.config(text='Sets:'+ str(sets_won1), bg=bg_1, fg=fg_2, font=sub_font4, width=7, height=1, bd=4, relief=groove_relief, anchor=W)

        self.label_9 = Label(root) #grid_forget()
        self.label_9.grid(row=1, column=0, sticky=E, padx=55)
        self.label_9.config(text=name2_collect, bg=bg_1, fg=fg_2, font=sub_font4, width=23, height=1, bd=4, relief=groove_relief)

        self.label_10 = Label(root) #grid_forget()
        self.label_10.grid(row=2, column=0, sticky=E, padx=180)
        self.label_10.config(text='Points:'+ str(points2), bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)

        self.label_11 = Label(root) #grid_forget()
        self.label_11.grid(row=2, column=0, sticky=E, padx=25)
        self.label_11.config(text='Games:'+ str(games_won2), bg=bg_1, fg=fg_2, font=sub_font4, width=9, height=1, bd=4, relief=groove_relief, anchor=W)

        self.label_12 = Label(root) #grid_forget()
        self.label_12.grid(row=2, column=0, sticky=E, padx=110)
        self.label_12.config(text='Sets:'+ str(sets_won2), bg=bg_1, fg=fg_2, font=sub_font4, width=7, height=1, bd=4, relief=groove_relief, anchor=W)

        self.button_6 = Button(root) #grid_forget()
        self.button_6.grid(row=3, sticky=N)
        self.button_6.config(text='Accept', bg=bg_2, activebackground=active_BG , fg=fg_1, activeforeground=active_FG, font='SimSun 10', width=14, bd=2, relief=raised_relief, cursor=hand_cursor, command=self.action_logic)

        #Dropdown List
        self.serve_menu = Menubutton(root)
        self.serve_menu.config(text='Select Serve', bg='green', fg=fg_2, font=sub_font4, width=14, height=1, bd=4, relief=groove_relief)
        self.serve_menu.grid(row=3)
        self.serve_menu.menu = Menu (self.serve_menu, tearoff = 0)
        self.serve_menu['menu'] = self.serve_menu.menu
        if first_server==1:
            self.serve_menu.menu.add_command(label=name1_collect+'\'s '+'Point', command=lambda: self.list_select('SPlayer'))
            self.serve_menu.menu.add_command(label=name2_collect+'\'s '+'Point', command=lambda: self.list_select('NSPlayer'))
            self.serve_menu.menu.add_command(label=name1_collect+'\'s '+'Foul', command=lambda: self.list_select('Foul'))
            self.serve_menu.menu.add_command(label=name1_collect+'\'s '+'Let', command=lambda: self.list_select('Let'))
            self.serve_menu.menu.add_command(label=name1_collect+'\'s '+'Ace', command=lambda: self.list_select('Ace'))
        else:
            self.serve_menu.menu.add_command(label=name2_collect+'\'s '+'Point', command=lambda: self.list_select('SPlayer'))
            self.serve_menu.menu.add_command(label=name1_collect+'\'s '+'Point', command=lambda: self.list_select('NSPlayer'))
            self.serve_menu.menu.add_command(label=name2_collect+'\'s '+'Foul', command=lambda: self.list_select('Foul'))
            self.serve_menu.menu.add_command(label=name2_collect+'\'s '+'Let', command=lambda: self.list_select('Let'))
            self.serve_menu.menu.add_command(label=name2_collect+'\'s '+'Ace', command=lambda: self.list_select('Ace'))

        #Config Manipulation + Images
        self.label_1.config(text='Mode: Normal')
        self.button_5.config(text='Abort Game', command=self.title_page)
        
        #Logic
        self.serve_select()


    def serve_select(self):
        #Determines where to place the ball image depending on who is first to serve
        if first_server==1:
            self.img_label_1.grid_forget()
            player1_Serve = PhotoImage(file=ballpath)
            player1_Serve.zoom(5)
            
            self.img_label_1 = Label(root)
            self.img_label_1.config(bg=bg_4, width=50, height=50, image=player1_Serve)
            self.img_label_1.image = player1_Serve
            self.img_label_1.grid(row=3, sticky=NW, padx=70)
        else:
            self.img_label_1.grid_forget()
            player2_Serve = PhotoImage(file=ballpath)
            player2_Serve.zoom(5)
            
            self.img_label_1 = Label(root)
            self.img_label_1.config(bg=bg_2, width=50, height=50, image=player2_Serve)
            self.img_label_1.image = player2_Serve
            self.img_label_1.grid(row=3, sticky=NE, padx=70)

        
    def list_select(self, option):
        #Sound Manipulation
        self.sound2()

        #Determines selection and config manipulation
        global selection
        if option == 'SPlayer':
            selection = 'SPlayer'
            self.serve_menu.config(text='SPlayer')
        elif option == 'NSPlayer':
            selection = 'NSPlayer'
            self.serve_menu.config(text='NSPlayer')
        elif option == 'Foul':
            selection = 'Foul'
            self.serve_menu.config(text='Foul')
        elif option == 'Let':
            selection = 'Let'
            self.serve_menu.config(text='Let')
        elif option == 'Ace':
            selection = 'Ace'
            self.serve_menu.config(text='Ace')


    def action_logic(self):
        #Sound Manipulation
        self.sound2()

        #Variable Manipulation
        global point_range1, point_range2, points1, points2, games_won1, games_won2, first_server, total_fouls1, total_fouls2, fouls1, fouls2, sets_won1, sets_won2, deuce1, deuce2, deuce_checker, selection, deuce, gender, lets1, lets2, aces1, aces2, status1, status2, total_games2, total_games1

        #Logic
        if first_server==1:
            if points1 == 40 and points2 == 40:
                if selection == 'SPlayer' and deuce1 != 2:
                    fouls1 = 0
                    deuce1 = deuce1+1
                    deuce2 = deuce2-1
                    if deuce1 == 1 and deuce2 < deuce1:
                        self.label_6.config(text='Points:Ad', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                        self.label_10.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                    elif deuce1 == 0 and deuce2 == 0:
                        self.label_6.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                        self.label_10.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                    
                elif selection == 'NSPlayer' and deuce1 != 2:
                    fouls1 = 0
                    deuce1 = deuce1-1
                    deuce2 = deuce2+1
                    if deuce2 == 1 and deuce1 < deuce2:
                        self.label_10.config(text='Points:Ad', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                        self.label_6.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                    elif deuce2 == 0 and deuce1 == 0:
                        self.label_10.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                        self.label_6.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                    
                elif selection == 'Foul' and deuce1 != 2:
                    fouls1 = fouls1+1
                    if fouls1 == 2:
                        total_fouls1 = total_fouls1+1
                        deuce1 = deuce1-1
                        deuce2 = deuce2+1
                        fouls1 = 0
                        if deuce1 == 0 and deuce2 == 0:
                            self.label_6.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                            self.label_10.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                        elif deuce2 == 1 and deuce1 < deuce2:
                            self.label_6.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                            self.label_10.config(text='Points:Ad', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)

                elif selection == 'Let':
                    fouls1 = 0
                    lets1 = lets1+1
                    print('Haha tough luck buddy')

                elif selection == 'Ace':
                    aces1 = aces1 + 1
                    fouls1 = 0
                    deuce1 = deuce1+1
                    deuce2 = deuce2-1
                    if deuce1 == 1 and deuce2 < deuce1:
                        self.label_6.config(text='Points:Ad', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                        self.label_10.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                    elif deuce1 == 0 and deuce2 == 0:
                        self.label_6.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                        self.label_10.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)

                if deuce2==2 and deuce1==-2:
                    games_won2 = games_won2+1
                    total_games2 = total_games2+1
                    points1 = 0
                    points2 = 0
                    point_range1 = 0
                    point_range2 = 0
                    first_server = 2
                    deuce_checker = 0
                    deuce1 = 0
                    deuce2 = 0
                    self.serve_select()
                    deuce = True
                    
                elif deuce1==2 and deuce2==-2:
                    games_won1 = games_won1+1
                    total_games1 = total_games1+1
                    points1 = 0
                    points2 = 0
                    point_range1 = 0
                    point_range2 = 0
                    first_server = 2
                    deuce_checker = 0
                    deuce1 = 0
                    deuce2 = 0
                    self.serve_select()
                    deuce = True
                    
        elif first_server==2:
            if points1 == 40 and points2 == 40:
                if selection == 'SPlayer' and deuce2 != 2:
                    fouls2 = 0
                    deuce2 = deuce2+1
                    deuce1 = deuce1-1
                    if deuce2 == 1 and deuce1 < deuce2:
                        self.label_10.config(text='Points:Ad', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                        self.label_6.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                    elif deuce2 == 0 and deuce1 == 0:
                        self.label_10.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                        self.label_6.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                        
                elif selection == 'NSPlayer' and deuce2 != 2:
                    fouls2 = 0
                    deuce2 = deuce2-1
                    deuce1 = deuce1+1
                    if deuce1 == 1 and deuce2 < deuce1:
                        self.label_6.config(text='Points:Ad', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                        self.label_10.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                    elif deuce1 == 0 and deuce2 == 0:
                        self.label_6.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                        self.label_10.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                
                elif selection == 'Foul' and deuce2 != 2:
                    total_fouls2 = total_fouls2+1
                    fouls2 = fouls2+1
                    if fouls2 == 2:
                        deuce1 = deuce1+1
                        deuce2 = deuce2-1
                        fouls2 = 0
                        if deuce1 == 0 and deuce2 == 0:
                            self.label_6.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                            self.label_10.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                        elif deuce1 == 1 and deuce2 < deuce1:
                            self.label_6.config(text='Points:Ad', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                            self.label_10.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                            
                elif selection == 'Let':
                    fouls2 = 0
                    lets2 = lets2+1
                    print('Haha tough luck buddy')

                elif selection == 'Ace':
                    aces2 = aces2 + 1
                    fouls2 = 0
                    deuce2 = deuce2+1
                    deuce1 = deuce1-1
                    if deuce2 == 1 and deuce1 < deuce2:
                        self.label_10.config(text='Points:Ad', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                        self.label_6.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                    elif deuce2 == 0 and deuce1 == 0:
                        self.label_10.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
                        self.label_6.config(text='Points:', bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)


                if deuce2==2 and deuce1==-2:
                    games_won2 = games_won2+1
                    total_games2 = total_games2+1
                    points1 = 0
                    points2 = 0
                    point_range1 = 0
                    point_range2 = 0
                    first_server = 1
                    deuce_checker = 0
                    deuce1 = 0
                    deuce2 = 0
                    self.serve_select()
                    deuce = True
                    
                elif deuce1==2 and deuce2==-2:
                    games_won1 = games_won1+1
                    total_games1 = total_games1+1
                    points1 = 0
                    points2 = 0
                    point_range1 = 0
                    point_range2 = 0
                    first_server = 1
                    deuce_checker = 0
                    deuce1 = 0
                    deuce2 = 0
                    self.serve_select()
                    deuce = True

        if first_server==1 and deuce == False:
            if points1 != 40 or points2 != 40:
                if selection == 'SPlayer':
                    fouls1 = 0
                    point_range1 = point_range1+1
                    if point_range1 == 1:
                        points1 = 15
                    elif point_range1 == 2:
                        points1 = 30
                    elif point_range1 == 3:
                        points1 = 40
                    elif point_range1 == 4:
                        games_won1 = games_won1+1
                        total_games1 = total_games1+1
                        points1 = 0
                        points2 = 0
                        point_range1 = 0
                        point_range2 = 0
                        first_server = 2
                        self.serve_select()

                elif selection == 'NSPlayer':
                    fouls1 = 0
                    point_range2 = point_range2+1
                    if point_range2 == 1:
                        points2 = 15
                    elif point_range2 == 2:
                        points2 = 30
                    elif point_range2 == 3:
                        points2 = 40
                    elif point_range2 == 4:
                        games_won2 = games_won2+1
                        total_games2 = total_games2+1
                        points2 = 0
                        points1 = 0
                        point_range2 = 0
                        point_range1 = 0
                        first_server = 2
                        self.serve_select()

                elif selection == 'Foul':
                    total_fouls1 = total_fouls1+1
                    fouls1 = fouls1+1
                    print(fouls1)
                    if fouls1 == 2:
                        fouls1 = 0
                        if points2 == 0:
                            points_range2 = 1
                            points2 = 15
                        elif points2 == 15:
                            points_range2 = 2
                            points2 = 30
                        elif points2 == 30:
                            points_range2 = 3
                            points2 = 40
                        elif points2 == 40:
                            games_won2 = games_won2+1
                            total_games2 = total_games2+1
                            points1 = 0
                            points2 = 0
                            point_range1 = 0
                            point_range2 = 0
                            first_server = 2
                            self.serve_select()

                elif selection == 'Let':
                    fouls1 = 0
                    lets1 = lets1+1
                    print('Haha tough luck buddy')

                elif selection == 'Ace':
                    aces1 = aces1 + 1
                    fouls1 = 0
                    point_range1 = point_range1+1
                    if point_range1 == 1:
                        points1 = 15
                    elif point_range1 == 2:
                        points1 = 30
                    elif point_range1 == 3:
                        points1 = 40
                    elif point_range1 == 4:
                        games_won1 = games_won1+1
                        total_games1 = total_games1+1
                        points1 = 0
                        points2 = 0
                        point_range1 = 0
                        point_range2 = 0
                        first_server = 2
                        self.serve_select()       
                selection == ''

        elif first_server==2 and deuce == False:
            if points1 != 40 or points2 != 40:
                if selection == 'SPlayer':
                    fouls2 = 0
                    point_range2 = point_range2+1
                    if point_range2 == 1:
                        points2 = 15
                    elif point_range2 == 2:
                        points2 = 30
                    elif point_range2 == 3:
                        points2 = 40
                    elif point_range2 == 4:
                        points2 = 0
                        points1 = 0
                        games_won2 = games_won2+1
                        total_games2 = total_games2+1
                        first_server = 1
                        point_range2 = 0
                        point_range1 = 0
                        self.serve_select()

                elif selection == 'NSPlayer':
                    fouls2 = 0
                    point_range1 = point_range1+1
                    if point_range1 == 1:
                        points1 = 15
                    elif point_range1 == 2:
                        points1 = 30
                    elif point_range1 == 3:
                        points1 = 40
                    elif point_range1 == 4:
                        games_won1 = games_won1+1
                        total_games1 = total_games1+1
                        points1 = 0
                        points2 = 0
                        point_range2 = 0
                        point_range1 = 0
                        first_server = 1
                        self.serve_select()
                        
                elif selection == 'Foul':
                    fouls2 = fouls2+1
                    if fouls2 == 2:
                        total_fouls2 = total_fouls2+1
                        fouls2 = 0
                        if points1 == 0:
                            points_range1 = 1
                            points1 = 15
                        elif points1 == 15:
                            points_range1 = 2
                            points1 = 30
                        elif points1 == 30:
                            points_range1 = 3
                            points1 = 40
                        elif points1 == 40:
                            games_won1 = games_won1+1
                            total_games1 = total_games1+1
                            points1 = 0
                            points2 = 0
                            point_range1 = 0
                            point_range2 = 0
                            first_server = 1
                            self.serve_select()

                elif selection == 'Let':
                    lets2 = lets2+1
                    fouls2 = 0
                    print('Haha tough luck buddy')

                elif selection == 'Ace':
                    aces2 = aces2 + 1
                    fouls2 = 0
                    point_range2 = point_range2+1
                    if point_range2 == 1:
                        points2 = 15
                    elif point_range2 == 2:
                        points2 = 30
                    elif point_range2 == 3:
                        points2 = 40
                    elif point_range2 == 4:
                        games_won2 = games_won2+1
                        total_games2 = total_games2+1
                        points1 = 0
                        points2 = 0
                        point_range1 = 0
                        point_range2 = 0
                        first_server = 1
                        self.serve_select()
                selection == ''

        #More Logic
        if points1 ==40 and points2 ==40 and deuce_checker == 0:
            deuce_checker = deuce_checker + 1
            self.label_6.config(text='Points:40')
            self.label_10.config(text='Points:40')
            print('Deuce!')

        if deuce == True:
            deuce = False
            self.label_1.config(text='Mode: Normal')

        if points1 == 40 and points2 == 40:
            self.label_1.config(text='Mode: Deuce!')

        if games_won1 == 7 and games_won2 !=7:
            self.label_1.config(text='Mode: Normal')
            games_won2 = 0
            games_won1 = 0
            sets_won1 = sets_won1 + 1
            
        elif games_won2 == 7 and games_won1 !=7:
            self.label_1.config(text='Mode: Normal')
            games_won2 = 0
            games_won1 = 0
            sets_won2 = sets_won2 + 1
            
        elif games_won1 == 6 and games_won2 == 6:
            self.label_1.config(text='Mode: Tie!')
            
        if points1 !=40 or points2 !=40:
            self.update()

        if gender == 'male':
            if sets_won1 == 3:
                status1 = 'WINNER'
                status2 = 'LOSER'
                self.winner()
            elif sets_won2 == 3:
                status2 = 'WINNER'
                status1 = 'LOSER'
                self.winner()
                
        elif gender == 'female':
            if sets_won1 == 2:
                status1 = 'WINNER'
                status2 = 'LOSER'
                self.winner()
            elif sets_won2 == 2:
                status2 = 'WINNER'
                status1 = 'LOSER'
                self.winner()   


    def winner(self):
        #Sound Manipulation
        self.sound1()

        #Grid Manipulation
        self.img_label_1.grid_forget()
        self.serve_menu.grid_forget()
        self.button_6.grid_forget()
        self.label_6.grid_forget()
        self.label_7.grid_forget()
        self.label_8.grid_forget()
        self.label_10.grid_forget()
        self.label_11.grid_forget()
        self.label_12.grid_forget()

        #Config Manipulation
        self.button_5.config(text='Go Back')
        self.label_1.config(text='Game Over')

        #Labels
        self.label_6 = Label(root)
        self.label_6.grid(row=2, column=0, sticky=W, padx=23)
        self.label_6.config(text='Total Aces:' + str(aces1) + '\nGames Won:' + str(total_games1), bg=bg_1, fg=fg_2, font=sub_font4, width=13, height=2, bd=4, relief=groove_relief, anchor=W)
        
        self.label_7 = Label(root)
        self.label_7.grid(row=2, column=0, sticky=W, padx=144)
        self.label_7.config(text='Total Fouls:' + str(total_fouls1) + '\nTotal Lets:' + str(lets1), bg=bg_1, fg=fg_2, font=sub_font4, width=13, height=2, bd=4, relief=groove_relief, anchor=W)

        self.label_10 = Label(root)
        self.label_10.grid(row=2, column=0, sticky=E, padx=147)
        self.label_10.config(text='Total Aces:'+ str(aces2) + '\nGames Won:' + str(total_games2), bg=bg_1, fg=fg_2, font=sub_font4, width=13, height=2, bd=4, relief=groove_relief, anchor=W)

        self.label_11 = Label(root)
        self.label_11.grid(row=2, column=0, sticky=E, padx=27)
        self.label_11.config(text='Total Fouls:' + str(total_fouls2) + '\nTotal Lets:'+ str(lets2), bg=bg_1, fg=fg_2, font=sub_font4, width=13, height=2, bd=4, relief=groove_relief, anchor=W)

        self.label_13 = Label(root)
        self.label_13.grid(row=3, column=0, sticky=W, padx=48)
        self.label_13.config(text=status1, bg=bg_1, fg=fg_2, font=sub_font4, width=23, height=1, bd=4, relief=groove_relief)

        self.label_14 = Label(root)
        self.label_14.grid(row=3, column=0, sticky=E, padx=55)
        self.label_14.config(text=status2, bg=bg_1, fg=fg_2, font=sub_font4, width=23, height=1, bd=4, relief=groove_relief)
        

    def update(self):
        #Variable Manipulation
        global total_games1, total_games2

        #Grid Manipulation
        self.label_6.grid_forget()
        self.label_7.grid_forget()
        self.label_8.grid_forget()
        self.label_10.grid_forget()
        self.label_11.grid_forget()
        self.label_12.grid_forget()

        #Labels
        self.label_6 = Label(root)
        self.label_6.grid(row=2, column=0, sticky=W, padx=23)
        self.label_6.config(text='Points:' + str(points1), bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)
        
        self.label_7 = Label(root)
        self.label_7.grid(row=2, column=0, sticky=W, padx=167)
        self.label_7.config(text='Games:' + str(games_won1), bg=bg_1, fg=fg_2, font=sub_font4, width=9, height=1, bd=4, relief=groove_relief, anchor=W)

        self.label_8 = Label(root)
        self.label_8.grid(row=2, column=0, sticky=W, padx=100)
        self.label_8.config(text='Sets:'+ str(sets_won1), bg=bg_1, fg=fg_2, font=sub_font4, width=7, height=1, bd=4, relief=groove_relief, anchor=W)

        self.label_10 = Label(root)
        self.label_10.grid(row=2, column=0, sticky=E, padx=180)
        self.label_10.config(text='Points:'+ str(points2), bg=bg_1, fg=fg_2, font=sub_font4, width=8, height=1, bd=4, relief=groove_relief, anchor=W)

        self.label_11 = Label(root)
        self.label_11.grid(row=2, column=0, sticky=E, padx=25)
        self.label_11.config(text='Games:'+ str(games_won2), bg=bg_1, fg=fg_2, font=sub_font4, width=9, height=1, bd=4, relief=groove_relief, anchor=W)

        self.label_12 = Label(root)
        self.label_12.grid(row=2, column=0, sticky=E, padx=110)
        self.label_12.config(text='Sets:'+ str(sets_won2), bg=bg_1, fg=fg_2, font=sub_font4, width=7, height=1, bd=4, relief=groove_relief, anchor=W)


    def exit_command(self):
        #Root Manipulation
        root.destroy()


    def male_select(self):
        #Sound Manipulation
        self.sound1()

        #Config Manipulation
        self.button_3.config(bg=active_BG, fg=active_FG)
        self.button_2.config(bg=bg_2, fg=fg_1)

        #Variable Manipulation
        global gender
        gender = 'male'


    def female_select(self):
        #Sound Manipulation
        self.sound1()

        #Config Manipulation
        self.button_2.config(bg=active_BG, fg=active_FG)
        self.button_3.config(bg=bg_2, fg=fg_1)

        #Variable Manipulation
        global gender
        gender = 'female'


    def player_names(self):
        #Sound Manipulation
        self.sound1()

        #Logic
        global gender
        if gender !='female' and gender !='male':
            self.gender_page()
        else:
            #Grid Manipulation
            self.button_2.grid_forget()
            self.button_3.grid_forget()

            #Variable Manipulation
            global name1, name2
            name1 = StringVar()
            name2 = StringVar()

            #Labels and Entries
            self.sub_label = Label(root)
            self.sub_label.grid(row=1)
            self.sub_label.config(text='PLAYER 1:', bg=bg_1, fg=fg_2, font=sub_font2, width='43', height='4', bd=10, relief=groove_relief, anchor=W, padx=15)

            self.sub_label2 = Label(root)
            self.sub_label2.grid(row=2)
            self.sub_label2.config(text='PLAYER 2:', bg=bg_1, fg=fg_2, font=sub_font2, width='43', height='4', bd=10, relief=groove_relief, anchor=W, padx=15)

            self.player1_entry = Entry(root)
            self.player1_entry.config(textvariable=name1, width=35, relief=ridge_relief, bd=3, bg=fg_2)
            self.player1_entry.grid(row=1)

            self.player2_entry = Entry(root)
            self.player2_entry.config(textvariable=name2, width=35, relief=ridge_relief, bd=3, bg=fg_2)
            self.player2_entry.grid(row=2)

            #Config Manipulation
            self.label_1.config(text='Player Names:')
            self.button_4.config(text='CONTINUE', command=self.collect_names)


    def collect_names(self):
        #Sound Manipulation
        self.sound1()

        #Variable Manipulation
        global name1_collect, name2_collect, gender_checker
        name1_collect = name1.get()
        name2_collect = name2.get()

        #Logic
        if len(name1_collect) == 0 or len(name2_collect) == 0:
            self.button_4.config(text='MISSING')
        else:
            gender_checker = 0
            self.serve_page()

            
    def serve_page(self):
        #Sound Manipulation
        self.sound1()
        
        #Grid Manipulation
        self.button_5.grid(row=4)
        self.player1_entry.grid_forget()
        self.player2_entry.grid_forget()
        self.sub_label.grid_forget()
        self.sub_label2.grid_forget()
        self.button_2.grid(row=1)
        self.button_3.grid(row=2)
        self.button_5.grid_forget()

        #Config Manipulation
        self.button_4.config(text='CONTINUE')
        self.label_1.config(text='First Serve:')
        
        self.button_2 = Button(root)
        self.button_2.grid(row=1)
        self.button_2.config(text=name1_collect, bg=bg_2, activebackground=active_BG , fg=fg_1, activeforeground=active_FG, font=sub_font, width=19, bd=5, relief=raised_relief, cursor=hand_cursor, command=self.plr1_select)
        
        self.button_3 = Button(root)
        self.button_3.grid(row=2)
        self.button_3.config(text=name2_collect, bg=bg_2, activebackground=active_BG , fg=fg_1, activeforeground=active_FG, font=sub_font, width=19, bd=5, relief=raised_relief, cursor=hand_cursor, command=self.plr2_select)

        #Logic
        global gender_checker
        gender_checker = gender_checker + 1
        if gender_checker == 1:
            self.button_4.config(text='CONTINUE', command=self.server_error)
        else:
            self.button_4.config(text='MISSING')


    def server_error(self):
        #Sound Manipulation
        self.sound1()

        #Logic
        if first_server !=1 and first_server !=2:
            self.serve_page()
        else:
            self.main_program()


    def plr1_select(self):
        #Sound Manipulation
        self.sound1()

        #Config Manipulation
        self.button_2.config(bg=active_BG, fg=active_FG)
        self.button_3.config(bg=bg_2, fg=fg_1)

        #Variable Manipulation
        global first_server
        first_server=1


    def plr2_select(self):
        #Sound Manipulation
        self.sound1()

        #Config Manipulation
        self.button_3.config(bg=active_BG, fg=active_FG)
        self.button_2.config(bg=bg_2, fg=fg_1)

        #Variable Manipulation
        global first_server
        first_server=2


    def gender_page(self):
        #Sound Manipulation
        self.sound1()

        #Grid Manipulation
        self.button_5.grid_forget()

        #Config Manipulation
        self.button_2.config(text='FEMALE', command=self.female_select)
        self.button_3.config(text='MALE', command=self.male_select)
        self.label_1.config(text='Sex:')
        self.button_5.config(text='Go Back', command=self.title_page)

        #Logic
        global gender_checker
        gender_checker = gender_checker + 1
        if gender_checker == 1:
            self.button_4.config(text='CONTINUE', command=self.player_names)
        else:
            self.button_4.config(text='MISSING')


    def instructions_page(self):
        #Sound Manipulation
        self.sound1()

        #Grid Manipulation
        self.button_2.grid_forget()
        self.button_3.grid_forget()
        self.button_4.grid_forget()

        #Labels
        self.references_label = Label(root)
        self.references_label.grid(row=1, rowspan=3, sticky=NW)
        self.references_label.config(text=instructions_text,bg=bg_1, fg=fg_2 , font=sub_font3, pady=18, padx=18)

        #Config Manipulation
        self.label_1.config(text='Instructions:')
        self.button_5.config(text='Go Back', command=self.title_page)

        #Variable Manipulation
        global arg_checker
        arg_checker = 'references'
        

    def credits_page(self):
        #Sound Manipulation
        self.sound1()

        #Grid Manipulation
        self.button_2.grid_forget()
        self.button_3.grid_forget()
        self.button_4.grid_forget()

        #Labels
        self.references_label = Label(root)
        self.references_label.grid(row=1, rowspan=3, sticky=N)
        self.references_label.config(text=reference_text,bg=bg_1, fg=fg_2 , font=sub_font3, pady=18)

        #Config Manipulation
        self.label_1.config(text='Credits:')
        self.button_5.config(text='Go Back', command=self.title_page)

        #Variable Manipulation
        global arg_checker
        arg_checker = 'references'


    def sound2(self):
        #Sound Definition
        PlaySound('Misc\\classic.wav', SND_FILENAME | SND_ASYNC)

        
    def sound1(self):
        #Sound Definition
        PlaySound('Misc\\techy.wav', SND_FILENAME | SND_ASYNC)

#*||Root Definition||*
        
root = Tk() #Creating the GUI Window
root.title('Tenalyzer v1.0') #Window Title Config
#root.wm_iconbitmap(iconpath) #Window Icon Config
root.resizable(False, False) #Window Resize Config
root.geometry('{}x{}'.format(540, 450)) #Window Size Config
key = tenalyzer_V1(root) #Defining the Class
root.mainloop() #Loop GUI to prevent program from exiting
