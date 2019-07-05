from tkinter import *
from tkinter import ttk
master = Tk()
master.title("JUEGO DE DAMAS")
canvas = Canvas(master,width=700, height=700)
canvas.place(x=0,y=0)
canvas.pack()
_lista = []
_posicion = {}
_indice = 0
_datos = {"item":None,"posx":0,"posy":0}
_posrojo = []
_posnegro = []
_pasos = 80
borde_tablero = canvas.create_rectangle(0,0,640,640,fill = "white")
for filas in range(0,8):
    for columnas in range(0,8):
        posi = filas*_pasos
        posj = columnas*_pasos
        if _indice % 2 == 0:
            if columnas%2 == 0:
                if _indice <= 2:
                    borde_tablero = canvas.create_oval(posi, posj, posi+_pasos, posj+_pasos, width = 4, fill = 'red', tags = ("roja","ficha"))
                    _posicion[str(posj)+"-"+str(posi)] = borde_tablero
                    _posicion[str(borde_tablero)] = {"posx":posj,"posy":posi}
                elif _indice <= 4:
                    pass
                else:
                    borde_tablero = canvas.create_oval(posi, posj, posi+_pasos, posj+_pasos, width = 4, fill = 'black', tags = ("negra","ficha"))
                    _posicion[str(posj)+"-"+str(posi)] = borde_tablero
                    _posicion[str(borde_tablero)] = {"posx":posj,"posy":posi}
            else:
                borde_tablero = canvas.create_rectangle(posi,posj,posi+_pasos,posj+_pasos,fill = 'brown')
        else:
            if columnas%2!=0:
                if _indice<=2:
                    borde_tablero = canvas.create_oval(posi, posj, posi+_pasos, posj+_pasos,fill = 'red',tags = ("roja","ficha"))
                    _posicion[str(posj)+"-"+str(posi)] = borde_tablero
                    _posicion[str(borde_tablero)] = {"posx":posj,"posy":posi}
                elif _indice <= 4:
                    pass
                else:
                    borde_tablero = canvas.create_oval(posi, posj, posi+_pasos, posj+_pasos, width = 4, fill = 'black', tags = ("negra","ficha"))
                    _posicion[str(posj)+"-"+str(posi)] = borde_tablero
                    _posicion[str(borde_tablero)] = {"posx":posj,"posy":posi}
            else:
                borde_tablero = canvas.create_rectangle(posi,posj,posi+_pasos,posj+_pasos,fill = 'brown')

        _lista.append(borde_tablero)
    _indice = _indice+1

senial = lambda x: (1, -1)[x<0]

def ClickBoton(event):
    pass
def BotonPresionado(event):
    global _datos
    _ficha = canvas.find_closest(event.x,event.y)[0]
    _etiqueta = canvas.gettags(_ficha)
    if "ficha" in _etiqueta:
        _ficha_key = str(_ficha)
        _validar = _posicion.get(_ficha_key,None)
        if _validar is not None:
            _datos["item"] = _ficha
            piso_x = event.x - (event.x % _pasos)
            piso_y = event.y - (event.y % _pasos)
            _datos["posx"] = event.x
            _datos["posy"] = event.y
            _datos["piso_x"] = piso_x
            _datos["piso_y"] = piso_y
            _datos["relativeOffsetX"] = event.x - _validar["posx"]
            _datos["relativeOffsetY"] = event.y - _validar["posy"]
        else:
            pass
    else:
    	_datos["item"] = None

def Boton_liberador(event):
    global _posicion,_datos,canvas
    _ficha = _datos["item"]
    if _ficha is None:
        return
    _posx = _datos["posx"]
    _posy = _datos["posy"]
    _piso_x = _datos["piso_x"]
    _piso_y = _datos["piso_y"]
    _ficha_key = str(_ficha)
    _ultima_posc = _posicion.get(_ficha_key,None)
    _ult_posx = _ultima_posc["posx"]
    _ult_posy = _ultima_posc["posy"]
    _etiqueta = canvas.gettags(_ficha)
    _fichas = canvas.find_overlapping(event.x,event.y,event.x,event.y)
    print(_fichas)
    if _fichas[1]!=1:
        piso_x = event.x - (event.x % _pasos)
        piso_y = event.y - (event.y % _pasos)
        _key = str(piso_x)+"-"+str(piso_y)
        delta_piso_x = piso_x - _piso_x
        delta_piso_y = piso_y - _piso_y
        abs_delta_pisox = abs(delta_piso_x)
        abs_delta_pisoy = abs(delta_piso_y)
        if(delta_piso_x==0 or delta_piso_y==0 or abs_delta_pisox!=abs_delta_pisoy or abs_delta_pisox>160):
                _deltax = _ult_posx - _posx + _datos["relativeOffsetX"]
                _deltay = _ult_posy - _posy + _datos["relativeOffsetY"]
                canvas.move(_ficha,_deltax,_deltay)
        else:
            if abs_delta_pisox>80:
                t_pisox = piso_x - senial(delta_piso_x)*_pasos
                t_pisoy = piso_y - senial(delta_piso_y)*_pasos
                _tkey = str(t_pisox)+"-"+str(t_pisoy)
                _t1key = str(piso_x)+"-"+str(piso_y)
                _validar = _posicion.get(_tkey,None)
                _validar1 = _posicion.get(_t1key,None)
                if _validar is None:
                    _deltax = _ult_posx - _posx + _datos["relativeOffsetX"]
                    _deltay = _ult_posy - _posy + _datos["relativeOffsetY"]
                    canvas.move(_ficha,_deltax,_deltay)
                else:
                    if _validar1 is None:
                        _otags = canvas.gettags(_validar)
                        if "ficha" in _otags:
                            if("roja" in _etiqueta and "negra" in _otags) or ("negra" in _etiqueta and "roja" in _otags):
                                _deltax = piso_x - _posx + _datos["relativeOffsetX"]
                                _deltay = piso_y - _posy + _datos["relativeOffsetY"]
                                canvas.move(_ficha,_deltax,_deltay)
                                _posicion[_key] = _ficha
                                _last_item_key = str(_posicion[_ficha_key]["posx"])+"-"+str(_posicion[_ficha_key]["posy"])
                                _posicion[_last_item_key] = None
                                _posicion[_ficha_key]["posx"] = piso_x
                                _posicion[_ficha_key]["posy"] = piso_y
                                canvas.delete(_validar)
                                _posicion[str(_validar)] = None
                                _posicion[str(_tkey)] = None
                            else:
                                _deltax = _ult_posx - _posx + _datos["relativeOffsetX"]
                                _deltay = _ult_posy - _posy + _datos["relativeOffsetY"]
                                canvas.move(_ficha,_deltax,_deltay)
                        else:
                            _deltax = _ult_posx - _posx + _datos["relativeOffsetX"]
                            _deltay = _ult_posy - _posy + _datos["relativeOffsetY"]
                            canvas.move(_ficha,_deltax,_deltay)
                    else:
                        _deltax = _ult_posx - _posx + _datos["relativeOffsetX"]
                        _deltay = _ult_posy - _posy + _datos["relativeOffsetY"]
                        canvas.move(_ficha,_deltax,_deltay)
            else:
                _validar = _posicion.get(_key,None)
                if _validar is not None:
                    _deltax = _ult_posx - _posx + _datos["relativeOffsetX"]
                    _deltay = _ult_posy - _posy + _datos["relativeOffsetY"]
                    canvas.move(_ficha,_deltax,_deltay)
                else:
                    _deltax = _ult_posx - _posx + _datos["relativeOffsetX"]
                    _deltay = _ult_posy - _posy + _datos["relativeOffsetY"]
                    canvas.move(_ficha,_deltax,_deltay)
                    _posicion[_key] = _ficha
                    _last_item_key = str(_posicion[_ficha_key]["posx"])+"-"+str(_posicion[_ficha_key]["posy"])
                    _posicion[_last_item_key] = None
                    _posicion[_ficha_key]["posx"] = piso_x
                    _posicion[_ficha_key]["posy"] = piso_y

def Movimiento(event):
    global _datos,canvas
    _ficha = _datos["item"]
    _posx = _datos["posx"]
    _posy = _datos["posy"]
    _deltax = event.x - _posx
    _deltay = event.y - _posy
    _datos["posx"] = event.x
    _datos["posy"] = event.y
    if _ficha is not None:
        _etiqueta = canvas.gettags(_ficha)
        if "ficha" in _etiqueta:
            canvas.tag_raise(_ficha)
            canvas.move(_ficha,_deltax,_deltay)
turn = "j1"
def turno():
    turno_texto = "Turno del jugador "
    if turno =="j1":
        turno_texto+=jugador1
    else:
    	turno_texto+=jugador2




canvas.tag_bind("ficha","<Button-1>", ClickBoton)
canvas.tag_bind("ficha", "<ButtonPress-1>", BotonPresionado)
canvas.tag_bind("ficha", "<ButtonRelease-1>", Boton_liberador)
canvas.tag_bind("ficha", "<B1-Motion>", Movimiento)
  

master.mainloop()