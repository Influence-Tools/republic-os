---
type: Jurisdiction
title: "Fergus County, MT"
classification: county
fips: "30027"
state: "MT"
demographics:
  population: 11687
  population_under_18: 2456
  population_18_64: 6300
  population_65_plus: 2931
  median_household_income: 63706
  poverty_rate: 15.13
  homeownership_rate: 63.36
  unemployment_rate: 4.21
  median_home_value: 236100
  gini_index: 0.4135
  vacancy_rate: 11.79
  race_white: 10868
  race_black: 66
  race_asian: 76
  race_native: 263
  hispanic: 278
  bachelors_plus: 2518
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/19"
    rel: in-district
    area_weight: 0.8077
  - to: "us/states/mt/districts/senate/39"
    rel: in-district
    area_weight: 0.1922
  - to: "us/states/mt/districts/house/37"
    rel: in-district
    area_weight: 0.8076
  - to: "us/states/mt/districts/house/78"
    rel: in-district
    area_weight: 0.1922
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Fergus County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11687 |
| Under 18 | 2456 |
| 18–64 | 6300 |
| 65+ | 2931 |
| Median household income | 63706 |
| Poverty rate | 15.13 |
| Homeownership rate | 63.36 |
| Unemployment rate | 4.21 |
| Median home value | 236100 |
| Gini index | 0.4135 |
| Vacancy rate | 11.79 |
| White | 10868 |
| Black | 66 |
| Asian | 76 |
| Native | 263 |
| Hispanic/Latino | 278 |
| Bachelor's or higher | 2518 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 19](/us/states/mt/districts/senate/19.md) — 81% (state senate)
- [MT Senate District 39](/us/states/mt/districts/senate/39.md) — 19% (state senate)
- [MT House District 37](/us/states/mt/districts/house/37.md) — 81% (state house)
- [MT House District 78](/us/states/mt/districts/house/78.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
