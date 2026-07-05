---
type: Jurisdiction
title: "Dorchester County, SC"
classification: county
fips: "45035"
state: "SC"
demographics:
  population: 167201
  population_under_18: 40253
  population_18_64: 101541
  population_65_plus: 25407
  median_household_income: 78198
  poverty_rate: 11.38
  homeownership_rate: 75.53
  unemployment_rate: 4.94
  median_home_value: 329300
  gini_index: 0.42
  vacancy_rate: 6.9
  race_white: 103549
  race_black: 42160
  race_asian: 3531
  race_native: 429
  hispanic: 12058
  bachelors_plus: 47029
districts:
  - to: "us/states/sc/districts/06"
    rel: in-district
    area_weight: 0.8128
  - to: "us/states/sc/districts/01"
    rel: in-district
    area_weight: 0.1872
  - to: "us/states/sc/districts/senate/39"
    rel: in-district
    area_weight: 0.5372
  - to: "us/states/sc/districts/senate/41"
    rel: in-district
    area_weight: 0.33
  - to: "us/states/sc/districts/senate/38"
    rel: in-district
    area_weight: 0.1279
  - to: "us/states/sc/districts/house/97"
    rel: in-district
    area_weight: 0.3398
  - to: "us/states/sc/districts/house/102"
    rel: in-district
    area_weight: 0.1675
  - to: "us/states/sc/districts/house/95"
    rel: in-district
    area_weight: 0.1609
  - to: "us/states/sc/districts/house/90"
    rel: in-district
    area_weight: 0.1408
  - to: "us/states/sc/districts/house/114"
    rel: in-district
    area_weight: 0.1313
  - to: "us/states/sc/districts/house/94"
    rel: in-district
    area_weight: 0.0264
  - to: "us/states/sc/districts/house/98"
    rel: in-district
    area_weight: 0.0234
  - to: "us/states/sc/districts/house/109"
    rel: in-district
    area_weight: 0.0097
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Dorchester County, SC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 167201 |
| Under 18 | 40253 |
| 18–64 | 101541 |
| 65+ | 25407 |
| Median household income | 78198 |
| Poverty rate | 11.38 |
| Homeownership rate | 75.53 |
| Unemployment rate | 4.94 |
| Median home value | 329300 |
| Gini index | 0.42 |
| Vacancy rate | 6.9 |
| White | 103549 |
| Black | 42160 |
| Asian | 3531 |
| Native | 429 |
| Hispanic/Latino | 12058 |
| Bachelor's or higher | 47029 |

## Districts

- [SC-06](/us/states/sc/districts/06.md) — 81% (congressional)
- [SC-01](/us/states/sc/districts/01.md) — 19% (congressional)
- [SC Senate District 39](/us/states/sc/districts/senate/39.md) — 54% (state senate)
- [SC Senate District 41](/us/states/sc/districts/senate/41.md) — 33% (state senate)
- [SC Senate District 38](/us/states/sc/districts/senate/38.md) — 13% (state senate)
- [SC House District 97](/us/states/sc/districts/house/97.md) — 34% (state house)
- [SC House District 102](/us/states/sc/districts/house/102.md) — 17% (state house)
- [SC House District 95](/us/states/sc/districts/house/95.md) — 16% (state house)
- [SC House District 90](/us/states/sc/districts/house/90.md) — 14% (state house)
- [SC House District 114](/us/states/sc/districts/house/114.md) — 13% (state house)
- [SC House District 94](/us/states/sc/districts/house/94.md) — 3% (state house)
- [SC House District 98](/us/states/sc/districts/house/98.md) — 2% (state house)
- [SC House District 109](/us/states/sc/districts/house/109.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
