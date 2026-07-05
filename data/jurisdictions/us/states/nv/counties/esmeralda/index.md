---
type: Jurisdiction
title: "Esmeralda County, NV"
classification: county
fips: "32009"
state: "NV"
demographics:
  population: 1028
  population_under_18: 132
  population_18_64: 641
  population_65_plus: 255
  median_household_income: 41715
  poverty_rate: 12.43
  homeownership_rate: 60.83
  unemployment_rate: 0.57
  median_home_value: 108900
  gini_index: 0.4459
  vacancy_rate: 27.1
  race_white: 730
  race_black: 3
  race_asian: 12
  race_native: 14
  hispanic: 324
  bachelors_plus: 245
districts:
  - to: "us/states/nv/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nv/districts/senate/17"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nv/districts/house/38"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nv]
timestamp: "2026-07-03"
---

# Esmeralda County, NV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1028 |
| Under 18 | 132 |
| 18–64 | 641 |
| 65+ | 255 |
| Median household income | 41715 |
| Poverty rate | 12.43 |
| Homeownership rate | 60.83 |
| Unemployment rate | 0.57 |
| Median home value | 108900 |
| Gini index | 0.4459 |
| Vacancy rate | 27.1 |
| White | 730 |
| Black | 3 |
| Asian | 12 |
| Native | 14 |
| Hispanic/Latino | 324 |
| Bachelor's or higher | 245 |

## Districts

- [NV-04](/us/states/nv/districts/04.md) — 100% (congressional)
- [NV Senate District 17](/us/states/nv/districts/senate/17.md) — 100% (state senate)
- [NV House District 38](/us/states/nv/districts/house/38.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
