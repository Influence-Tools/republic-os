---
type: Jurisdiction
title: "Menifee County, KY"
classification: county
fips: "21165"
state: "KY"
demographics:
  population: 6230
  population_under_18: 1311
  population_18_64: 3460
  population_65_plus: 1459
  median_household_income: 45096
  poverty_rate: 26.92
  homeownership_rate: 75.46
  unemployment_rate: 7.9
  median_home_value: 125800
  gini_index: 0.4748
  vacancy_rate: 26.4
  race_white: 6029
  race_black: 9
  race_asian: 0
  race_native: 0
  hispanic: 177
  bachelors_plus: 953
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 0.9948
  - to: "us/states/ky/districts/06"
    rel: in-district
    area_weight: 0.0052
  - to: "us/states/ky/districts/senate/28"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ky/districts/house/74"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Menifee County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6230 |
| Under 18 | 1311 |
| 18–64 | 3460 |
| 65+ | 1459 |
| Median household income | 45096 |
| Poverty rate | 26.92 |
| Homeownership rate | 75.46 |
| Unemployment rate | 7.9 |
| Median home value | 125800 |
| Gini index | 0.4748 |
| Vacancy rate | 26.4 |
| White | 6029 |
| Black | 9 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 177 |
| Bachelor's or higher | 953 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 99% (congressional)
- [KY-06](/us/states/ky/districts/06.md) — 1% (congressional)
- [KY Senate District 28](/us/states/ky/districts/senate/28.md) — 100% (state senate)
- [KY House District 74](/us/states/ky/districts/house/74.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
