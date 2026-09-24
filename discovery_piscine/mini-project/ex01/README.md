# Rush00 – ex01 (Bonus)

## Part 1: รับไฟล์กระดานเป็น argument

```
$> python3 main.py boards/valid_board.chess | cat -e
Success$
$> python3 main.py boards/invalid_board.chess boards/valid_board2.chess | cat -e
Error$
Success$
```

- แต่ละไฟล์พิมพ์ผลหนึ่งบรรทัด: `Success`, `Fail` หรือ `Error`
- `Error` เมื่อ: เปิดไฟล์ไม่ได้ / ไม่มีไฟล์ / เป็นโฟลเดอร์ / ไฟล์ว่าง / กระดานไม่เป็นจัตุรัส / ไม่มี King หรือมี King มากกว่าหนึ่งตัว
- ไฟล์ที่ผิดไม่ทำให้ไฟล์ถัดไปหยุดทำงาน
- ไม่ใส่ไฟล์เลย → แสดงวิธีใช้ทาง stderr

## Part 2 (creative): `--explain`

```
$> python3 main.py --explain boards/checkmate.chess
Success
  King at (row 1, col 1)
  attacked by Rook at (row 1, col 3)

  K * R
  . . R
  . . .

  King has no safe move
  >>> CHECKMATE <<<
```

สิ่งที่แสดง:
1. หมากทุกตัวที่กำลังรุก King พร้อมตำแหน่ง
2. กระดาน โดยใช้ `*` แสดงเส้นทางที่หมากใช้รุก
3. ช่องที่ King หนีไปได้อย่างปลอดภัย (รวมถึงการกินหมากศัตรู)
4. บอกว่าเป็น **CHECKMATE** (โดนรุกและหนีไม่ได้) หรือ **STALEMATE** (ไม่โดนรุกแต่เดินไม่ได้)

เหตุผล: โจทย์บอกแค่ว่าโดนรุกหรือไม่ แต่ไม่บอกว่า *ทำไม* ฟีเจอร์นี้ช่วยให้ตรวจสอบได้ว่า
โปรแกรมคิดถูก ใช้ debug กระดานยากๆ ได้ง่าย และต่อยอดจาก "in check" ไปสู่
"checkmate" จริงตามชื่อ Rush ในเกมนี้ฝั่งเรามีแค่ King จึงหนีได้ทางเดียวคือเดิน King
ดังนั้นการเช็กช่องหนีครบ 8 ทิศคือการตรวจ checkmate ที่สมบูรณ์

## ไฟล์ทดสอบใน `boards/`
| ไฟล์ | ผลลัพธ์ |
|---|---|
| valid_board.chess, valid_board2.chess, checkmate.chess | Success |
| valid_fail.chess, stalemate.chess | Fail |
| invalid_board*.chess, empty.chess | Error |
