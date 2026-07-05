---
type: Jurisdiction
title: "Ozaukee County, WI"
classification: county
fips: "55089"
state: "WI"
demographics:
  population: 92966
  population_under_18: 19455
  population_18_64: 53406
  population_65_plus: 20105
  median_household_income: 96996
  poverty_rate: 4.99
  homeownership_rate: 72.88
  unemployment_rate: 2.77
  median_home_value: 390200
  gini_index: 0.4785
  vacancy_rate: 3.92
  race_white: 83279
  race_black: 1392
  race_asian: 2028
  race_native: 136
  hispanic: 3470
  bachelors_plus: 46119
districts:
  - to: "us/states/wi/districts/06"
    rel: in-district
    area_weight: 0.2095
  - to: "us/states/wi/districts/senate/8"
    rel: in-district
    area_weight: 0.1112
  - to: "us/states/wi/districts/senate/20"
    rel: in-district
    area_weight: 0.0994
  - to: "us/states/wi/districts/house/59"
    rel: in-district
    area_weight: 0.0993
  - to: "us/states/wi/districts/house/22"
    rel: in-district
    area_weight: 0.0935
  - to: "us/states/wi/districts/house/23"
    rel: in-district
    area_weight: 0.0178
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Ozaukee County, WI

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 92966 |
| Under 18 | 19455 |
| 18–64 | 53406 |
| 65+ | 20105 |
| Median household income | 96996 |
| Poverty rate | 4.99 |
| Homeownership rate | 72.88 |
| Unemployment rate | 2.77 |
| Median home value | 390200 |
| Gini index | 0.4785 |
| Vacancy rate | 3.92 |
| White | 83279 |
| Black | 1392 |
| Asian | 2028 |
| Native | 136 |
| Hispanic/Latino | 3470 |
| Bachelor's or higher | 46119 |

## Districts

- [WI-06](/us/states/wi/districts/06.md) — 21% (congressional)
- [WI Senate District 8](/us/states/wi/districts/senate/8.md) — 11% (state senate)
- [WI Senate District 20](/us/states/wi/districts/senate/20.md) — 10% (state senate)
- [WI House District 59](/us/states/wi/districts/house/59.md) — 10% (state house)
- [WI House District 22](/us/states/wi/districts/house/22.md) — 9% (state house)
- [WI House District 23](/us/states/wi/districts/house/23.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
