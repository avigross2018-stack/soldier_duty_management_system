def input_valid_day(days:list) -> str:
    '''
    arg days: list of 5 days
    input: enter day in the 5 days
    check if day in days if not exception ValueError
    if True return day
    '''
    pass

def input_name_duty() -> str:
    '''
    input: name of duty
    check if str if not return exception ValueError
    return name of duty
    '''
    

def existing_duty(soldier_id:int, duty_name:str, soldiers:dict) -> bool:
    '''
    arg soldier_id: id of soldier
    arg duty_name: the name of the duty
    arg soldiers: the soldiers data
    check if the duty_name exist in the soldier_id in soldiers
    if exist return True
    if not return False
    '''
    pass

def add_duty():
    '''
    call: func valid_id_input()
    call: func input_valid_day(days:list)
    call: func input_name_duty()
    call: func existing_duty(soldier_id:int, duty_name:str, soldiers:dict)
    if False update the duty in soldier_id {name_duty : {"day" : valid_day, "status" : "pending"}}
    if True return exception ValueError
    '''
    pass

def input_valid_status(available_status:list):
    '''
    input: some status
    check: if status in available_status
    if True return the status
    if False exception ValueError
    '''
    pass

def update_status(soldiers:dict):
    '''
    call: func valid_id_input()
    call: func input_name_duty()
    call: func existing_duty(soldier_id:int, duty_name:str, soldiers:dict)
    if True call func input_valid_status(available_status:list) and update the status
    if False return KeyError
    '''
    pass

def print_soldier_duty(soldiers:dict):
    '''
    call: func valid_id_input()
    return: the soldier info with is duties in a graphical way
    '''
    pass
