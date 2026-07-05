---
type: Jurisdiction
title: "Alexander County, NC"
classification: county
fips: "37003"
state: "NC"
demographics:
  population: 36412
  population_under_18: 7144
  population_18_64: 21547
  population_65_plus: 7721
  median_household_income: 65354
  poverty_rate: 12.57
  homeownership_rate: 80.68
  unemployment_rate: 5.03
  median_home_value: 211800
  gini_index: 0.4417
  vacancy_rate: 12.9
  race_white: 31805
  race_black: 1828
  race_asian: 363
  race_native: 368
  hispanic: 2031
  bachelors_plus: 5902
districts:
  - to: "us/states/nc/districts/05"
    rel: in-district
    area_weight: 0.9979
  - to: "us/states/nc/districts/senate/36"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nc/districts/house/94"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Alexander County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36412 |
| Under 18 | 7144 |
| 18–64 | 21547 |
| 65+ | 7721 |
| Median household income | 65354 |
| Poverty rate | 12.57 |
| Homeownership rate | 80.68 |
| Unemployment rate | 5.03 |
| Median home value | 211800 |
| Gini index | 0.4417 |
| Vacancy rate | 12.9 |
| White | 31805 |
| Black | 1828 |
| Asian | 363 |
| Native | 368 |
| Hispanic/Latino | 2031 |
| Bachelor's or higher | 5902 |

## Districts

- [NC-05](/us/states/nc/districts/05.md) — 100% (congressional)
- [NC Senate District 36](/us/states/nc/districts/senate/36.md) — 100% (state senate)
- [NC House District 94](/us/states/nc/districts/house/94.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
