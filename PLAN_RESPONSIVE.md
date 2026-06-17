# Plan de Actualización: Interfaces Responsivas y Optimización Móvil

Este documento detalla la planificación y los pasos necesarios para asegurar que todas las interfaces del sistema de votación se visualicen correctamente y ofrezcan una excelente experiencia de usuario (UX) en dispositivos móviles.

## 1. Análisis del Estado Actual

El proyecto actual está construido utilizando el framework **Bootstrap 4**, el cual es inherentemente responsivo mediante su sistema de cuadrícula (Grid System). La etiqueta `<meta name="viewport" content="width=device-width, initial-scale=1.0">` ya se encuentra configurada correctamente en el `base.html`.

Sin embargo, existen componentes específicos que requieren ajustes para evitar desbordamientos horizontales o problemas de visualización en pantallas pequeñas.

## 2. Objetivos de la Actualización

1.  **Evitar el desbordamiento horizontal:** Asegurar que ningún elemento (especialmente tablas e imágenes) sobrepase el ancho de la pantalla del dispositivo.
2.  **Optimizar los espacios (Paddings y Margins):** Reducir los espacios en blanco excesivos en pantallas pequeñas para aprovechar mejor el área visible.
3.  **Mejorar la usabilidad táctil:** Asegurar que botones, menús desplegables y controles de formulario tengan un tamaño adecuado para ser pulsados cómodamente.
4.  **Adaptar los componentes interactivos:** Asegurar que el componente de validación facial (cámara web) y los gráficos de resultados se redimensionen dinámicamente.

## 3. Tareas a Ejecutar

### Tarea 1: Envoltura Responsiva para Tablas
Se identificarán todas las tablas HTML en las vistas (especialmente en el panel de administración) que carecen del contenedor `.table-responsive`. Esto permitirá el desplazamiento horizontal táctil de la tabla sin romper el diseño de la página.

*   **Archivos a modificar:**
    *   `src/templates/admin/list_users.html`
    *   `src/templates/admin/admin.html`
    *   `src/templates/main/period_results.html`
*   **Acción:** Envolver cada elemento `<table>` con `<div class="table-responsive">`.

### Tarea 2: Ajuste del Componente de Validación Facial (Biometría)
La ventana emergente o sección donde se abre la cámara (por ejemplo, al votar en `show_lists.html`) define un ancho fijo para el elemento `<video>` (`width="320" height="240"`). En teléfonos muy estrechos, esto puede causar desbordamiento junto con los márgenes del contenedor.

*   **Archivos a modificar:**
    *   `src/templates/voting/show_lists.html`
*   **Acción:** Aplicar clases de Bootstrap como `w-100` y estilos CSS como `max-width: 100%; height: auto;` al `<video>` y su `<canvas>` superpuesto para que se adapten al 100% del contenedor disponible.

### Tarea 3: Refinamiento de Estilos en `index.css` (Media Queries)
Añadir reglas CSS específicas para pantallas pequeñas (Media Queries) para reducir los espaciados (paddings) en las tarjetas premium y botones grandes que funcionan bien en escritorio pero ocupan mucho espacio en móviles.

*   **Archivos a modificar:**
    *   `src/static/css/index.css`
*   **Acción:**
    *   Añadir `@media (max-width: 768px)` para reducir los paddings dentro de `.card-premium`.
    *   Ajustar el tamaño del texto general si es necesario en `.display-3`, `.display-4` para que no provoquen saltos de línea incómodos.
    *   Asegurar que `.btn-premium` ocupe todo el ancho en formularios móviles (`w-100`).

### Tarea 4: Revisión de la Barra de Navegación (Navbar)
La barra de navegación ya utiliza el componente *collapse* de Bootstrap, pero se debe verificar que, al desplegarse en móvil, los elementos internos (como el menú desplegable del perfil de usuario y la imagen de perfil) estén correctamente alineados y no presenten problemas de superposición (`z-index`).

### Tarea 5: Adaptación de los Gráficos de Resultados
Los gráficos creados con *Chart.js* (en `results.html`) tienen una altura fija (`height: 400px`). En teléfonos, puede ser conveniente ajustar esa altura mediante CSS o configuraciones de *Chart.js* (por ejemplo `maintainAspectRatio: false`) para que el gráfico sea más legible.

*   **Archivos a modificar:**
    *   `src/templates/admin/results.html`

## 4. Metodología de Pruebas

Una vez realizados los ajustes, se procederá a:
1.  **Simulación en navegador:** Utilizar las DevTools de Chrome/Firefox para emular dispositivos móviles comunes (iPhone SE, Pixel 5, Samsung Galaxy).
2.  **Pruebas de la cámara:** Comprobar que el inicio y validación de la cámara web sigue funcionando y encajando visualmente en los modelos estrechos.
3.  **Inspección de las tablas:** Verificar que el desplazamiento horizontal funciona con el dedo (o el ratón simulando el tacto) sin mover el resto de la página.

## 5. Próximos Pasos

1.  Aprobar este plan de desarrollo.
2.  Aplicar las modificaciones en las plantillas HTML mencionadas.
3.  Ajustar el archivo `index.css`.
4.  Realizar las pruebas de validación visual y confirmación de funcionamiento táctil.
