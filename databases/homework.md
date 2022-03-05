# Peter Tsun 3/5/2022 HW: Database


[Homework on Google Collab](https://colab.research.google.com/drive/1iBFYn7t6_Gijxlp4pSq6RS0iDInstcH5?usp=sharing)


## Homework
`
    SELECT p.FIRST, p.Last, p.StudentID, p.Grade, ScanTime, Status, p.Date, p.courseSection, p.Attendance, p.period, p.teacher  
    FROM periodAtt AS p  
    INNER JOIN Scan AS s  
    ON p.StudentID = s.StudentID AND p.Date = substr(ScanTime, 1, instr(scanTime,' ')-1)  
    WHERE p.Attendance = 'A'  
    ORDER BY p.LAST ASC  
    `

## Async

`
  SELECT teacher, COUNT(teacher) as numCuts FROM (SELECT p.FIRST, p.Last, p.StudentID, p.Grade, ScanTime, Status, p.Date, p.courseSection, p.Attendance, p.period, p.teacher
    FROM periodAtt AS p
    INNER JOIN Scan AS s
    ON p.StudentID = s.StudentID AND p.Date = substr(ScanTime, 1, instr(scanTime,' ')-1)
    WHERE p.Attendance = 'A'
    ORDER BY p.LAST ASC) AS allCuts
    GROUP BY TEACHER
    ORDER BY numCuts DESC
`
