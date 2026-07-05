---
type: Jurisdiction
title: "Hart County, GA"
classification: county
fips: "13147"
state: "GA"
demographics:
  population: 26939
  population_under_18: 5477
  population_18_64: 15367
  population_65_plus: 6095
  median_household_income: 59385
  poverty_rate: 11.85
  homeownership_rate: 77.77
  unemployment_rate: 3.41
  median_home_value: 215100
  gini_index: 0.4588
  vacancy_rate: 16.41
  race_white: 19932
  race_black: 4576
  race_asian: 368
  race_native: 141
  hispanic: 1145
  bachelors_plus: 5599
districts:
  - to: "us/states/ga/districts/10"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/ga/districts/senate/24"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ga/districts/house/33"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Hart County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26939 |
| Under 18 | 5477 |
| 18–64 | 15367 |
| 65+ | 6095 |
| Median household income | 59385 |
| Poverty rate | 11.85 |
| Homeownership rate | 77.77 |
| Unemployment rate | 3.41 |
| Median home value | 215100 |
| Gini index | 0.4588 |
| Vacancy rate | 16.41 |
| White | 19932 |
| Black | 4576 |
| Asian | 368 |
| Native | 141 |
| Hispanic/Latino | 1145 |
| Bachelor's or higher | 5599 |

## Districts

- [GA-10](/us/states/ga/districts/10.md) — 100% (congressional)
- [GA Senate District 24](/us/states/ga/districts/senate/24.md) — 100% (state senate)
- [GA House District 33](/us/states/ga/districts/house/33.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
