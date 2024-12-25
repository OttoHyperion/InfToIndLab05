import requests

URL = "http://localhost:8082"
TOKEN = "token1"

def create_note():
    response = requests.post(f"{URL}/note", params={"token": TOKEN})
    if response.status_code == 200:
        note_id = response.json().get("id")
        print(f"Заметка создана с ID: {note_id}")
    else:
        print(f"Не удалось создать заметку: {response.text}")

def get_note_text(note_id: int):
    response = requests.get(f"{URL}/note/{note_id}", params={"token": TOKEN})
    if response.status_code == 200:
        note = response.json()
        print(f"Текст заметки: {note['text']}")
    else:
        print(f"Не удалось получить текст заметки: {response.text}")

def get_note_info(note_id: int):
    response = requests.get(f"{URL}/note-info/{note_id}", params={"token": TOKEN})
    if response.status_code == 200:
        note_info = response.json()
        print(f"Заметка создана в: {note_info['created_at']}")
        print(f"Заметка изменена в: {note_info['updated_at']}")
    else:
        print(f"Не удалось получить информацию о заметке: {response.text}")

def update_note(note_id: int, note_text: str):
    response = requests.patch(f"{URL}/note/{note_id}", params={"token": TOKEN, "text": note_text})
    if response.status_code == 200:
        print(f"Заметка {note_id} изменена")
    else:
        print(f"Не удалось изменить заметку: {response.text}")

def delete_note(note_id: int):
    response = requests.delete(f"{URL}/note/{note_id}", params={"token": TOKEN})
    if response.status_code == 200:
        print(f"Заметка {note_id} удалена")
    else:
        print(f"Не удалось удалить заметку: {response.text}")

def list_notes():
    response = requests.get(f"{URL}/note", params={"token": TOKEN})
    if response.status_code == 200:
        notes = response.json()['list']
        print(f"Список заметок: {notes}")
    else:
        print(f"Не удалось получить список заметок: {response.text}")


while True:
    print("1. Создать заметку")
    print("2. Прочитать заметку")
    print("3. Информация о заметке")
    print("4. Изменить заметку")
    print("5. Удалить заметку")
    print("6. Список заметок")
    print("0. Выход")
    choice = input("Выберите действие: ")

    if choice == "1":
        create_note()
    elif choice == "2":
        id = int(input("ID заметки: "))
        get_note_text(id)
    elif choice == "3":
        id = int(input("ID заметки: "))
        get_note_info(id)
    elif choice == "4":
        id = int(input("ID заметки: "))
        text = input("Новый текст заметки: ")
        update_note(id, text)
    elif choice == "5":
        id = int(input("ID заметки: "))
        delete_note(id)
    elif choice == "6":
        list_notes()
    elif choice == "0":
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")
