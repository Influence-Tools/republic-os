---
type: Jurisdiction
title: "Jones County, NC"
classification: county
fips: "37103"
state: "NC"
demographics:
  population: 9302
  population_under_18: 1724
  population_18_64: 5330
  population_65_plus: 2248
  median_household_income: 59641
  poverty_rate: 18.36
  homeownership_rate: 79.44
  unemployment_rate: 4.35
  median_home_value: 130300
  gini_index: 0.4496
  vacancy_rate: 12.2
  race_white: 5905
  race_black: 2480
  race_asian: 112
  race_native: 43
  hispanic: 471
  bachelors_plus: 1714
districts:
  - to: "us/states/nc/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nc/districts/senate/9"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/nc/districts/house/12"
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

# Jones County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9302 |
| Under 18 | 1724 |
| 18–64 | 5330 |
| 65+ | 2248 |
| Median household income | 59641 |
| Poverty rate | 18.36 |
| Homeownership rate | 79.44 |
| Unemployment rate | 4.35 |
| Median home value | 130300 |
| Gini index | 0.4496 |
| Vacancy rate | 12.2 |
| White | 5905 |
| Black | 2480 |
| Asian | 112 |
| Native | 43 |
| Hispanic/Latino | 471 |
| Bachelor's or higher | 1714 |

## Districts

- [NC-03](/us/states/nc/districts/03.md) — 100% (congressional)
- [NC Senate District 9](/us/states/nc/districts/senate/9.md) — 100% (state senate)
- [NC House District 12](/us/states/nc/districts/house/12.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
