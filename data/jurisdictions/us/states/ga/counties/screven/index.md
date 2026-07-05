---
type: Jurisdiction
title: "Screven County, GA"
classification: county
fips: "13251"
state: "GA"
demographics:
  population: 14130
  population_under_18: 2941
  population_18_64: 8261
  population_65_plus: 2928
  median_household_income: 52792
  poverty_rate: 17.18
  homeownership_rate: 69.85
  unemployment_rate: 4.61
  median_home_value: 124300
  gini_index: 0.4825
  vacancy_rate: 24.9
  race_white: 7889
  race_black: 5531
  race_asian: 0
  race_native: 3
  hispanic: 375
  bachelors_plus: 2232
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 0.9973
  - to: "us/states/ga/districts/senate/23"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ga/districts/house/159"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Screven County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14130 |
| Under 18 | 2941 |
| 18–64 | 8261 |
| 65+ | 2928 |
| Median household income | 52792 |
| Poverty rate | 17.18 |
| Homeownership rate | 69.85 |
| Unemployment rate | 4.61 |
| Median home value | 124300 |
| Gini index | 0.4825 |
| Vacancy rate | 24.9 |
| White | 7889 |
| Black | 5531 |
| Asian | 0 |
| Native | 3 |
| Hispanic/Latino | 375 |
| Bachelor's or higher | 2232 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 23](/us/states/ga/districts/senate/23.md) — 100% (state senate)
- [GA House District 159](/us/states/ga/districts/house/159.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
