select student,count(case when grade>=80 then 1 else null end) as A,count(case when grade>=60 and grade<80 then 1 else null end) as B,count(case when grade>=40 and grade<60 then 1 else null end) as C,count(case when grade<40 then 1 else null end) as D from exams group by student;