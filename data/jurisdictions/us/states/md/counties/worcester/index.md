---
type: Jurisdiction
title: "Worcester County, MD"
classification: county
fips: "24047"
state: "MD"
demographics:
  population: 53700
  population_under_18: 9185
  population_18_64: 29144
  population_65_plus: 15371
  median_household_income: 81745
  poverty_rate: 9.94
  homeownership_rate: 77.96
  unemployment_rate: 6.71
  median_home_value: 374700
  gini_index: 0.4861
  vacancy_rate: 57.56
  race_white: 42164
  race_black: 6534
  race_asian: 743
  race_native: 29
  hispanic: 2165
  bachelors_plus: 20052
districts:
  - to: "us/states/md/districts/01"
    rel: in-district
    area_weight: 0.8414
  - to: "us/states/md/districts/senate/38"
    rel: in-district
    area_weight: 0.8408
  - to: "us/states/md/districts/house/38a"
    rel: in-district
    area_weight: 0.4813
  - to: "us/states/md/districts/house/38c"
    rel: in-district
    area_weight: 0.3595
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Worcester County, MD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 53700 |
| Under 18 | 9185 |
| 18–64 | 29144 |
| 65+ | 15371 |
| Median household income | 81745 |
| Poverty rate | 9.94 |
| Homeownership rate | 77.96 |
| Unemployment rate | 6.71 |
| Median home value | 374700 |
| Gini index | 0.4861 |
| Vacancy rate | 57.56 |
| White | 42164 |
| Black | 6534 |
| Asian | 743 |
| Native | 29 |
| Hispanic/Latino | 2165 |
| Bachelor's or higher | 20052 |

## Districts

- [MD-01](/us/states/md/districts/01.md) — 84% (congressional)
- [MD Senate District 38](/us/states/md/districts/senate/38.md) — 84% (state senate)
- [MD House District 38A](/us/states/md/districts/house/38a.md) — 48% (state house)
- [MD House District 38C](/us/states/md/districts/house/38c.md) — 36% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
