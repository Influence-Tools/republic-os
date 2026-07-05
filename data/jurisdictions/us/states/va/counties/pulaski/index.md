---
type: Jurisdiction
title: "Pulaski County, VA"
classification: county
fips: "51155"
state: "VA"
demographics:
  population: 33687
  population_under_18: 6002
  population_18_64: 19976
  population_65_plus: 7709
  median_household_income: 62028
  poverty_rate: 14.37
  homeownership_rate: 73.42
  unemployment_rate: 3.21
  median_home_value: 191700
  gini_index: 0.4644
  vacancy_rate: 15.24
  race_white: 30325
  race_black: 1576
  race_asian: 148
  race_native: 17
  hispanic: 749
  bachelors_plus: 7224
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/5"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/va/districts/house/42"
    rel: in-district
    area_weight: 0.7905
  - to: "us/states/va/districts/house/46"
    rel: in-district
    area_weight: 0.2092
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Pulaski County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33687 |
| Under 18 | 6002 |
| 18–64 | 19976 |
| 65+ | 7709 |
| Median household income | 62028 |
| Poverty rate | 14.37 |
| Homeownership rate | 73.42 |
| Unemployment rate | 3.21 |
| Median home value | 191700 |
| Gini index | 0.4644 |
| Vacancy rate | 15.24 |
| White | 30325 |
| Black | 1576 |
| Asian | 148 |
| Native | 17 |
| Hispanic/Latino | 749 |
| Bachelor's or higher | 7224 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 5](/us/states/va/districts/senate/5.md) — 100% (state senate)
- [VA House District 42](/us/states/va/districts/house/42.md) — 79% (state house)
- [VA House District 46](/us/states/va/districts/house/46.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
