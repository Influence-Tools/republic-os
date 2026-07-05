---
type: Jurisdiction
title: "Northumberland County, PA"
classification: county
fips: "42097"
state: "PA"
demographics:
  population: 90560
  population_under_18: 17819
  population_18_64: 52537
  population_65_plus: 20204
  median_household_income: 60583
  poverty_rate: 12.59
  homeownership_rate: 75.47
  unemployment_rate: 3.69
  median_home_value: 162400
  gini_index: 0.4277
  vacancy_rate: 12.7
  race_white: 81389
  race_black: 2372
  race_asian: 382
  race_native: 91
  hispanic: 4702
  bachelors_plus: 16873
districts:
  - to: "us/states/pa/districts/09"
    rel: in-district
    area_weight: 0.9951
  - to: "us/states/pa/districts/senate/27"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/pa/districts/house/107"
    rel: in-district
    area_weight: 0.5588
  - to: "us/states/pa/districts/house/108"
    rel: in-district
    area_weight: 0.4409
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Northumberland County, PA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 90560 |
| Under 18 | 17819 |
| 18–64 | 52537 |
| 65+ | 20204 |
| Median household income | 60583 |
| Poverty rate | 12.59 |
| Homeownership rate | 75.47 |
| Unemployment rate | 3.69 |
| Median home value | 162400 |
| Gini index | 0.4277 |
| Vacancy rate | 12.7 |
| White | 81389 |
| Black | 2372 |
| Asian | 382 |
| Native | 91 |
| Hispanic/Latino | 4702 |
| Bachelor's or higher | 16873 |

## Districts

- [PA-09](/us/states/pa/districts/09.md) — 100% (congressional)
- [PA Senate District 27](/us/states/pa/districts/senate/27.md) — 100% (state senate)
- [PA House District 107](/us/states/pa/districts/house/107.md) — 56% (state house)
- [PA House District 108](/us/states/pa/districts/house/108.md) — 44% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
