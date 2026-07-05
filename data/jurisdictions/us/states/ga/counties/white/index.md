---
type: Jurisdiction
title: "White County, GA"
classification: county
fips: "13311"
state: "GA"
demographics:
  population: 28810
  population_under_18: 5573
  population_18_64: 16542
  population_65_plus: 6695
  median_household_income: 70666
  poverty_rate: 12.4
  homeownership_rate: 78.82
  unemployment_rate: 3.78
  median_home_value: 278900
  gini_index: 0.4453
  vacancy_rate: 23.1
  race_white: 25899
  race_black: 538
  race_asian: 165
  race_native: 34
  hispanic: 1091
  bachelors_plus: 6934
districts:
  - to: "us/states/ga/districts/09"
    rel: in-district
    area_weight: 0.9972
  - to: "us/states/ga/districts/senate/50"
    rel: in-district
    area_weight: 0.562
  - to: "us/states/ga/districts/senate/51"
    rel: in-district
    area_weight: 0.4379
  - to: "us/states/ga/districts/house/8"
    rel: in-district
    area_weight: 0.8404
  - to: "us/states/ga/districts/house/9"
    rel: in-district
    area_weight: 0.1592
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# White County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28810 |
| Under 18 | 5573 |
| 18–64 | 16542 |
| 65+ | 6695 |
| Median household income | 70666 |
| Poverty rate | 12.4 |
| Homeownership rate | 78.82 |
| Unemployment rate | 3.78 |
| Median home value | 278900 |
| Gini index | 0.4453 |
| Vacancy rate | 23.1 |
| White | 25899 |
| Black | 538 |
| Asian | 165 |
| Native | 34 |
| Hispanic/Latino | 1091 |
| Bachelor's or higher | 6934 |

## Districts

- [GA-09](/us/states/ga/districts/09.md) — 100% (congressional)
- [GA Senate District 50](/us/states/ga/districts/senate/50.md) — 56% (state senate)
- [GA Senate District 51](/us/states/ga/districts/senate/51.md) — 44% (state senate)
- [GA House District 8](/us/states/ga/districts/house/8.md) — 84% (state house)
- [GA House District 9](/us/states/ga/districts/house/9.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
