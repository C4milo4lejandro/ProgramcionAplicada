def dibuja_comparacion(sombra, y_calc):
    sombra_np = np.array(sombra)
    y_calc_np = np.array(y_calc)

    #Determina el tamaño de la figura
    plt.figure(figsize=(5, 5))

    # Dibujar puntos de la sombra original
    plt.scatter(*sombra_np.T, color='blue', label='Sombra original')

    # Dibujar puntos de la proyección calculada
    plt.scatter(*y_calc_np.T, color='red', label='Proyección calculada')

    # Conectar cada punto de la sombra con su correspondiente en la proyección
    for s, y in zip(sombra_np, y_calc_np):
        plt.plot([s[0], y[0]], [s[1], y[1]], 'gray', linestyle='--', linewidth=0.8)

    # Aristas del cubo proyectado original (líneas negras, como en tu función original)
    p1 = [sombra[0], sombra[2],
          sombra[6], sombra[4],
          sombra[0], sombra[1],
          sombra[3], sombra[2], sombra[3],
          sombra[7], sombra[6], sombra[7],
          sombra[5], sombra[4], sombra[5],
          sombra[1]]
    p1 = np.array(p1).T
    plt.plot(*p1, color='black', linewidth=0.8)

    # Estética
    plt.title("Sombra original vs. Proyección calculada")
    plt.axis([0, 1.2, 0, 1.2])
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

dibuja_comparacion(sombra, y_calc)
