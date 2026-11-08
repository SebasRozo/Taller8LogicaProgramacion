def mostrar_conjunto(titulo, conjunto):
    contenido = ", ".join(sorted(conjunto))
    print(f"{titulo}: {{{contenido}}}")


def mostrar_analisis(curso_a, curso_b):
    print("\n========== ESTUDIANTES INSCRITOS ==========")
    mostrar_conjunto("Curso A - Fundamentos de programación", curso_a)
    mostrar_conjunto("Curso B - Introducción a bases de datos", curso_b)

    todos = curso_a | curso_b
    ambos = curso_a & curso_b
    solo_a = curso_a - curso_b
    solo_b = curso_b - curso_a
    exactamente_uno = curso_a ^ curso_b

    print("\n========== ANÁLISIS DE LOS CONJUNTOS ==========")
    print(f"Cantidad de estudiantes diferentes: {len(todos)}")

    mostrar_conjunto("Estudiantes inscritos en ambos cursos", ambos)
    mostrar_conjunto("Estudiantes únicamente en el curso A", solo_a)
    mostrar_conjunto("Estudiantes únicamente en el curso B", solo_b)
    mostrar_conjunto("Estudiantes inscritos en exactamente uno de los cursos", exactamente_uno)

    if curso_a <= curso_b:
        print("¿Todos los estudiantes del curso A también están en el curso B? Sí.")
    else:
        print("¿Todos los estudiantes del curso A también están en el curso B? No.")


def main():
    curso_a = {
        "Ana", "Carlos", "Laura", "Pedro",
        "Sofia", "Andres", "Camila"
    }

    curso_b = {
        "Laura", "Pedro", "Daniel", "Sofia",
        "Mateo", "Valentina"
    }

    print("\n========== EJERCICIO 2 ==========")
    print("ANÁLISIS DE PARTICIPACIÓN EN CURSOS")

    mostrar_analisis(curso_a, curso_b)

    print("\n========== AGREGAR UN ESTUDIANTE ==========")

    while True:
        curso = input("¿A qué curso desea agregar el estudiante? (A/B): ").strip().upper()

        if curso in ("A", "B"):
            break

        print("Opción no válida. Escriba A o B.")

    nombre = input("Ingrese el nombre del estudiante: ").strip().title()

    if not nombre:
        print("No se agregó ningún estudiante porque el nombre estaba vacío.")

    elif curso == "A":
        cantidad_anterior = len(curso_a)
        curso_a.add(nombre)

        if len(curso_a) == cantidad_anterior:
            print(f"{nombre} ya estaba inscrito en el curso A.")
        else:
            print(f"{nombre} fue agregado al curso A.")

    else:
        cantidad_anterior = len(curso_b)
        curso_b.add(nombre)

        if len(curso_b) == cantidad_anterior:
            print(f"{nombre} ya estaba inscrito en el curso B.")
        else:
            print(f"{nombre} fue agregado al curso B.")

    print("\n========== RESULTADOS ACTUALIZADOS ==========")
    mostrar_analisis(curso_a, curso_b)


if __name__ == "__main__":
    main()
