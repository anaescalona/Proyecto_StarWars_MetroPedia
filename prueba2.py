from Clases.Weapon import Weapon
from Clases.Mision import Mision, menu_misiones
from Clases.Planets import Planets 
from Clases.Movil import Starships
from Clases.People import People


mision1=Mision('1',Planets(1,1,1,1,1,1,1,1,1,1,'Tierra',1),Starships(1,1,1,1,1,1,1,1,1,1,1,1,1,'Apolo 11',1,1,1),[Weapon(1,'Pistola',1,1,1,1,1,1,1)],[People(1,1,1,1,1,1,1,1,1,'Jordan',1,1,1)])

mision2=Mision('2',Planets(1,1,1,1,1,1,1,1,1,1,'Marte',1),Starships(1,1,1,1,1,1,1,1,1,1,1,1,1,'Aveo LS',1,1,1),[Weapon(1,'Metralleta',1,1,1,1,1,1,1)],[People(1,1,1,1,1,1,1,1,1,'Julio',1,1,1)])

Lista_misiones=[mision1,mision2]

menu_misiones()