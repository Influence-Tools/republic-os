---
type: Jurisdiction
title: "Greene County, MO"
classification: county
fips: "29077"
state: "MO"
demographics:
  population: 303375
  population_under_18: 63125
  population_18_64: 188214
  population_65_plus: 52036
  median_household_income: 61479
  poverty_rate: 13.65
  homeownership_rate: 57.48
  unemployment_rate: 3.4
  median_home_value: 221300
  gini_index: 0.4654
  vacancy_rate: 5.78
  race_white: 260352
  race_black: 9184
  race_asian: 5902
  race_native: 866
  hispanic: 15605
  bachelors_plus: 93385
districts:
  - to: "us/states/mo/districts/07"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/senate/20"
    rel: in-district
    area_weight: 0.8635
  - to: "us/states/mo/districts/senate/30"
    rel: in-district
    area_weight: 0.1365
  - to: "us/states/mo/districts/house/131"
    rel: in-district
    area_weight: 0.5508
  - to: "us/states/mo/districts/house/137"
    rel: in-district
    area_weight: 0.2532
  - to: "us/states/mo/districts/house/130"
    rel: in-district
    area_weight: 0.0797
  - to: "us/states/mo/districts/house/135"
    rel: in-district
    area_weight: 0.031
  - to: "us/states/mo/districts/house/134"
    rel: in-district
    area_weight: 0.0266
  - to: "us/states/mo/districts/house/136"
    rel: in-district
    area_weight: 0.023
  - to: "us/states/mo/districts/house/133"
    rel: in-district
    area_weight: 0.0186
  - to: "us/states/mo/districts/house/132"
    rel: in-district
    area_weight: 0.0171
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Greene County, MO

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 303375 |
| Under 18 | 63125 |
| 18–64 | 188214 |
| 65+ | 52036 |
| Median household income | 61479 |
| Poverty rate | 13.65 |
| Homeownership rate | 57.48 |
| Unemployment rate | 3.4 |
| Median home value | 221300 |
| Gini index | 0.4654 |
| Vacancy rate | 5.78 |
| White | 260352 |
| Black | 9184 |
| Asian | 5902 |
| Native | 866 |
| Hispanic/Latino | 15605 |
| Bachelor's or higher | 93385 |

## Districts

- [MO-07](/us/states/mo/districts/07.md) — 100% (congressional)
- [MO Senate District 20](/us/states/mo/districts/senate/20.md) — 86% (state senate)
- [MO Senate District 30](/us/states/mo/districts/senate/30.md) — 14% (state senate)
- [MO House District 131](/us/states/mo/districts/house/131.md) — 55% (state house)
- [MO House District 137](/us/states/mo/districts/house/137.md) — 25% (state house)
- [MO House District 130](/us/states/mo/districts/house/130.md) — 8% (state house)
- [MO House District 135](/us/states/mo/districts/house/135.md) — 3% (state house)
- [MO House District 134](/us/states/mo/districts/house/134.md) — 3% (state house)
- [MO House District 136](/us/states/mo/districts/house/136.md) — 2% (state house)
- [MO House District 133](/us/states/mo/districts/house/133.md) — 2% (state house)
- [MO House District 132](/us/states/mo/districts/house/132.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
