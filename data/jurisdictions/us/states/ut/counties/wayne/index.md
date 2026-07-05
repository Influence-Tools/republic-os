---
type: Jurisdiction
title: "Wayne County, UT"
classification: county
fips: "49055"
state: "UT"
demographics:
  population: 2584
  population_under_18: 547
  population_18_64: 1377
  population_65_plus: 660
  median_household_income: 76607
  poverty_rate: 10.58
  homeownership_rate: 79.33
  unemployment_rate: 2.14
  median_home_value: 411800
  gini_index: 0.3878
  vacancy_rate: 33.37
  race_white: 2379
  race_black: 9
  race_asian: 0
  race_native: 0
  hispanic: 78
  bachelors_plus: 617
districts:
  - to: "us/states/ut/districts/02"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ut/districts/senate/26"
    rel: in-district
    area_weight: 0.6328
  - to: "us/states/ut/districts/senate/27"
    rel: in-district
    area_weight: 0.3672
  - to: "us/states/ut/districts/house/69"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Wayne County, UT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2584 |
| Under 18 | 547 |
| 18–64 | 1377 |
| 65+ | 660 |
| Median household income | 76607 |
| Poverty rate | 10.58 |
| Homeownership rate | 79.33 |
| Unemployment rate | 2.14 |
| Median home value | 411800 |
| Gini index | 0.3878 |
| Vacancy rate | 33.37 |
| White | 2379 |
| Black | 9 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 78 |
| Bachelor's or higher | 617 |

## Districts

- [UT-02](/us/states/ut/districts/02.md) — 100% (congressional)
- [UT Senate District 26](/us/states/ut/districts/senate/26.md) — 63% (state senate)
- [UT Senate District 27](/us/states/ut/districts/senate/27.md) — 37% (state senate)
- [UT House District 69](/us/states/ut/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
