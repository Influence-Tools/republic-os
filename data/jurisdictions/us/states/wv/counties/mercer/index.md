---
type: Jurisdiction
title: "Mercer County, WV"
classification: county
fips: "54055"
state: "WV"
demographics:
  population: 58563
  population_under_18: 12204
  population_18_64: 32966
  population_65_plus: 13393
  median_household_income: 53210
  poverty_rate: 16.49
  homeownership_rate: 72.87
  unemployment_rate: 2.65
  median_home_value: 121700
  gini_index: 0.4513
  vacancy_rate: 17.45
  race_white: 52059
  race_black: 2372
  race_asian: 127
  race_native: 245
  hispanic: 789
  bachelors_plus: 12898
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/wv/districts/senate/6"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/wv/districts/house/39"
    rel: in-district
    area_weight: 0.4292
  - to: "us/states/wv/districts/house/41"
    rel: in-district
    area_weight: 0.2466
  - to: "us/states/wv/districts/house/37"
    rel: in-district
    area_weight: 0.2246
  - to: "us/states/wv/districts/house/38"
    rel: in-district
    area_weight: 0.0991
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Mercer County, WV

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 58563 |
| Under 18 | 12204 |
| 18–64 | 32966 |
| 65+ | 13393 |
| Median household income | 53210 |
| Poverty rate | 16.49 |
| Homeownership rate | 72.87 |
| Unemployment rate | 2.65 |
| Median home value | 121700 |
| Gini index | 0.4513 |
| Vacancy rate | 17.45 |
| White | 52059 |
| Black | 2372 |
| Asian | 127 |
| Native | 245 |
| Hispanic/Latino | 789 |
| Bachelor's or higher | 12898 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 6](/us/states/wv/districts/senate/6.md) — 100% (state senate)
- [WV House District 39](/us/states/wv/districts/house/39.md) — 43% (state house)
- [WV House District 41](/us/states/wv/districts/house/41.md) — 25% (state house)
- [WV House District 37](/us/states/wv/districts/house/37.md) — 22% (state house)
- [WV House District 38](/us/states/wv/districts/house/38.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
