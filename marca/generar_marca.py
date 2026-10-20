"""Genera la marca de Vueltito: el caramelo, el ícono de la app y el logotipo con las letras pasadas a curvas.

Uso (necesita fontTools):
    python generar_marca.py Geist-Bold.ttf marca/ InstrumentSerif-Italic.ttf

Las fuentes son de Google Fonts (OFL) y no van en el repo: Geist en peso 800 e Instrument Serif itálica. Los PNG,
el .ico y la vista previa se sacan de estos SVG (ver README.md de esta carpeta).
"""
import pathlib
import sys

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FUENTE, SALIDA = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
SALIDA.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------- caramelo
# Coordenadas locales: centro del caramelo en (0, 0), sin rotar. Mide ~712 x 320.
ABANICO = ("M 182 -30 C 220 -58, 256 -100, 298 -134 C 316 -98, 302 -70, 316 -44 "
           "C 328 -18, 314 6, 322 28 C 332 56, 314 88, 302 134 C 258 104, 220 58, 182 30 Z")
PLIEGUES = ["M 196 -14 L 290 -104", "M 200 0 L 312 -4", "M 196 14 L 294 104"]


def caramelo(p, *, cuerpo, raya, env_a, env_b, pliegue, nudo, simple=False, brillo=True):
    """Devuelve (defs, grupo) del caramelo con el prefijo de ids p."""
    defs = f"""
    <linearGradient id="{p}env" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{env_a}"/><stop offset="1" stop-color="{env_b}"/></linearGradient>
    <radialGradient id="{p}vol" cx="34%" cy="28%" r="80%"><stop offset="0" stop-color="#fff" stop-opacity=".55"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#5a0838" stop-opacity=".26"/></radialGradient>
    <clipPath id="{p}clip"><ellipse rx="178" ry="150"/></clipPath>"""
    ancho_raya = 62 if simple else 46
    rayas = "".join(f'<rect x="{x}" y="-320" width="{ancho_raya}" height="640"/>' for x in ((-176, -34, 108) if simple else (-186, -70, 46, 162)))
    pliegues = "" if simple else "".join(
        f'<path d="{d}" fill="none" stroke="{pliegue}" stroke-width="7" stroke-linecap="round" stroke-opacity=".38"/>' for d in PLIEGUES)
    abanico = f'<path d="{ABANICO}" fill="url(#{p}env)"/>{pliegues}'
    reflejos = "" if (simple or not brillo) else (
        '<ellipse cx="-72" cy="-84" rx="64" ry="22" fill="#fff" fill-opacity=".85" transform="rotate(-18 -72 -84)"/>'
        '<ellipse cx="6" cy="-112" rx="13" ry="6" fill="#fff" fill-opacity=".6" transform="rotate(-10 6 -112)"/>')
    grupo = f"""
    <g>{abanico}</g><g transform="scale(-1 1)">{abanico}</g>
    <ellipse cx="-184" rx="18" ry="36" fill="{nudo}"/><ellipse cx="184" rx="18" ry="36" fill="{nudo}"/>
    <ellipse rx="178" ry="150" fill="{cuerpo}"/>
    <g clip-path="url(#{p}clip)"><g transform="rotate(32)" fill="{raya}">{rayas}</g></g>
    <ellipse rx="178" ry="150" fill="url(#{p}vol)"/>{reflejos}"""
    return defs, grupo


ICONO_CARAMELO = dict(cuerpo="#fffafc", raya="#ff4d9a", env_a="#ffeaf3", env_b="#ffbfdc", pliegue="#e0187a", nudo="#ffb3d4")
MARCA_CARAMELO = dict(cuerpo="#ff4d9a", raya="#ffffff", env_a="#ffc7e0", env_b="#ff8cc0", pliegue="#ffffff", nudo="#ff7ab8")


def fondo_icono(p, *, redondeado=True):
    radio = 'rx="232"' if redondeado else ""
    defs = f"""
    <linearGradient id="{p}bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ff7ab8"/><stop offset=".5" stop-color="#e0187a"/><stop offset="1" stop-color="#9e117a"/></linearGradient>
    <radialGradient id="{p}luz" cx="22%" cy="16%" r="70%"><stop offset="0" stop-color="#fff" stop-opacity=".42"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
    <filter id="{p}sombra" x="-50%" y="-200%" width="200%" height="500%"><feGaussianBlur stdDeviation="26"/></filter>"""
    capa = f"""
    <rect width="1024" height="1024" {radio} fill="url(#{p}bg)"/>
    <rect width="1024" height="1024" {radio} fill="url(#{p}luz)"/>
    <rect x="6" y="6" width="1012" height="1012" {'rx="226"' if redondeado else ''} fill="none" stroke="#fff" stroke-opacity=".16" stroke-width="4"/>"""
    return defs, capa


def icono(nombre, *, simple=False, redondeado=True, escala=1.0):
    d1, fondo = fondo_icono("f", redondeado=redondeado)
    d2, dulce = caramelo("c", simple=simple, **ICONO_CARAMELO)
    sombra = "" if simple else f'<ellipse cx="512" cy="{760 if escala >= 1 else 700}" rx="{215*escala:.0f}" ry="30" fill="#4a0630" fill-opacity=".3" filter="url(#fsombra)"/>'
    e = escala * (1.22 if simple else 1.12)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><defs>{d1}{d2}</defs>{fondo}{sombra}
  <g transform="translate(512 {500 if escala >= 1 else 506}) rotate(-24) scale({e:.3f})">{dulce}</g></svg>"""
    (SALIDA / nombre).write_text(svg)


def marca(nombre, colores):
    d, dulce = caramelo("m", **colores)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="-380 -380 760 760"><defs>{d}</defs>
  <g transform="rotate(-24)">{dulce}</g></svg>"""
    (SALIDA / nombre).write_text(svg)


icono("vueltito-icono.svg")
icono("vueltito-icono-chico.svg", simple=True)
icono("vueltito-icono-maskable.svg", redondeado=False, escala=.78)
icono("vueltito-icono-cuadrado.svg", redondeado=False)
marca("vueltito-caramelo.svg", MARCA_CARAMELO)
marca("vueltito-caramelo-blanco.svg", ICONO_CARAMELO)

# ---------------------------------------------------------------- logotipo
fuente = TTFont(FUENTE)
glifos = fuente.getGlyphSet()
cmap = fuente.getBestCmap()
hmtx = fuente["hmtx"]
TRACKING = -55  # el mismo -0.055em de la página
TEXTO = "vueltıto"
x = 0
trazos, cajas, i_centro = [], [], None
for letra in TEXTO:
    g = cmap[ord(letra)]
    pen = SVGPathPen(glifos)
    glifos[g].draw(TransformPen(pen, (1, 0, 0, -1, x, 0)))
    trazos.append(pen.getCommands())
    bp = BoundsPen(glifos)
    glifos[g].draw(bp)
    if bp.bounds:
        x0, y0, x1, y1 = bp.bounds
        cajas.append((x + x0, -y1, x + x1, -y0))
    if letra == "ı":
        i_centro = x + (bp.bounds[0] + bp.bounds[2]) / 2
    x += hmtx[g][0] + TRACKING
xh = fuente["OS/2"].sxHeight
# El caramelo hace de punto de la i: centrado sobre el palo, un poco más arriba que el punto real.
CARAMELO_ESCALA, CARAMELO_Y = .5, -(xh + 175)
izq = min(c[0] for c in cajas) - 20
der = max(c[2] for c in cajas) + 20
arriba = min(min(c[1] for c in cajas), CARAMELO_Y - 210) - 20
abajo = max(c[3] for c in cajas) + 20
ancho, alto = der - izq, abajo - arriba
for nombre, color in (("vueltito-logo.svg", "#1a0f15"), ("vueltito-logo-blanco.svg", "#ffffff"), ("vueltito-logo-rosa.svg", "#e0187a")):
    d, dulce = caramelo("w", **MARCA_CARAMELO) if color != "#ffffff" else caramelo("w", **ICONO_CARAMELO)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="{izq:.0f} {arriba:.0f} {ancho:.0f} {alto:.0f}"><defs>{d}</defs>
  <path fill="{color}" d="{' '.join(trazos)}"/>
  <g transform="translate({i_centro:.1f} {CARAMELO_Y:.1f}) rotate(-24) scale({CARAMELO_ESCALA})">{dulce}</g></svg>"""
    (SALIDA / nombre).write_text(svg)
print("listo", f"logo {ancho:.0f}x{alto:.0f}", "i_centro", round(i_centro), "cajas", [tuple(round(v) for v in c[::2]) for c in cajas])

# ---------------------------------------------------------------- logotipo con el lema "sin vueltas"
if len(sys.argv) > 3:
    def a_curvas(ruta, texto, escala, tracking, x, base):
        """Pasa un texto a un path SVG. Devuelve (d, caja, x final)."""
        f = TTFont(ruta)
        gs, cm, hm = f.getGlyphSet(), f.getBestCmap(), f["hmtx"]
        partes, cx0, cy0, cx1, cy1 = [], 1e9, 1e9, -1e9, -1e9
        for letra in texto:
            g = cm[ord(letra)]
            pen = SVGPathPen(gs)
            gs[g].draw(TransformPen(pen, (escala, 0, 0, -escala, x, base)))
            partes.append(pen.getCommands())
            bp = BoundsPen(gs)
            gs[g].draw(bp)
            if bp.bounds:
                b0, b1, b2, b3 = bp.bounds
                cx0, cx1 = min(cx0, x + b0 * escala), max(cx1, x + b2 * escala)
                cy0, cy1 = min(cy0, base - b3 * escala), max(cy1, base - b1 * escala)
            x += (hm[g][0] + tracking) * escala
        return " ".join(partes), (cx0, cy0, cx1, cy1), x

    SERIF = sys.argv[3]
    LETRAS = " ".join(trazos)
    # el trazo a mano de la página, estirado debajo de "vueltas"
    def trazo(x0, x1, y, alto):
        def px(v): return x0 + (x1 - x0) * v / 240
        def py(v): return y + alto * (v - 5) / 16
        return (f"M {px(4):.0f} {py(15):.0f} C {px(50):.0f} {py(5):.0f}, {px(92):.0f} {py(21):.0f}, {px(132):.0f} {py(12):.0f} "
                f"S {px(206):.0f} {py(6):.0f}, {px(236):.0f} {py(13):.0f}")

    def lema(nombre, *, apilado, blanco):
        tinta = "#ffffff" if blanco else "#1a0f15"
        d, dulce = caramelo("w", **(ICONO_CARAMELO if blanco else MARCA_CARAMELO))
        ancho_marca = der - izq - 40
        if apilado:
            esc = .74
            prueba = a_curvas(SERIF, "sin vueltas", esc, -6, 0, 0)
            inicio = izq + 20 + (ancho_marca - (prueba[1][2] - prueba[1][0])) / 2 - prueba[1][0]
            base = 760
        else:
            esc, inicio, base = 1.14, der + 230, 0
        d_sin, caja_sin, x = a_curvas(SERIF, "sin", esc, -6, inicio, base)
        x += 190 * esc
        d_vue, caja_vue, _ = a_curvas(SERIF, "vueltas", esc, -6, x, base)
        caja = (min(caja_sin[0], caja_vue[0]), min(caja_sin[1], caja_vue[1]), max(caja_sin[2], caja_vue[2]), max(caja_sin[3], caja_vue[3]))
        y_trazo = base + 110 * esc
        grosor = 36 * esc
        relleno_lema = "#ffd1e6" if blanco else "url(#lema)"
        trazo_color = "#ffffff" if blanco else "url(#lema)"
        x0 = min(izq, caja[0] - 30)
        x1 = max(der, caja[2] + 30)
        y0 = arriba
        y1 = max(abajo, y_trazo + 190 * esc)
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.0f} {y0:.0f} {x1 - x0:.0f} {y1 - y0:.0f}"><defs>{d}
    <linearGradient id="lema" gradientUnits="userSpaceOnUse" x1="{caja[0]:.0f}" y1="0" x2="{caja[2]:.0f}" y2="0"><stop offset="0" stop-color="#ff4d9a"/><stop offset=".55" stop-color="#e0187a"/><stop offset="1" stop-color="#b03bff"/></linearGradient></defs>
  <path fill="{tinta}" d="{LETRAS}"/>
  <g transform="translate({i_centro:.1f} {CARAMELO_Y:.1f}) rotate(-24) scale({CARAMELO_ESCALA})">{dulce}</g>
  <path fill="{relleno_lema}" d="{d_sin} {d_vue}"/>
  <path d="{trazo(caja_vue[0] - 10, caja_vue[2] + 10, y_trazo, 170 * esc)}" fill="none" stroke="{trazo_color}" stroke-width="{grosor:.0f}" stroke-linecap="round"{' stroke-opacity=".8"' if blanco else ''}/></svg>"""
        (SALIDA / nombre).write_text(svg)
        return x1 - x0, y1 - y0

    for nombre, apilado, blanco in (("vueltito-lema.svg", False, False), ("vueltito-lema-blanco.svg", False, True),
                                    ("vueltito-lema-apilado.svg", True, False), ("vueltito-lema-apilado-blanco.svg", True, True)):
        w, h = lema(nombre, apilado=apilado, blanco=blanco)
        print(nombre, f"{w:.0f}x{h:.0f}")
