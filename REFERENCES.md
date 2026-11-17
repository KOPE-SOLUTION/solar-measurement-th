# แหล่งอ้างอิง

แหล่งด้านล่างรองรับเฉพาะประเด็นที่ระบุ ตัวเลขและสถานการณ์ในบทเรียนเป็นตัวอย่างสมมติของผู้จัดทำ ข้อมูลบรรณานุกรมและส่วนที่ใช้ตรวจอ่านเมื่อ 17 พฤศจิกายน 2026

## บท 01

- [NIST SP 330 ส่วน 2 ตาราง 4–5](https://www.nist.gov/pml/special-publication-330/sp-330-section-2) — หน่วยกำลัง W และ irradiance W/m²
- [Datla และ Parr, Introduction to Optical Radiometry, หน้า 8](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=104704) — irradiance เป็นกำลังรังสีตกกระทบต่อพื้นที่
- [Australian Bureau of Meteorology, Solar Radiation Definitions, ส่วน Radiation units](https://www.bom.gov.au/climate/austmaps/solar-radiation-glossary.shtml) — irradiance กับ radiant exposure และการรวมตามเวลา
- [JCGM Annotated VIM3 ข้อ 2.3](https://jcgm.bipm.org/vim/en/2.3.html) — ปริมาณที่ตั้งใจวัดหรือ measurand

## บท 04 ตอน 1

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
- [pvlib ineichen](https://pvlib-python.readthedocs.io/en/stable/reference/generated/pvlib.clearsky.ineichen.html) — อินพุตและผลลัพธ์ของแบบจำลอง Ineichen–Perez
- [Reno และ Hansen (2016) หน้าผลงาน Sandia](https://www.sandia.gov/research/publications/details/identification-of-periods-of-clear-sky-irradiance-in-time-series-of-ghi-mea-2016-05-01/) และ [บทความต้นฉบับ](https://doi.org/10.1016/j.renene.2015.12.031) — ต้องอ่านส่วนวิธีวิจัยเพิ่มเติมก่อนผลิตบทเต็ม
- [pvlib detect_clearsky](https://pvlib-python.readthedocs.io/en/stable/reference/generated/pvlib.clearsky.detect_clearsky.html) — implementation หน้าต่าง พารามิเตอร์ และ alpha
- [Best Practices Handbook for the Collection and Use of Solar Resource Data for Solar Energy Applications, Fourth Edition (2024)](https://doi.org/10.2172/2448063) — แหล่งสำหรับอ่านเพิ่มเรื่องเครื่องมือและคุณภาพข้อมูล
