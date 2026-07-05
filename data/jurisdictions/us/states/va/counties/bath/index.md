---
type: Jurisdiction
title: "Bath County, VA"
classification: county
fips: "51017"
state: "VA"
demographics:
  population: 4100
  population_under_18: 710
  population_18_64: 2273
  population_65_plus: 1117
  median_household_income: 56184
  poverty_rate: 23.78
  homeownership_rate: 71.3
  unemployment_rate: 1.32
  median_home_value: 206700
  gini_index: 0.4911
  vacancy_rate: 43.56
  race_white: 3766
  race_black: 140
  race_asian: 10
  race_native: 0
  hispanic: 125
  bachelors_plus: 735
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/va/districts/senate/2"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/va/districts/house/35"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Bath County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4100 |
| Under 18 | 710 |
| 18–64 | 2273 |
| 65+ | 1117 |
| Median household income | 56184 |
| Poverty rate | 23.78 |
| Homeownership rate | 71.3 |
| Unemployment rate | 1.32 |
| Median home value | 206700 |
| Gini index | 0.4911 |
| Vacancy rate | 43.56 |
| White | 3766 |
| Black | 140 |
| Asian | 10 |
| Native | 0 |
| Hispanic/Latino | 125 |
| Bachelor's or higher | 735 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 100% (congressional)
- [VA Senate District 2](/us/states/va/districts/senate/2.md) — 100% (state senate)
- [VA House District 35](/us/states/va/districts/house/35.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
