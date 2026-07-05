---
type: Jurisdiction
title: "Conecuh County, AL"
classification: county
fips: "01035"
state: "AL"
demographics:
  population: 11275
  population_under_18: 2261
  population_18_64: 6205
  population_65_plus: 2809
  median_household_income: 41327
  poverty_rate: 27.85
  homeownership_rate: 74.33
  unemployment_rate: 8.7
  median_home_value: 105300
  gini_index: 0.5089
  vacancy_rate: 31.46
  race_white: 5660
  race_black: 5101
  race_asian: 9
  race_native: 22
  hispanic: 117
  bachelors_plus: 1559
districts:
  - to: "us/states/al/districts/02"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/al/districts/senate/23"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/al/districts/house/90"
    rel: in-district
    area_weight: 0.5484
  - to: "us/states/al/districts/house/68"
    rel: in-district
    area_weight: 0.4514
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Conecuh County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11275 |
| Under 18 | 2261 |
| 18–64 | 6205 |
| 65+ | 2809 |
| Median household income | 41327 |
| Poverty rate | 27.85 |
| Homeownership rate | 74.33 |
| Unemployment rate | 8.7 |
| Median home value | 105300 |
| Gini index | 0.5089 |
| Vacancy rate | 31.46 |
| White | 5660 |
| Black | 5101 |
| Asian | 9 |
| Native | 22 |
| Hispanic/Latino | 117 |
| Bachelor's or higher | 1559 |

## Districts

- [AL-02](/us/states/al/districts/02.md) — 100% (congressional)
- [AL Senate District 23](/us/states/al/districts/senate/23.md) — 100% (state senate)
- [AL House District 90](/us/states/al/districts/house/90.md) — 55% (state house)
- [AL House District 68](/us/states/al/districts/house/68.md) — 45% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
