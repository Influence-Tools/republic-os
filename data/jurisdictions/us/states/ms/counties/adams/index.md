---
type: Jurisdiction
title: "Adams County, MS"
classification: county
fips: "28001"
state: "MS"
demographics:
  population: 28803
  population_under_18: 5892
  population_18_64: 16571
  population_65_plus: 6340
  median_household_income: 43644
  poverty_rate: 27.04
  homeownership_rate: 68.14
  unemployment_rate: 6.4
  median_home_value: 108700
  gini_index: 0.5181
  vacancy_rate: 23.2
  race_white: 10835
  race_black: 16144
  race_asian: 65
  race_native: 14
  hispanic: 1012
  bachelors_plus: 5510
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.9959
  - to: "us/states/ms/districts/senate/37"
    rel: in-district
    area_weight: 0.6178
  - to: "us/states/ms/districts/senate/38"
    rel: in-district
    area_weight: 0.3815
  - to: "us/states/ms/districts/house/94"
    rel: in-district
    area_weight: 0.4345
  - to: "us/states/ms/districts/house/96"
    rel: in-district
    area_weight: 0.3132
  - to: "us/states/ms/districts/house/97"
    rel: in-district
    area_weight: 0.2517
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Adams County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28803 |
| Under 18 | 5892 |
| 18–64 | 16571 |
| 65+ | 6340 |
| Median household income | 43644 |
| Poverty rate | 27.04 |
| Homeownership rate | 68.14 |
| Unemployment rate | 6.4 |
| Median home value | 108700 |
| Gini index | 0.5181 |
| Vacancy rate | 23.2 |
| White | 10835 |
| Black | 16144 |
| Asian | 65 |
| Native | 14 |
| Hispanic/Latino | 1012 |
| Bachelor's or higher | 5510 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 37](/us/states/ms/districts/senate/37.md) — 62% (state senate)
- [MS Senate District 38](/us/states/ms/districts/senate/38.md) — 38% (state senate)
- [MS House District 94](/us/states/ms/districts/house/94.md) — 43% (state house)
- [MS House District 96](/us/states/ms/districts/house/96.md) — 31% (state house)
- [MS House District 97](/us/states/ms/districts/house/97.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
