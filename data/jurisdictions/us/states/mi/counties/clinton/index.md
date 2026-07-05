---
type: Jurisdiction
title: "Clinton County, MI"
classification: county
fips: "26037"
state: "MI"
demographics:
  population: 79626
  population_under_18: 17005
  population_18_64: 47650
  population_65_plus: 14971
  median_household_income: 88210
  poverty_rate: 9.68
  homeownership_rate: 82.19
  unemployment_rate: 3.83
  median_home_value: 259500
  gini_index: 0.4296
  vacancy_rate: 5.03
  race_white: 70643
  race_black: 1541
  race_asian: 1226
  race_native: 229
  hispanic: 4147
  bachelors_plus: 27680
districts:
  - to: "us/states/mi/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/senate/28"
    rel: in-district
    area_weight: 0.8761
  - to: "us/states/mi/districts/senate/34"
    rel: in-district
    area_weight: 0.1238
  - to: "us/states/mi/districts/house/93"
    rel: in-district
    area_weight: 0.3747
  - to: "us/states/mi/districts/house/75"
    rel: in-district
    area_weight: 0.318
  - to: "us/states/mi/districts/house/77"
    rel: in-district
    area_weight: 0.3073
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Clinton County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 79626 |
| Under 18 | 17005 |
| 18–64 | 47650 |
| 65+ | 14971 |
| Median household income | 88210 |
| Poverty rate | 9.68 |
| Homeownership rate | 82.19 |
| Unemployment rate | 3.83 |
| Median home value | 259500 |
| Gini index | 0.4296 |
| Vacancy rate | 5.03 |
| White | 70643 |
| Black | 1541 |
| Asian | 1226 |
| Native | 229 |
| Hispanic/Latino | 4147 |
| Bachelor's or higher | 27680 |

## Districts

- [MI-07](/us/states/mi/districts/07.md) — 100% (congressional)
- [MI Senate District 28](/us/states/mi/districts/senate/28.md) — 88% (state senate)
- [MI Senate District 34](/us/states/mi/districts/senate/34.md) — 12% (state senate)
- [MI House District 93](/us/states/mi/districts/house/93.md) — 37% (state house)
- [MI House District 75](/us/states/mi/districts/house/75.md) — 32% (state house)
- [MI House District 77](/us/states/mi/districts/house/77.md) — 31% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
