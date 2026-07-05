---
type: Jurisdiction
title: "Boone County, MO"
classification: county
fips: "29019"
state: "MO"
demographics:
  population: 188043
  population_under_18: 37890
  population_18_64: 124807
  population_65_plus: 25346
  median_household_income: 72758
  poverty_rate: 16.58
  homeownership_rate: 57.7
  unemployment_rate: 3.78
  median_home_value: 272800
  gini_index: 0.4753
  vacancy_rate: 6.26
  race_white: 144850
  race_black: 18277
  race_asian: 9111
  race_native: 188
  hispanic: 8454
  bachelors_plus: 85571
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 0.579
  - to: "us/states/mo/districts/03"
    rel: in-district
    area_weight: 0.4209
  - to: "us/states/mo/districts/senate/19"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mo/districts/house/44"
    rel: in-district
    area_weight: 0.5305
  - to: "us/states/mo/districts/house/47"
    rel: in-district
    area_weight: 0.3791
  - to: "us/states/mo/districts/house/50"
    rel: in-district
    area_weight: 0.0373
  - to: "us/states/mo/districts/house/46"
    rel: in-district
    area_weight: 0.0367
  - to: "us/states/mo/districts/house/45"
    rel: in-district
    area_weight: 0.0159
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Boone County, MO

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 188043 |
| Under 18 | 37890 |
| 18–64 | 124807 |
| 65+ | 25346 |
| Median household income | 72758 |
| Poverty rate | 16.58 |
| Homeownership rate | 57.7 |
| Unemployment rate | 3.78 |
| Median home value | 272800 |
| Gini index | 0.4753 |
| Vacancy rate | 6.26 |
| White | 144850 |
| Black | 18277 |
| Asian | 9111 |
| Native | 188 |
| Hispanic/Latino | 8454 |
| Bachelor's or higher | 85571 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 58% (congressional)
- [MO-03](/us/states/mo/districts/03.md) — 42% (congressional)
- [MO Senate District 19](/us/states/mo/districts/senate/19.md) — 100% (state senate)
- [MO House District 44](/us/states/mo/districts/house/44.md) — 53% (state house)
- [MO House District 47](/us/states/mo/districts/house/47.md) — 38% (state house)
- [MO House District 50](/us/states/mo/districts/house/50.md) — 4% (state house)
- [MO House District 46](/us/states/mo/districts/house/46.md) — 4% (state house)
- [MO House District 45](/us/states/mo/districts/house/45.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
