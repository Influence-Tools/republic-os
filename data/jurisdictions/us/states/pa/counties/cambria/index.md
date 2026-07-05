---
type: Jurisdiction
title: "Cambria County, PA"
classification: county
fips: "42021"
state: "PA"
demographics:
  population: 131538
  population_under_18: 25261
  population_18_64: 74787
  population_65_plus: 31490
  median_household_income: 58418
  poverty_rate: 14.23
  homeownership_rate: 76.37
  unemployment_rate: 4.65
  median_home_value: 121000
  gini_index: 0.4592
  vacancy_rate: 13.16
  race_white: 119720
  race_black: 4024
  race_asian: 754
  race_native: 62
  hispanic: 2796
  bachelors_plus: 30434
districts:
  - to: "us/states/pa/districts/13"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/pa/districts/senate/35"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/pa/districts/house/71"
    rel: in-district
    area_weight: 0.5192
  - to: "us/states/pa/districts/house/72"
    rel: in-district
    area_weight: 0.3168
  - to: "us/states/pa/districts/house/73"
    rel: in-district
    area_weight: 0.164
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Cambria County, PA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 131538 |
| Under 18 | 25261 |
| 18–64 | 74787 |
| 65+ | 31490 |
| Median household income | 58418 |
| Poverty rate | 14.23 |
| Homeownership rate | 76.37 |
| Unemployment rate | 4.65 |
| Median home value | 121000 |
| Gini index | 0.4592 |
| Vacancy rate | 13.16 |
| White | 119720 |
| Black | 4024 |
| Asian | 754 |
| Native | 62 |
| Hispanic/Latino | 2796 |
| Bachelor's or higher | 30434 |

## Districts

- [PA-13](/us/states/pa/districts/13.md) — 100% (congressional)
- [PA Senate District 35](/us/states/pa/districts/senate/35.md) — 100% (state senate)
- [PA House District 71](/us/states/pa/districts/house/71.md) — 52% (state house)
- [PA House District 72](/us/states/pa/districts/house/72.md) — 32% (state house)
- [PA House District 73](/us/states/pa/districts/house/73.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
