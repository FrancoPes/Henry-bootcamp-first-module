import matplotlib.pyplot as plt
import numpy as np


xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
#//------------------------------------------------------------------------------------------------------------------------------------------------------#
#? PUNTOS
plt.plot(xpoints, ypoints)
plt.show()       #show es como un print

# dibujar dos puntos
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()


# lineas con multiples puntos
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()


# por defecto
ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()

# marcar los puntos
plt.plot(ypoints, marker = '*')

#otras formas de marcar puntos
'''
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'
'''

#//------------------------------------------------------------------------------------------------------------------------------------------------------#
#FORMA DE LAS LINEAS


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'd:r')
plt.show()

'''

'-'	Solid line	
':'	Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted line


'''

# color de las lineas
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()

'''
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White
'''


#grosor de las lines
plt.plot(ypoints, linewidth = '20.5')
plt.show()




#dos lines
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()
#//------------------------------------------------------------------------------------------------------------------------------------------------------#
#? LABELS

# poner la etiqueta a los ejes
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
z = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y, z)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.zlabel("whatever Burnage")



#TITULO
plt.title("Sports Watch Data")

# Color y size de los labels
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

#posicion

plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
#//------------------------------------------------------------------------------------------------------------------------------------------------------#
#? GRID
#cuadriculado simple
plt.grid()

#un eje
plt.grid(axis = 'y')

#//------------------------------------------------------------------------------------------------------------------------------------------------------#
#?VARIOS GRAFICOS

# con plt.subplot(1, 2, 1) puedo hacer varios graficos al mismo tiempo. 
# #el primer elemento es la file, el segundo la columna, el tercero el orden del grafico


#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()
#//------------------------------------------------------------------------------------------------------------------------------------------------------
#? scatter: grafico de puntos

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

# puntos con tamanios
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()
#//------------------------------------------------------------------------------------------------------------------------------------------------------
#? BARS GRAPHICS

#sintaxis basica
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

#agregar color
plt.bar(x, y, color = "red")
plt.show()            

#ancho
plt.bar(x, y, width = 0.1)
plt.show()

#alto

plt.barh(x, y, height = 0.1)
plt.show()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              


plt.barh(x, y, height = 0.1)

#//------------------------------------------------------------------------------------------------------------------------------------------------------
#? HISTOGRAMA

x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show() 


#//------------------------------------------------------------------------------------------------------------------------------------------------------
#? PIE GRAPHICS
y = np.array([35, 25, 25, 15])
#TENGO QUE PONERLE LOS PORCENTAJES
plt.pie(y)
plt.show()

#PONERLE LABELS
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 

# ADD A SHADOW
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show() 

# ESPECIFICAR UN LUGAR
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 

#ADD A LEGEND
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show() 
 #LEGEND WITH TITLE
plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")















































