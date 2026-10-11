"""Ajustes posteriores al build del kit: cantidades de FPS en verde y columnas numericas de las tablas de rendimiento en verde.
Uso: python postbuild.py index.html
"""
import io, sys
p = sys.argv[1]
s = io.open(p, encoding="utf-8").read()
extra = """
<style>.fps{color:#5AB9A7;font-weight:700;white-space:nowrap}</style>
<script>
(function(){
  var re=/(\\d[\\d.,]*\\s*\\+?(?:\\s*(?:a|y|\\/)\\s*\\d[\\d.,]*)?\\s*FPS)/g;
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
      if(td.tagName==='TD' && /^\\s*\\d/.test(td.textContent) && !td.querySelector('.fps')) td.classList.add('fps');
    });
  });
})();
</script>
"""
if ".fps{" not in s:
    s = s.replace("</body>", extra + "</body>")
io.open(p, "w", encoding="utf-8").write(s)
print("postbuild ok")
