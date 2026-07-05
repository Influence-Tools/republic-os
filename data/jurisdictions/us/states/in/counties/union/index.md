---
type: Jurisdiction
title: "Union County, IN"
classification: county
fips: "18161"
state: "IN"
demographics:
  population: 6985
  population_under_18: 1443
  population_18_64: 4070
  population_65_plus: 1472
  median_household_income: 76424
  poverty_rate: 8.47
  homeownership_rate: 79.83
  unemployment_rate: 4.25
  median_home_value: 173500
  gini_index: 0.417
  vacancy_rate: 9.68
  race_white: 6644
  race_black: 40
  race_asian: 30
  race_native: 4
  hispanic: 178
  bachelors_plus: 1186
districts:
  - to: "us/states/in/districts/06"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/in/districts/senate/27"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/house/55"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Union County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6985 |
| Under 18 | 1443 |
| 18–64 | 4070 |
| 65+ | 1472 |
| Median household income | 76424 |
| Poverty rate | 8.47 |
| Homeownership rate | 79.83 |
| Unemployment rate | 4.25 |
| Median home value | 173500 |
| Gini index | 0.417 |
| Vacancy rate | 9.68 |
| White | 6644 |
| Black | 40 |
| Asian | 30 |
| Native | 4 |
| Hispanic/Latino | 178 |
| Bachelor's or higher | 1186 |

## Districts

- [IN-06](/us/states/in/districts/06.md) — 100% (congressional)
- [IN Senate District 27](/us/states/in/districts/senate/27.md) — 100% (state senate)
- [IN House District 55](/us/states/in/districts/house/55.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
