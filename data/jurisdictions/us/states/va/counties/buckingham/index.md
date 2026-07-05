---
type: Jurisdiction
title: "Buckingham County, VA"
classification: county
fips: "51029"
state: "VA"
demographics:
  population: 16976
  population_under_18: 3017
  population_18_64: 10423
  population_65_plus: 3536
  median_household_income: 60828
  poverty_rate: 12.46
  homeownership_rate: 77.32
  unemployment_rate: 4.73
  median_home_value: 173400
  gini_index: 0.4147
  vacancy_rate: 13.87
  race_white: 10432
  race_black: 5195
  race_asian: 65
  race_native: 25
  hispanic: 447
  bachelors_plus: 2419
districts:
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/10"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/va/districts/house/56"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Buckingham County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16976 |
| Under 18 | 3017 |
| 18–64 | 10423 |
| 65+ | 3536 |
| Median household income | 60828 |
| Poverty rate | 12.46 |
| Homeownership rate | 77.32 |
| Unemployment rate | 4.73 |
| Median home value | 173400 |
| Gini index | 0.4147 |
| Vacancy rate | 13.87 |
| White | 10432 |
| Black | 5195 |
| Asian | 65 |
| Native | 25 |
| Hispanic/Latino | 447 |
| Bachelor's or higher | 2419 |

## Districts

- [VA-05](/us/states/va/districts/05.md) — 100% (congressional)
- [VA Senate District 10](/us/states/va/districts/senate/10.md) — 100% (state senate)
- [VA House District 56](/us/states/va/districts/house/56.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
