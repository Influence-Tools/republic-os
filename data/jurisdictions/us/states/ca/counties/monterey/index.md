---
type: Jurisdiction
title: "Monterey County, CA"
classification: county
fips: "06053"
state: "CA"
demographics:
  population: 437613
  population_under_18: 112274
  population_18_64: 260271
  population_65_plus: 65068
  median_household_income: 97230
  poverty_rate: 12.73
  homeownership_rate: 52.07
  unemployment_rate: 5.2
  median_home_value: 781000
  gini_index: 0.4642
  vacancy_rate: 8.92
  race_white: 158316
  race_black: 9414
  race_asian: 25129
  race_native: 3800
  hispanic: 269490
  bachelors_plus: 111881
districts:
  - to: "us/states/ca/districts/18"
    rel: in-district
    area_weight: 0.6412
  - to: "us/states/ca/districts/19"
    rel: in-district
    area_weight: 0.2366
  - to: "us/states/ca/districts/senate/17"
    rel: in-district
    area_weight: 0.8782
  - to: "us/states/ca/districts/house/30"
    rel: in-district
    area_weight: 0.541
  - to: "us/states/ca/districts/house/29"
    rel: in-district
    area_weight: 0.3372
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Monterey County, CA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 437613 |
| Under 18 | 112274 |
| 18–64 | 260271 |
| 65+ | 65068 |
| Median household income | 97230 |
| Poverty rate | 12.73 |
| Homeownership rate | 52.07 |
| Unemployment rate | 5.2 |
| Median home value | 781000 |
| Gini index | 0.4642 |
| Vacancy rate | 8.92 |
| White | 158316 |
| Black | 9414 |
| Asian | 25129 |
| Native | 3800 |
| Hispanic/Latino | 269490 |
| Bachelor's or higher | 111881 |

## Districts

- [CA-18](/us/states/ca/districts/18.md) — 64% (congressional)
- [CA-19](/us/states/ca/districts/19.md) — 24% (congressional)
- [CA Senate District 17](/us/states/ca/districts/senate/17.md) — 88% (state senate)
- [CA House District 30](/us/states/ca/districts/house/30.md) — 54% (state house)
- [CA House District 29](/us/states/ca/districts/house/29.md) — 34% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
