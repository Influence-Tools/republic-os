---
type: Jurisdiction
title: "Morgan County, UT"
classification: county
fips: "49029"
state: "UT"
demographics:
  population: 12802
  population_under_18: 4241
  population_18_64: 6979
  population_65_plus: 1582
  median_household_income: 130929
  poverty_rate: 1.42
  homeownership_rate: 88.82
  unemployment_rate: 2.32
  median_home_value: 654900
  gini_index: 0.3695
  vacancy_rate: 3.98
  race_white: 12029
  race_black: 12
  race_asian: 27
  race_native: 9
  hispanic: 375
  bachelors_plus: 3945
districts:
  - to: "us/states/ut/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ut/districts/senate/3"
    rel: in-district
    area_weight: 0.8311
  - to: "us/states/ut/districts/senate/5"
    rel: in-district
    area_weight: 0.0862
  - to: "us/states/ut/districts/senate/7"
    rel: in-district
    area_weight: 0.0826
  - to: "us/states/ut/districts/house/4"
    rel: in-district
    area_weight: 0.9783
  - to: "us/states/ut/districts/house/8"
    rel: in-district
    area_weight: 0.0215
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Morgan County, UT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12802 |
| Under 18 | 4241 |
| 18–64 | 6979 |
| 65+ | 1582 |
| Median household income | 130929 |
| Poverty rate | 1.42 |
| Homeownership rate | 88.82 |
| Unemployment rate | 2.32 |
| Median home value | 654900 |
| Gini index | 0.3695 |
| Vacancy rate | 3.98 |
| White | 12029 |
| Black | 12 |
| Asian | 27 |
| Native | 9 |
| Hispanic/Latino | 375 |
| Bachelor's or higher | 3945 |

## Districts

- [UT-01](/us/states/ut/districts/01.md) — 100% (congressional)
- [UT Senate District 3](/us/states/ut/districts/senate/3.md) — 83% (state senate)
- [UT Senate District 5](/us/states/ut/districts/senate/5.md) — 9% (state senate)
- [UT Senate District 7](/us/states/ut/districts/senate/7.md) — 8% (state senate)
- [UT House District 4](/us/states/ut/districts/house/4.md) — 98% (state house)
- [UT House District 8](/us/states/ut/districts/house/8.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
