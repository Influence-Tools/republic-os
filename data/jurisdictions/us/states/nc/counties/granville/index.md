---
type: Jurisdiction
title: "Granville County, NC"
classification: county
fips: "37077"
state: "NC"
demographics:
  population: 60877
  population_under_18: 12593
  population_18_64: 37513
  population_65_plus: 10771
  median_household_income: 71111
  poverty_rate: 15.18
  homeownership_rate: 77.09
  unemployment_rate: 4.57
  median_home_value: 247700
  gini_index: 0.4469
  vacancy_rate: 9.33
  race_white: 34534
  race_black: 17711
  race_asian: 225
  race_native: 274
  hispanic: 6751
  bachelors_plus: 14675
districts:
  - to: "us/states/nc/districts/13"
    rel: in-district
    area_weight: 0.9415
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.0581
  - to: "us/states/nc/districts/senate/18"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/32"
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

# Granville County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 60877 |
| Under 18 | 12593 |
| 18–64 | 37513 |
| 65+ | 10771 |
| Median household income | 71111 |
| Poverty rate | 15.18 |
| Homeownership rate | 77.09 |
| Unemployment rate | 4.57 |
| Median home value | 247700 |
| Gini index | 0.4469 |
| Vacancy rate | 9.33 |
| White | 34534 |
| Black | 17711 |
| Asian | 225 |
| Native | 274 |
| Hispanic/Latino | 6751 |
| Bachelor's or higher | 14675 |

## Districts

- [NC-13](/us/states/nc/districts/13.md) — 94% (congressional)
- [NC-01](/us/states/nc/districts/01.md) — 6% (congressional)
- [NC Senate District 18](/us/states/nc/districts/senate/18.md) — 100% (state senate)
- [NC House District 32](/us/states/nc/districts/house/32.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
