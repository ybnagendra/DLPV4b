#!/usr/bin/env python                                                                                                                               
                                                                                                                                                    
import time                                                                                                                                         
import DS3231_Driver                                                                                                                                
from OmegaExpansion import oledExp                                                                                                                  
                                                                                                                                                    
def welcomeMessage():                                                                                                                               
    oledExp.setVerbosity(0)                                                                                                                         
    oledExp.driverInit()                                                                                                                            
    oledExp.setCursor(3, 0)                                                                                                                         
    oledExp.write("Welcome to OnionOmega")                                                                                                          
    oledExp.setCursor(4, 0)                                                                                                                         
    oledExp.write("Data Logger Project")                                                                                                            
    time.sleep(2)  
    
def Message2():                                                                                                                               
    #oledExp.setVerbosity(0)                                                                                                                         
    #oledExp.driverInit()                                                                                                                            
    oledExp.setCursor(3, 0)                                                                                                                         
    oledExp.write("Message2")                                                                                                          
    oledExp.setCursor(4, 0)                                                                                                                         
    oledExp.write("Data Logger Project")                                                                                                            
    time.sleep(2)   
                                                                                                                                                    
if __name__ == "__main__":  

    try:
      welcomeMessage() 
    except:
      print("welcome Message")
    try:
      Message2()
    except:
      print("Message")
   
