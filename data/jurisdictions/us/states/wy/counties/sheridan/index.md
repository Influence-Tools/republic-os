---
type: Jurisdiction
title: "Sheridan County, WY"
classification: county
fips: "56033"
state: "WY"
demographics:
  population: 32055
  population_under_18: 6839
  population_18_64: 18036
  population_65_plus: 7180
  median_household_income: 71388
  poverty_rate: 10.23
  homeownership_rate: 70.65
  unemployment_rate: 2.16
  median_home_value: 394900
  gini_index: 0.4437
  vacancy_rate: 10.45
  race_white: 29234
  race_black: 221
  race_asian: 318
  race_native: 282
  hispanic: 1596
  bachelors_plus: 9734
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wy/districts/senate/22"
    rel: in-district
    area_weight: 0.5271
  - to: "us/states/wy/districts/senate/21"
    rel: in-district
    area_weight: 0.4727
  - to: "us/states/wy/districts/house/51"
    rel: in-district
    area_weight: 0.4378
  - to: "us/states/wy/districts/house/40"
    rel: in-district
    area_weight: 0.3215
  - to: "us/states/wy/districts/house/30"
    rel: in-district
    area_weight: 0.238
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Sheridan County, WY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32055 |
| Under 18 | 6839 |
| 18–64 | 18036 |
| 65+ | 7180 |
| Median household income | 71388 |
| Poverty rate | 10.23 |
| Homeownership rate | 70.65 |
| Unemployment rate | 2.16 |
| Median home value | 394900 |
| Gini index | 0.4437 |
| Vacancy rate | 10.45 |
| White | 29234 |
| Black | 221 |
| Asian | 318 |
| Native | 282 |
| Hispanic/Latino | 1596 |
| Bachelor's or higher | 9734 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 22](/us/states/wy/districts/senate/22.md) — 53% (state senate)
- [WY Senate District 21](/us/states/wy/districts/senate/21.md) — 47% (state senate)
- [WY House District 51](/us/states/wy/districts/house/51.md) — 44% (state house)
- [WY House District 40](/us/states/wy/districts/house/40.md) — 32% (state house)
- [WY House District 30](/us/states/wy/districts/house/30.md) — 24% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
