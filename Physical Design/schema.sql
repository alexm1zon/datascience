CREATE TYPE season as ENUM('winter','spring','summer','fall');

CREATE TABLE project.Date (
  date_key int PRIMARY KEY,
  day int ,
  month int,
  year int,
  weekend boolean,
  season_canada season
);

CREATE TABLE project.Disaster (
  disaster_key int PRIMARY KEY,
  disaster_type text,
  disaster_subgroup text,
  disaster_group text,
  disaster_category text,
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
  latitude numeric,
  description text,
  query text,
  population int
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
  evacuated int,
  population int
)