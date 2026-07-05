---
type: Jurisdiction
title: "Halifax County, NC"
classification: county
fips: "37083"
state: "NC"
demographics:
  population: 47675
  population_under_18: 10113
  population_18_64: 27047
  population_65_plus: 10515
  median_household_income: 45590
  poverty_rate: 22.82
  homeownership_rate: 62.94
  unemployment_rate: 9.27
  median_home_value: 106200
  gini_index: 0.4835
  vacancy_rate: 18.05
  race_white: 17676
  race_black: 24627
  race_asian: 438
  race_native: 1378
  hispanic: 1612
  bachelors_plus: 7258
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nc/districts/senate/2"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/nc/districts/house/27"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Halifax County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47675 |
| Under 18 | 10113 |
| 18–64 | 27047 |
| 65+ | 10515 |
| Median household income | 45590 |
| Poverty rate | 22.82 |
| Homeownership rate | 62.94 |
| Unemployment rate | 9.27 |
| Median home value | 106200 |
| Gini index | 0.4835 |
| Vacancy rate | 18.05 |
| White | 17676 |
| Black | 24627 |
| Asian | 438 |
| Native | 1378 |
| Hispanic/Latino | 1612 |
| Bachelor's or higher | 7258 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 100% (congressional)
- [NC Senate District 2](/us/states/nc/districts/senate/2.md) — 100% (state senate)
- [NC House District 27](/us/states/nc/districts/house/27.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
