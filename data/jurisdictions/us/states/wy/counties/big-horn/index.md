---
type: Jurisdiction
title: "Big Horn County, WY"
classification: county
fips: "56003"
state: "WY"
demographics:
  population: 11828
  population_under_18: 2902
  population_18_64: 6355
  population_65_plus: 2571
  median_household_income: 62101
  poverty_rate: 12.73
  homeownership_rate: 75.9
  unemployment_rate: 3.34
  median_home_value: 216500
  gini_index: 0.4294
  vacancy_rate: 16.98
  race_white: 10444
  race_black: 79
  race_asian: 66
  race_native: 89
  hispanic: 1143
  bachelors_plus: 2439
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wy/districts/senate/19"
    rel: in-district
    area_weight: 0.5766
  - to: "us/states/wy/districts/senate/20"
    rel: in-district
    area_weight: 0.4233
  - to: "us/states/wy/districts/house/26"
    rel: in-district
    area_weight: 0.5766
  - to: "us/states/wy/districts/house/27"
    rel: in-district
    area_weight: 0.2447
  - to: "us/states/wy/districts/house/28"
    rel: in-district
    area_weight: 0.1786
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Big Horn County, WY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11828 |
| Under 18 | 2902 |
| 18–64 | 6355 |
| 65+ | 2571 |
| Median household income | 62101 |
| Poverty rate | 12.73 |
| Homeownership rate | 75.9 |
| Unemployment rate | 3.34 |
| Median home value | 216500 |
| Gini index | 0.4294 |
| Vacancy rate | 16.98 |
| White | 10444 |
| Black | 79 |
| Asian | 66 |
| Native | 89 |
| Hispanic/Latino | 1143 |
| Bachelor's or higher | 2439 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 19](/us/states/wy/districts/senate/19.md) — 58% (state senate)
- [WY Senate District 20](/us/states/wy/districts/senate/20.md) — 42% (state senate)
- [WY House District 26](/us/states/wy/districts/house/26.md) — 58% (state house)
- [WY House District 27](/us/states/wy/districts/house/27.md) — 24% (state house)
- [WY House District 28](/us/states/wy/districts/house/28.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
