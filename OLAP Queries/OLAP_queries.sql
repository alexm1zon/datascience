
--TOP N
-- determine the 5 cities in Canada with the most floods.
SELECT l.city, count(*) as flood_count
FROM fact
INNER JOIN location l ON fact.location_key = l.location_key
INNER JOIN disaster d ON fact.disaster_key = d.disaster_key
WHERE disaster_type = 'Flood' AND country = 'Canada'
GROUP BY city
ORDER BY count(*) DESC
LIMIT 5;

--SLICE

--SLICE : average population affected (in thousands) by types in disaster in the the fall season 
select d.disaster_type, CAST(AVG(f.population/1000) as int) as average_population_affected_in_thousands, CAST(AVG(f.evacuated) as int) as average_evacuted
from fact f, disaster d, date dt 
WHERE dt.season_canada='fall' and f.disaster_key = d.disaster_key and f.start_date_key=dt.date_key
group by (d.disaster_type)
order by average_population_affected_in_thousands DESC

--SLICE : average population affected (in thousands) by types in disaster in the the winter season 
select  d.disaster_type, CAST(AVG(f.population/1000) as int) as average_population_affected_in_thousands, CAST(AVG(f.evacuated) as int) as average_evacuted
from fact f, disaster d, date dt 
WHERE dt.season_canada='winter' and f.disaster_key = d.disaster_key and f.start_date_key=dt.date_key
group by (d.disaster_type )
order by average_population_affected_in_thousands DESC

--SLICE : average population affected (in thousands) by types in disaster in the the summer season 
select  d.disaster_type, CAST(AVG(f.population/1000) as int) as average_population_affected_in_thousands, CAST(AVG(f.evacuated) as int) as average_evacuted
from fact f, disaster d, date dt 
WHERE dt.season_canada='summer' and f.disaster_key = d.disaster_key and f.start_date_key=dt.date_key
group by (d.disaster_type )
order by average_population_affected_in_thousands DESC

--SLICE : average population affected (in thousands) by types in disaster in the the spring season 
select  d.disaster_type, CAST(AVG(f.population/1000) as int) as average_population_affected_in_thousands, CAST(AVG(f.evacuated) as int) as average_evacuted
from fact f, disaster d, date dt 
WHERE dt.season_canada='spring' and f.disaster_key = d.disaster_key and f.start_date_key=dt.date_key
group by (d.disaster_type )
order by average_population_affected_in_thousands DESC




--DICE
-- Contrast the the total number of fatalities in Ontario and Quebec from 2010 to 2016
SELECT  
  l.province,
  SUM(f.fatalities) as total_fatalities
FROM fact f, date d, location l 
WHERE (l.province = 'Ontario' OR l.province = 'Quebec') 
AND d.year between 2010 and 2016 
and f.start_date_key = d.date_key and f.location_key=l.location_key
GROUP BY province


--DRILL DOWN
--YEAR DRILL DOWN:listing number of technology disasters each year, month day 
select d.year,  DI.disaster_group, count(*) as total_count
from
fact f, date d, disaster DI
where f.start_date_key=D.date_key and f.disaster_key=DI.disaster_key and DI.disaster_group='Technology'
group by (d.year, DI.disaster_group)
order by d.year DESC;

--SEASON DRILL DOWN:listing number of technology disasters each year, season
select d.year, d.season_canada, DI.disaster_group, count(*) as total_count
from
fact f, date d, disaster DI
where f.start_date_key=D.date_key and f.disaster_key=DI.disaster_key and DI.disaster_group='Technology'
group by (d.year, d.season_canada, DI.disaster_group)
order by d.year, d.season_canada DESC;

--MONTH DRILL DOWN:listing number of technology disasters each year,season, month
select d.year, d.season_canada, d.month, DI.disaster_group, count(*) as total_count
from
fact f, date d, disaster DI
where f.start_date_key=D.date_key and f.disaster_key=DI.disaster_key and DI.disaster_group='Technology'
group by (d.year, d.season_canada, d.month,DI.disaster_group)
order by d.year, d.season_canada, d.month DESC;

--DAY DRILL DOWN:listing number of technology disasters each year, season, month, day 
select d.year, d.season_canada, d.month, d.day, DI.disaster_group, count(*) as total_count
from
fact f, date d, disaster DI
where f.start_date_key=D.date_key and f.disaster_key=DI.disaster_key and DI.disaster_group='Technology'
group by (d.year, d.season_canada, d.month,d.day,DI.disaster_group)
order by d.year, d.season_canada, d.month , d.day DESC;


--ROLL-UP

--ROLL UP BY CITY: Listing the total number of fatalities from 1990 to 2005 by city-> province -> country
select l.country, l.province, l.city, sum(f.fatalities) as total_fatalities
from fact f, location l, date d
where
f.location_key=l.location_key and f.start_date_key=d.date_key and d.year between 1990 and 2005
GROUP BY l.country, l.province, l.city
ORDER BY l.country, l.province, l.city ASC;

--ROLL UP BY PROVINCE: Listing the total number of fatalities from 1990 to 2005 by province -> country
select l.country, l.province,  sum(f.fatalities) as total_fatalities
from fact f, location l, date d
where
f.location_key=l.location_key and f.start_date_key=d.date_key and d.year between 1990 and 2005
GROUP BY l.country, l.province
ORDER BY l.country, l.province ASC;

--ROLL UP BY YEAR: Listing the total number of fatalities from 1990 to 2005 by country
select l.country,   sum(f.fatalities) as total_fatalities
from fact f, location l, date d
where
f.location_key=l.location_key and f.start_date_key=d.date_key and d.year between 1990 and 2005
GROUP BY l.country
ORDER BY l.country ASC;

