---
type: Jurisdiction
title: "Pulaski County, IN"
classification: county
fips: "18131"
state: "IN"
demographics:
  population: 12441
  population_under_18: 2746
  population_18_64: 7036
  population_65_plus: 2659
  median_household_income: 62792
  poverty_rate: 12.12
  homeownership_rate: 74.59
  unemployment_rate: 1.83
  median_home_value: 156400
  gini_index: 0.4214
  vacancy_rate: 15.38
  race_white: 11399
  race_black: 31
  race_asian: 46
  race_native: 7
  hispanic: 526
  bachelors_plus: 1614
districts:
  - to: "us/states/in/districts/02"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/in/districts/senate/5"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/house/16"
    rel: in-district
    area_weight: 0.7598
  - to: "us/states/in/districts/house/17"
    rel: in-district
    area_weight: 0.2401
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Pulaski County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12441 |
| Under 18 | 2746 |
| 18–64 | 7036 |
| 65+ | 2659 |
| Median household income | 62792 |
| Poverty rate | 12.12 |
| Homeownership rate | 74.59 |
| Unemployment rate | 1.83 |
| Median home value | 156400 |
| Gini index | 0.4214 |
| Vacancy rate | 15.38 |
| White | 11399 |
| Black | 31 |
| Asian | 46 |
| Native | 7 |
| Hispanic/Latino | 526 |
| Bachelor's or higher | 1614 |

## Districts

- [IN-02](/us/states/in/districts/02.md) — 100% (congressional)
- [IN Senate District 5](/us/states/in/districts/senate/5.md) — 100% (state senate)
- [IN House District 16](/us/states/in/districts/house/16.md) — 76% (state house)
- [IN House District 17](/us/states/in/districts/house/17.md) — 24% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
