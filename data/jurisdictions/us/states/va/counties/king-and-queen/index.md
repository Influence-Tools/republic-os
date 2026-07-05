---
type: Jurisdiction
title: "King and Queen County, VA"
classification: county
fips: "51097"
state: "VA"
demographics:
  population: 6695
  population_under_18: 1164
  population_18_64: 3937
  population_65_plus: 1594
  median_household_income: 70469
  poverty_rate: 17.88
  homeownership_rate: 75.72
  unemployment_rate: 5.15
  median_home_value: 231600
  gini_index: 0.417
  vacancy_rate: 14.47
  race_white: 4504
  race_black: 1463
  race_asian: 5
  race_native: 47
  hispanic: 221
  bachelors_plus: 1218
districts:
  - to: "us/states/va/districts/01"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/va/districts/senate/25"
    rel: in-district
    area_weight: 0.8789
  - to: "us/states/va/districts/senate/26"
    rel: in-district
    area_weight: 0.1211
  - to: "us/states/va/districts/house/68"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# King and Queen County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6695 |
| Under 18 | 1164 |
| 18–64 | 3937 |
| 65+ | 1594 |
| Median household income | 70469 |
| Poverty rate | 17.88 |
| Homeownership rate | 75.72 |
| Unemployment rate | 5.15 |
| Median home value | 231600 |
| Gini index | 0.417 |
| Vacancy rate | 14.47 |
| White | 4504 |
| Black | 1463 |
| Asian | 5 |
| Native | 47 |
| Hispanic/Latino | 221 |
| Bachelor's or higher | 1218 |

## Districts

- [VA-01](/us/states/va/districts/01.md) — 100% (congressional)
- [VA Senate District 25](/us/states/va/districts/senate/25.md) — 88% (state senate)
- [VA Senate District 26](/us/states/va/districts/senate/26.md) — 12% (state senate)
- [VA House District 68](/us/states/va/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
