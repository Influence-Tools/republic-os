---
type: Jurisdiction
title: "Northampton County, PA"
classification: county
fips: "42095"
state: "PA"
demographics:
  population: 318580
  population_under_18: 61011
  population_18_64: 192826
  population_65_plus: 64743
  median_household_income: 89184
  poverty_rate: 8.75
  homeownership_rate: 71.11
  unemployment_rate: 4.57
  median_home_value: 308600
  gini_index: 0.4411
  vacancy_rate: 5.27
  race_white: 236417
  race_black: 20188
  race_asian: 9781
  race_native: 635
  hispanic: 49253
  bachelors_plus: 108520
districts:
  - to: "us/states/pa/districts/07"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/pa/districts/senate/18"
    rel: in-district
    area_weight: 0.6537
  - to: "us/states/pa/districts/senate/14"
    rel: in-district
    area_weight: 0.346
  - to: "us/states/pa/districts/house/138"
    rel: in-district
    area_weight: 0.4651
  - to: "us/states/pa/districts/house/183"
    rel: in-district
    area_weight: 0.2117
  - to: "us/states/pa/districts/house/137"
    rel: in-district
    area_weight: 0.1259
  - to: "us/states/pa/districts/house/136"
    rel: in-district
    area_weight: 0.1141
  - to: "us/states/pa/districts/house/135"
    rel: in-district
    area_weight: 0.054
  - to: "us/states/pa/districts/house/131"
    rel: in-district
    area_weight: 0.0289
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Northampton County, PA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 318580 |
| Under 18 | 61011 |
| 18–64 | 192826 |
| 65+ | 64743 |
| Median household income | 89184 |
| Poverty rate | 8.75 |
| Homeownership rate | 71.11 |
| Unemployment rate | 4.57 |
| Median home value | 308600 |
| Gini index | 0.4411 |
| Vacancy rate | 5.27 |
| White | 236417 |
| Black | 20188 |
| Asian | 9781 |
| Native | 635 |
| Hispanic/Latino | 49253 |
| Bachelor's or higher | 108520 |

## Districts

- [PA-07](/us/states/pa/districts/07.md) — 100% (congressional)
- [PA Senate District 18](/us/states/pa/districts/senate/18.md) — 65% (state senate)
- [PA Senate District 14](/us/states/pa/districts/senate/14.md) — 35% (state senate)
- [PA House District 138](/us/states/pa/districts/house/138.md) — 47% (state house)
- [PA House District 183](/us/states/pa/districts/house/183.md) — 21% (state house)
- [PA House District 137](/us/states/pa/districts/house/137.md) — 13% (state house)
- [PA House District 136](/us/states/pa/districts/house/136.md) — 11% (state house)
- [PA House District 135](/us/states/pa/districts/house/135.md) — 5% (state house)
- [PA House District 131](/us/states/pa/districts/house/131.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
