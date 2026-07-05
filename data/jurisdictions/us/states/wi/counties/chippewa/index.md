---
type: Jurisdiction
title: "Chippewa County, WI"
classification: county
fips: "55017"
state: "WI"
demographics:
  population: 66799
  population_under_18: 14291
  population_18_64: 39320
  population_65_plus: 13188
  median_household_income: 74680
  poverty_rate: 10.23
  homeownership_rate: 74.16
  unemployment_rate: 3.06
  median_home_value: 257900
  gini_index: 0.4102
  vacancy_rate: 7.58
  race_white: 61893
  race_black: 967
  race_asian: 881
  race_native: 370
  hispanic: 1311
  bachelors_plus: 14675
districts:
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 0.7881
  - to: "us/states/wi/districts/03"
    rel: in-district
    area_weight: 0.2119
  - to: "us/states/wi/districts/senate/23"
    rel: in-district
    area_weight: 0.7811
  - to: "us/states/wi/districts/senate/31"
    rel: in-district
    area_weight: 0.2189
  - to: "us/states/wi/districts/house/68"
    rel: in-district
    area_weight: 0.6973
  - to: "us/states/wi/districts/house/92"
    rel: in-district
    area_weight: 0.1297
  - to: "us/states/wi/districts/house/91"
    rel: in-district
    area_weight: 0.0893
  - to: "us/states/wi/districts/house/69"
    rel: in-district
    area_weight: 0.0463
  - to: "us/states/wi/districts/house/67"
    rel: in-district
    area_weight: 0.0374
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Chippewa County, WI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 66799 |
| Under 18 | 14291 |
| 18–64 | 39320 |
| 65+ | 13188 |
| Median household income | 74680 |
| Poverty rate | 10.23 |
| Homeownership rate | 74.16 |
| Unemployment rate | 3.06 |
| Median home value | 257900 |
| Gini index | 0.4102 |
| Vacancy rate | 7.58 |
| White | 61893 |
| Black | 967 |
| Asian | 881 |
| Native | 370 |
| Hispanic/Latino | 1311 |
| Bachelor's or higher | 14675 |

## Districts

- [WI-07](/us/states/wi/districts/07.md) — 79% (congressional)
- [WI-03](/us/states/wi/districts/03.md) — 21% (congressional)
- [WI Senate District 23](/us/states/wi/districts/senate/23.md) — 78% (state senate)
- [WI Senate District 31](/us/states/wi/districts/senate/31.md) — 22% (state senate)
- [WI House District 68](/us/states/wi/districts/house/68.md) — 70% (state house)
- [WI House District 92](/us/states/wi/districts/house/92.md) — 13% (state house)
- [WI House District 91](/us/states/wi/districts/house/91.md) — 9% (state house)
- [WI House District 69](/us/states/wi/districts/house/69.md) — 5% (state house)
- [WI House District 67](/us/states/wi/districts/house/67.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
