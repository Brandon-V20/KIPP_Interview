select avg(g.typical_fall_to_spring_growth) as avg from (select distinct * from mydb.map_scores where map_term = 'Fall' and subject = 'Math' order by student_id) as g  ;

select * from (select distinct * from mydb.map_scores where map_term = 'Spring' and subject = 'Reading' order by student_id) as g 