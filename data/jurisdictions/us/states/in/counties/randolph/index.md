---
type: Jurisdiction
title: "Randolph County, IN"
classification: county
fips: "18135"
state: "IN"
demographics:
  population: 24387
  population_under_18: 5529
  population_18_64: 13827
  population_65_plus: 5031
  median_household_income: 60791
  poverty_rate: 15.85
  homeownership_rate: 77.28
  unemployment_rate: 4.53
  median_home_value: 113400
  gini_index: 0.4329
  vacancy_rate: 9.18
  race_white: 22324
  race_black: 173
  race_asian: 114
  race_native: 75
  hispanic: 1287
  bachelors_plus: 3478
districts:
  - to: "us/states/in/districts/06"
    rel: in-district
    area_weight: 0.5506
  - to: "us/states/in/districts/03"
    rel: in-district
    area_weight: 0.4487
  - to: "us/states/in/districts/senate/26"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/in/districts/house/33"
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

# Randolph County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24387 |
| Under 18 | 5529 |
| 18–64 | 13827 |
| 65+ | 5031 |
| Median household income | 60791 |
| Poverty rate | 15.85 |
| Homeownership rate | 77.28 |
| Unemployment rate | 4.53 |
| Median home value | 113400 |
| Gini index | 0.4329 |
| Vacancy rate | 9.18 |
| White | 22324 |
| Black | 173 |
| Asian | 114 |
| Native | 75 |
| Hispanic/Latino | 1287 |
| Bachelor's or higher | 3478 |

## Districts

- [IN-06](/us/states/in/districts/06.md) — 55% (congressional)
- [IN-03](/us/states/in/districts/03.md) — 45% (congressional)
- [IN Senate District 26](/us/states/in/districts/senate/26.md) — 100% (state senate)
- [IN House District 33](/us/states/in/districts/house/33.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
