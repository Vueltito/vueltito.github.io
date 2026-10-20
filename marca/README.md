# Marca de Vueltito

El caramelo envuelto: el vuelto que se daba cuando no había monedas. Todo sale de `generar_marca.py` (las letras son
Geist Bold y el lema Instrument Serif itálica, pasadas a curvas: los SVG no dependen de tener las fuentes instaladas).

| Archivo | Para qué |
|---|---|
| `vueltito-icono.svg` | El ícono de la app: cuadrado redondeado rosa con el caramelo blanco. |
| `vueltito-icono-chico.svg` | El mismo, simplificado para 16–32 px (pestaña del navegador, barra de tareas). |
| `vueltito-icono-cuadrado.svg` | Sin esquinas redondeadas, para iOS y Android, que las redondean solos. |
| `vueltito-icono-maskable.svg` | Con margen de seguridad, para íconos *maskable* de Android. |
| `vueltito-caramelo.svg` / `-blanco.svg` | El caramelo solo, rosa (sobre fondo claro) o blanco (sobre rosa). |
| `vueltito-logo.svg` / `-blanco.svg` / `-rosa.svg` | El logotipo: "vueltito" con el caramelo de punto de la i. |
| `vueltito-lema.svg` / `-blanco.svg` | El logotipo con el lema: "vueltito *sin vueltas*", en una línea. |
| `vueltito-lema-apilado.svg` / `-blanco.svg` | Lo mismo en dos líneas, para cuadrados y perfiles. |
| `png/lema-*.png` | Esas cuatro versiones en PNG (fondo transparente). |
| `vueltito.ico` | Windows: 16, 24, 32, 48, 64, 128 y 256 px. Es el ícono del acceso directo de la caja en el escritorio. |
| `png/icono-*.png` | El ícono en PNG, de 16 a 1024 px. |
| `png/app-*.png`, `png/apple-touch-icon.png` | Para instalar como app en el celu (manifest y iPhone). |
| `png/og-1200x630.png` | La vista previa cuando se comparte el link (WhatsApp, redes). |

En la app de escritorio: el acceso directo de Windows usa `vueltito.ico`; la versión del celu (`/celu`) usa
`png/app-192.png`, `png/app-512.png` y `png/app-maskable-512.png` en su manifest.

Colores: rosa `#e0187a` (fondo con texto blanco), rosa vivo `#ff4d9a`, chicle `#ff9cc8`, tinta `#1a0f15`,
fondo `#fffafc`.
