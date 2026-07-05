---
type: Jurisdiction
title: "Bollinger County, MO"
classification: county
fips: "29017"
state: "MO"
demographics:
  population: 10559
  population_under_18: 2296
  population_18_64: 6031
  population_65_plus: 2232
  median_household_income: 63814
  poverty_rate: 13.63
  homeownership_rate: 82.29
  unemployment_rate: 3.46
  median_home_value: 179800
  gini_index: 0.3995
  vacancy_rate: 21.9
  race_white: 10007
  race_black: 89
  race_asian: 5
  race_native: 3
  hispanic: 175
  bachelors_plus: 1493
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/27"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/house/151"
    rel: in-district
    area_weight: 0.5677
  - to: "us/states/mo/districts/house/144"
    rel: in-district
    area_weight: 0.4322
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Bollinger County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10559 |
| Under 18 | 2296 |
| 18–64 | 6031 |
| 65+ | 2232 |
| Median household income | 63814 |
| Poverty rate | 13.63 |
| Homeownership rate | 82.29 |
| Unemployment rate | 3.46 |
| Median home value | 179800 |
| Gini index | 0.3995 |
| Vacancy rate | 21.9 |
| White | 10007 |
| Black | 89 |
| Asian | 5 |
| Native | 3 |
| Hispanic/Latino | 175 |
| Bachelor's or higher | 1493 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 27](/us/states/mo/districts/senate/27.md) — 100% (state senate)
- [MO House District 151](/us/states/mo/districts/house/151.md) — 57% (state house)
- [MO House District 144](/us/states/mo/districts/house/144.md) — 43% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
