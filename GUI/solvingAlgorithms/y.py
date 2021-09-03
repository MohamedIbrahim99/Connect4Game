import numpy as np

x= np.array([[0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 2, 0, 0, 0, 0],
   [0, 0, 0, 1, 0, 0, 0, 0],
   [0, 0, 1, 2, 0, 0, 0, 0],
   [0, 0, 2, 2, 2, 2, 0, 2],
   [1, 1, 1, 1, 1, 1, 1, 2]])

#decision = make_decision(x, 5, True)
#print(decision)

#new_state, new_utility = make_decision(state, 8, True)
#column = random.randint(0,7) # AI

# ---------------------------       will be deleted , sys, random # ---------------------------       will be deleted
#if __name__ == "__main__":
    #App = QApplication(sys.argv)
    #window1 = Ui_GameWindow(False, 10)
    #window1.show()
    #sys.exit(App.exec_()) 

text = "test \n"
text = text + "test2"
print(text)

print(x)

y = np.zeros((8,8), dtype=int)
z = x[7]
print(z[0]==1)



q = 3 + -1
print(q)