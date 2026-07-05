---
type: Jurisdiction
title: "Conejos County, CO"
classification: county
fips: "08021"
state: "CO"
demographics:
  population: 7530
  population_under_18: 1903
  population_18_64: 4078
  population_65_plus: 1549
  median_household_income: 50978
  poverty_rate: 11.68
  homeownership_rate: 76.52
  unemployment_rate: 4.77
  median_home_value: 193400
  gini_index: 0.4394
  vacancy_rate: 22.94
  race_white: 4172
  race_black: 11
  race_asian: 29
  race_native: 213
  hispanic: 3750
  bachelors_plus: 1792
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/co/districts/senate/6"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/co/districts/house/62"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Conejos County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7530 |
| Under 18 | 1903 |
| 18–64 | 4078 |
| 65+ | 1549 |
| Median household income | 50978 |
| Poverty rate | 11.68 |
| Homeownership rate | 76.52 |
| Unemployment rate | 4.77 |
| Median home value | 193400 |
| Gini index | 0.4394 |
| Vacancy rate | 22.94 |
| White | 4172 |
| Black | 11 |
| Asian | 29 |
| Native | 213 |
| Hispanic/Latino | 3750 |
| Bachelor's or higher | 1792 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 6](/us/states/co/districts/senate/6.md) — 100% (state senate)
- [CO House District 62](/us/states/co/districts/house/62.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
