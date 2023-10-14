katz_deli = []

def take_a_number(katz_deli, name):
    
    katz_deli.append(name)
    index = len(katz_deli)    
    print(f"Welcome, {name}. You are number {index} in line.") 
    
take_a_number(katz_deli, "Logan") 
take_a_number(katz_deli, "Avi")  
take_a_number(katz_deli, "Spencer")


def line(katz_deli):
    
    if len(katz_deli) == 0:
        print("The line is currently empty.")
        
    else:
        message = [f"{index}. {name}" for index, name in enumerate(katz_deli, start=1)]
        line_str = " ".join(message)
        print(f"The line is currently: {line_str}")
           
line(katz_deli)

def now_serving(katz_deli):
    
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
        
    else:
        name = katz_deli[0]
        katz_deli.remove(name)
        
        print(f"Currently serving {name}.") 
        
            
now_serving(katz_deli)
now_serving(katz_deli)
now_serving(katz_deli)
now_serving(katz_deli)

