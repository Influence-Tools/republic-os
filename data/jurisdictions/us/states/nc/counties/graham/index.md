---
type: Jurisdiction
title: "Graham County, NC"
classification: county
fips: "37075"
state: "NC"
demographics:
  population: 8072
  population_under_18: 1544
  population_18_64: 4466
  population_65_plus: 2062
  median_household_income: 49684
  poverty_rate: 6.7
  homeownership_rate: 80.7
  unemployment_rate: 7.02
  median_home_value: 170600
  gini_index: 0.4082
  vacancy_rate: 32.75
  race_white: 6853
  race_black: 30
  race_asian: 54
  race_native: 817
  hispanic: 240
  bachelors_plus: 1379
districts:
  - to: "us/states/nc/districts/11"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/nc/districts/senate/50"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/nc/districts/house/120"
    rel: in-district
    area_weight: 0.9988
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Graham County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8072 |
| Under 18 | 1544 |
| 18–64 | 4466 |
| 65+ | 2062 |
| Median household income | 49684 |
| Poverty rate | 6.7 |
| Homeownership rate | 80.7 |
| Unemployment rate | 7.02 |
| Median home value | 170600 |
| Gini index | 0.4082 |
| Vacancy rate | 32.75 |
| White | 6853 |
| Black | 30 |
| Asian | 54 |
| Native | 817 |
| Hispanic/Latino | 240 |
| Bachelor's or higher | 1379 |

## Districts

- [NC-11](/us/states/nc/districts/11.md) — 100% (congressional)
- [NC Senate District 50](/us/states/nc/districts/senate/50.md) — 100% (state senate)
- [NC House District 120](/us/states/nc/districts/house/120.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
