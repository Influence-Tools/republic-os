---
type: Jurisdiction
title: "Rowan County, KY"
classification: county
fips: "21205"
state: "KY"
demographics:
  population: 24578
  population_under_18: 4821
  population_18_64: 16074
  population_65_plus: 3683
  median_household_income: 54321
  poverty_rate: 24.22
  homeownership_rate: 61.52
  unemployment_rate: 4.14
  median_home_value: 161800
  gini_index: 0.5101
  vacancy_rate: 9.71
  race_white: 23010
  race_black: 429
  race_asian: 233
  race_native: 124
  hispanic: 588
  bachelors_plus: 5826
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 0.9952
  - to: "us/states/ky/districts/senate/27"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/ky/districts/house/99"
    rel: in-district
    area_weight: 0.999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Rowan County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24578 |
| Under 18 | 4821 |
| 18–64 | 16074 |
| 65+ | 3683 |
| Median household income | 54321 |
| Poverty rate | 24.22 |
| Homeownership rate | 61.52 |
| Unemployment rate | 4.14 |
| Median home value | 161800 |
| Gini index | 0.5101 |
| Vacancy rate | 9.71 |
| White | 23010 |
| Black | 429 |
| Asian | 233 |
| Native | 124 |
| Hispanic/Latino | 588 |
| Bachelor's or higher | 5826 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 27](/us/states/ky/districts/senate/27.md) — 100% (state senate)
- [KY House District 99](/us/states/ky/districts/house/99.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
