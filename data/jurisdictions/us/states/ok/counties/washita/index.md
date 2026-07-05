---
type: Jurisdiction
title: "Washita County, OK"
classification: county
fips: "40149"
state: "OK"
demographics:
  population: 10815
  population_under_18: 2614
  population_18_64: 6069
  population_65_plus: 2132
  median_household_income: 63501
  poverty_rate: 14.1
  homeownership_rate: 75.99
  unemployment_rate: 5.68
  median_home_value: 118400
  gini_index: 0.4208
  vacancy_rate: 19.63
  race_white: 9168
  race_black: 140
  race_asian: 14
  race_native: 234
  hispanic: 1045
  bachelors_plus: 1998
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/38"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/house/55"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Washita County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10815 |
| Under 18 | 2614 |
| 18–64 | 6069 |
| 65+ | 2132 |
| Median household income | 63501 |
| Poverty rate | 14.1 |
| Homeownership rate | 75.99 |
| Unemployment rate | 5.68 |
| Median home value | 118400 |
| Gini index | 0.4208 |
| Vacancy rate | 19.63 |
| White | 9168 |
| Black | 140 |
| Asian | 14 |
| Native | 234 |
| Hispanic/Latino | 1045 |
| Bachelor's or higher | 1998 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 38](/us/states/ok/districts/senate/38.md) — 100% (state senate)
- [OK House District 55](/us/states/ok/districts/house/55.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
