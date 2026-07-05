---
type: Jurisdiction
title: "Person County, NC"
classification: county
fips: "37145"
state: "NC"
demographics:
  population: 39542
  population_under_18: 8159
  population_18_64: 22965
  population_65_plus: 8418
  median_household_income: 63300
  poverty_rate: 17.49
  homeownership_rate: 77.28
  unemployment_rate: 5.58
  median_home_value: 213900
  gini_index: 0.4777
  vacancy_rate: 13.57
  race_white: 25705
  race_black: 10220
  race_asian: 43
  race_native: 43
  hispanic: 2499
  bachelors_plus: 7237
districts:
  - to: "us/states/nc/districts/13"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/nc/districts/senate/23"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/nc/districts/house/2"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Person County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39542 |
| Under 18 | 8159 |
| 18–64 | 22965 |
| 65+ | 8418 |
| Median household income | 63300 |
| Poverty rate | 17.49 |
| Homeownership rate | 77.28 |
| Unemployment rate | 5.58 |
| Median home value | 213900 |
| Gini index | 0.4777 |
| Vacancy rate | 13.57 |
| White | 25705 |
| Black | 10220 |
| Asian | 43 |
| Native | 43 |
| Hispanic/Latino | 2499 |
| Bachelor's or higher | 7237 |

## Districts

- [NC-13](/us/states/nc/districts/13.md) — 100% (congressional)
- [NC Senate District 23](/us/states/nc/districts/senate/23.md) — 100% (state senate)
- [NC House District 2](/us/states/nc/districts/house/2.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
