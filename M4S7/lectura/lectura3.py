def bool_return():
    try:
        return True #si hay un break, continue o return --> el finally antes de ejecutar esto
    finally: #hay un break, continue o return, se ejecuta este primero
        return False

bool_return()