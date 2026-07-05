---
type: Jurisdiction
title: "Grant Parish, LA"
classification: county
fips: "22043"
state: "LA"
demographics:
  population: 22095
  population_under_18: 4614
  population_18_64: 14003
  population_65_plus: 3478
  median_household_income: 64016
  poverty_rate: 17.04
  homeownership_rate: 79.42
  unemployment_rate: 3.7
  median_home_value: 143300
  gini_index: 0.4299
  vacancy_rate: 18.34
  race_white: 17155
  race_black: 3348
  race_asian: 185
  race_native: 243
  hispanic: 1389
  bachelors_plus: 3019
districts:
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 0.9928
  - to: "us/states/la/districts/senate/35"
    rel: in-district
    area_weight: 0.7033
  - to: "us/states/la/districts/senate/29"
    rel: in-district
    area_weight: 0.2964
  - to: "us/states/la/districts/house/22"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Grant Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22095 |
| Under 18 | 4614 |
| 18–64 | 14003 |
| 65+ | 3478 |
| Median household income | 64016 |
| Poverty rate | 17.04 |
| Homeownership rate | 79.42 |
| Unemployment rate | 3.7 |
| Median home value | 143300 |
| Gini index | 0.4299 |
| Vacancy rate | 18.34 |
| White | 17155 |
| Black | 3348 |
| Asian | 185 |
| Native | 243 |
| Hispanic/Latino | 1389 |
| Bachelor's or higher | 3019 |

## Districts

- [LA-04](/us/states/la/districts/04.md) — 99% (congressional)
- [LA Senate District 35](/us/states/la/districts/senate/35.md) — 70% (state senate)
- [LA Senate District 29](/us/states/la/districts/senate/29.md) — 30% (state senate)
- [LA House District 22](/us/states/la/districts/house/22.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
