---
type: Jurisdiction
title: "Jefferson County, KS"
classification: county
fips: "20087"
state: "KS"
demographics:
  population: 18349
  population_under_18: 4033
  population_18_64: 10650
  population_65_plus: 3666
  median_household_income: 81278
  poverty_rate: 5.64
  homeownership_rate: 85.7
  unemployment_rate: 2.4
  median_home_value: 216900
  gini_index: 0.3958
  vacancy_rate: 7.79
  race_white: 16980
  race_black: 111
  race_asian: 45
  race_native: 92
  hispanic: 648
  bachelors_plus: 4414
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.9964
  - to: "us/states/ks/districts/senate/18"
    rel: in-district
    area_weight: 0.6656
  - to: "us/states/ks/districts/senate/1"
    rel: in-district
    area_weight: 0.3344
  - to: "us/states/ks/districts/house/47"
    rel: in-district
    area_weight: 0.8862
  - to: "us/states/ks/districts/house/42"
    rel: in-district
    area_weight: 0.1137
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Jefferson County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18349 |
| Under 18 | 4033 |
| 18–64 | 10650 |
| 65+ | 3666 |
| Median household income | 81278 |
| Poverty rate | 5.64 |
| Homeownership rate | 85.7 |
| Unemployment rate | 2.4 |
| Median home value | 216900 |
| Gini index | 0.3958 |
| Vacancy rate | 7.79 |
| White | 16980 |
| Black | 111 |
| Asian | 45 |
| Native | 92 |
| Hispanic/Latino | 648 |
| Bachelor's or higher | 4414 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 18](/us/states/ks/districts/senate/18.md) — 67% (state senate)
- [KS Senate District 1](/us/states/ks/districts/senate/1.md) — 33% (state senate)
- [KS House District 47](/us/states/ks/districts/house/47.md) — 89% (state house)
- [KS House District 42](/us/states/ks/districts/house/42.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
