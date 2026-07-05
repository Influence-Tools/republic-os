---
type: Jurisdiction
title: "Huerfano County, CO"
classification: county
fips: "08055"
state: "CO"
demographics:
  population: 6972
  population_under_18: 1088
  population_18_64: 3460
  population_65_plus: 2424
  median_household_income: 52526
  poverty_rate: 17.33
  homeownership_rate: 75.1
  unemployment_rate: 7.96
  median_home_value: 247800
  gini_index: 0.4984
  vacancy_rate: 35.19
  race_white: 5467
  race_black: 0
  race_asian: 15
  race_native: 146
  hispanic: 2136
  bachelors_plus: 2052
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/co/districts/senate/35"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/co/districts/house/47"
    rel: in-district
    area_weight: 0.6267
  - to: "us/states/co/districts/house/62"
    rel: in-district
    area_weight: 0.3732
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Huerfano County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6972 |
| Under 18 | 1088 |
| 18–64 | 3460 |
| 65+ | 2424 |
| Median household income | 52526 |
| Poverty rate | 17.33 |
| Homeownership rate | 75.1 |
| Unemployment rate | 7.96 |
| Median home value | 247800 |
| Gini index | 0.4984 |
| Vacancy rate | 35.19 |
| White | 5467 |
| Black | 0 |
| Asian | 15 |
| Native | 146 |
| Hispanic/Latino | 2136 |
| Bachelor's or higher | 2052 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 35](/us/states/co/districts/senate/35.md) — 100% (state senate)
- [CO House District 47](/us/states/co/districts/house/47.md) — 63% (state house)
- [CO House District 62](/us/states/co/districts/house/62.md) — 37% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
