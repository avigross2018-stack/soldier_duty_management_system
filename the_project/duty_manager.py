import utils
def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str, valid_days:list, soldiers:list) -> None:
    """
    מוסיפה תורנות חדשה לחייל.
    
    סוג: לוגיקה עסקית (Business Logic)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
        duty_name (str): שם התורנות
        day (str): יום בשבוע (sunday/monday/tuesday/wednesday/thursday)
    
    מחזירה:
        None - הפונקציה מוסיפה את התורנות או זורקת exception
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
        ValueError: אם תורנות עם שם זה כבר קיימת לחייל
        ValueError: אם day לא חוקי (friday/saturday או ערך לא תקין)
    
    למה הפונקציה קיימת:
    לוגיקה עסקית של הוספת תורנות.
    מבצעת בדיקות ומוסיפה תורנות לחייל.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    exist_soldier = utils.find_soldier_by_id(soldier_id, soldiers)
    if exist_soldier == None:
        raise KeyError(f"{soldier_id} Not found")
    exist_duty = utils.find_duty_by_name(exist_soldier['duties'],duty_name)
    if exist_duty != None:
        raise ValueError(f"{duty_name} already exist.")
    valid_day = utils.is_valid_day(day, valid_days)
    if not valid_day:
        raise ValueError(f"{day} Invalid day!!")
    soldier_index = soldiers.index(exist_soldier)
    exist_soldier['duties'].append({"name" : duty_name.strip(), "day" : day.lower().strip(), "status" : "pending"})
    soldiers[soldier_index] = exist_soldier
    


def update_duty_status(soldier_id: int, duty_name: str, new_status: str, soldiers:list, valid_status:list) -> None:
    """
    מעדכנת את הסטטוס של תורנות.
    
    סוג: לוגיקה עסקית (Business Logic)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
        duty_name (str): שם התורנות
        new_status (str): סטטוס חדש (pending/completed/missed)
    
    מחזירה:
        None - הפונקציה מעדכנת את הסטטוס או זורקת exception
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
        KeyError: אם תורנות עם שם זה לא נמצאה לחייל
        ValueError: אם new_status לא חוקי (לא pending/completed/missed)
    
    למה הפונקציה קיימת:
    לוגיקה עסקית של עדכון סטטוס.
    מבצעת בדיקות ומעדכנת את הסטטוס.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    exist_soldier = utils.find_soldier_by_id(soldier_id, soldiers)
    if exist_soldier == None:
        raise KeyError(f"{soldier_id} Not found")
    exist_duty = utils.find_duty_by_name(exist_soldier['duties'],duty_name)
    if exist_duty == None:
        raise ValueError(f"{duty_name} not found.")
    validate_status = utils.is_valid_status(new_status, valid_status)
    if not validate_status:
        raise ValueError(f'{new_status} Invalid status.')
    # exist_duty["status"] = new_status.strip().lower()
    for s in soldiers:
        if s['id'] == soldier_id:
            for d in s['duties']:
                if d['name'] == duty_name:
                    d['status'] = new_status


def get_soldier_duties(soldier_id: int, soldiers:list) -> list:
    """
    מחזירה את רשימת התורנויות של חייל.
    
    סוג: גישה לנתונים (Data Access)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
    
    מחזירה:
        list: רשימת תורנויות (מילונים)
              רשימה ריקה אם אין תורנויות
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
    
    למה הפונקציה קיימת:
    גישה מבוקרת לתורנויות של חייל.
    מפרידה בין הנתונים לבין הגישה אליהם.
    זורקת exception אם החייל לא קיים (במקום להחזיר רשימה ריקה).
    """
    exist_soldier = utils.find_soldier_by_id(soldier_id, soldiers)
    if exist_soldier == None:
        raise KeyError(f"{soldier_id} Not found")
    return exist_soldier['duties']