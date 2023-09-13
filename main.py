import matplotlib.pyplot as plt
import numpy as np
plt.plot([95,0],[0,290])
plt.scatter(58,111)
plt.text(2500,100,"90x+5y<=10000")
plt.axhline(y=111,c="green")
plt.xlim(0,300) #устанавливаем лимиты осей
plt.ylim(0,300)
plt.ylabel('y')
plt.xlabel('x')
plt.grid() # включение отображение сетки
plt.title('Продажи')
plt.yticks(range(0, 300, 20))
plt.xticks(range(0, 300, 20))
#plt.fill_between([0,14],[17,17],color="silver")
#plt.fill_between([13.8,19],[17,13],color="silver")

plt.arrow(1,1,30,30, width=1.2)
plt.show()
