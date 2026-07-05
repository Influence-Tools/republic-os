---
type: Jurisdiction
title: "Woodbury County, IA"
classification: county
fips: "19193"
state: "IA"
demographics:
  population: 106247
  population_under_18: 27391
  population_18_64: 61992
  population_65_plus: 16864
  median_household_income: 73658
  poverty_rate: 13.95
  homeownership_rate: 68.19
  unemployment_rate: 4.11
  median_home_value: 183200
  gini_index: 0.4363
  vacancy_rate: 6.2
  race_white: 75553
  race_black: 5255
  race_asian: 2513
  race_native: 1899
  hispanic: 20316
  bachelors_plus: 22274
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/ia/districts/senate/7"
    rel: in-district
    area_weight: 0.8726
  - to: "us/states/ia/districts/senate/1"
    rel: in-district
    area_weight: 0.1272
  - to: "us/states/ia/districts/house/13"
    rel: in-district
    area_weight: 0.7689
  - to: "us/states/ia/districts/house/2"
    rel: in-district
    area_weight: 0.1108
  - to: "us/states/ia/districts/house/14"
    rel: in-district
    area_weight: 0.1037
  - to: "us/states/ia/districts/house/1"
    rel: in-district
    area_weight: 0.0164
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Woodbury County, IA

County jurisdiction — 5 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 106247 |
| Under 18 | 27391 |
| 18–64 | 61992 |
| 65+ | 16864 |
| Median household income | 73658 |
| Poverty rate | 13.95 |
| Homeownership rate | 68.19 |
| Unemployment rate | 4.11 |
| Median home value | 183200 |
| Gini index | 0.4363 |
| Vacancy rate | 6.2 |
| White | 75553 |
| Black | 5255 |
| Asian | 2513 |
| Native | 1899 |
| Hispanic/Latino | 20316 |
| Bachelor's or higher | 22274 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 7](/us/states/ia/districts/senate/7.md) — 87% (state senate)
- [IA Senate District 1](/us/states/ia/districts/senate/1.md) — 13% (state senate)
- [IA House District 13](/us/states/ia/districts/house/13.md) — 77% (state house)
- [IA House District 2](/us/states/ia/districts/house/2.md) — 11% (state house)
- [IA House District 14](/us/states/ia/districts/house/14.md) — 10% (state house)
- [IA House District 1](/us/states/ia/districts/house/1.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
