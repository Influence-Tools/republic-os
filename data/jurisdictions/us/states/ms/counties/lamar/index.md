---
type: Jurisdiction
title: "Lamar County, MS"
classification: county
fips: "28073"
state: "MS"
demographics:
  population: 65713
  population_under_18: 15975
  population_18_64: 39676
  population_65_plus: 10062
  median_household_income: 70909
  poverty_rate: 14.68
  homeownership_rate: 69.53
  unemployment_rate: 4.83
  median_home_value: 224700
  gini_index: 0.4693
  vacancy_rate: 8.32
  race_white: 46820
  race_black: 14306
  race_asian: 611
  race_native: 118
  hispanic: 2419
  bachelors_plus: 21044
districts:
  - to: "us/states/ms/districts/04"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ms/districts/senate/44"
    rel: in-district
    area_weight: 0.7853
  - to: "us/states/ms/districts/senate/41"
    rel: in-district
    area_weight: 0.2146
  - to: "us/states/ms/districts/house/87"
    rel: in-district
    area_weight: 0.3702
  - to: "us/states/ms/districts/house/99"
    rel: in-district
    area_weight: 0.3062
  - to: "us/states/ms/districts/house/100"
    rel: in-district
    area_weight: 0.1808
  - to: "us/states/ms/districts/house/106"
    rel: in-district
    area_weight: 0.0756
  - to: "us/states/ms/districts/house/101"
    rel: in-district
    area_weight: 0.0661
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Lamar County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 65713 |
| Under 18 | 15975 |
| 18–64 | 39676 |
| 65+ | 10062 |
| Median household income | 70909 |
| Poverty rate | 14.68 |
| Homeownership rate | 69.53 |
| Unemployment rate | 4.83 |
| Median home value | 224700 |
| Gini index | 0.4693 |
| Vacancy rate | 8.32 |
| White | 46820 |
| Black | 14306 |
| Asian | 611 |
| Native | 118 |
| Hispanic/Latino | 2419 |
| Bachelor's or higher | 21044 |

## Districts

- [MS-04](/us/states/ms/districts/04.md) — 100% (congressional)
- [MS Senate District 44](/us/states/ms/districts/senate/44.md) — 79% (state senate)
- [MS Senate District 41](/us/states/ms/districts/senate/41.md) — 21% (state senate)
- [MS House District 87](/us/states/ms/districts/house/87.md) — 37% (state house)
- [MS House District 99](/us/states/ms/districts/house/99.md) — 31% (state house)
- [MS House District 100](/us/states/ms/districts/house/100.md) — 18% (state house)
- [MS House District 106](/us/states/ms/districts/house/106.md) — 8% (state house)
- [MS House District 101](/us/states/ms/districts/house/101.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
