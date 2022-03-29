from chrome import open_chrome

def search_process(get_data):
      
    
    if len(get_data) == 0:
        return('please enter data')
    
    else:
        return search_data(get_data)

def search_data(get_data):
    
    if 'syntax' in get_data:
        return('when a proper syntax of the language is not followed then syntax error is thrown')
        
    if 'zerodivision' in get_data:
        return('when an error occurs in a run time and it is undefined')
       
    elif 'indentation' in get_data:
        return('when spacing is not correct')
    
    elif 'index' in get_data:
        return('your code is trying to access an index that is invalid')
    
    elif 'assertion' in get_data:
        return('it is thrown when assert statement fails.')
    
    elif 'attribute' in get_data:
        return('it is thrown when attributr assignment is failed')
    
    elif 'import' in get_data:
        return('it occus when import module is not found.')
    
    elif 'keyboard interrupt' in get_data:
        return('raised when user hits interrupt key such as ctrl-c or del')
    
    elif 'name' in get_data:
        return('it occurs when he variable is not defined')
        
    elif 'memory' in get_data:
        return('it means the programme ran out of  memory')
    
    elif 'floatingpoint' in get_data:
        return('it mean there was an error in the floating point.')
        
    elif 'modulenotfound' in get_data:
        return('raised by import when a module could not be found.')
    
    elif 'type' in get_data:
        return('when a function or operation of different types are bounded.')
    
    elif 'key' in get_data:
        return('it occurs when thet directory key is not found.')
    
    elif 'notimplemented' in get_data:
        return('should raise this exception when the derived classes override the method.')
        
    elif 'overflow' in get_data:
        return('raised when the result of an arithmetic operation is out of range.')
    
    elif 'recursion' in get_data:
        return('this exception is aised when the interpreter dectects that the maximum recursion depth is exceeded.')
    
    elif 'reference' in get_data:
        return('raised when a weak reference proxy is used to access an attribute of the referent after the garbage collection.')
    
    elif 'runtime' in get_data:
        return('raised when no other exception applies')
    
    elif 'system' in get_data:
        return('called when sys.exit() function is called')
    
    elif 'unboundlocal' in get_data:
        return('called when no value is assined o a local variable in a function.')
    
    elif 'unicode' in get_data:
        return('thrown when a unicode-related encoding or decoding error occurs')
    
    elif 'value' in get_data:
        return('when a built-in operation or function recieves an argument that has the right type but an invalid value.')
        
    elif 'eof' in get_data:
        return('raised when the input() function hits the end-of-file condition.')
    
    elif 'system' in get_data:
        return('when the intrepreter detects internal error.')
        
    else:
        return open_chrome(get_data)
