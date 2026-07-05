---
type: Jurisdiction
title: "Pickaway County, OH"
classification: county
fips: "39129"
state: "OH"
demographics:
  population: 60131
  population_under_18: 12970
  population_18_64: 37301
  population_65_plus: 9860
  median_household_income: 74040
  poverty_rate: 11.54
  homeownership_rate: 74.04
  unemployment_rate: 3.55
  median_home_value: 256800
  gini_index: 0.4186
  vacancy_rate: 4.71
  race_white: 54799
  race_black: 1899
  race_asian: 49
  race_native: 93
  hispanic: 1165
  bachelors_plus: 12276
districts:
  - to: "us/states/oh/districts/02"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/oh/districts/senate/3"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/house/12"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Pickaway County, OH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 60131 |
| Under 18 | 12970 |
| 18–64 | 37301 |
| 65+ | 9860 |
| Median household income | 74040 |
| Poverty rate | 11.54 |
| Homeownership rate | 74.04 |
| Unemployment rate | 3.55 |
| Median home value | 256800 |
| Gini index | 0.4186 |
| Vacancy rate | 4.71 |
| White | 54799 |
| Black | 1899 |
| Asian | 49 |
| Native | 93 |
| Hispanic/Latino | 1165 |
| Bachelor's or higher | 12276 |

## Districts

- [OH-02](/us/states/oh/districts/02.md) — 100% (congressional)
- [OH Senate District 3](/us/states/oh/districts/senate/3.md) — 100% (state senate)
- [OH House District 12](/us/states/oh/districts/house/12.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
