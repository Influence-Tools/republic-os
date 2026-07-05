---
type: Jurisdiction
title: "Lamar County, AL"
classification: county
fips: "01075"
state: "AL"
demographics:
  population: 13693
  population_under_18: 3030
  population_18_64: 7594
  population_65_plus: 3069
  median_household_income: 50000
  poverty_rate: 18.0
  homeownership_rate: 75.68
  unemployment_rate: 5.47
  median_home_value: 114000
  gini_index: 0.4392
  vacancy_rate: 28.6
  race_white: 11834
  race_black: 1371
  race_asian: 6
  race_native: 25
  hispanic: 262
  bachelors_plus: 1681
districts:
  - to: "us/states/al/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/al/districts/senate/5"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/al/districts/house/17"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Lamar County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13693 |
| Under 18 | 3030 |
| 18–64 | 7594 |
| 65+ | 3069 |
| Median household income | 50000 |
| Poverty rate | 18.0 |
| Homeownership rate | 75.68 |
| Unemployment rate | 5.47 |
| Median home value | 114000 |
| Gini index | 0.4392 |
| Vacancy rate | 28.6 |
| White | 11834 |
| Black | 1371 |
| Asian | 6 |
| Native | 25 |
| Hispanic/Latino | 262 |
| Bachelor's or higher | 1681 |

## Districts

- [AL-04](/us/states/al/districts/04.md) — 100% (congressional)
- [AL Senate District 5](/us/states/al/districts/senate/5.md) — 100% (state senate)
- [AL House District 17](/us/states/al/districts/house/17.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
