---
type: Jurisdiction
title: "Pike County, OH"
classification: county
fips: "39131"
state: "OH"
demographics:
  population: 27044
  population_under_18: 6344
  population_18_64: 15545
  population_65_plus: 5155
  median_household_income: 52736
  poverty_rate: 21.33
  homeownership_rate: 68.47
  unemployment_rate: 5.35
  median_home_value: 163800
  gini_index: 0.5208
  vacancy_rate: 10.25
  race_white: 25666
  race_black: 260
  race_asian: 117
  race_native: 27
  hispanic: 150
  bachelors_plus: 4053
districts:
  - to: "us/states/oh/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/oh/districts/senate/17"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/house/91"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Pike County, OH

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27044 |
| Under 18 | 6344 |
| 18–64 | 15545 |
| 65+ | 5155 |
| Median household income | 52736 |
| Poverty rate | 21.33 |
| Homeownership rate | 68.47 |
| Unemployment rate | 5.35 |
| Median home value | 163800 |
| Gini index | 0.5208 |
| Vacancy rate | 10.25 |
| White | 25666 |
| Black | 260 |
| Asian | 117 |
| Native | 27 |
| Hispanic/Latino | 150 |
| Bachelor's or higher | 4053 |

## Districts

- [OH-02](/us/states/oh/districts/02.md) — 100% (congressional)
- [OH Senate District 17](/us/states/oh/districts/senate/17.md) — 100% (state senate)
- [OH House District 91](/us/states/oh/districts/house/91.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
