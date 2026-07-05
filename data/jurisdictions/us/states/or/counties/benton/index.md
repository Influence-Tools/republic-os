---
type: Jurisdiction
title: "Benton County, OR"
classification: county
fips: "41003"
state: "OR"
demographics:
  population: 96303
  population_under_18: 15150
  population_18_64: 63835
  population_65_plus: 17318
  median_household_income: 77702
  poverty_rate: 18.2
  homeownership_rate: 56.95
  unemployment_rate: 6.98
  median_home_value: 513000
  gini_index: 0.5023
  vacancy_rate: 5.89
  race_white: 76292
  race_black: 1260
  race_asian: 6413
  race_native: 1011
  hispanic: 9031
  bachelors_plus: 48458
districts:
  - to: "us/states/or/districts/04"
    rel: in-district
    area_weight: 0.9966
  - to: "us/states/or/districts/senate/5"
    rel: in-district
    area_weight: 0.8208
  - to: "us/states/or/districts/senate/8"
    rel: in-district
    area_weight: 0.1791
  - to: "us/states/or/districts/house/10"
    rel: in-district
    area_weight: 0.8208
  - to: "us/states/or/districts/house/16"
    rel: in-district
    area_weight: 0.1682
  - to: "us/states/or/districts/house/15"
    rel: in-district
    area_weight: 0.0108
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Benton County, OR

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 96303 |
| Under 18 | 15150 |
| 18–64 | 63835 |
| 65+ | 17318 |
| Median household income | 77702 |
| Poverty rate | 18.2 |
| Homeownership rate | 56.95 |
| Unemployment rate | 6.98 |
| Median home value | 513000 |
| Gini index | 0.5023 |
| Vacancy rate | 5.89 |
| White | 76292 |
| Black | 1260 |
| Asian | 6413 |
| Native | 1011 |
| Hispanic/Latino | 9031 |
| Bachelor's or higher | 48458 |

## Districts

- [OR-04](/us/states/or/districts/04.md) — 100% (congressional)
- [OR Senate District 5](/us/states/or/districts/senate/5.md) — 82% (state senate)
- [OR Senate District 8](/us/states/or/districts/senate/8.md) — 18% (state senate)
- [OR House District 10](/us/states/or/districts/house/10.md) — 82% (state house)
- [OR House District 16](/us/states/or/districts/house/16.md) — 17% (state house)
- [OR House District 15](/us/states/or/districts/house/15.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
