"""
Autor: Juan David Zuluaga Lopez
"""
#librerias
import re

#clases para el objeto aljebraico (limitado a expresiones de sumas y restas)
class expresion_algebraica:
    expresion = ""
    variable = ""
    terminos = []
    operadores = []
    ordentermino = []
    orden = 0
    
    def __init__(self,expresion):
        try:
            if expresion.find(":") == 1:
                self.variable = expresion[0:1]
                expresion = expresion[2:len(expresion)].replace(' ','')
                self.expresion = expresion
            else:
                self.variable = "x"
                expresion = expresion.replace(' ','')          
                self.expresion = expresion
            
            patron = re.compile(r'\b[-+]\b')
            self.terminos = patron.split(expresion)
            self.operadores = patron.findall(expresion)
            
            if expresion[0:1] != "+" and expresion[0:1] != "-":
                self.operadores.insert(0, '+')
            
            for x in range(len(self.terminos)):
                temp = self.terminos[x].find(self.variable)
                if temp >= 0:
                    self.ordentermino.append(self.terminos[x][temp+2:temp+3])
                    if self.ordentermino[x] == "":
                       self.ordentermino[x] = "1" 
                else:
                    self.ordentermino.append("0")
                
                if int(self.ordentermino[x])>self.orden:
                    self.orden = int(self.ordentermino[x])
                
            
        except Exception as e:
            print("Error al leer la expresion.\n\n",e)
            self.expresion = ""
            self.variable = ""
    
    def evaluar_expresion(self,valor):
        try:
            resultado = 0
            total = len(self.expresion.terminos)
            term = 0
            
            for i in range(total):
                if self.expresion.ordentermino[i] == "0":
                    resultado += int(self.expresion.operadores[i]+self.expresion.terminos[i])
                else:
                    term = int(self.expresion.operadores[i]+self.expresion.terminos[i][0:self.expresion.terminos[i].find(self.expresion.variable)])
                    resultado += term * pow(valor, int(self.expresion.ordentermino[i]))
                
            return resultado
        except Exception as e:
            print("No se pudo evaluar.\n\n",e)
            return -1

class operacion_algebraica:
    def simplificar(self,expresion1):
        try:
            ordenmayor = expresion1.orden
            resultado = []
            total1 = len(expresion1.terminos)
            
            for i in range(ordenmayor+1):
                for j in range(total1):
                    if int(expresion1.ordentermino[j]) == i:
                        if len(resultado) == i:
                            resultado.append(expresion1.terminos[j])
                        else:
                            if i == 0:
                                sumar = int(resultado[i]) + int(expresion1.operadores[j]+expresion1.terminos[j])
                                resultado[i] = str(sumar)
                            elif i == 1:    
                                sumar = int(resultado[i][0:resultado[i].find(expresion1.variable)]) + int(expresion1.operadores[j]+expresion1.terminos[j][0:expresion1.terminos[j].find(expresion1.variable)])
                                resultado[i] = str(sumar)+expresion1.variable
                            else:
                                sumar = int(resultado[i][0:resultado[i].find(expresion1.variable)]) + int(expresion1.operadores[j]+expresion1.terminos[j][0:expresion1.terminos[j].find(expresion1.variable)])
                                resultado[i] = str(sumar)+expresion1.variable+"^"+str(i)
            
                if len(resultado) == i:
                    resultado.append("0")
                    
            resultadofinal=""
            
            for i in range(ordenmayor,-1,-1):
                if resultado[i][0:1] != "0":
                    if resultado[i][0:1] == "-":
                        resultadofinal += resultado[i]
                    else:
                        resultadofinal += "+" + resultado[i]
            
            if resultadofinal[0:1] == "+":
                temp = len(resultadofinal)
                resultadofinal = resultadofinal[1:temp]
            
            return resultadofinal
        except Exception as e:
            print("No se pudo simplificar.\n\n",e)
            return ""
    
    def suma(self,expresion1,expresion2):
        try:
            if expresion1.orden>expresion2.orden:
                ordenmayor = expresion1.orden
            else:
                ordenmayor = expresion2.orden
            resultado = []
            total1 = len(expresion1.terminos)
            total2 = len(expresion2.terminos)
            
            for i in range(ordenmayor+1):
                for j in range(total1):
                    if int(expresion1.ordentermino[j]) == i:
                        if len(resultado) == i:
                            resultado.append(expresion1.terminos[j])
                        else:
                            if i == 0:
                                sumar = int(resultado[i]) + int(expresion1.operadores[j]+expresion1.terminos[j])
                                resultado[i] = str(sumar)
                            elif i == 1:    
                                sumar = int(resultado[i][0:resultado[i].find(expresion1.variable)]) + int(expresion1.operadores[j]+expresion1.terminos[j][0:expresion1.terminos[j].find(expresion1.variable)])
                                resultado[i] = str(sumar)+expresion1.variable
                            else:
                                sumar = int(resultado[i][0:resultado[i].find(expresion1.variable)]) + int(expresion1.operadores[j]+expresion1.terminos[j][0:expresion1.terminos[j].find(expresion1.variable)])
                                resultado[i] = str(sumar)+expresion1.variable+"^"+str(i)
            
                for j in range(total2):
                    if int(expresion2.ordentermino[j]) == i:
                        if len(resultado) == i:
                            resultado.append(expresion2.terminos[j])
                        else:
                            if i == 0:
                                sumar = int(resultado[i]) + int(expresion2.operadores[j]+expresion2.terminos[j])
                                resultado[i] = str(sumar)
                            elif i == 1:    
                                sumar = int(resultado[i][0:resultado[i].find(expresion2.variable)]) + int(expresion2.operadores[j]+expresion2.terminos[j][0:expresion2.terminos[j].find(expresion2.variable)])
                                resultado[i] = str(sumar)+expresion2.variable
                            else:
                                sumar = int(resultado[i][0:resultado[i].find(expresion2.variable)]) + int(expresion2.operadores[j]+expresion2.terminos[j][0:expresion2.terminos[j].find(expresion2.variable)])
                                resultado[i] = str(sumar)+expresion2.variable+"^"+str(i)
            
                if len(resultado) == i:
                    resultado.append("0")
                    
            resultadofinal=""
            
            for i in range(ordenmayor,-1,-1):
                if resultado[i][0:1] != "0":
                    if resultado[i][0:1] == "-":
                        resultadofinal += resultado[i]
                    else:
                        resultadofinal += "+" + resultado[i]
            
            if resultadofinal[0:1] == "+":
                temp = len(resultadofinal)
                resultadofinal = resultadofinal[1:temp]
            
            return resultadofinal
        except Exception as e:
            print("No se pudo sumar.\n\n",e)
            return ""
        
    def resta(self,expresion1,expresion2):
        try:
            if expresion1.orden>expresion2.orden:
                ordenmayor = expresion1.orden
            else:
                ordenmayor = expresion2.orden
            resultado = []
            total1 = len(expresion1.terminos)
            total2 = len(expresion2.terminos)
            
            for i in range(ordenmayor+1):
                for j in range(total1):
                    if int(expresion1.ordentermino[j]) == i:
                        if len(resultado) == i:
                            resultado.append(expresion1.terminos[j])
                        else:
                            if i == 0:
                                sumar = int(resultado[i]) - int(expresion1.operadores[j]+expresion1.terminos[j])
                                resultado[i] = str(sumar)
                            elif i == 1:    
                                sumar = int(resultado[i][0:resultado[i].find(expresion1.variable)]) - int(expresion1.operadores[j]+expresion1.terminos[j][0:expresion1.terminos[j].find(expresion1.variable)])
                                resultado[i] = str(sumar)+expresion1.variable
                            else:
                                sumar = int(resultado[i][0:resultado[i].find(expresion1.variable)]) - int(expresion1.operadores[j]+expresion1.terminos[j][0:expresion1.terminos[j].find(expresion1.variable)])
                                resultado[i] = str(sumar)+expresion1.variable+"^"+str(i)
            
                for j in range(total2):
                    if int(expresion2.ordentermino[j]) == i:
                        if len(resultado) == i:
                            resultado.append(expresion2.terminos[j])
                        else:
                            if i == 0:
                                sumar = int(resultado[i]) - int(expresion2.operadores[j]+expresion2.terminos[j])
                                resultado[i] = str(sumar)
                            elif i == 1:    
                                sumar = int(resultado[i][0:resultado[i].find(expresion2.variable)]) - int(expresion2.operadores[j]+expresion2.terminos[j][0:expresion2.terminos[j].find(expresion2.variable)])
                                resultado[i] = str(sumar)+expresion2.variable
                            else:
                                sumar = int(resultado[i][0:resultado[i].find(expresion2.variable)]) - int(expresion2.operadores[j]+expresion2.terminos[j][0:expresion2.terminos[j].find(expresion2.variable)])
                                resultado[i] = str(sumar)+expresion2.variable+"^"+str(i)
                    
                if len(resultado) == i:
                    resultado.append("0")
                        
            resultadofinal=""
            
            for i in range(ordenmayor,-1,-1):
                if resultado[i][0:1] != "0":
                    if resultado[i][0:1] == "-":
                        resultadofinal += resultado[i]
                    else:
                        resultadofinal += "+" + resultado[i]
            
            if resultadofinal[0:1] == "+":
                temp = len(resultadofinal)
                resultadofinal = resultadofinal[1:temp]
            
            return resultadofinal
        except Exception as e:
            print("No se pudo restar.\n\n",e)
            return ""
        
    def multiplicacion(self,expresion1,expresion2):
        try:
            resultado = []
            total1 = len(expresion1.terminos)
            total2 = len(expresion2.terminos)
            term1 = 0
            term2 = 0
            
            for i in range(total1):
                if expresion1.ordentermino[i] == "0":
                    term1 = int(expresion1.operadores[i]+expresion1.terminos[i])
                else:
                    term1 = int(expresion1.operadores[i]+expresion1.terminos[i][0:expresion1.terminos[i].find(expresion1.variable)])
                
                for j in range(total2):
                    if expresion2.ordentermino[j] == "0":
                        term2 = int(expresion2.operadores[j]+expresion2.terminos[j])
                    else:
                        term2 = int(expresion2.operadores[j]+expresion2.terminos[j][0:expresion2.terminos[j].find(expresion2.variable)])
                    
                    multiplicar = term1 * term2
                    
                    if int(expresion1.ordentermino[i]) + int(expresion2.ordentermino[j]) == 0:
                        resultado.append(str(multiplicar))
                    elif int(expresion1.ordentermino[i]) + int(expresion2.ordentermino[j]) == 1:
                        resultado.append(str(multiplicar)+"x")
                    else:
                        resultado.append(str(multiplicar)+"x^"+str(int(expresion1.ordentermino[i]) + int(expresion2.ordentermino[j])))
            
            total = len(resultado)
            resultadofinal=""
            
            for i in range(total):
                if resultado[i][0:1] != "0":
                    if resultado[i][0:1] == "-":
                        resultadofinal += resultado[i]
                    else:
                        resultadofinal += "+" + resultado[i]
                        
            if resultadofinal[0:1] == "+":
                temp = len(resultadofinal)
                resultadofinal = resultadofinal[1:temp]
                
            resultadofinal = operacion_algebraica.simplificar(expresion_algebraica(resultadofinal))
            
            return resultadofinal
        except Exception as e:
            print("No se pudo multiplicar.\n\n",e)
            return ""

    def multiplicacion_escalar(self,expresion,escalar):
        try:
            resultado = []
            total = len(expresion.terminos)
            term = 0
            
            for i in range(total):
                if expresion.ordentermino[i] == "0":
                    term = int(expresion.operadores[i]+expresion.terminos[i])
                else:
                    term = int(expresion.operadores[i]+expresion.terminos[i][0:expresion.terminos[i].find(expresion.variable)])
                
                multiplicar = term * escalar
                
                if int(expresion.ordentermino[i]) == 0:
                    resultado.append(str(multiplicar))
                elif int(expresion.ordentermino[i]) == 1:
                    resultado.append(str(multiplicar)+"x")
                else:
                    resultado.append(str(multiplicar)+"x^"+str(int(expresion.ordentermino[i])))
            
            total = len(resultado)
            resultadofinal=""
            
            for i in range(total):
                if resultado[i][0:1] != "0":
                    if resultado[i][0:1] == "-":
                        resultadofinal += resultado[i]
                    else:
                        resultadofinal += "+" + resultado[i]
                        
            if resultadofinal[0:1] == "+":
                temp = len(resultadofinal)
                resultadofinal = resultadofinal[1:temp]
            
            return resultadofinal
        except Exception as e:
            print("No se pudo multipicar.\n\n",e)
            return ""
