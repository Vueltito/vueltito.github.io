# Vueltito · landing

La página de Vueltito: un solo `index.html` estático, sin build, servido por GitHub Pages desde la raíz de este
repo en <https://vueltito.github.io/>.

```sh
python3 -m http.server 8765   # http://localhost:8765
```

Lo que dice la página sale de lo que el sistema hace hoy (los README de la base y de cada comercio). No se nombra a
ningún cliente ni se publica un canal de contacto que no exista: lo pendiente está marcado con `data-pendiente`.

## Dominio propio

Para servirla en `vueltito.legios.com.ar`: un registro `CNAME vueltito → vueltito.github.io` en Cloudflare
(proxied, como el resto del contenido estático de legios), y después un archivo `CNAME` en la raíz con ese
dominio. En ese orden: con el archivo y sin el DNS, Pages redirige a un dominio que no resuelve.
