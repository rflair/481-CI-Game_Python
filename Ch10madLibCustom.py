# Mad Lib Customized

from tkinter import *

class Application(Frame):
    """ GUI application that creates mad lib story. """
    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets to get story information and to display it. """
        # create instruction label
        Label(self,
              text = "Enter information for you personal ad!"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # create label and text entry for user's name
        Label(self,
              text = "Name: "
              ).grid(row = 1, column = 0, sticky = W)
        self.name_ent = Entry(self)
        self.name_ent.grid(row = 1, column = 1, sticky = W)

        # create label for ad target (friend, husband, wife)
        Label(self,
              text = "What are you looking for?"
              ).grid(row = 2, column = 0, sticky = W)

        # create variable for target
        self.target = StringVar()
        self.target.set(None)

        # create radio buttons for ad target (friend, husband, wife)
        targets = ["friend", "husband", "wife"]
        column = 1
        for i in targets:
            Radiobutton(self,
                        text = i,
                        variable = self.target,
                        value = i
                        ).grid(row = 2, column = column, sticky = W)
            column += 1

        # create a label and text entry for an adjective
        Label(self,
              text = "Adjective: "
              ).grid(row = 3, column = 0, sticky = W)
        self.adj_ent = Entry(self)
        self.adj_ent.grid(row = 3, column = 1, sticky = W)

        # create a label and text entry for a verb ending in "ing"
        Label(self,
              text = "Verb ending in 'ing': "
              ).grid(row = 4, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 4, column = 1, sticky = W)

        # create a label and text entry for a food
        Label(self,
              text = "Food: "
              ).grid(row = 5, column = 0, sticky = W)
        self.food_ent = Entry(self)
        self.food_ent.grid(row = 5, column = 1, sticky = W)

        # create a label and text entry for a noun
        Label(self,
              text = "Plural noun: "
              ).grid(row = 6, column = 0, sticky = W)
        self.noun1_ent = Entry(self)
        self.noun1_ent.grid(row = 6, column = 1, sticky = W)

        # create a label and text entry for a celebrity
        Label(self,
              text = "Celebrity: "
              ).grid(row = 7, column = 0, sticky = W)
        self.celeb_ent = Entry(self)
        self.celeb_ent.grid(row = 7, column = 1, sticky = W)

        # create a label and text entry for a noun
        Label(self,
              text = "Noun: "
              ).grid(row = 8, column = 0, sticky = W)
        self.noun2_ent = Entry(self)
        self.noun2_ent.grid(row = 8, column = 1, sticky = W)

        # create a label for occupation
        Label(self,
              text = "Occupation: "
              ).grid(row = 9, column = 0, sticky = W)
        self.occup_ent = Entry(self)
        self.occup_ent.grid(row = 9, column = 1, sticky = W)

        # create a label and text entry for a number
        Label(self,
              text = "Number: "
              ).grid(row = 10, column = 0, sticky = W)
        self.num_ent = Entry(self)
        self.num_ent.grid(row = 10, column = 1, sticky = W)

        # create a submit button
        Button(self,
               text = "Click for ad",
               command = self.tell_story
               ).grid(row = 11, column = 0, sticky = W)
        self.story_txt = Text(self, width = 100, height = 10, wrap = WORD)
        self.story_txt.grid(row = 12, column = 0, columnspan = 4)

    def tell_story(self):
        """ Fill text box with new ad based on input. """
        # get values from GUI
        person = self.name_ent.get()
        adjective = self.adj_ent.get()
        verb = self.verb_ent.get()
        food = self.food_ent.get()
        noun1 = self.noun1_ent.get()
        celeb = self.celeb_ent.get()
        noun2 = self.noun2_ent.get()
        occup = self.occup_ent.get()
        num = self.num_ent.get()
        target = self.target.get()

        # create ad
        ad = "Hello, my name is "
        ad += person
        ad += " and I'm looking for a "
        ad += target + ". "
        ad += "I enjoy long, "
        ad += adjective
        ad += " walks on the beach and "
        ad += verb
        ad += " in the rain. "
        ad += "My favorite food is "
        ad += food
        ad += " mixed with "
        ad += noun1 + ". "
        ad += "Some people say I look just like "
        ad += celeb
        ad += " but with more "
        ad += noun2
        ad += "-like feet. My only negative is that I get really stressed sometimes"
        ad += " (I am a "
        ad += occup
        ad += "). I have been searching for a "
        ad += target
        ad += " for "
        ad += num
        ad += " years so I hope someone answers my ad!"

        # display ad
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, ad)

# main
root = Tk()
root.title("Mad Lib")
app = Application(root)
root.mainloop()


        
        
        

        
        

        

        

        
