---
type: Jurisdiction
title: "Saguache County, CO"
classification: county
fips: "08109"
state: "CO"
demographics:
  population: 6580
  population_under_18: 1174
  population_18_64: 3652
  population_65_plus: 1754
  median_household_income: 50082
  poverty_rate: 17.77
  homeownership_rate: 76.92
  unemployment_rate: 10.33
  median_home_value: 212600
  gini_index: 0.551
  vacancy_rate: 12.94
  race_white: 4431
  race_black: 9
  race_asian: 80
  race_native: 38
  hispanic: 2422
  bachelors_plus: 2376
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/co/districts/senate/6"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/co/districts/house/62"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Saguache County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6580 |
| Under 18 | 1174 |
| 18–64 | 3652 |
| 65+ | 1754 |
| Median household income | 50082 |
| Poverty rate | 17.77 |
| Homeownership rate | 76.92 |
| Unemployment rate | 10.33 |
| Median home value | 212600 |
| Gini index | 0.551 |
| Vacancy rate | 12.94 |
| White | 4431 |
| Black | 9 |
| Asian | 80 |
| Native | 38 |
| Hispanic/Latino | 2422 |
| Bachelor's or higher | 2376 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 6](/us/states/co/districts/senate/6.md) — 100% (state senate)
- [CO House District 62](/us/states/co/districts/house/62.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
