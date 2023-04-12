select avg(typical_fall_to_spring_growth) as avg
from (SELECT * From mydb.special_programs order by student_id) as gen join 
(select 
		fr.student_id as student_id,
		fr.rit_score as Fall_Reading_rit_score,
        sr.rit_score as Spring_Reading_rit_score,
        sr.rit_score - fr.rit_score as Score_Changes,
        fr.rit_score + fr.typical_fall_to_spring_growth as Goal,
        fr.typical_fall_to_spring_growth,
        case when (sr.rit_score - fr.rit_score) >= fr.typical_fall_to_spring_growth then 'Yes'
        when (sr.rit_score - fr.rit_score) < fr.typical_fall_to_spring_growth then 'No' end as  'Percentage_Kept'
from (select * from (select distinct * from mydb.map_scores_fall where map_term = 'Fall' and subject = 'Reading' order by student_id) as g) as fr left join 
(select * from (select distinct * from mydb.map_scores where map_term = 'Spring' and subject = 'Reading' order by student_id) as o) as sr on fr.student_id = sr.student_id
) as fr on gen.student_id = fr.student_id