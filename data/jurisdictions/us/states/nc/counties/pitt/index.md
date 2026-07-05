---
type: Jurisdiction
title: "Pitt County, NC"
classification: county
fips: "37147"
state: "NC"
demographics:
  population: 177193
  population_under_18: 37244
  population_18_64: 114247
  population_65_plus: 25702
  median_household_income: 58188
  poverty_rate: 19.84
  homeownership_rate: 51.45
  unemployment_rate: 7.8
  median_home_value: 208900
  gini_index: 0.4814
  vacancy_rate: 9.81
  race_white: 93301
  race_black: 61982
  race_asian: 3545
  race_native: 663
  hispanic: 13948
  bachelors_plus: 51687
districts:
  - to: "us/states/nc/districts/03"
    rel: in-district
    area_weight: 0.9969
  - to: "us/states/nc/districts/senate/5"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/nc/districts/house/9"
    rel: in-district
    area_weight: 0.5961
  - to: "us/states/nc/districts/house/8"
    rel: in-district
    area_weight: 0.4034
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Pitt County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 177193 |
| Under 18 | 37244 |
| 18–64 | 114247 |
| 65+ | 25702 |
| Median household income | 58188 |
| Poverty rate | 19.84 |
| Homeownership rate | 51.45 |
| Unemployment rate | 7.8 |
| Median home value | 208900 |
| Gini index | 0.4814 |
| Vacancy rate | 9.81 |
| White | 93301 |
| Black | 61982 |
| Asian | 3545 |
| Native | 663 |
| Hispanic/Latino | 13948 |
| Bachelor's or higher | 51687 |

## Districts

- [NC-03](/us/states/nc/districts/03.md) — 100% (congressional)
- [NC Senate District 5](/us/states/nc/districts/senate/5.md) — 100% (state senate)
- [NC House District 9](/us/states/nc/districts/house/9.md) — 60% (state house)
- [NC House District 8](/us/states/nc/districts/house/8.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
