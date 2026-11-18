# แหล่งอ้างอิง

แหล่งด้านล่างรองรับเฉพาะประเด็นที่ระบุ โจทย์คำนวณและตัวเลขตัวอย่างเป็นข้อมูลสมมติของผู้จัดทำ ส่วนเรื่องเปิดบทนำ (EP 0) เป็นประสบการณ์ที่ผู้จัดทำเล่า ข้อมูลบรรณานุกรมและส่วนที่ใช้ตรวจอ่านเมื่อ 17 พฤศจิกายน 2026 ยกเว้นบทที่ 2 (EP 2) ซึ่งตรวจอ่านเมื่อ 18 พฤศจิกายน 2026

## บทนำ (EP 0) — SRAD, NRAD และชนิดเซ็นเซอร์วัดรังสี

[เปิดบทนำ](chapters/00/README.md) · [เรียนผ่านภาพ](chapters/00/visual-guide.md) · [ชนิดเซ็นเซอร์และ Class](chapters/00/sensor-types.md)

### หน่วยงานไทย

- [กรมควบคุมมลพิษ — ประกาศข้อกำหนดการปฏิบัติงานและโครงสร้างข้อมูลตามกรอบการกำกับดูแลข้อมูล เรื่อง การกำกับดูแลข้อมูลจากสถานีตรวจวัดอัตโนมัติด้านคุณภาพอากาศ](https://epo14.pcd.go.th/th/download/?file=oHM3ERkDoF5aAKD3nGE4BKN3oGO3Z0j3oGOaZUD4nGM4ZKNmoGO3BHjloGAaZaDjnGW4YKNmoGW3Z0jmoGMaZUDmnGq4ZUNjoGu3AxjkoGAaZUD5nGW4Z3NloGO3ZxjgoJIaoUEcnJM4Y3OyoJk3nHkzoF9aqKEcnGM4AaNkoF93MRkuoJ9aoUEjnKI4YjWewEb3QWewEb3Q&n=8E8F~1&t=GTMgq2qxqS9cMUug) — ตรวจตาราง Attribute แถว SRAD และ NRAD: ค่ารังสีดวงอาทิตย์และค่ารังสีสุทธิ โดยแสดงหน่วย w/m2 ทั้งคู่ บทเรียนปรับรูปแบบหน่วยเป็น W/m² ตาม SI เอกสารเผยแพร่ผ่าน [สำนักงานสิ่งแวดล้อมและควบคุมมลพิษที่ 14](https://epo14.pcd.go.th/th/information/more/1425/page/2)
- [สถาบันมาตรวิทยาแห่งชาติ — ศัพท์มาตรวิทยาระหว่างประเทศ (VIM) ฉบับไทย–อังกฤษ, JCGM 200:2008 (En/Th)](https://mx.nimt.or.th/wp-content/uploads/2020/06/6.VIM-3rd-Edition_E-TH.pdf) — ข้อ 2.3 หน้าเอกสาร 21 (หน้าไฟล์ PDF 36) เรื่องสิ่งที่เจตนาวัด ใช้ประกอบการแยกปริมาณก่อนอ่านค่า

ชื่อช่องและหน่วยตามเอกสาร คพ. ใช้อธิบายโครงสร้างข้อมูลในเอกสารนั้น ไม่ยืนยันรุ่นเครื่องมือ ช่วงคลื่น กติกาเครื่องหมาย หรือช่วงเฉลี่ยของสถานีตรวจวัดที่ผู้จัดทำเคยพบ รายการตรวจบริบทและตัวอย่างประโยครายงานเป็นข้อเสนอเพื่อการสอนของผู้จัดทำ

### แหล่งสากล

- [FAO, Irrigation and Drainage Paper 56, Chapter 3 — Meteorological data](https://www.fao.org/4/X0490E/x0490e07.htm) — หัวข้อ Net radiation อธิบายสมดุลรังสีเข้าและออกที่รวมคลื่นสั้นและคลื่นยาว ใช้อธิบายหลักการรังสีสุทธิ ไม่ใช้รับรองรายละเอียดของช่อง NRAD ในระบบใดระบบหนึ่ง
- [JCGM Annotated VIM3 ข้อ 2.3](https://jcgm.bipm.org/vim/en/2.3.html) — ปริมาณที่ตั้งใจวัดหรือ measurand

### เครื่องมือและภาพประกอบ

- [Hukx — Solar radiation sensors: become a pyranometer expert](https://www.hukx.com/us/library/solar-radiation-sensors-become-a-pyranometer-expert) — หัวข้อ The physics behind thermopile pyranometers: ผิวดูดกลืนรังสี ความต่างอุณหภูมิ และแรงดันของ thermopile
- [Apogee — คู่มือ SP-212/SP-215](https://www.apogeeinstruments.com/content/SP-212-215-manual.pdf) — หน้า 5 และ 9: diffuser, photodiode, วงจร และการตอบสนองตามความยาวคลื่น; [หน้ากลุ่ม silicon-cell](https://www.apogeeinstruments.com/silicon-cell-pyranometers/) ใช้ดูรูปและตัวเลือกเอาต์พุต; [หน้ากลุ่ม pyranometer](https://www.apogeeinstruments.com/pyranometer/) ใช้ตัวอย่างว่าผู้ผลิตมีทั้ง silicon-cell และ thermopile ที่ระบุ Class C
- [IMT — Silicon Irradiance Sensors for Measurement of Solar Irradiance](https://imt-technology.com/fileadmin/docs/en/products/DS_Si-Sensors_EN_2024-06.pdf) — หน้า 2–3: เซลล์ซิลิคอนกับ shunt การสอบเทียบและชดเชยอุณหภูมิตามรุ่น โครงสร้างคล้ายโมดูล PV และอินเทอร์เฟซ ข้อมูลนี้อธิบายเครื่องมือของผู้ผลิต ไม่ยืนยันรุ่นในภาพจาก Commons หรือรุ่นในประสบการณ์ผู้เล่า
- [ISO 9060:2018](https://www.iso.org/standard/67464.html) — ขอบเขตการจัดประเภทเครื่องมือและสถานะยืนยันมาตรฐานในปี 2024; [Hukx — ISO 9060 pyranometer classification หน้า 1–3](https://www.hukx.com/uploads/ISO-9060-pyranometer-classification.pdf?v=1765534259) — Class A/B/C และคุณสมบัติเพิ่มเติม spectrally flat/fast response ไม่ใช้แทนการประเมินความไม่แน่นอนรายระบบ
- [Hukseflux — NR01 brochure หน้า 2–3](https://www.hukseflux.com/uploads/product-documents/NR01_v2301.pdf) — องค์ประกอบรังสีสี่ส่วน ได้แก่ คลื่นสั้นเข้า–ออกและคลื่นยาวเข้า–ออก การใช้ pyranometer วัดคลื่นสั้นและ pyrgeometer วัดคลื่นยาว และการคำนวณรังสีสุทธิของเครื่องมือตัวอย่าง
- [NovaLynx Corporation — 240-8110 Net Radiometer, หน้าไฟล์ PDF 1](https://novalynx.com/brochures/240-8110.pdf) — แหล่งภาพรูปลักษณ์ที่ผู้จัดทำเลือกเทียบกับเครื่องที่เคยซ่อมบำรุง และข้อมูลโดม Lupolene, silica gel กับสัญญาณรังสีสุทธิของรุ่นตัวอย่าง ไม่ยืนยันรุ่นหรือการต่อช่อง SRAD/NRAD ของระบบเดิม สิทธิ์ภาพคงตามเจ้าของต้นฉบับ
- ภาพถ่าย [SR11](https://commons.wikimedia.org/wiki/File:Hukseflux_radiometer_sr11_photo.jpg) และ [NR01](https://commons.wikimedia.org/wiki/File:Hukseflux_netto_radiometer_nr01_photo.jpg) — ผลงานของ Hukseflux เผยแพร่เป็น Public domain (PD-self) บน Wikimedia Commons ใช้แสดงรูปร่างของตัวอย่างเครื่องมือ ไม่ใช้ยืนยันรุ่นที่ผู้เล่าหรือ คพ. ใช้งาน
- ภาพ [PV reference cell](https://commons.wikimedia.org/wiki/File:PV_reference_cell_mounted_in_plane_of_array_for_irradiance_measurement.jpg) โดย SerkanEmr — [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); ใช้ภาพต้นฉบับไม่แก้ไขเพื่อเปรียบเทียบรูปร่าง
- [เครดิตภาพบทนำ](chapters/00/assets/README.md) — แยกภาพถ่ายจากแหล่งภายนอกและภาพหลักการที่โครงการสร้างเอง

## บทที่ 1 (EP 1) — กำลังและพลังงานรังสี: W/m² และ Wh/m²

[เปิดบทเรียนฉบับอ่าน](chapters/01/README.md) · [เรียนผ่านภาพ](chapters/01/visual-guide.md)

### หน่วยงานไทย

- [กรมอุตุนิยมวิทยา — การแผ่รังสี Radiation](https://www5.tmd.go.th/info/การแผรงส) — ใช้เฉพาะหัวข้อ Irradiance และ Irradiation เพื่อประกอบนิยามรังสีต่อพื้นที่และความสัมพันธ์กับเวลา กรณีคูณระดับรังสีกับระยะเวลาในบทเรียนกำหนดให้รังสีคงที่หรือใช้ค่าเฉลี่ยตามเวลาของช่วงนั้น
- [สถาบันมาตรวิทยาแห่งชาติ — ศัพท์มาตรวิทยาระหว่างประเทศ (VIM) ฉบับไทย–อังกฤษ, JCGM 200:2008 (En/Th)](https://mx.nimt.or.th/wp-content/uploads/2020/06/6.VIM-3rd-Edition_E-TH.pdf) — ข้อ 1.19 หน้าเอกสาร 15 (หน้าไฟล์ PDF 30) เรื่องค่าปริมาณ และข้อ 2.3 หน้าเอกสาร 21 (หน้าไฟล์ PDF 36) เรื่องสิ่งที่เจตนาวัด ฉบับนี้เป็นการเผยแพร่ศัพท์สากลพร้อมคำแปลไทย

### แหล่งสากล

- [NIST SP 330 ส่วน 2 ตาราง 4–5](https://www.nist.gov/pml/special-publication-330/sp-330-section-2) — หน่วยกำลัง W และ irradiance W/m²
- [Datla และ Parr, Introduction to Optical Radiometry, หน้า 8](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=104704) — irradiance เป็นกำลังรังสีตกกระทบต่อพื้นที่
- [Australian Bureau of Meteorology, Solar Radiation Definitions, ส่วน Radiation units](https://www.bom.gov.au/climate/austmaps/solar-radiation-glossary.shtml) — irradiance กับ radiant exposure และการรวมตามเวลา
- [JCGM Annotated VIM3 ข้อ 2.3](https://jcgm.bipm.org/vim/en/2.3.html) — ปริมาณที่ตั้งใจวัดหรือ measurand

[เครดิตภาพบทที่ 1](chapters/01/assets/README.md) — ภาพพื้นที่ กราฟ และแบบฝึกหัดสร้างจากข้อมูลสมมติของผู้จัดทำ

## บทที่ 2 (EP 2) — รังสีตรง รังสีกระจาย และ GHI/DNI/DHI

[เปิดบทเรียนฉบับอ่าน](chapters/02/README.md) · [เรียนผ่านภาพ](chapters/02/visual-guide.md)

ตรวจอ่านส่วนที่ระบุเมื่อ 18 พฤศจิกายน 2026

### หน่วยงานไทย

- [กรมอุตุนิยมวิทยา — การแผ่รังสี Radiation](https://www5.tmd.go.th/info/การแผรงส) — หัวข้อ Sky radiation, Direct solar radiation, Diffuse solar radiation และ Global radiation ใช้รองรับการกระเจิงและนิยามองค์ประกอบรังสีบนแนวราบ บทเรียนใช้คำว่า “รังสีรวมบนแนวราบ” สำหรับ GHI และแยกจากรังสีคลื่นยาวจากโลก

### แหล่งสากล

- [Sandia PVPMC — Irradiance & Insolation](https://pvpmc.sandia.gov/modeling-guide/1-weather-design-inputs/irradiance-insolation/) — การระบุ collection plane และส่วนของรังสี เพื่อแยก GHI/DNI/DHI
- [Sandia PVPMC — Global Horizontal Irradiance](https://pvpmc.sandia.gov/modeling-guide/1-weather-design-inputs/irradiance-insolation/global-horizontal-irradiance/) — นิยาม GHI และ pyranometer บนแนวราบ
- [Sandia PVPMC — Direct Normal Irradiance](https://pvpmc.sandia.gov/modeling-guide/1-weather-design-inputs/irradiance-insolation/direct-normal-irradiance/) — Pyrheliometer, มุมมองเครื่องมือ, การติดตามดวงอาทิตย์ และการประมาณ DNI เมื่อมีข้อมูลเพิ่มเติม
- [Sandia PVPMC — Diffuse Horizontal Irradiance](https://pvpmc.sandia.gov/modeling-guide/1-weather-design-inputs/irradiance-insolation/diffuse-horizontal-irradiance/) — การบังลำแสงด้วยจาน ลูกกลม หรือแถบบัง และการแก้ผลจากรังสีกระจายส่วนที่ถูกบัง
- [Australian Bureau of Meteorology — Solar and Terrestrial Radiation: Glossary](https://www.bom.gov.au/climate/austmaps/solar-radiation-glossary.shtml) — หัวข้อ Radiation, Direct solar irradiance, Diffuse solar irradiance และ Global solar irradiance; ใช้สมการองค์ประกอบบนแนวราบและตัวคูณ cos ของมุมเซนิท
- [Sandia PVPMC — Plane of Array Irradiance](https://pvpmc.sandia.gov/modeling-guide/1-weather-design-inputs/plane-of-array-poa-irradiance/) — ส่วนตรงบนระนาบ ส่วนกระจายจากท้องฟ้า และส่วนสะท้อนจากพื้นดิน สำหรับอธิบายความต่างระหว่าง POA กับ GHI

[เครดิตภาพบทที่ 2](chapters/02/assets/README.md) — ภาพหลักการและกราฟต้นฉบับ 7 ภาพพร้อมไฟล์ SVG ตัวเลขและแบบฝึกหัดเป็นข้อมูลสมมติ คำอ่านไทยเป็นการถอดเสียงโดยประมาณของผู้จัดทำ ไม่ใช่ข้อมูลการออกเสียงจากแหล่งข้างต้น

## แหล่งสำหรับบท 04 ตอน 1 ซึ่งอยู่ในแผน

- [JCGM VIM3 ข้อ 5.18](https://jcgm.bipm.org/vim/en/5.18.html) — ค่าอ้างอิง
- [JCGM VIM3 ข้อ 2.16](https://jcgm.bipm.org/vim/en/2.16.html) — measurement error
- [JCGM VIM3 ข้อ 2.9 Note 2](https://jcgm.bipm.org/vim/en/2.9.html) — ผลการวัดและความไม่แน่นอน
- [NIST SP 330 ส่วน 2 ตาราง 5](https://www.nist.gov/pml/special-publication-330/sp-330-section-2) — หน่วย irradiance
- [NIST TN 1297 Appendix D.1.1.4](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d1-terminology) — absolute error of measurement อาจต่างจาก absolute value of error; บทเรียนระบุ |T−R| เมื่อหมายถึงขนาดผลต่าง
- [JCGM 106:2012 ข้อ 5.1.1–5.1.4](https://www.bipm.org/documents/20126/2071204/JCGM_106_2012_E.pdf/fe9537d2-e7d7-e146-5abb-2649c3450b25) — กติกาตัดสินความสอดคล้องกับข้อกำหนด
- Hyndman, R. J. และ Koehler, A. B. (2006), *Another look at measures of forecast accuracy*, International Journal of Forecasting 22(4), 679–688 — [บทความตีพิมพ์](https://doi.org/10.1016/j.ijforecast.2006.03.001), [ฉบับผู้เขียนที่ใช้ ส่วน 2.1–2.2 ลงวันที่ 2 พฤศจิกายน 2005](https://robjhyndman.com/papers/mase.pdf)

บทความ Hyndman และ Koehler ใช้อ้างนิยาม MAE/MAPE และพฤติกรรมตัวหารศูนย์หรือใกล้ศูนย์ในบริบทคณิตศาสตร์ ไม่ใช่มาตรฐานการประเมินเซ็นเซอร์ การกำหนดเครื่องหมายผลต่างในซีรีส์ใช้ T−R ตามนิยามที่ประกาศไว้

## จุดเริ่มต้นสำหรับบทถัดไป

รายการต่อไปนี้เป็นฐานค้นคว้า ต้องตรวจรายละเอียดเพิ่มตามข้ออ้างของตอนที่จะผลิต

- [NIST Policy on Metrological Traceability](https://www.nist.gov/calibrations/traceability) — ความสอบกลับได้และความเหมาะสมต่อการใช้งาน
- [pvlib Time and time zones](https://pvlib-python.readthedocs.io/en/stable/user_guide/modeling_topics/timetimezones.html) — เวลาและ timezone
- [JCGM VIM3 ข้อ 2.39](https://jcgm.bipm.org/vim/en/2.39.html) และ [NIST Models for instrument calibration](https://www.itl.nist.gov/div898/handbook/mpc/section3/mpc361.htm) — นิยาม calibration และแบบจำลอง
- [pvlib Clear sky](https://pvlib-python.readthedocs.io/en/stable/user_guide/modeling_topics/clearsky.html) — แหล่งสาธารณะสำหรับหลักการและรูปแบบตัวอย่างในแผนบทที่ 8–9 ตัวอย่างของซีรีส์จะสร้างขึ้นใหม่ด้วยข้อมูลสมมติ โดยระบุสมมติฐานและที่มาของค่าที่ใช้สาธิต
- [pvlib ineichen](https://pvlib-python.readthedocs.io/en/stable/reference/generated/pvlib.clearsky.ineichen.html) — ตรวจชื่อฟังก์ชัน อินพุต และผลลัพธ์ของ **Ineichen–Perez**: clear-sky GHI/DNI/DHI ใช้รองรับคำแนะนำแบบจำลองในภาพรวมและแผนบทที่ 8 ซึ่งเน้นหลักการและข้อมูลสมมติ คำอ่านไทยเป็นการถอดเสียงโดยประมาณ ไม่ใช่ข้อมูลการออกเสียงจาก pvlib
- [Reno และ Hansen (2016) หน้าผลงาน Sandia](https://www.sandia.gov/research/publications/details/identification-of-periods-of-clear-sky-irradiance-in-time-series-of-ghi-mea-2016-05-01/) และ [บทความต้นฉบับ](https://doi.org/10.1016/j.renene.2015.12.031) — ต้องอ่านส่วนวิธีวิจัยเพิ่มเติมก่อนผลิตบทเต็ม
- [pvlib detect_clearsky](https://pvlib-python.readthedocs.io/en/stable/reference/generated/pvlib.clearsky.detect_clearsky.html) — หลักการตรวจจับ หน้าต่างเวลา ความหมายของพารามิเตอร์และ alpha สำหรับแผนบทที่ 9 ใช้ประกอบตัวอย่างข้อมูลสมมติ ไม่ใช้ถ่ายทอดวิธีปรับจูนหรือกระบวนการเฉพาะของบริษัท
- [Best Practices Handbook for the Collection and Use of Solar Resource Data for Solar Energy Applications, Fourth Edition (2024)](https://doi.org/10.2172/2448063) — แหล่งสำหรับอ่านเพิ่มเรื่องเครื่องมือและคุณภาพข้อมูล
