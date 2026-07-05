---
type: Jurisdiction
title: "Dickenson County, VA"
classification: county
fips: "51051"
state: "VA"
demographics:
  population: 13733
  population_under_18: 2627
  population_18_64: 7729
  population_65_plus: 3377
  median_household_income: 47254
  poverty_rate: 17.33
  homeownership_rate: 76.07
  unemployment_rate: 2.26
  median_home_value: 102700
  gini_index: 0.4339
  vacancy_rate: 19.38
  race_white: 13423
  race_black: 134
  race_asian: 13
  race_native: 30
  hispanic: 101
  bachelors_plus: 1290
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/va/districts/senate/6"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/va/districts/house/43"
    rel: in-district
    area_weight: 0.7801
  - to: "us/states/va/districts/house/45"
    rel: in-district
    area_weight: 0.2193
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Dickenson County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13733 |
| Under 18 | 2627 |
| 18–64 | 7729 |
| 65+ | 3377 |
| Median household income | 47254 |
| Poverty rate | 17.33 |
| Homeownership rate | 76.07 |
| Unemployment rate | 2.26 |
| Median home value | 102700 |
| Gini index | 0.4339 |
| Vacancy rate | 19.38 |
| White | 13423 |
| Black | 134 |
| Asian | 13 |
| Native | 30 |
| Hispanic/Latino | 101 |
| Bachelor's or higher | 1290 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 6](/us/states/va/districts/senate/6.md) — 100% (state senate)
- [VA House District 43](/us/states/va/districts/house/43.md) — 78% (state house)
- [VA House District 45](/us/states/va/districts/house/45.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
