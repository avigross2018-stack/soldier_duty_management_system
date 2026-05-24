from soldier_manager import add_soldier, remove_soldier, get_all_soldiers
from duty_manager import add_duty_to_soldier, update_duty_status, get_soldier_duties
from data import soldiers
from utils import VALID_DAYS, VALID_STATUS
def show_menu() -> None:
    """
    מציגה את התפריט הראשי למשתמש.
    
    מקבלת: כלום
    מחזירה: כלום (מדפיסה לקונסול)
    
    למה הפונקציה קיימת:
    הפרדה בין הצגת התפריט לבין הלוגיקה העסקית.
    אם נרצה לשנות את התצוגה, נשנה רק כאן.
    """
    print("-- Duty manager --\n")
    print("1. ADD SOLDIER TO SYSTEM")
    print("2. REMOVE SOLDIER FROM SYSTEM")
    print("3. SHOW ALL SOLDIERS")
    print("4. ADD DUTY TO SOLDIER")
    print("5. UPDATE DUTY STATUS")
    print("6. SHOW DUTIES OF A SOLDIER")
    print("7. EXIT")
    print("===================")


def get_user_choice() -> str:
    """
    מקבלת בחירה מהמשתמש.
    
    מקבלת: כלום
    מחזירה: מחרוזת המייצגת את בחירת המשתמש
    
    למה הפונקציה קיימת:
    הפרדת קבלת קלט מהמשתמש מהלוגיקה של עיבוד הבחירה.
    מאפשר להחליף את שיטת הקלט בעתיד (למשל, GUI).
    """
    return input("Choose an action (1-7).").strip()


def handle_add_soldier() -> None:
    """
    מטפלת בתהליך הוספת חייל חדש.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    מפרידה בין הקלט/פלט לבין הלוגיקה העסקית.
    main.py אחראי על אינטראקציה עם המשתמש,
    soldier_manager.py אחראי על הלוגיקה.
    """
    try:
        soldier_id = int(input("Enter soldier ID. "))
        name = input("Enter soldier name. ")
        add_soldier(soldier_id, name, soldiers)
        print("Soldier added...")
    except ValueError as e:
        print("You can enter only numbers.")
 

def handle_remove_soldier() -> None:
    """
    מטפלת בתהליך הסרת חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id = int(input("Enter soldier ID"))
        remove_soldier(soldier_id, soldiers)
        print("Soldier removed...")
    except ValueError:
        print("You can enter only numbers.")
    except KeyError as e:
        print(f"ERROR {e}")


def handle_view_soldiers() -> None:
    """
    מטפלת בתהליך הצגת כל החיילים.
    קוראת לפונקציה המתאימה ומציגה את התוצאה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין קבלת הנתונים לבין הצגתם.
    """
    soldiers_info = get_all_soldiers(soldiers)
    if not soldiers_info:
        print("No soldiers in the system...")
        return
    print("--- SOLDIERS LIST ---")
    for s in soldiers_info:
        amount_duties = len(s['duties'])
        print(f"ID: {s['id']} \nNAME: {s['name']} \nAMOUNT DUTIES: {amount_duties}")


def handle_add_duty() -> None:
    """
    מטפלת בתהליך הוספת תורנות לחייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id = int(input("Enter ID. "))
        duty_name = input("Enter duty name. ")
        day = input("Enter day of duty (sunday/monday/tuesday/wednesday/thursday). ")
        add_duty_to_soldier(soldier_id, duty_name, day, VALID_DAYS, soldiers)
        print("Duty added...")
    except ValueError as e:
        print(f'ERROR {e}')
    except KeyError as e:
        print(f'ERROR {e}')



def handle_update_duty_status() -> None:
    """

    מטפלת בתהליך עדכון סטטוס תורנות.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:    
        soldier_id = int(input("Enter ID. "))
        duty_name = input("Enter duty name. ")
        new_status = input("Enter new status (pending/completed/missed). ")
        update_duty_status(soldier_id, duty_name, new_status, soldiers, VALID_STATUS)
        print("Status updated...")
    except ValueError as e:
        print(f"ERROR {e}")
    except KeyError as e:
        print(f'ERROR {e}')

def handle_view_soldier_duties() -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id = int(input("Enter ID: "))
        duties = get_soldier_duties(soldier_id, soldiers)
        
        if not duties:
            print("This soldier has no duties.")
            return
            
        print(f"\n--- DUTIES FOR SOLDIER {soldier_id} ---")
        for duty in duties:
            print(f"Name: {duty['name']} | Day: {duty['day']} | Status: {duty['status']}")
            
    except ValueError:
        print("You can enter only numbers for ID.")
    except KeyError as e:
        print(f"ERROR: {e}")


def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """
flag = True
while flag:
        show_menu()
        choice = get_user_choice()
        match choice:
            case'1':
                handle_add_soldier()
            case'2':
                handle_remove_soldier()
            case '3':
                handle_view_soldiers()
            case '4':
                handle_add_duty()
            case '5':
                handle_update_duty_status()
            case '6':
                handle_view_soldier_duties()
            case '7':
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please select 1-7.")  


if __name__ == '__main__':
    main()