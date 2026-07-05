---
type: Jurisdiction
title: "Tate County, MS"
classification: county
fips: "28137"
state: "MS"
demographics:
  population: 28321
  population_under_18: 6308
  population_18_64: 17269
  population_65_plus: 4744
  median_household_income: 69704
  poverty_rate: 16.86
  homeownership_rate: 75.96
  unemployment_rate: 4.66
  median_home_value: 209000
  gini_index: 0.41
  vacancy_rate: 5.78
  race_white: 18696
  race_black: 8266
  race_asian: 19
  race_native: 0
  hispanic: 917
  bachelors_plus: 6235
districts:
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/ms/districts/senate/10"
    rel: in-district
    area_weight: 0.6687
  - to: "us/states/ms/districts/senate/11"
    rel: in-district
    area_weight: 0.3307
  - to: "us/states/ms/districts/house/8"
    rel: in-district
    area_weight: 0.798
  - to: "us/states/ms/districts/house/9"
    rel: in-district
    area_weight: 0.1703
  - to: "us/states/ms/districts/house/11"
    rel: in-district
    area_weight: 0.0312
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Tate County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28321 |
| Under 18 | 6308 |
| 18–64 | 17269 |
| 65+ | 4744 |
| Median household income | 69704 |
| Poverty rate | 16.86 |
| Homeownership rate | 75.96 |
| Unemployment rate | 4.66 |
| Median home value | 209000 |
| Gini index | 0.41 |
| Vacancy rate | 5.78 |
| White | 18696 |
| Black | 8266 |
| Asian | 19 |
| Native | 0 |
| Hispanic/Latino | 917 |
| Bachelor's or higher | 6235 |

## Districts

- [MS-01](/us/states/ms/districts/01.md) — 100% (congressional)
- [MS Senate District 10](/us/states/ms/districts/senate/10.md) — 67% (state senate)
- [MS Senate District 11](/us/states/ms/districts/senate/11.md) — 33% (state senate)
- [MS House District 8](/us/states/ms/districts/house/8.md) — 80% (state house)
- [MS House District 9](/us/states/ms/districts/house/9.md) — 17% (state house)
- [MS House District 11](/us/states/ms/districts/house/11.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
