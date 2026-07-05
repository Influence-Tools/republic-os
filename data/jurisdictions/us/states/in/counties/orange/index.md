---
type: Jurisdiction
title: "Orange County, IN"
classification: county
fips: "18117"
state: "IN"
demographics:
  population: 19767
  population_under_18: 4531
  population_18_64: 11125
  population_65_plus: 4111
  median_household_income: 65873
  poverty_rate: 13.42
  homeownership_rate: 78.7
  unemployment_rate: 3.12
  median_home_value: 158700
  gini_index: 0.4637
  vacancy_rate: 12.43
  race_white: 18493
  race_black: 234
  race_asian: 89
  race_native: 18
  hispanic: 360
  bachelors_plus: 2928
districts:
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/in/districts/senate/44"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/in/districts/house/65"
    rel: in-district
    area_weight: 0.7902
  - to: "us/states/in/districts/house/74"
    rel: in-district
    area_weight: 0.2098
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Orange County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19767 |
| Under 18 | 4531 |
| 18–64 | 11125 |
| 65+ | 4111 |
| Median household income | 65873 |
| Poverty rate | 13.42 |
| Homeownership rate | 78.7 |
| Unemployment rate | 3.12 |
| Median home value | 158700 |
| Gini index | 0.4637 |
| Vacancy rate | 12.43 |
| White | 18493 |
| Black | 234 |
| Asian | 89 |
| Native | 18 |
| Hispanic/Latino | 360 |
| Bachelor's or higher | 2928 |

## Districts

- [IN-08](/us/states/in/districts/08.md) — 100% (congressional)
- [IN Senate District 44](/us/states/in/districts/senate/44.md) — 100% (state senate)
- [IN House District 65](/us/states/in/districts/house/65.md) — 79% (state house)
- [IN House District 74](/us/states/in/districts/house/74.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
