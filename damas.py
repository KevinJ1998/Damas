from tkinter import *
master = Tk()
master.title("JUEGO DE DAMAS")
canvas = Canvas(master, width=640, height=640)
master.geometry('640x640')
canvas.place(x=0, y=0)
_lista = []
_picionar = {} 
_index = 0 
_datos_act = {"item":None,"px":0,"py":0}
_posazul = [];
_posamarillo = [];
_pasos = 80

borde_tablero = canvas.create_rectangle(0,0,640,640, fill="white")

for i in range(8):
	for j in range(8):
		pi = i*_pasos
		pj = j*_pasos
		if _index % 2 == 0: 
			if j % 2==0:
				if _index<=2: 			
					borde_tablero = canvas.create_oval(pj, pi, pj+_pasos, pi+_pasos, width = 4, fill = 'red', tags = ("roja","ficha"))
					_picionar[str(pj)+"-"+str(pi)] = borde_tablero
					_picionar[str(borde_tablero)] = {"px":pj,"py":pi}
				else:
					if _index<=4: 	
						pass	
					else: 
						borde_tablero = canvas.create_oval(pj, pi, pj+_pasos, pi+_pasos, width = 4, fill = 'black', tags = ("negra","ficha"))
						_picionar[str(pj)+"-"+str(pi)] = borde_tablero
						_picionar[str(borde_tablero)] = {"px":pj,"py":pi}
			else:
				borde_tablero = canvas.create_rectangle(pj,pi,pj+_pasos,pi+_pasos, fill="brown")
		else:
			if j % 2!=0:
				if _index<=2: 
					borde_tablero = canvas.create_oval(pj, pi, pj+_pasos, pi+_pasos, width = 4, fill = 'red', tags = ("roja","ficha"))
					_picionar[str(pj)+"-"+str(pi)] = borde_tablero
					_picionar[str(borde_tablero)] = {"px":pj,"py":pi}
				else:
					if _index<=4: 	
						pass			
					else: 
						borde_tablero = canvas.create_oval(pj, pi, pj+_pasos, pi+_pasos, width = 4, fill = 'black', tags = ("negra","ficha"))
						_picionar[str(pj)+"-"+str(pi)] = borde_tablero
						_picionar[str(borde_tablero)] = {"px":pj,"py":pi}
			else:
				borde_tablero = canvas.create_rectangle(pj,pi,pj+_pasos,pi+_pasos,fill="brown")
		 
		_lista.append(borde_tablero)
	_index+=1 

 
sign = lambda x: (1, -1)[x < 0]

def Click(event):
	pass
def Presionar(event):

	global _datos_act
	_item = canvas.find_closest(event.x, event.y)[0] 
	_tags = canvas.gettags(_item)
	if "ficha" in _tags:
		_item_key = str(_item)
		_val = _picionar.get(_item_key,None)
		if _val is not None:
			_datos_act["item"] = _item
			floorX = event.x - (event.x % _pasos)
			floorY = event.y - (event.y % _pasos) 
			_datos_act["px"] = event.x
			_datos_act["py"] = event.y  
			_datos_act["fpx"] = floorX
			_datos_act["fpy"] = floorY 
			_datos_act["relativeOffsetX"] = event.x-_val["px"]
			_datos_act["relativeOffsetY"] = event.y-_val["py"]
		else:
			pass
	else:
		_datos_act["item"] = None 
	

def BotonLanzamiento(event):
	global _picionar
	global _datos_act
	global canvas
	_item = _datos_act["item"]
	if _item is None:
		return
	_px = _datos_act["px"]
	_py = _datos_act["py"]

	_fpx = _datos_act["fpx"]
	_fpy = _datos_act["fpy"]
	_item_key = str(_item)
	_last_pos = _picionar.get(_item_key,None) 
	_lpx = _last_pos["px"]
	_lpy = _last_pos["py"] 
	_tags = canvas.gettags(_item)
	_items = canvas.find_overlapping(event.x, event.y,event.x, event.y) 
	print(_items)
	if _items[1]!=1:
		floorX = event.x - (event.x % _pasos)
		floorY = event.y - (event.y % _pasos) 
		_key = str(floorX)+"-"+str(floorY)
		deltaFloorX = floorX - _fpx
		deltaFloorY = floorY - _fpy
		abs_deltaFloorX = abs(deltaFloorX)
		abs_deltaFloorY = abs(deltaFloorY)
		if(
			deltaFloorX==0 or 
			deltaFloorY==0 or 
			abs_deltaFloorX!=abs_deltaFloorY or 
			abs_deltaFloorX>160
		):

			_deltaX = _lpx - _px + _datos_act["relativeOffsetX"]
			_deltaY = _lpy - _py + _datos_act["relativeOffsetY"] 
			canvas.move(_item,_deltaX,_deltaY)		
		else: 
			if abs_deltaFloorX>80:
				tfloorX = floorX - sign(deltaFloorX) * _pasos
				tfloorY = floorY - sign(deltaFloorY) * _pasos
				_tkey = str(tfloorX)+"-"+str(tfloorY) 
				_t1key = str(floorX)+"-"+str(floorY) 
				_val = _picionar.get(_tkey,None) 
				_val1 = _picionar.get(_t1key,None) 
				if _val is None:   

					_deltaX = _lpx - _px + _datos_act["relativeOffsetX"]
					_deltaY = _lpy - _py + _datos_act["relativeOffsetY"] 
					canvas.move(_item,_deltaX,_deltaY)					 
				else:  
					if _val1 is None:
						_otags = canvas.gettags(_val)
						if "ficha" in _otags:
							if ("roja" in _tags and "negra" in _otags) or ("roja" in _otags and "negra" in _tags):
								_deltaX = floorX -_px + _datos_act["relativeOffsetX"]
								_deltaY = floorY - _py + _datos_act["relativeOffsetY"]
								canvas.move(_item,_deltaX,_deltaY)
								_picionar[_key] = _item
								_last_item_key = str(_picionar[_item_key]["px"])+"-"+str(_picionar[_item_key]["py"])
								_picionar[_last_item_key] = None
								_picionar[_item_key]["px"]=floorX
								_picionar[_item_key]["py"]=floorY
								canvas.delete(_val);
								_picionar[str(_val)] = None
								_picionar[_tkey] = None 							
							else:

								_deltaX = _lpx - _px + _datos_act["relativeOffsetX"]
								_deltaY = _lpy - _py + _datos_act["relativeOffsetY"] 
								canvas.move(_item,_deltaX,_deltaY) 
						else:

							_deltaX = _lpx - _px + _datos_act["relativeOffsetX"]
							_deltaY = _lpy - _py + _datos_act["relativeOffsetY"] 
							canvas.move(_item,_deltaX,_deltaY) 
					else:

						_deltaX = _lpx - _px + _datos_act["relativeOffsetX"]
						_deltaY = _lpy - _py + _datos_act["relativeOffsetY"] 
						canvas.move(_item,_deltaX,_deltaY) 

			else:
				_val = _picionar.get(_key,None) 
				if _val is not None:   

					_deltaX = _lpx - _px + _datos_act["relativeOffsetX"]
					_deltaY = _lpy - _py + _datos_act["relativeOffsetY"] 
					canvas.move(_item,_deltaX,_deltaY)  
				else:
					_deltaX = floorX -_px + _datos_act["relativeOffsetX"]
					_deltaY = floorY - _py + _datos_act["relativeOffsetY"]
					canvas.move(_item,_deltaX,_deltaY)
					_picionar[_key] = _item
					_last_item_key = str(_picionar[_item_key]["px"])+"-"+str(_picionar[_item_key]["py"])
					_picionar[_last_item_key] = None
					_picionar[_item_key]["px"]=floorX
					_picionar[_item_key]["py"]=floorY

def Movimiento(event):
	global _datos_act
	global canvas
	_item = _datos_act["item"]
	_px = _datos_act["px"]
	_py = _datos_act["py"]
	_deltaX = event.x - _px
	_deltaY = event.y - _py
	_datos_act["px"] = event.x
	_datos_act["py"] = event.y
	if  _item is not None:
		_tags = canvas.gettags(_item)
		if "ficha" in _tags:
			canvas.tag_raise(_item)
			canvas.move(_item,_deltaX,_deltaY)

 
canvas.tag_bind("ficha","<Button-1>", Click) 
canvas.tag_bind("ficha","<ButtonPress-1>", Presionar) 
canvas.tag_bind("ficha","<ButtonRelease-1>", BotonLanzamiento) 
canvas.tag_bind("ficha","<B1-Motion>", Movimiento) 


master.mainloop()