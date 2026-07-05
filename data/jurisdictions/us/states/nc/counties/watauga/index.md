---
type: Jurisdiction
title: "Watauga County, NC"
classification: county
fips: "37189"
state: "NC"
demographics:
  population: 55123
  population_under_18: 6676
  population_18_64: 39012
  population_65_plus: 9435
  median_household_income: 51693
  poverty_rate: 25.45
  homeownership_rate: 62.07
  unemployment_rate: 7.86
  median_home_value: 358900
  gini_index: 0.5394
  vacancy_rate: 36.45
  race_white: 49473
  race_black: 1112
  race_asian: 487
  race_native: 168
  hispanic: 3410
  bachelors_plus: 21722
districts:
  - to: "us/states/nc/districts/05"
    rel: in-district
    area_weight: 0.9973
  - to: "us/states/nc/districts/senate/47"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/nc/districts/house/93"
    rel: in-district
    area_weight: 0.9108
  - to: "us/states/nc/districts/house/87"
    rel: in-district
    area_weight: 0.0885
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Watauga County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 55123 |
| Under 18 | 6676 |
| 18–64 | 39012 |
| 65+ | 9435 |
| Median household income | 51693 |
| Poverty rate | 25.45 |
| Homeownership rate | 62.07 |
| Unemployment rate | 7.86 |
| Median home value | 358900 |
| Gini index | 0.5394 |
| Vacancy rate | 36.45 |
| White | 49473 |
| Black | 1112 |
| Asian | 487 |
| Native | 168 |
| Hispanic/Latino | 3410 |
| Bachelor's or higher | 21722 |

## Districts

- [NC-05](/us/states/nc/districts/05.md) — 100% (congressional)
- [NC Senate District 47](/us/states/nc/districts/senate/47.md) — 100% (state senate)
- [NC House District 93](/us/states/nc/districts/house/93.md) — 91% (state house)
- [NC House District 87](/us/states/nc/districts/house/87.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
