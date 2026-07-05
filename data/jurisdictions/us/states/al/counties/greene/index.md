---
type: Jurisdiction
title: "Greene County, AL"
classification: county
fips: "01063"
state: "AL"
demographics:
  population: 7424
  population_under_18: 1602
  population_18_64: 3958
  population_65_plus: 1864
  median_household_income: 29200
  poverty_rate: 40.14
  homeownership_rate: 61.61
  unemployment_rate: 4.04
  median_home_value: 81200
  gini_index: 0.5184
  vacancy_rate: 24.63
  race_white: 1326
  race_black: 6034
  race_asian: 3
  race_native: 9
  hispanic: 10
  bachelors_plus: 1050
districts:
  - to: "us/states/al/districts/07"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/al/districts/senate/24"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/al/districts/house/72"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Greene County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7424 |
| Under 18 | 1602 |
| 18–64 | 3958 |
| 65+ | 1864 |
| Median household income | 29200 |
| Poverty rate | 40.14 |
| Homeownership rate | 61.61 |
| Unemployment rate | 4.04 |
| Median home value | 81200 |
| Gini index | 0.5184 |
| Vacancy rate | 24.63 |
| White | 1326 |
| Black | 6034 |
| Asian | 3 |
| Native | 9 |
| Hispanic/Latino | 10 |
| Bachelor's or higher | 1050 |

## Districts

- [AL-07](/us/states/al/districts/07.md) — 100% (congressional)
- [AL Senate District 24](/us/states/al/districts/senate/24.md) — 100% (state senate)
- [AL House District 72](/us/states/al/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
