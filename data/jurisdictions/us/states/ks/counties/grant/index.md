---
type: Jurisdiction
title: "Grant County, KS"
classification: county
fips: "20067"
state: "KS"
demographics:
  population: 7229
  population_under_18: 2214
  population_18_64: 3977
  population_65_plus: 1038
  median_household_income: 66476
  poverty_rate: 9.3
  homeownership_rate: 76.67
  unemployment_rate: 0.69
  median_home_value: 110300
  gini_index: 0.4029
  vacancy_rate: 18.89
  race_white: 4417
  race_black: 13
  race_asian: 9
  race_native: 132
  hispanic: 3858
  bachelors_plus: 1558
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/39"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/124"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Grant County, KS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7229 |
| Under 18 | 2214 |
| 18–64 | 3977 |
| 65+ | 1038 |
| Median household income | 66476 |
| Poverty rate | 9.3 |
| Homeownership rate | 76.67 |
| Unemployment rate | 0.69 |
| Median home value | 110300 |
| Gini index | 0.4029 |
| Vacancy rate | 18.89 |
| White | 4417 |
| Black | 13 |
| Asian | 9 |
| Native | 132 |
| Hispanic/Latino | 3858 |
| Bachelor's or higher | 1558 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 39](/us/states/ks/districts/senate/39.md) — 100% (state senate)
- [KS House District 124](/us/states/ks/districts/house/124.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
