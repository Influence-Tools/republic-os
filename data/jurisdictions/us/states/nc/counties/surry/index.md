---
type: Jurisdiction
title: "Surry County, NC"
classification: county
fips: "37171"
state: "NC"
demographics:
  population: 71425
  population_under_18: 15042
  population_18_64: 41636
  population_65_plus: 14747
  median_household_income: 55656
  poverty_rate: 16.82
  homeownership_rate: 73.42
  unemployment_rate: 4.38
  median_home_value: 177600
  gini_index: 0.4752
  vacancy_rate: 11.49
  race_white: 59905
  race_black: 2692
  race_asian: 476
  race_native: 253
  hispanic: 8952
  bachelors_plus: 13954
districts:
  - to: "us/states/nc/districts/05"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/nc/districts/senate/36"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/nc/districts/house/90"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Surry County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 71425 |
| Under 18 | 15042 |
| 18–64 | 41636 |
| 65+ | 14747 |
| Median household income | 55656 |
| Poverty rate | 16.82 |
| Homeownership rate | 73.42 |
| Unemployment rate | 4.38 |
| Median home value | 177600 |
| Gini index | 0.4752 |
| Vacancy rate | 11.49 |
| White | 59905 |
| Black | 2692 |
| Asian | 476 |
| Native | 253 |
| Hispanic/Latino | 8952 |
| Bachelor's or higher | 13954 |

## Districts

- [NC-05](/us/states/nc/districts/05.md) — 100% (congressional)
- [NC Senate District 36](/us/states/nc/districts/senate/36.md) — 100% (state senate)
- [NC House District 90](/us/states/nc/districts/house/90.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
