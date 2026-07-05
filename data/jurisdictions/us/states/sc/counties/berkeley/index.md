---
type: Jurisdiction
title: "Berkeley County, SC"
classification: county
fips: "45015"
state: "SC"
demographics:
  population: 246802
  population_under_18: 58289
  population_18_64: 151898
  population_65_plus: 36615
  median_household_income: 84358
  poverty_rate: 9.92
  homeownership_rate: 74.55
  unemployment_rate: 3.19
  median_home_value: 310300
  gini_index: 0.4217
  vacancy_rate: 6.85
  race_white: 154062
  race_black: 56699
  race_asian: 6365
  race_native: 1205
  hispanic: 22587
  bachelors_plus: 68941
districts:
  - to: "us/states/sc/districts/01"
    rel: in-district
    area_weight: 0.9963
  - to: "us/states/sc/districts/senate/37"
    rel: in-district
    area_weight: 0.5723
  - to: "us/states/sc/districts/senate/32"
    rel: in-district
    area_weight: 0.2536
  - to: "us/states/sc/districts/senate/39"
    rel: in-district
    area_weight: 0.1387
  - to: "us/states/sc/districts/senate/44"
    rel: in-district
    area_weight: 0.0354
  - to: "us/states/sc/districts/house/103"
    rel: in-district
    area_weight: 0.3106
  - to: "us/states/sc/districts/house/102"
    rel: in-district
    area_weight: 0.3075
  - to: "us/states/sc/districts/house/100"
    rel: in-district
    area_weight: 0.1625
  - to: "us/states/sc/districts/house/101"
    rel: in-district
    area_weight: 0.1287
  - to: "us/states/sc/districts/house/99"
    rel: in-district
    area_weight: 0.045
  - to: "us/states/sc/districts/house/117"
    rel: in-district
    area_weight: 0.0276
  - to: "us/states/sc/districts/house/92"
    rel: in-district
    area_weight: 0.0128
  - to: "us/states/sc/districts/house/15"
    rel: in-district
    area_weight: 0.0051
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Berkeley County, SC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 246802 |
| Under 18 | 58289 |
| 18–64 | 151898 |
| 65+ | 36615 |
| Median household income | 84358 |
| Poverty rate | 9.92 |
| Homeownership rate | 74.55 |
| Unemployment rate | 3.19 |
| Median home value | 310300 |
| Gini index | 0.4217 |
| Vacancy rate | 6.85 |
| White | 154062 |
| Black | 56699 |
| Asian | 6365 |
| Native | 1205 |
| Hispanic/Latino | 22587 |
| Bachelor's or higher | 68941 |

## Districts

- [SC-01](/us/states/sc/districts/01.md) — 100% (congressional)
- [SC Senate District 37](/us/states/sc/districts/senate/37.md) — 57% (state senate)
- [SC Senate District 32](/us/states/sc/districts/senate/32.md) — 25% (state senate)
- [SC Senate District 39](/us/states/sc/districts/senate/39.md) — 14% (state senate)
- [SC Senate District 44](/us/states/sc/districts/senate/44.md) — 4% (state senate)
- [SC House District 103](/us/states/sc/districts/house/103.md) — 31% (state house)
- [SC House District 102](/us/states/sc/districts/house/102.md) — 31% (state house)
- [SC House District 100](/us/states/sc/districts/house/100.md) — 16% (state house)
- [SC House District 101](/us/states/sc/districts/house/101.md) — 13% (state house)
- [SC House District 99](/us/states/sc/districts/house/99.md) — 4% (state house)
- [SC House District 117](/us/states/sc/districts/house/117.md) — 3% (state house)
- [SC House District 92](/us/states/sc/districts/house/92.md) — 1% (state house)
- [SC House District 15](/us/states/sc/districts/house/15.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
