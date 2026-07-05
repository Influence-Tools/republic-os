---
type: Jurisdiction
title: "Wicomico County, MD"
classification: county
fips: "24045"
state: "MD"
demographics:
  population: 104914
  population_under_18: 23644
  population_18_64: 63822
  population_65_plus: 17448
  median_household_income: 76210
  poverty_rate: 13.94
  homeownership_rate: 62.28
  unemployment_rate: 5.89
  median_home_value: 254700
  gini_index: 0.4468
  vacancy_rate: 8.29
  race_white: 62073
  race_black: 27997
  race_asian: 2574
  race_native: 120
  hispanic: 7463
  bachelors_plus: 27377
districts:
  - to: "us/states/md/districts/01"
    rel: in-district
    area_weight: 0.9656
  - to: "us/states/md/districts/senate/37"
    rel: in-district
    area_weight: 0.5346
  - to: "us/states/md/districts/senate/38"
    rel: in-district
    area_weight: 0.4262
  - to: "us/states/md/districts/house/37b"
    rel: in-district
    area_weight: 0.3907
  - to: "us/states/md/districts/house/38c"
    rel: in-district
    area_weight: 0.2903
  - to: "us/states/md/districts/house/37a"
    rel: in-district
    area_weight: 0.1438
  - to: "us/states/md/districts/house/38b"
    rel: in-district
    area_weight: 0.0748
  - to: "us/states/md/districts/house/38a"
    rel: in-district
    area_weight: 0.0611
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Wicomico County, MD

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 104914 |
| Under 18 | 23644 |
| 18–64 | 63822 |
| 65+ | 17448 |
| Median household income | 76210 |
| Poverty rate | 13.94 |
| Homeownership rate | 62.28 |
| Unemployment rate | 5.89 |
| Median home value | 254700 |
| Gini index | 0.4468 |
| Vacancy rate | 8.29 |
| White | 62073 |
| Black | 27997 |
| Asian | 2574 |
| Native | 120 |
| Hispanic/Latino | 7463 |
| Bachelor's or higher | 27377 |

## Districts

- [MD-01](/us/states/md/districts/01.md) — 97% (congressional)
- [MD Senate District 37](/us/states/md/districts/senate/37.md) — 53% (state senate)
- [MD Senate District 38](/us/states/md/districts/senate/38.md) — 43% (state senate)
- [MD House District 37B](/us/states/md/districts/house/37b.md) — 39% (state house)
- [MD House District 38C](/us/states/md/districts/house/38c.md) — 29% (state house)
- [MD House District 37A](/us/states/md/districts/house/37a.md) — 14% (state house)
- [MD House District 38B](/us/states/md/districts/house/38b.md) — 7% (state house)
- [MD House District 38A](/us/states/md/districts/house/38a.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
