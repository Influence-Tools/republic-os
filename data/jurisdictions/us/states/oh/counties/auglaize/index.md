---
type: Jurisdiction
title: "Auglaize County, OH"
classification: county
fips: "39011"
state: "OH"
demographics:
  population: 46125
  population_under_18: 11026
  population_18_64: 26028
  population_65_plus: 9071
  median_household_income: 78660
  poverty_rate: 7.08
  homeownership_rate: 78.11
  unemployment_rate: 2.72
  median_home_value: 189800
  gini_index: 0.3881
  vacancy_rate: 5.56
  race_white: 43647
  race_black: 447
  race_asian: 152
  race_native: 12
  hispanic: 868
  bachelors_plus: 9411
districts:
  - to: "us/states/oh/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/senate/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/oh/districts/house/84"
    rel: in-district
    area_weight: 0.5075
  - to: "us/states/oh/districts/house/78"
    rel: in-district
    area_weight: 0.4924
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Auglaize County, OH

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 46125 |
| Under 18 | 11026 |
| 18–64 | 26028 |
| 65+ | 9071 |
| Median household income | 78660 |
| Poverty rate | 7.08 |
| Homeownership rate | 78.11 |
| Unemployment rate | 2.72 |
| Median home value | 189800 |
| Gini index | 0.3881 |
| Vacancy rate | 5.56 |
| White | 43647 |
| Black | 447 |
| Asian | 152 |
| Native | 12 |
| Hispanic/Latino | 868 |
| Bachelor's or higher | 9411 |

## Districts

- [OH-04](/us/states/oh/districts/04.md) — 100% (congressional)
- [OH Senate District 12](/us/states/oh/districts/senate/12.md) — 100% (state senate)
- [OH House District 84](/us/states/oh/districts/house/84.md) — 51% (state house)
- [OH House District 78](/us/states/oh/districts/house/78.md) — 49% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
