---
type: Jurisdiction
title: "Larue County, KY"
classification: county
fips: "21123"
state: "KY"
demographics:
  population: 15107
  population_under_18: 3401
  population_18_64: 8969
  population_65_plus: 2737
  median_household_income: 67067
  poverty_rate: 17.91
  homeownership_rate: 79.39
  unemployment_rate: 1.52
  median_home_value: 183500
  gini_index: 0.4022
  vacancy_rate: 8.78
  race_white: 13764
  race_black: 318
  race_asian: 3
  race_native: 7
  hispanic: 502
  bachelors_plus: 2503
districts:
  - to: "us/states/ky/districts/02"
    rel: in-district
    area_weight: 0.9967
  - to: "us/states/ky/districts/senate/14"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ky/districts/house/24"
    rel: in-district
    area_weight: 0.9991
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Larue County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15107 |
| Under 18 | 3401 |
| 18–64 | 8969 |
| 65+ | 2737 |
| Median household income | 67067 |
| Poverty rate | 17.91 |
| Homeownership rate | 79.39 |
| Unemployment rate | 1.52 |
| Median home value | 183500 |
| Gini index | 0.4022 |
| Vacancy rate | 8.78 |
| White | 13764 |
| Black | 318 |
| Asian | 3 |
| Native | 7 |
| Hispanic/Latino | 502 |
| Bachelor's or higher | 2503 |

## Districts

- [KY-02](/us/states/ky/districts/02.md) — 100% (congressional)
- [KY Senate District 14](/us/states/ky/districts/senate/14.md) — 100% (state senate)
- [KY House District 24](/us/states/ky/districts/house/24.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
