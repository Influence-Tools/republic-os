---
type: Jurisdiction
title: "Franklin County, MS"
classification: county
fips: "28037"
state: "MS"
demographics:
  population: 7622
  population_under_18: 1764
  population_18_64: 4217
  population_65_plus: 1641
  median_household_income: 52939
  poverty_rate: 25.42
  homeownership_rate: 81.69
  unemployment_rate: 3.97
  median_home_value: 101900
  gini_index: 0.5102
  vacancy_rate: 28.99
  race_white: 4758
  race_black: 2670
  race_asian: 2
  race_native: 0
  hispanic: 81
  bachelors_plus: 1490
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ms/districts/senate/37"
    rel: in-district
    area_weight: 0.7492
  - to: "us/states/ms/districts/senate/39"
    rel: in-district
    area_weight: 0.2508
  - to: "us/states/ms/districts/house/85"
    rel: in-district
    area_weight: 0.4239
  - to: "us/states/ms/districts/house/53"
    rel: in-district
    area_weight: 0.2507
  - to: "us/states/ms/districts/house/97"
    rel: in-district
    area_weight: 0.166
  - to: "us/states/ms/districts/house/94"
    rel: in-district
    area_weight: 0.1593
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Franklin County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7622 |
| Under 18 | 1764 |
| 18–64 | 4217 |
| 65+ | 1641 |
| Median household income | 52939 |
| Poverty rate | 25.42 |
| Homeownership rate | 81.69 |
| Unemployment rate | 3.97 |
| Median home value | 101900 |
| Gini index | 0.5102 |
| Vacancy rate | 28.99 |
| White | 4758 |
| Black | 2670 |
| Asian | 2 |
| Native | 0 |
| Hispanic/Latino | 81 |
| Bachelor's or higher | 1490 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 37](/us/states/ms/districts/senate/37.md) — 75% (state senate)
- [MS Senate District 39](/us/states/ms/districts/senate/39.md) — 25% (state senate)
- [MS House District 85](/us/states/ms/districts/house/85.md) — 42% (state house)
- [MS House District 53](/us/states/ms/districts/house/53.md) — 25% (state house)
- [MS House District 97](/us/states/ms/districts/house/97.md) — 17% (state house)
- [MS House District 94](/us/states/ms/districts/house/94.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
