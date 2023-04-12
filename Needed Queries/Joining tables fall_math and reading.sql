select fr.student_id, fm.rit_score as 'Fall_Math_Score', fr.rit_score as 'Fall_Reading_Score', (fm.rit_score - fr.rit_score) as Difference
from (select * from (select distinct * from mydb.map_scores_fall where map_term = 'Fall' and subject = 'Reading' order by student_id) as o) as fr left join 
(select * from (select distinct * from mydb.map_scores_fall where map_term = 'Fall' and subject = 'Math' order by student_id) as g) as fm on fr.student_id = fm.student_id
order by fr.student_id





