
quiere_helado_input = input("¿Quiere un helado? (Si / No): ").upper()

if quiere_helado_input == "SI":
    quiere_helado = True
elif quiere_helado_input == "NO":
    quiere_helado = False
else:
    print("Te dije que pongas SI o NO, no entiendo que has dicho")
    quiere_helado = False

tiene_dinero_input = input("¿Tenes dinero para un helado? (Si / No): ").upper()
esta_el_heladero_input = input("¿Esta el heladero? (Si / No): ").upper()
esta_tu_mama_input = input("¿Estas con tu mama? (Si / No): ").upper()

tiene_dinero = tiene_dinero_input == "SI"
esta_tu_mama = esta_tu_mama_input == "SI"
puede_permitirselo = tiene_dinero_input or esta_tu_mama_input
esta_el_heladero = esta_el_heladero_input == "SI"

if quiere_helado == "SI" and puede_permitirselo == "SI" and esta_el_heladero == "SI":
    print("Entonces comete uno")
else:
    print("Entonces nada")
