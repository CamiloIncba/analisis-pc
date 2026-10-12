"""Ajustes posteriores al build del kit:
- "Para tener en cuenta" pasa a ser un parrafo y una fila dentro del Resumen (no una seccion aparte).
- Los enlaces internos de las galerias abren en la misma pestaña.
- Cantidades de FPS en verde y columnas numericas de las tablas de rendimiento en verde.
Uso: python postbuild.py index.html
"""
import io, re, sys

p = sys.argv[1]
s = io.open(p, encoding="utf-8").read()

CSS = (".section-sub{margin-top:48px;padding-top:28px;border-top:1px solid var(--tone-border)}"
       ".section-sub h3{font-family:var(--font-display);font-size:22px;font-weight:700;margin:0 0 8px;color:var(--tone-fg)}"
       ".section-sub p{font-size:15px;line-height:1.6;color:var(--tone-muted);margin:0 0 22px;max-width:760px}"
"#resumen .gallery{gap:14px}#resumen .gallery-img{aspect-ratio:16/7}#resumen .gallery-text{padding:10px 12px 12px;gap:3px}"
       "#resumen .gallery-text strong{font-size:14px}#resumen .gallery-text>span{font-size:12.5px;line-height:1.4}#resumen .gallery-cta{font-size:12px;margin-top:2px}"
       "#resumen .gallery.cols-2{max-width:calc(66.666% - 5px)}#resumen .section-sub{margin-top:26px;padding-top:18px}#resumen .section-sub h3{font-size:18px}"
       "#resumen .section-sub p{font-size:14px;margin:0 0 14px}#resumen .section-subtitle{margin-bottom:14px}"
       "@media(max-width:980px){#resumen .gallery.cols-2{max-width:none}#resumen .gallery-img{aspect-ratio:16/9}}"
       ".fps{color:#5AB9A7;font-weight:700;white-space:nowrap}")

JS = r"""
(function(){
  var re=/(\d[\d.,]*\s*\+?(?:\s*(?:a|y|\/)\s*\d[\d.,]*)?\s*FPS)/g;
  function wrap(node){
    if(node.nodeType===3){
      if(!re.test(node.nodeValue)) return; re.lastIndex=0;
      var span=document.createElement('span');
      span.innerHTML=node.nodeValue.replace(/[&<>]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c];}).replace(re,'<span class="fps">$1</span>');
      node.parentNode.replaceChild(span,node);
    } else if(node.nodeType===1 && !/^(SCRIPT|STYLE)$/.test(node.tagName) && !node.classList.contains('fps')){
      Array.prototype.slice.call(node.childNodes).forEach(wrap);
    }
  }
  wrap(document.body);
  /* tablas de rendimiento: toda celda numerica (salvo la primera columna) es una cantidad de FPS */
  document.querySelectorAll('section[id$="-fps"] table tr').forEach(function(tr){
    Array.prototype.slice.call(tr.children).slice(1).forEach(function(td){
      if(td.tagName==='TD' && /^\s*\d/.test(td.textContent) && !td.querySelector('.fps')) td.classList.add('fps');
    });
  });
})();
"""

# 1. fusionar "Para tener en cuenta" dentro del Resumen
m = re.search(r'<section class="section" id="tener-en-cuenta">\s*<div class="inner reveal">(.*?)</div>\s*</section>', s, re.S)
if m:
    inner = m.group(1)
    tag = re.search(r'<div class="section-tag">(.*?)</div>', inner, re.S).group(1)
    sub = re.search(r'<p class="section-subtitle">(.*?)</p>', inner, re.S).group(1)
    cuerpo = inner[inner.index('<div class="gallery'):]
    bloque = '<div class="section-sub"><h3>' + tag + '</h3><p>' + sub + '</p></div>\n' + cuerpo
    s = s[:m.start()] + s[m.end():]
    r = re.search(r'(<section class="section light" id="resumen">.*?)(\s*</div>\s*</section>)', s, re.S)
    s = s[:r.end(1)] + '\n' + bloque + s[r.end(1):]

# 2. enlaces internos de las galerias en la misma pestaña
s = re.sub(r'(<a class="gallery-item" href="#[^"]*") target="_blank" rel="noopener"', r'\1', s)

# 3. estilos y script
if ".fps{" not in s:
    s = s.replace("</body>", "\n<style>" + CSS + "</style>\n<script>" + JS + "</script>\n</body>")

io.open(p, "w", encoding="utf-8").write(s)
print("postbuild ok")
