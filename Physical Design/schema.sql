CREATE TYPE season as ENUM('winter','spring','summer','fall');

CREATE TABLE project.Date (
  date_key int PRIMARY KEY,
  day int CHECK (day >= 1 AND day <= 7),
  week int CHECK (week >= 1 AND week <= 53),
  month int CHECK (month >= 1 AND month <= 12),
  year int,
  weekend boolean,
  season_canada season,
  season_international season
);

CREATE TYPE disaster_category AS ENUM ('incident','disaster');
CREATE TYPE disaster_group AS ENUM ('conflict','natural','technology');

CREATE TABLE project.Disaster (
  disaster_key int PRIMARY KEY,
  disaster_type text,
  disaster_subgroup text,
  disaster_group disaster_group,
  disaster_category disaster_category,
  magnitude numeric,
  utility_people_affected int
);

CREATE TABLE project.Summary (
  description_key int PRIMARY KEY,
  summary text,
  keyword1 text,
  keyword2 text,
  keyword3 text
);

CREATE TABLE project.Location (
  location_key int PRIMARY KEY,
  city text,
  province text,
  country text,
  canada boolean,
  longitude numeric,
  latitude numeric
);

CREATE TABLE project.Costs (
  costs_key int PRIMARY KEY,
  estimated_total_cost numeric,
  normalized_total_cost numeric,
  federal_dfaa_payments numeric,
  provincial_dfaa_payments numeric,
  provincial_payments numeric,
  municipal_cost numeric,
  insurance_payments numeric,
  ogd_costs numeric,
  ngo_payments numeric
);

CREATE TABLE project.Fact (
  start_date_key int,
  end_date_key int,
  location_key int,
  disaster_key int,
  description_key int,
  costs_key int,
  fatalities int,
  injured int,
  evacuated int
)

