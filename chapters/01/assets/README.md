# ที่มาและเครดิตภาพ — บทที่ 1

[กลับชุดภาพ](../visual-guide.md) · [กลับบทเรียน](../README.md)

ตรวจที่มาและสิทธิ์ภาพถ่ายเมื่อ 17 พฤศจิกายน 2026 ภาพถ่ายทั้งสองเป็นตัวอย่างเครื่องมือจากแหล่งสาธารณะ ไม่ได้ยืนยันรุ่นที่ผู้จัดทำหรือกรมควบคุมมลพิษใช้งาน

| ไฟล์ | ประเภทและที่มา | สิทธิ์ / หมายเหตุ |
|---|---|---|
| [pyranometer-sr11.jpg](pyranometer-sr11.jpg) | ภาพถ่าย Hukseflux SR11 โดย Hukseflux, 800 × 600 px; [หน้าต้นฉบับ](https://commons.wikimedia.org/wiki/File:Hukseflux_radiometer_sr11_photo.jpg) | เจ้าของผลงานเผยแพร่เป็น Public domain (PD-self) เก็บภาพต้นฉบับโดยไม่แก้ไข |
| [net-radiometer-nr01.jpg](net-radiometer-nr01.jpg) | ภาพถ่าย Hukseflux NR01 โดย Hukseflux, 800 × 600 px; [หน้าต้นฉบับ](https://commons.wikimedia.org/wiki/File:Hukseflux_netto_radiometer_nr01_photo.jpg) | เจ้าของผลงานเผยแพร่เป็น Public domain (PD-self) เก็บภาพต้นฉบับโดยไม่แก้ไข |
| [srad-nrad-radiation-flow.png](srad-nrad-radiation-flow.png) | ภาพอธิบายหลักการ สร้างด้วยเครื่องมือ imagegen ภายใน Codex (built-in tool mode) | เป็นภาพสร้างด้วย AI ไม่ใช่ภาพถ่ายหรือแบบจำลองผลิตภัณฑ์จริง ตรวจชื่อ หน่วย และทิศลูกศรเทียบหลักการแล้ว |
| [irradiance-vs-irradiation.png](irradiance-vs-irradiation.png) | กราฟสร้างจากตัวเลขสมมติด้วย Matplotlib, 1920 × 1080 px | รังสีคงที่ในแต่ละกรณี; แกนทั้งสองกราฟมีสเกลเดียวกัน: 800 × 0.5 = 400 × 1 = 400 Wh/m² |
| [two-interval-energy.png](two-interval-energy.png) | กราฟสร้างจากตัวเลขสมมติด้วย Matplotlib, 1920 × 1080 px | รังสีคงที่ในแต่ละช่วง: 800 × 0.25 + 400 × 0.25 = 300 Wh/m² |

ภาพหลักการและกราฟจัดทำขึ้นสำหรับซีรีส์นี้ เครดิตภาพถ่ายแบบสั้นที่ใช้ได้คือ “ภาพ: Hukseflux / Wikimedia Commons / Public domain” พร้อมเชื่อมหน้าต้นฉบับตามรายการข้างต้น

## แหล่งรองรับคำอธิบายเครื่องมือ

[Hukseflux — NR01 brochure หน้า 2–3](https://www.hukseflux.com/uploads/product-documents/NR01_v2301.pdf) อธิบายการใช้ pyranometer วัดรังสีดวงอาทิตย์ และ pyrgeometer วัดคลื่นยาว โดยเครื่อง NR01 วัดสี่องค์ประกอบเพื่อหารังสีสุทธิ ส่วน [FAO — Net radiation](https://www.fao.org/4/X0490E/x0490e07.htm) รองรับหลักการสมดุลรังสีเข้าและออก

รหัส SRAD/NRAD ในเอกสาร คพ. เป็นรหัสช่องข้อมูล การใช้ภาพเครื่องมือตัวอย่างไม่ได้ทำให้รหัสนั้นเป็นชื่อรุ่นหรือข้อกำหนดชนิดเซ็นเซอร์สากล
