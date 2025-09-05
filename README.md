Organiza tu código en funciones y usa un menú principal que solo se encargue de llamarlas. Así evitas repetir código, lo vuelves más claro y fácil de mantener.

Ejemplo de estructura con funciones:


def registrar_usuario(usuarios):
    print("\n--- Registrar usuario ---")
    nombre = input("Nombre: ")
    documento = input("Documento: ")
    cargo = input("Cargo: ")
    usuarios[documento] = {"nombre": nombre, "cargo": cargo, "asistencias": []}
    print("Usuario registrado.")

def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Registrar nuevo usuario")
    print("2. Registrar asistencia")
    print("3. Ver historial de asistencias")
    print("4. Salir")
    return input("Seleccione una opción: ")

# Programa principal
usuarios = {}
opcion = ""
while opcion != "4":
    opcion = mostrar_menu()
    if opcion == "1":
        registrar_usuario(usuarios)
    elif opcion == "2":
        print("Aquí iría la función de asistencia...")
    elif opcion == "3":
        print("Aquí iría la función de historial...")
    elif opcion == "4":
        print("Saliendo del sistema...")
    else:
        print("Opción inválida.")




de rest van muy bien

           /\        /\    
            ;  ;      ;  ;   
           ;    ;    ;    ;  
          ;  .   ;  ;   .  ; 
          ;   o   ;;   o   ; 
          ;       ;;       ; 
           ;   ^    ^^   ;  
            ;    '-'    ;   
             ;;;;;;;;;;;    
           ;;           ;;  
         ;;               ;; 
       ;;                   ;;
      ;;                     ;;
     ;;                       ;;
    ;;                         ;;
   ;;                           ;;

                Vas bien 😺
