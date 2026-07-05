---
type: Jurisdiction
title: "Cumberland County, PA"
classification: county
fips: "42041"
state: "PA"
demographics:
  population: 268323
  population_under_18: 54926
  population_18_64: 162411
  population_65_plus: 50986
  median_household_income: 87494
  poverty_rate: 7.48
  homeownership_rate: 71.34
  unemployment_rate: 3.68
  median_home_value: 277600
  gini_index: 0.4247
  vacancy_rate: 4.36
  race_white: 220348
  race_black: 11921
  race_asian: 15553
  race_native: 110
  hispanic: 13809
  bachelors_plus: 104961
districts:
  - to: "us/states/pa/districts/10"
    rel: in-district
    area_weight: 0.7019
  - to: "us/states/pa/districts/13"
    rel: in-district
    area_weight: 0.2981
  - to: "us/states/pa/districts/senate/34"
    rel: in-district
    area_weight: 0.946
  - to: "us/states/pa/districts/senate/31"
    rel: in-district
    area_weight: 0.0539
  - to: "us/states/pa/districts/house/199"
    rel: in-district
    area_weight: 0.4194
  - to: "us/states/pa/districts/house/193"
    rel: in-district
    area_weight: 0.2946
  - to: "us/states/pa/districts/house/87"
    rel: in-district
    area_weight: 0.2064
  - to: "us/states/pa/districts/house/88"
    rel: in-district
    area_weight: 0.0512
  - to: "us/states/pa/districts/house/103"
    rel: in-district
    area_weight: 0.0281
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Cumberland County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 268323 |
| Under 18 | 54926 |
| 18–64 | 162411 |
| 65+ | 50986 |
| Median household income | 87494 |
| Poverty rate | 7.48 |
| Homeownership rate | 71.34 |
| Unemployment rate | 3.68 |
| Median home value | 277600 |
| Gini index | 0.4247 |
| Vacancy rate | 4.36 |
| White | 220348 |
| Black | 11921 |
| Asian | 15553 |
| Native | 110 |
| Hispanic/Latino | 13809 |
| Bachelor's or higher | 104961 |

## Districts

- [PA-10](/us/states/pa/districts/10.md) — 70% (congressional)
- [PA-13](/us/states/pa/districts/13.md) — 30% (congressional)
- [PA Senate District 34](/us/states/pa/districts/senate/34.md) — 95% (state senate)
- [PA Senate District 31](/us/states/pa/districts/senate/31.md) — 5% (state senate)
- [PA House District 199](/us/states/pa/districts/house/199.md) — 42% (state house)
- [PA House District 193](/us/states/pa/districts/house/193.md) — 29% (state house)
- [PA House District 87](/us/states/pa/districts/house/87.md) — 21% (state house)
- [PA House District 88](/us/states/pa/districts/house/88.md) — 5% (state house)
- [PA House District 103](/us/states/pa/districts/house/103.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
