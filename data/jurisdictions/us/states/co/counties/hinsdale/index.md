---
type: Jurisdiction
title: "Hinsdale County, CO"
classification: county
fips: "08053"
state: "CO"
demographics:
  population: 1005
  population_under_18: 186
  population_18_64: 508
  population_65_plus: 311
  median_household_income: 75972
  poverty_rate: 4.08
  homeownership_rate: 76.13
  unemployment_rate: 0.0
  median_home_value: 437900
  gini_index: 0.3771
  vacancy_rate: 61.95
  race_white: 870
  race_black: 3
  race_asian: 0
  race_native: 29
  hispanic: 19
  bachelors_plus: 494
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/senate/5"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/co/districts/house/58"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Hinsdale County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1005 |
| Under 18 | 186 |
| 18–64 | 508 |
| 65+ | 311 |
| Median household income | 75972 |
| Poverty rate | 4.08 |
| Homeownership rate | 76.13 |
| Unemployment rate | 0.0 |
| Median home value | 437900 |
| Gini index | 0.3771 |
| Vacancy rate | 61.95 |
| White | 870 |
| Black | 3 |
| Asian | 0 |
| Native | 29 |
| Hispanic/Latino | 19 |
| Bachelor's or higher | 494 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 5](/us/states/co/districts/senate/5.md) — 100% (state senate)
- [CO House District 58](/us/states/co/districts/house/58.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
