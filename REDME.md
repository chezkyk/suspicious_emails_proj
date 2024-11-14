1.  כדי למצוא את כל תכני המייל כולל החשודים, נעשה שאילתה אחת למונגו ומשם נביא רק את השדה של המשפטים
ובכדי להביא את התוכן שמכיל חטוף או פיצוץ נעשה שאילתה עם JOIN לפוסטגרס ונביא משם את הנתונים
2. עושה שאילתה לפוסטגרס ומביא משם את החטופים והפצצות ומשתמש בפונקציית איחוד וככה אני מקבל אחד גדול,ואז אני משתמש כהמלצת הצבחן ב COUNTER ו MOST_COMMON שהם מתודות קיימות שעוזרות למצוא את המילה הכי נפוצה
## הרצת הפרויקט
## להסיר את הקפקא דוקר ע''י הפקודה הבאה
## docker compose down
## להרים את הדוקר קפקא עי הפקודה הבאה 
## docker compose up 
## הרצת הקונסיומרים 
## python .\all-messages-consumer\all_messages_consumer.py
## python .\explosiv-messages-consumer\explosiv_messages_consumer.py
## python .\hostage-messages-consumer\hostage_messages_consumer.py
## python .\main-file\main.py (מריץ את הראוטים והפרודוסר)
## להריץ את הפרויקט של עומר לשליחת הודעות
## בדיקת תוכן לפי אימייל
## http://127.0.0.1:5000/api/suspicious_content/elizabethwilliams@example.org
## הרצת בדיקה המילה הנפוצה ביותר 
## http://127.0.0.1:5000/api/most_common_word