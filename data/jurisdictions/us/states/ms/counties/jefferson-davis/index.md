---
type: Jurisdiction
title: "Jefferson Davis County, MS"
classification: county
fips: "28065"
state: "MS"
demographics:
  population: 11117
  population_under_18: 2204
  population_18_64: 6181
  population_65_plus: 2732
  median_household_income: 38548
  poverty_rate: 28.67
  homeownership_rate: 84.46
  unemployment_rate: 9.57
  median_home_value: 90100
  gini_index: 0.461
  vacancy_rate: 21.9
  race_white: 4251
  race_black: 6613
  race_asian: 3
  race_native: 5
  hispanic: 80
  bachelors_plus: 1371
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/35"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ms/districts/house/91"
    rel: in-district
    area_weight: 0.8895
  - to: "us/states/ms/districts/house/90"
    rel: in-district
    area_weight: 0.1104
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Jefferson Davis County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11117 |
| Under 18 | 2204 |
| 18–64 | 6181 |
| 65+ | 2732 |
| Median household income | 38548 |
| Poverty rate | 28.67 |
| Homeownership rate | 84.46 |
| Unemployment rate | 9.57 |
| Median home value | 90100 |
| Gini index | 0.461 |
| Vacancy rate | 21.9 |
| White | 4251 |
| Black | 6613 |
| Asian | 3 |
| Native | 5 |
| Hispanic/Latino | 80 |
| Bachelor's or higher | 1371 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 100% (congressional)
- [MS Senate District 35](/us/states/ms/districts/senate/35.md) — 100% (state senate)
- [MS House District 91](/us/states/ms/districts/house/91.md) — 89% (state house)
- [MS House District 90](/us/states/ms/districts/house/90.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
