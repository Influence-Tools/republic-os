---
type: Jurisdiction
title: "Susquehanna County, PA"
classification: county
fips: "42115"
state: "PA"
demographics:
  population: 38219
  population_under_18: 7194
  population_18_64: 21402
  population_65_plus: 9623
  median_household_income: 68487
  poverty_rate: 11.41
  homeownership_rate: 78.48
  unemployment_rate: 5.87
  median_home_value: 216400
  gini_index: 0.4711
  vacancy_rate: 27.31
  race_white: 36197
  race_black: 99
  race_asian: 177
  race_native: 31
  hispanic: 924
  bachelors_plus: 7591
districts:
  - to: "us/states/pa/districts/09"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/pa/districts/senate/20"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/pa/districts/house/111"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Susquehanna County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 38219 |
| Under 18 | 7194 |
| 18–64 | 21402 |
| 65+ | 9623 |
| Median household income | 68487 |
| Poverty rate | 11.41 |
| Homeownership rate | 78.48 |
| Unemployment rate | 5.87 |
| Median home value | 216400 |
| Gini index | 0.4711 |
| Vacancy rate | 27.31 |
| White | 36197 |
| Black | 99 |
| Asian | 177 |
| Native | 31 |
| Hispanic/Latino | 924 |
| Bachelor's or higher | 7591 |

## Districts

- [PA-09](/us/states/pa/districts/09.md) — 100% (congressional)
- [PA Senate District 20](/us/states/pa/districts/senate/20.md) — 100% (state senate)
- [PA House District 111](/us/states/pa/districts/house/111.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
