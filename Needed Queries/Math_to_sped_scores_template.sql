select avg(typical_fall_to_spring_growth) as avg
from (SELECT * From mydb.special_programs) as gen join  
(select 
		fm.student_id as student_id,
		fm.rit_score as Fall_Math_rit_score,
        sm.rit_score as Spring_Math_rit_score,
        sm.rit_score - fm.rit_score as Score_Changes,
        fm.rit_score + fm.typical_fall_to_spring_growth as Goal,
        fm.typical_fall_to_spring_growth,
        case when (sm.rit_score - fm.rit_score) >= fm.typical_fall_to_spring_growth then 'Yes'
        when (sm.rit_score - fm.rit_score) < fm.typical_fall_to_spring_growth then 'No' end as  'Percentage_Kept'
from (select * from (select distinct * from mydb.map_scores_fall where map_term = 'Fall' and subject = 'Math' order by student_id) as g) as fm left join 
(select * from (select distinct * from mydb.map_scores where map_term = 'Spring' and subject = 'Math' order by student_id) as o) as sm on fm.student_id = sm.student_id
) as fm on gen.student_id = fm.student_id
order by fm.student_id