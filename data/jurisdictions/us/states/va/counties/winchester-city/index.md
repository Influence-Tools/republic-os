---
type: Jurisdiction
title: "Winchester city, VA"
classification: county
fips: "51840"
state: "VA"
demographics:
  population: 27913
  population_under_18: 6286
  population_18_64: 16956
  population_65_plus: 4671
  median_household_income: 63974
  poverty_rate: 21.49
  homeownership_rate: 43.6
  unemployment_rate: 6.42
  median_home_value: 343000
  gini_index: 0.4698
  vacancy_rate: 8.36
  race_white: 17403
  race_black: 2215
  race_asian: 613
  race_native: 101
  hispanic: 5848
  bachelors_plus: 8445
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/house/32"
    rel: in-district
    area_weight: 0.9991
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Winchester city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27913 |
| Under 18 | 6286 |
| 18–64 | 16956 |
| 65+ | 4671 |
| Median household income | 63974 |
| Poverty rate | 21.49 |
| Homeownership rate | 43.6 |
| Unemployment rate | 6.42 |
| Median home value | 343000 |
| Gini index | 0.4698 |
| Vacancy rate | 8.36 |
| White | 17403 |
| Black | 2215 |
| Asian | 613 |
| Native | 101 |
| Hispanic/Latino | 5848 |
| Bachelor's or higher | 8445 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 100% (congressional)
- [VA Senate District 1](/us/states/va/districts/senate/1.md) — 100% (state senate)
- [VA House District 32](/us/states/va/districts/house/32.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
