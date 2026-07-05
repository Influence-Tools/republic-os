---
type: Jurisdiction
title: "Douglas County, WI"
classification: county
fips: "55031"
state: "WI"
demographics:
  population: 44229
  population_under_18: 8471
  population_18_64: 26613
  population_65_plus: 9145
  median_household_income: 75099
  poverty_rate: 10.76
  homeownership_rate: 71.89
  unemployment_rate: 3.11
  median_home_value: 205800
  gini_index: 0.4137
  vacancy_rate: 17.25
  race_white: 39928
  race_black: 375
  race_asian: 331
  race_native: 621
  hispanic: 860
  bachelors_plus: 11794
districts:
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 0.9065
  - to: "us/states/wi/districts/senate/25"
    rel: in-district
    area_weight: 0.9067
  - to: "us/states/wi/districts/house/74"
    rel: in-district
    area_weight: 0.5833
  - to: "us/states/wi/districts/house/73"
    rel: in-district
    area_weight: 0.3234
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Douglas County, WI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 44229 |
| Under 18 | 8471 |
| 18–64 | 26613 |
| 65+ | 9145 |
| Median household income | 75099 |
| Poverty rate | 10.76 |
| Homeownership rate | 71.89 |
| Unemployment rate | 3.11 |
| Median home value | 205800 |
| Gini index | 0.4137 |
| Vacancy rate | 17.25 |
| White | 39928 |
| Black | 375 |
| Asian | 331 |
| Native | 621 |
| Hispanic/Latino | 860 |
| Bachelor's or higher | 11794 |

## Districts

- [WI-07](/us/states/wi/districts/07.md) — 91% (congressional)
- [WI Senate District 25](/us/states/wi/districts/senate/25.md) — 91% (state senate)
- [WI House District 74](/us/states/wi/districts/house/74.md) — 58% (state house)
- [WI House District 73](/us/states/wi/districts/house/73.md) — 32% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
