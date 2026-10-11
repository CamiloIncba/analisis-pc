# Análisis de hardware para PC gaming en Chile (octubre 2026)

Cuatro configuraciones armadas con precios reales de tiendas chilenas (SoloTodo, 11 de octubre de 2026) y con el
rendimiento medido por Juan Isaacs (Zona Technosensual) en sus videos de 2025 y 2026.

| Gama | Objetivo | Configuración base | Total torre (CLP) |
|---|---|---|---|
| Entrada | World of Warcraft a 60+ FPS en 1080p | Ryzen 5 5500 + RX 7600 8 GB + 16 GB DDR4 | 808.070 |
| Media | AAA (Battlefield 6, Baldur's Gate 3, RDR2, GTA 6) a 144+ FPS en 1080p | Ryzen 5 7600X + RX 9070 GRE 12 GB + 16 GB DDR5 | 1.502.785 |
| Alta | Los mismos AAA a 144+ FPS en 1440p | Ryzen 7 7800X3D + RX 9070 XT 16 GB + 32 GB DDR5 | 2.587.560 |
| Estado del arte | 4K con lo mejor disponible en Chile | Ryzen 7 9850X3D + RTX 5090 32 GB + 48 GB DDR5-6000 | 7.390.875 |

Los totales son de la torre completa (sin monitor, periféricos ni Windows). El monitor recomendado va aparte en cada gama.

## 1. Fuentes y método

**Precios.** API pública de SoloTodo (`publicapi.solotodo.com`), snapshot del 11-10-2026 con 10 categorías: tarjetas de video
(211 productos con oferta en Chile), procesadores (179), placas madre (318), RAM (400), SSD (245), discos (223), fuentes (365),
gabinetes (543), coolers (510) y monitores (626). 317 tiendas registradas. Para cada componente elegido se consultaron las
tiendas que lo venden (endpoint `entities`) y se anota la más barata con stock. El precio es el "precio oferta" que publica la
tienda, que en muchas de ellas corresponde a pago con transferencia o efectivo. Los datos crudos quedan en `data/solotodo/`.

**Benchmarks.** Se revisaron los 220 videos del canal y se seleccionaron 31 de hardware de escritorio. De cada uno se bajó la
transcripción automática en español, la descripción (con la lista de componentes y enlaces a SoloTodo) y el video, del que se
extrajeron fotogramas cada 2 segundos. Un detector de gráficos de barras y revisión manual de hojas de contacto permitieron leer
los FPS exactos de cada gráfico. Todos los valores leídos están en `data/youtube/benchmarks.md`, con el ID del video y el
minuto. Los videos que sustentan este análisis:

| Video (fecha) | Qué aporta |
|---|---|
| PC por 700 lucas (11-09-2026) | RX 7600 vs RTX 5050 vs RX 9050 en 1080p ultra, 21 juegos, con Ryzen 5 5500 |
| PC de 1,5 millones (18-01-2026) | RX 9070 XT con Ryzen 5 7600, 20 juegos en 1440p y 4K ultra |
| Review RX 9070 GRE (10-08-2026) | 1440p ultra con FSR 4, 11 juegos, overlay con AVG y 1% low |
| Review RX 9060 XT 8 GB (05-06-2025) | 9060 XT vs 4060 Ti vs B580 vs RX 7600 vs 4060, 1080p y 1440p |
| PC de 500 mil versión 2025 (06-05-2025) | RTX 4060, RX 7600, RTX 3060, RX 6600 y RTX 3050 en 20 juegos a 1080p, incluye RDR2 |
| RTX 5070 Ti (18-08-2025) y RTX 5080 (13-02-2025, 07-10-2025) | 1440p y 4K con DLSS 4 y generación múltiple de frames |
| 9850X3D vs 7800X3D (12-04-2026) y review 9850X3D (28-01-2026) | Escalado de CPU en competitivos a 720p y 1080p |
| Core Ultra 5 250K Plus y 270K Plus (23-07-2026) | Alternativa Intel LGA1851, precio y rendimiento, costo de plataforma |
| Ryzen 5 8500G (18-03-2026) | Cuánto pesa la CPU a 1080p con una GPU de entrada; gráficos integrados |
| 9800X3D vs 7800X3D vs 5800X3D (11-11-2024) | Diferencia entre CPU a 1080p, 1440p y 4K con una GPU tope |
| Colusión de las RAM (17-12-2025) | Contexto del precio de la memoria y recomendación de comprar 16 GB ahora |
| Monitores GS25F2A, MO27Q28G, Odyssey OLED G8 y G6 | Monitores por gama, todos probados por el canal |

**Reglas del autor que se aplican en todas las gamas** (repetidas en varios videos): la tarjeta de video explica entre el
70 % y el 80 % de los FPS y es lo primero que se actualiza; la placa madre no agrega FPS; 16 GB de RAM alcanzan para jugar en
2026 y la ampliación a 32 GB se deja para cuando el precio se normalice; con una fuente de 650 W se parte y 750 W a 850 W dejan
margen para cambiar GPU; a 1440p y 4K el procesador deja de ser cuello de botella y a 1080p competitivo sí marca diferencia.

## 2. Contexto del mercado chileno en octubre de 2026

- **RAM.** Es el componente que distorsiona todos los presupuestos. Un módulo de 16 GB DDR5-5600 cuesta 239.995 y un kit de
  32 GB DDR5-5200 cuesta 499.900. En DDR4, 16 GB cuestan 104.990. El canal lo atribuye a la demanda de memoria HBM para centros de
  datos de IA y a que solo tres fabricantes (Samsung, SK Hynix y Micron) controlan los chips; Micron cerró Crucial.
- **Tarjetas de video.** La RX 9070 XT que costaba 759.900 en enero de 2026 hoy parte en 954.990. La RTX 5070 Ti real más barata
  con stock está en 1.163.990 y la RTX 5080 en 1.766.930. La RTX 5090 tiene 5 modelos en Chile y el más barato con tienda
  confirmada cuesta 4.269.205.
- **Gama de entrada.** La RX 7600 (318.900) sigue siendo la mejor relación precio/FPS del segmento según el ranking del propio
  canal (RX 7600 100 %, RTX 5050 93,9 %, RX 9050 91,6 %). La RTX 5050 cuesta 51.000 más y agrega DLSS 4 con multiframe.
- **Plataformas.** AM4 (Ryzen 5500, DDR4) es la vía más barata y llega hasta el 5700X3D. AM5 tiene actualización confirmada hasta
  2027 o más. LGA1851 (Core Ultra 200) rinde muy bien a 1080p pero el autor advierte que no recibirá más procesadores.

## 3. Gama de entrada: World of Warcraft a 60+ FPS en 1080p

**Lógica.** WoW exige poco de la GPU y bastante de un solo núcleo de CPU en ciudades y raids. Ninguno de los videos del canal
prueba WoW, así que el dimensionamiento se hace con los juegos más exigentes que sí midió con esta misma plataforma: con
Ryzen 5 5500 y RX 7600 en 1080p ultra, Red Dead Redemption 2 promedia 101 FPS, God of War Ragnarok 95 y Battlefield 6 109.
Un juego con el perfil de WoW queda muy por sobre los 60 FPS con calidad alta (preset 7 a 8); en raids de 20 jugadores el
límite lo pone el procesador y el 5500 se mantiene sobre 60 FPS bajando sombras y densidad de partículas. Si el presupuesto lo
permite, el Core i5-12400F (164.800) o un Ryzen 5 5600X mejoran los mínimos en raid.

| Componente | Modelo | Precio (CLP) | Tienda más barata | Enlace |
|---|---|---|---|---|
| Procesador | AMD Ryzen 5 5500 (6 núcleos, cooler incluido) | 92.900 | Notebooksya! | https://www.solotodo.cl/products/137994 |
| Placa madre | Gigabyte A520M K V2 (AM4, micro ATX) | 48.900 | DazBog Store / Sandos | https://www.solotodo.cl/products/206282 |
| Memoria | Norvm 16 GB DDR4-3200 (1 módulo) | 104.990 | Tecnomas.cl | https://www.solotodo.cl/products/401444 |
| Tarjeta de video | ASUS Dual Radeon RX 7600 EVO OC 8 GB | 318.900 | Sandos | https://www.solotodo.cl/products/270835 |
| SSD | Kingston NV3 1 TB NVMe PCIe 4.0 | 151.490 | Notebooksya! / Xtreme Components | https://www.solotodo.cl/products/253373 |
| Fuente | MSI MAG 650GN II 650 W 80 Plus Gold | 45.900 | PC Express | https://www.solotodo.cl/products/394047 |
| Gabinete | Antec VCX300 ARGB (3 ventiladores, vidrio) | 44.990 | PC Factory | https://www.solotodo.cl/products/365008 |
| **Total torre** | | **808.070** | | |

**Monitor sugerido (aparte):** Gigabyte GS24F14A 24" 1080p 175 Hz IPS, 79.900 en PC Express. Si se quiere el que el canal
revisó para competitivo, Gigabyte GS25F2A 25" 240 Hz, 92.900 en Sandos.

**Rendimiento esperado (medido por el canal con Ryzen 5 5500 + RX 7600, 1080p, calidad ultra, FSR calidad + generación de frames, RT activo):**

| Juego | FPS promedio / 1% low | Video |
|---|---|---|
| Red Dead Redemption 2 (FSR, sin FG) | 101 / 74 | PC 500 mil 2025 |
| Battlefield 6 | 109 / 65 | PC 700 lucas |
| God of War Ragnarok | 95 / 76 | PC 500 mil 2025 |
| The Last of Us Part II | 92 / 77 | PC 700 lucas |
| Doom The Dark Ages | 101 / 76 | PC 700 lucas |
| Counter Strike 2 (alta) | 201 / 110 | PC 700 lucas |
| Valorant (alta) | 335 / 112 | PC 700 lucas |
| Spider-Man 2 con RT | 33 / 26 (71 sin RT) | PC 700 lucas |

**Alternativas.**
- Nvidia: Gigabyte RTX 5050 Windforce OC 8 GB, 369.990 (Eylstore / Tecnomas.cl). Total 859.160. Mismo rendimiento promedio
  (93,9 % del ratio precio/FPS de la 7600) con DLSS 4 multiframe (252 FPS en 007 First Light con DLSS x6).
- Sin tarjeta de video, plataforma AM5 con gráficos integrados: Ryzen 5 8500G (134.990, UG Store) + ASUS Prime A620M-K (69.900,
  Sandos) + 16 GB DDR5-4800 A-DATA (228.990, Tecnomas.cl) + los mismos SSD, fuente y gabinete. Total 676.260. El canal midió con
  los gráficos integrados del 8500G Counter Strike 2 sobre 100 FPS en media, Overwatch 2 entre 70 y 80, Battlefield 6 en 50 FPS
  en baja. Para WoW a 60 FPS obliga a calidad media o baja en raids; su ventaja es que después recibe cualquier GPU y cualquier
  Ryzen 7000/9000.
- Intel: Core i5-12400F (164.800, Nice One) + ASUS Prime H610M-K (59.900, PC Express). Suma 82.900 sobre la base AM4 y da más
  margen de CPU (hasta i7-14700) con la misma DDR4.
- Para rebajar: gabinete Cougar MX110 RGB 32.970 (MyShop) y RAM Norvm MEM16G32PL 87.500 (sin tienda confirmada hoy).

## 4. Gama media: AAA a 144+ FPS en 1080p

**Lógica.** Para sostener 144 FPS en títulos como Battlefield 6 y Red Dead Redemption 2 en 1080p con calidad alta o ultra se
necesita una GPU de la clase RX 9070 GRE o superior y un procesador AM5 actual. La evidencia: la RX 9060 XT de 8 GB, un escalón
más abajo, queda en 1080p ultra con reescalado y FG en 172 FPS en Doom The Dark Ages y 231 en Delta Force, pero en 91 en
Expedition 33, 69 en Assassin's Creed Shadows y 52 en Spider-Man 2 por falta de VRAM. La RX 9070 GRE de 12 GB, medida por el
canal en 1440p ultra con FSR 4 calidad y FG, entrega 155 FPS en Battlefield 6, 155 en God of War Ragnarok, 225 en The Last of
Us Part II, 158 en Pragmata, 134 en Resident Evil Requiem y 258 en Overwatch 2; en 1080p esos valores suben y el límite pasa a
ser la CPU. Baldur's Gate 3 depende de la CPU en el acto 3 (ciudad), por eso se elige un Ryzen 7000 de 6 núcleos a 5,3 GHz en
vez de un AM4. GTA 6 aún no tiene versión de PC ni requisitos publicados; la configuración queda con 12 GB de VRAM, PCIe 4.0 y
socket AM5 para absorberlo con una actualización de GPU si hiciera falta.

| Componente | Modelo | Precio (CLP) | Tienda más barata | Enlace |
|---|---|---|---|---|
| Procesador | AMD Ryzen 5 7600X (6 núcleos, 5,3 GHz, sin cooler) | 179.990 | Xtreme Components | https://www.solotodo.cl/products/151869 |
| Cooler | Thermalright Assassin X 120 Refined SE ARGB | 23.900 | Centrale | https://www.solotodo.cl/products/158446 |
| Placa madre | MSI B840M Gaming WiFi 6E (AM5, micro ATX, 2 M.2) | 109.440 | Winpy | https://www.solotodo.cl/products/356069 |
| Memoria | Kingston 16 GB DDR5-5600 (1 módulo) | 239.995 | SP Digital | https://www.solotodo.cl/products/252385 |
| Tarjeta de video | Gigabyte Radeon RX 9070 GRE Gaming OC 12 GB | 689.990 | DazBog Store / Progaming | https://www.solotodo.cl/products/406331 |
| SSD | Kingston NV3 1 TB NVMe PCIe 4.0 | 151.490 | Notebooksya! / Xtreme Components | https://www.solotodo.cl/products/253373 |
| Fuente | be quiet! Pure Power 12 750 W 80 Plus Gold | 62.990 | Dust2 | https://www.solotodo.cl/products/358155 |
| Gabinete | Antec VCX300 ARGB | 44.990 | PC Factory | https://www.solotodo.cl/products/365008 |
| **Total torre** | | **1.502.785** | | |

El 7600X cuesta 36.910 menos que el Ryzen 5 7600 con cooler (216.900) y es más rápido; con el cooler de 23.900 sigue siendo más
barato. El canal usó la misma placa B840M en el PC de 1,5 millones y comprobó que a 1440p y 4K el Ryzen 5 7600 no limita ni a
una RX 9070 XT.

**Monitor sugerido (aparte):** Gigabyte GS25F2A 25" 1080p 240 Hz IPS, 92.900 en Sandos. Es el que el canal usó para explicar por
qué 1080p sigue siendo el estándar competitivo. Si se prefiere 27", Xiaomi G27i 2026 1080p 165 Hz, 114.990 en Notebooksya!.

**Rendimiento esperado (medido por el canal con la RX 9070 GRE en 1440p; en 1080p los valores suben):**

| Juego (1440p ultra, FSR 4 calidad + FG) | FPS promedio / 1% low |
|---|---|
| Battlefield 6 | 155 / 53 |
| God of War Ragnarok | 155 / 101 |
| The Last of Us Part II | 225 / 174 |
| Resident Evil Requiem | 134 / 90 |
| Pragmata | 158 / 130 |
| The Finals | 230 / 170 |
| Overwatch 2 | 258 / 221 |
| Counter Strike 2 | 395 a 457 |
| Doom The Dark Ages (nativo, RT, sin reescalado) | 76 (171 con FSR + FG) |

Advertencia del propio video: en Battlefield 6 a 1440p ultra la GRE superó sus 12 GB de VRAM (12,4 GB usados), lo que explica
el 1% low de 53. En 1080p ese problema desaparece.

**Alternativas.**
- Nvidia: Gigabyte RTX 5070 Eagle OC SFF 12 GB, 899.990 (PC Factory). Total 1.712.785. Suma DLSS 4 con multiframe x4 y mejor
  comportamiento con path tracing.
- Más barata: ASUS Dual RX 9060 XT 16 GB, 549.990 (MyShop). Total 1.362.785. Rinde cerca de 20 % menos que la GRE; sostiene
  144 FPS en competitivos y en varios AAA con FSR + FG, con 16 GB de VRAM que la GRE no tiene.
- RAM: cuando el mercado se normalice, kit Corsair Vengeance RGB 32 GB DDR5-5200 (499.900 hoy en Natcom) o un segundo módulo igual.
- Placa con PCIe 5.0 para la GPU: MSI PRO B850M-B GEN4 112.480 (Winpy) o Biostar B850MT2-E 117.990.

## 5. Gama alta: AAA a 144+ FPS en 1440p

**Lógica.** El canal midió exactamente este objetivo con la RX 9070 XT y un Ryzen 5 7600 (PC de 1,5 millones): 270 FPS en
Battlefield 6, 242 en God of War Ragnarok, 244 en The Last of Us Part II, 201 en Horizon Forbidden West, 201 en Space Marine 2 y
171 en The Finals, todo en 1440p ultra con FSR y generación de frames. Red Dead Redemption 2 queda en 123 FPS en ultra (el juego
no tiene generación de frames); en calidad alta supera los 144. Los únicos títulos bajo 100 son los que usan path tracing
(Cyberpunk 82, Wukong 97, Doom 64, Alan Wake 2 58), que ninguna GPU por debajo de la RTX 5080 mueve a 144 FPS.
Para esta gama se sube el procesador al Ryzen 7 7800X3D: a 1440p la diferencia con un 7600 es pequeña en promedios, pero el
3D V-Cache mejora los mínimos y es la CPU que hace que Baldur's Gate 3 y los competitivos escalen a 144+ en todo momento. El
9850X3D rinde entre 4 % y 6 % más a 1440p (medición del canal con RTX 4090 y 9800X3D) por 120.000 adicionales.

| Componente | Modelo | Precio (CLP) | Tienda más barata | Enlace |
|---|---|---|---|---|
| Procesador | AMD Ryzen 7 7800X3D (8 núcleos, 96 MB L3) | 429.990 | Xtreme Components | https://www.solotodo.cl/products/200671 |
| Cooler | Deepcool AK400 (torre 120 mm) | 37.990 | DazBog Store | https://www.solotodo.cl/products/155066 |
| Placa madre | ASRock X870 Pro RS (AM5, ATX, PCIe 5.0, USB4) | 237.900 | Nice One | https://www.solotodo.cl/products/256193 |
| Memoria | Corsair Vengeance RGB 32 GB (2 x 16) DDR5-5200 | 499.900 | Natcom | https://www.solotodo.cl/products/149227 |
| Tarjeta de video | ASUS Prime Radeon RX 9070 XT OC 16 GB | 954.990 | PC Factory | https://www.solotodo.cl/products/276343 |
| SSD | Kingston NV3 2 TB NVMe PCIe 4.0 | 266.990 | Tecnomas.cl | https://www.solotodo.cl/products/279707 |
| Fuente | MSI MAG A850GN PCIE5 850 W 80 Plus Gold | 69.900 | PC Express | https://www.solotodo.cl/products/394045 |
| Gabinete | Airflow Roble Artis Black/Wood (4 ventiladores, USB-C) | 89.900 | Nice One | https://www.solotodo.cl/products/367704 |
| **Total torre** | | **2.587.560** | | |

**Monitor sugerido (aparte):** Samsung Odyssey G5 G53F 27" 1440p 200 Hz IPS, 144.990 en Tecnomas.cl. Opción OLED probada por el
canal y recomendada sin reparos: Gigabyte MO27Q28G 27" 1440p 280 Hz Tandem WOLED, 549.900 en Sandos.

**Rendimiento esperado (medido por el canal con RX 9070 XT + Ryzen 5 7600, 1440p ultra, FSR + FG):**

| Juego | 1440p | 2160p (referencia) |
|---|---|---|
| Battlefield 6 | 270 | 121 |
| Red Dead Redemption 2 | 123 | 61 |
| God of War Ragnarok | 242 | 174 |
| The Last of Us Part II Remastered | 244 | 161 |
| Horizon Forbidden West | 201 | 80 |
| Warhammer 40K Space Marine 2 | 201 | 118 |
| Marvel Rivals | 163 | 92 |
| The Finals | 171 (315 en 1080p) | 84 |
| Counter Strike 2 | 224 (380 en 1080p) | 192 |
| Cyberpunk 2077 con path tracing | 82 | 38 (72 sin PT) |
| Doom The Dark Ages con path tracing | 64 | 42 (70 sin PT) |

**Alternativas.**
- Nvidia: Gigabyte RTX 5070 Ti Windforce OC SFF 16 GB, 1.163.990 (Dust2). Total 2.796.560. El canal la llama "la más sensata":
  en 1440p con DLSS 4 calidad y multiframe x4 entrega 280 FPS en Doom The Dark Ages con full RT, 149 en Wukong cinematográfico y
  cerca de 200 en Cyberpunk con todo en ultra; The Finals 400 FPS. Es la opción si se quiere path tracing a 144 FPS.
- CPU más barata: Ryzen 7 9700X 329.990 (Xtreme Components), 100.000 menos, con render de video 30 % más rápido que el 7800X3D y
  algunos FPS menos en competitivos. Intel: Core Ultra 5 250K Plus 284.544 (Winpy) + MSI PRO Z890-S WiFi 242.990; el canal lo
  recomienda por precio, pero la plataforma Intel completa le salió 190.000 más cara que AM4 y no tendrá más CPU.
- RAM: con un solo módulo de 16 GB DDR5-5600 (239.995) el total baja a 2.327.655 y se completa después.
- Placa con WiFi: ASRock X870 Pro RS WiFi 254.990, o micro ATX MSI PRO B850M-B GEN4 112.480 si no se usará USB4.

## 6. Estado del arte: 4K con lo mejor que se vende en Chile

**Lógica.** La única GPU que promedia sobre 144 FPS en 4K es la RTX 5090: 151 FPS de media en 15 juegos (Cyberpunk, Elden Ring,
Horizon, Alan Wake 2, Doom Eternal, Ghost of Tsushima, Starfield, Baldur's Gate 3, Counter Strike 2 y otros), frente a 112 de la
RTX 4090 y 101 de la RTX 5080, según los gráficos que el canal reprodujo en su review de la 5080. En Cyberpunk 4K con RT ultra y
reescalado calidad da 80 FPS (64 en 1% low) y con DLSS 4 multiframe supera los 200. La RTX 5080 es el "4K sensato": el canal
la probó en Doom The Dark Ages 4K con 86 FPS nativos, 139 con DLSS calidad + FG x4 y 157 a 170 con DLSS rendimiento x4, y en
Cyberpunk, Alan Wake 2 y Hogwarts Legacy sobre 100 FPS con path tracing y DLSS 4. El procesador es el Ryzen 7 9850X3D, hoy el más
rápido para juegos según todas las pruebas del canal; a 4K la diferencia con un 7800X3D es de 2 % a 6 %, pero en esta gama el
objetivo es no dejar nada sobre la mesa y tener los mejores mínimos. La memoria se lleva a 48 GB DDR5-6000 CL36, que es el
punto óptimo de AM5 que el canal usa en su banco de pruebas, y el almacenamiento a 4 TB PCIe 5.0.

| Componente | Modelo | Precio (CLP) | Tienda más barata | Enlace |
|---|---|---|---|---|
| Procesador | AMD Ryzen 7 9850X3D (8 núcleos, 3D V-Cache 2ª gen.) | 549.900 | Sandos | https://www.solotodo.cl/products/382839 |
| Cooler | Thermalright Frozen Magic 360 Digital ARGB V2 (AIO 360) | 71.990 | TYT Gamer Chile | https://www.solotodo.cl/products/280233 |
| Placa madre | Gigabyte X870E AORUS Elite WiFi 7 (AM5, ATX, PCIe 5.0 x16 + M.2 Gen5, USB4) | 349.990 | MegaBytes / MegaDrive | https://www.solotodo.cl/products/256222 |
| Memoria | Corsair Vengeance 48 GB (2 x 24) DDR5-6000 CL36 | 799.990 | MyShop | https://www.solotodo.cl/products/382889 |
| Tarjeta de video | Gigabyte AORUS GeForce RTX 5090 Stealth Ice 32 GB | 4.269.205 | Invasión Gamer (SoloTodo referencia 4.035.110) | https://www.solotodo.cl/products/395177 |
| SSD | Kingston FURY Renegade G5 4 TB PCIe 5.0 (14.800 MB/s) | 944.900 | Centrale | https://www.solotodo.cl/products/273935 |
| Fuente | be quiet! Pure Power 13 M 1200 W 80 Plus Gold, ATX 3.1, 12V-2x6 | 155.900 | Sandos | https://www.solotodo.cl/products/385343 |
| Gabinete | Hyte Y70 (panel envolvente, GPU vertical) | 249.000 | Nice One | https://www.solotodo.cl/products/259907 |
| **Total torre** | | **7.390.875** | | |

**Monitor sugerido (aparte):** Samsung Odyssey OLED G8 G81SF 32" 4K 240 Hz, 899.990 (Falabella, Paris y Ripley Marketplace).
El canal lo califica como "probablemente el mejor panel 4K de 32 pulgadas que te puedes comprar" y destaca que es el más barato
con esas especificaciones en SoloTodo. Opción IPS: MSI MAG 321UPD 32" 4K 144 Hz, 408.990 en MyShop.

**Rendimiento esperado en 4K (datos citados por el canal para la RTX 5090):** media de 15 juegos 151 FPS; Cyberpunk 2077 RT
ultra 80 / 64; Black Myth Wukong very high RT 62 / 50; Spider-Man Remastered RT 128; con DLSS 4 multiframe todos superan los
144 FPS salvo los escenarios de path tracing completo. Para Battlefield 6, Baldur's Gate 3 y Red Dead Redemption 2 en 4K ultra,
la referencia medida por el canal con la RX 9070 XT (121, no medido y 61 FPS) se multiplica por 2,2 a 2,5 según la media
comparativa (151 vs 87 FPS de la RX 7900 XTX, que rinde como la 9070 XT en raster).

**Alternativas.**
- "4K sensato": MSI RTX 5080 Inspire 3X OC 16 GB, 1.766.930 (SIPO). Total 4.888.600. Con DLSS 4 sostiene 100 a 170 FPS en 4K en
  los juegos probados; en raster puro rinde 10 % más que una 4080 Super.
- Procesador para trabajo y juego: Ryzen 9 9950X3D, 776.990 (Tecnomas.cl), 16 núcleos con 3D V-Cache.
- Placa que el canal usa en su banco: Gigabyte X870E AORUS Elite X3D, 439.000 (Nice One).
- RAM 64 GB: Kingston Fury Beast RGB 2 x 32 DDR5-5600, 1.191.343 (KDTEC).
- Almacenamiento: Kingston NV3 4 TB PCIe 4.0, 543.990 (Tecnomas.cl), 400.000 menos sin impacto en FPS.
- ASUS ROG Astral RTX 5090 OC, 5.915.232 (Winpy), para quien quiera el modelo tope de refrigeración y silencio.

## 7. Camino de actualización de cada pack

La vía de actualización depende de la plataforma. AM4 con DDR4 es la más barata para entrar, pero el procesador tiene techo
y la memoria DDR4 ya no recibe nuevos productos. AM5 con DDR5 tiene actualización de CPU confirmada por AMD hasta 2027 o más,
por eso las gamas media, alta y estado del arte comparten socket y pueden escalar sin cambiar placa ni memoria.

| Pack | Siguiente paso de GPU | Techo de CPU en la misma placa | RAM | Qué obliga a cambiar la plataforma |
|---|---|---|---|---|
| Entrada (AM4, DDR4) | RX 9060 XT 16 GB (549.990) o RX 9070 GRE (689.990) con la fuente de 650 W; RX 9070 XT (954.990) exige fuente de 750 W. La A520M es PCIe 3.0 x16, que el canal comprobó suficiente incluso para una 9070 XT. | Ryzen 7 5700X (228.310) o Ryzen 7 5800X3D (437.900). Es un socket cerrado: el 5800X3D cuesta más que un 7600X con placa AM5, por eso el salto de CPU conviene hacerlo cambiando de plataforma. | Segundo módulo de 16 GB DDR4 (104.990) para llegar a 32 GB en doble canal. | Cuando se quiera una CPU superior al 5800X3D: placa AM5 (109.440) + Ryzen 5 7600X (179.990) + 16 GB DDR5 (239.995), cerca de 530.000, reutilizando GPU, SSD, fuente y gabinete. |
| Media (AM5, B840M) | RX 9070 XT (954.990) con la misma fuente de 750 W; RTX 5070 Ti (1.163.990) o RTX 5080 (1.766.930) con fuente de 850 W. PCIe 4.0 x16 y dos M.2. | Ryzen 7 7800X3D (429.990) o Ryzen 7 9850X3D (549.900), previa actualización de BIOS. Zen 6 se anunció para AM5. | Segundo módulo de 16 GB DDR5-5600 (239.995) para 32 GB. | Nada en el horizonte de 3 a 4 años; la placa es micro ATX y sin PCIe 5.0, que hoy no cambia los FPS. |
| Alta (AM5, X870) | RTX 5080 (1.766.930) con la fuente de 850 W; RTX 5090 (4.269.205) exige fuente de 1.000 a 1.200 W con conector 12V-2x6. PCIe 5.0 x16, USB4. | Ryzen 7 9850X3D (549.900) o Ryzen 9 9950X3D (776.990) para trabajo y juego. | Kit de 2 x 32 GB (1.191.343) para 64 GB; los cuatro zócalos admiten combinar con el kit actual a menor frecuencia. | Nada; la placa cubre GPU y SSD de próxima generación. |
| Estado del arte (AM5, X870E) | Próxima generación Nvidia o AMD por PCIe 5.0, con la fuente de 1.200 W ya dimensionada. | Cualquier Ryzen AM5 futuro (Zen 6) con actualización de BIOS. | 96 GB (2 x 48) o 128 GB (4 x 32) para trabajo profesional. | Nada; cuatro M.2 (uno Gen5), USB4 y WiFi 7 ya incluidos. |

Orden de actualización recomendado por el canal y aplicable a las cuatro gamas: primero la tarjeta de video (explica 70 % a 80 %
de los FPS), después el procesador, luego RAM y almacenamiento, y al final placa y fuente. Al cambiar de GPU conviene revisar
el largo máximo del gabinete (todos los elegidos admiten tarjetas de 360 mm o más) y la potencia de la fuente.

## 8. Comparativa y recomendaciones transversales

| | Entrada | Media | Alta | Estado del arte |
|---|---|---|---|---|
| Total torre | 808.070 | 1.502.785 | 2.587.560 | 7.390.875 |
| Con monitor sugerido | 887.970 | 1.595.685 | 2.732.550 | 8.290.865 |
| Plataforma | AM4, DDR4 | AM5, DDR5 | AM5, DDR5 | AM5, DDR5 |
| VRAM | 8 GB | 12 GB | 16 GB | 32 GB |
| RAM | 16 GB | 16 GB | 32 GB | 48 GB |
| Fuente | 650 W Gold | 750 W Gold | 850 W Gold | 1200 W Gold ATX 3.1 |
| Vía de actualización | Hasta Ryzen 5700X3D y GPU de hasta 250 W | Cualquier Ryzen 7000/9000 y GPU hasta 300 W | Cualquier Ryzen 9000 y GPU hasta 360 W | Completa |

- **Comprar pronto y en pocas tiendas.** El canal recomienda cotizar y decidir rápido mientras la RAM sigue subiendo, y
  concentrar la compra en una o dos tiendas para reducir despachos y para pedir la actualización de BIOS de la placa AM5 al
  momento de comprarla (obligatoria para Ryzen 9000 en placas B840/B850/X870 con firmware antiguo).
- **Stock.** Los precios de SoloTodo cambian a diario; cada fila tiene el enlace al producto para verificar antes de pagar.
  Varias ofertas corresponden a pago con transferencia.
- **RAM.** En las gamas de entrada y media se parte con 16 GB en un módulo para dejar el segundo zócalo libre; el canal
  comprobó que 16 GB bastan para los 20 títulos probados y pide esperar a que baje el precio para pasar a 32 GB.
- **Monitores.** La tasa de refresco debe acompañar a los FPS: 165 a 240 Hz en 1080p, 200 a 280 Hz en 1440p y 144 a 240 Hz en 4K.
  Un monitor 4K de 240 Hz solo se aprovecha con la RTX 5090 o la 5080 con DLSS 4.
- **GTA 6.** Sin versión de PC anunciada ni requisitos publicados a la fecha; las gamas media y alta quedan con socket AM5 y
  fuente con margen para absorber un cambio de GPU cuando se conozcan.

## 9. Anexos y cómo actualizar

- Página publicada: https://camiloincba.github.io/analisis-pc/ (repositorio CamiloIncba/analisis-pc; se genera desde `site/propuesta.json` con la skill propuesta-web del incba-kit).
- `data/youtube/benchmarks.md`: todos los FPS leídos de los gráficos, por video, con condiciones de prueba.
- `data/youtube/text/<id>.md`: transcripción y descripción de cada uno de los 31 videos; `_indice.md` resume fechas y títulos.
- `data/youtube/frames/<id>/charts_sheets/`: hojas de contacto con los gráficos detectados en cada video.
- `data/solotodo/*.json`: snapshot completo de precios por categoría; `_resumen.txt` y `_candidatos.md` son las vistas usadas.
- Scripts en `scripts/`: `solotodo_snapshot.py` (descarga), `solotodo_resumen.py`, `solotodo_candidatos.py` (tabla con tiendas),
  `yt_transcripts.py`, `yt_charts.py` (detector de gráficos), `yt_peek.py` (fotogramas en instantes dados), `yt_charts_all.sh`.

Para refrescar precios:

```bash
cd C:/Proyectos/PC-GAMING && python -X utf8 -I scripts/solotodo_snapshot.py && python -X utf8 -I scripts/solotodo_candidatos.py > data/solotodo/_candidatos.md
```
