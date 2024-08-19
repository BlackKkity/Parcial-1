import sqlite3

def connect_db():
    return sqlite3.connect('budget.db')

def register_item(name, amount, category):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        INSERT INTO items (name, amount, category)
        VALUES (?, ?, ?)
    ''', (name, amount, category))
    conn.commit()
    conn.close()
    print("Artículo registrado exitosamente.")

def search_item(name):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        SELECT * FROM items WHERE name = ?
    ''', (name,))
    item = c.fetchone()
    conn.close()
    if item:
        print(f"ID: {item[0]}, Nombre: {item[1]}, Monto: {item[2]}, Categoría: {item[3]}")
    else:
        print("Artículo no encontrado.")

def edit_item(item_id, name, amount, category):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        UPDATE items
        SET name = ?, amount = ?, category = ?
        WHERE id = ?
    ''', (name, amount, category, item_id))
    conn.commit()
    conn.close()
    print("Artículo actualizado exitosamente.")

def delete_item(item_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        DELETE FROM items WHERE id = ?
    ''', (item_id,))
    conn.commit()
    conn.close()
    print("Artículo eliminado exitosamente.")

def main():
    while True:
        print("\nSistema de Registro de Presupuesto")
        print("1. Registrar artículo")
        print("2. Buscar artículo")
        print("3. Editar artículo")
        print("4. Eliminar artículo")
        print("5. Salir")
        choice = input("Elige una opción: ")

        if choice == '1':
            name = input("Nombre del artículo: ")
            amount = float(input("Monto: "))
            category = input("Categoría: ")
            register_item(name, amount, category)
        elif choice == '2':
            name = input("Nombre del artículo a buscar: ")
            search_item(name)
        elif choice == '3':
            item_id = int(input("ID del artículo a editar: "))
            name = input("Nuevo nombre del artículo: ")
            amount = float(input("Nuevo monto: "))
            category = input("Nueva categoría: ")
            edit_item(item_id, name, amount, category)
        elif choice == '4':
            item_id = int(input("ID del artículo a eliminar: "))
            delete_item(item_id)
        elif choice == '5':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
