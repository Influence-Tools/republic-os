---
type: Jurisdiction
title: "Mineral County, NV"
classification: county
fips: "32021"
state: "NV"
demographics:
  population: 4542
  population_under_18: 941
  population_18_64: 2415
  population_65_plus: 1186
  median_household_income: 54855
  poverty_rate: 18.47
  homeownership_rate: 72.51
  unemployment_rate: 9.8
  median_home_value: 156200
  gini_index: 0.3875
  vacancy_rate: 19.77
  race_white: 2639
  race_black: 144
  race_asian: 4
  race_native: 954
  hispanic: 789
  bachelors_plus: 557
districts:
  - to: "us/states/nv/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nv/districts/senate/17"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nv/districts/house/38"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nv]
timestamp: "2026-07-03"
---

# Mineral County, NV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4542 |
| Under 18 | 941 |
| 18–64 | 2415 |
| 65+ | 1186 |
| Median household income | 54855 |
| Poverty rate | 18.47 |
| Homeownership rate | 72.51 |
| Unemployment rate | 9.8 |
| Median home value | 156200 |
| Gini index | 0.3875 |
| Vacancy rate | 19.77 |
| White | 2639 |
| Black | 144 |
| Asian | 4 |
| Native | 954 |
| Hispanic/Latino | 789 |
| Bachelor's or higher | 557 |

## Districts

- [NV-04](/us/states/nv/districts/04.md) — 100% (congressional)
- [NV Senate District 17](/us/states/nv/districts/senate/17.md) — 100% (state senate)
- [NV House District 38](/us/states/nv/districts/house/38.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
