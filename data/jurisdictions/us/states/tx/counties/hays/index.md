---
type: Jurisdiction
title: "Hays County, TX"
classification: county
fips: "48209"
state: "TX"
demographics:
  population: 268638
  population_under_18: 60220
  population_18_64: 175756
  population_65_plus: 32662
  median_household_income: 89097
  poverty_rate: 12.13
  homeownership_rate: 64.14
  unemployment_rate: 4.43
  median_home_value: 399800
  gini_index: 0.4587
  vacancy_rate: 4.61
  race_white: 162563
  race_black: 11062
  race_asian: 5497
  race_native: 1966
  hispanic: 105942
  bachelors_plus: 98680
districts:
  - to: "us/states/tx/districts/21"
    rel: in-district
    area_weight: 0.8196
  - to: "us/states/tx/districts/35"
    rel: in-district
    area_weight: 0.1801
  - to: "us/states/tx/districts/senate/25"
    rel: in-district
    area_weight: 0.6929
  - to: "us/states/tx/districts/senate/21"
    rel: in-district
    area_weight: 0.3071
  - to: "us/states/tx/districts/house/73"
    rel: in-district
    area_weight: 0.5387
  - to: "us/states/tx/districts/house/45"
    rel: in-district
    area_weight: 0.4612
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Hays County, TX

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 268638 |
| Under 18 | 60220 |
| 18–64 | 175756 |
| 65+ | 32662 |
| Median household income | 89097 |
| Poverty rate | 12.13 |
| Homeownership rate | 64.14 |
| Unemployment rate | 4.43 |
| Median home value | 399800 |
| Gini index | 0.4587 |
| Vacancy rate | 4.61 |
| White | 162563 |
| Black | 11062 |
| Asian | 5497 |
| Native | 1966 |
| Hispanic/Latino | 105942 |
| Bachelor's or higher | 98680 |

## Districts

- [TX-21](/us/states/tx/districts/21.md) — 82% (congressional)
- [TX-35](/us/states/tx/districts/35.md) — 18% (congressional)
- [TX Senate District 25](/us/states/tx/districts/senate/25.md) — 69% (state senate)
- [TX Senate District 21](/us/states/tx/districts/senate/21.md) — 31% (state senate)
- [TX House District 73](/us/states/tx/districts/house/73.md) — 54% (state house)
- [TX House District 45](/us/states/tx/districts/house/45.md) — 46% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
