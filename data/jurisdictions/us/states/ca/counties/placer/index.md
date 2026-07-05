---
type: Jurisdiction
title: "Placer County, CA"
classification: county
fips: "06061"
state: "CA"
demographics:
  population: 419156
  population_under_18: 91287
  population_18_64: 242047
  population_65_plus: 85822
  median_household_income: 115998
  poverty_rate: 6.76
  homeownership_rate: 74.77
  unemployment_rate: 4.8
  median_home_value: 688100
  gini_index: 0.4467
  vacancy_rate: 11.89
  race_white: 289678
  race_black: 6924
  race_asian: 38592
  race_native: 2075
  hispanic: 65841
  bachelors_plus: 173843
districts:
  - to: "us/states/ca/districts/03"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ca/districts/senate/4"
    rel: in-district
    area_weight: 0.4532
  - to: "us/states/ca/districts/senate/1"
    rel: in-district
    area_weight: 0.2907
  - to: "us/states/ca/districts/senate/6"
    rel: in-district
    area_weight: 0.2561
  - to: "us/states/ca/districts/house/1"
    rel: in-district
    area_weight: 0.7069
  - to: "us/states/ca/districts/house/5"
    rel: in-district
    area_weight: 0.1787
  - to: "us/states/ca/districts/house/3"
    rel: in-district
    area_weight: 0.1143
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Placer County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 419156 |
| Under 18 | 91287 |
| 18–64 | 242047 |
| 65+ | 85822 |
| Median household income | 115998 |
| Poverty rate | 6.76 |
| Homeownership rate | 74.77 |
| Unemployment rate | 4.8 |
| Median home value | 688100 |
| Gini index | 0.4467 |
| Vacancy rate | 11.89 |
| White | 289678 |
| Black | 6924 |
| Asian | 38592 |
| Native | 2075 |
| Hispanic/Latino | 65841 |
| Bachelor's or higher | 173843 |

## Districts

- [CA-03](/us/states/ca/districts/03.md) — 100% (congressional)
- [CA Senate District 4](/us/states/ca/districts/senate/4.md) — 45% (state senate)
- [CA Senate District 1](/us/states/ca/districts/senate/1.md) — 29% (state senate)
- [CA Senate District 6](/us/states/ca/districts/senate/6.md) — 26% (state senate)
- [CA House District 1](/us/states/ca/districts/house/1.md) — 71% (state house)
- [CA House District 5](/us/states/ca/districts/house/5.md) — 18% (state house)
- [CA House District 3](/us/states/ca/districts/house/3.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
