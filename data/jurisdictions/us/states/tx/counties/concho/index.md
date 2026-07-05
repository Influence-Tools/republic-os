---
type: Jurisdiction
title: "Concho County, TX"
classification: county
fips: "48095"
state: "TX"
demographics:
  population: 3328
  population_under_18: 390
  population_18_64: 2279
  population_65_plus: 659
  median_household_income: 65795
  poverty_rate: 11.39
  homeownership_rate: 80.47
  unemployment_rate: 1.53
  median_home_value: 107400
  gini_index: 0.3714
  vacancy_rate: 42.43
  race_white: 2248
  race_black: 158
  race_asian: 56
  race_native: 0
  hispanic: 1062
  bachelors_plus: 513
districts:
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/72"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Concho County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3328 |
| Under 18 | 390 |
| 18–64 | 2279 |
| 65+ | 659 |
| Median household income | 65795 |
| Poverty rate | 11.39 |
| Homeownership rate | 80.47 |
| Unemployment rate | 1.53 |
| Median home value | 107400 |
| Gini index | 0.3714 |
| Vacancy rate | 42.43 |
| White | 2248 |
| Black | 158 |
| Asian | 56 |
| Native | 0 |
| Hispanic/Latino | 1062 |
| Bachelor's or higher | 513 |

## Districts

- [TX-11](/us/states/tx/districts/11.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 72](/us/states/tx/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
