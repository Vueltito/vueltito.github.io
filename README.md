# Vueltito · landing

La página de Vueltito: un solo `index.html` estático, sin build, servido por GitHub Pages desde la raíz de este
repo en <https://vueltito.legios.com.ar/> (también responde en <https://vueltito.github.io/>, que redirige).

```sh
python3 -m http.server 8765   # http://localhost:8765
```

Lo que dice la página sale de lo que el sistema hace hoy (los README de la base y de cada comercio). No se nombra a
ningún cliente ni se publica un canal de contacto que no exista: lo pendiente está marcado con `data-pendiente`.

## Dominio

`vueltito.legios.com.ar` es un `CNAME vueltito → vueltito.github.io` en la zona de legios en Cloudflare, con proxy
(igual que `quartermaster`; la zona está en SSL *Full*). El archivo `CNAME` de este repo le dice a Pages qué dominio
servir: si algún día se saca el registro, hay que sacar también el archivo, o Pages redirige a un dominio que no
resuelve.
