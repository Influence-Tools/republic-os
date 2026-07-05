---
type: Jurisdiction
title: "Medina County, OH"
classification: county
fips: "39103"
state: "OH"
demographics:
  population: 183660
  population_under_18: 39216
  population_18_64: 108089
  population_65_plus: 36355
  median_household_income: 94968
  poverty_rate: 6.27
  homeownership_rate: 80.25
  unemployment_rate: 2.9
  median_home_value: 287000
  gini_index: 0.4217
  vacancy_rate: 4.09
  race_white: 169009
  race_black: 2061
  race_asian: 1787
  race_native: 219
  hispanic: 5002
  bachelors_plus: 63571
districts:
  - to: "us/states/oh/districts/07"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/oh/districts/senate/22"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/house/66"
    rel: in-district
    area_weight: 0.5995
  - to: "us/states/oh/districts/house/67"
    rel: in-district
    area_weight: 0.4004
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Medina County, OH

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 183660 |
| Under 18 | 39216 |
| 18–64 | 108089 |
| 65+ | 36355 |
| Median household income | 94968 |
| Poverty rate | 6.27 |
| Homeownership rate | 80.25 |
| Unemployment rate | 2.9 |
| Median home value | 287000 |
| Gini index | 0.4217 |
| Vacancy rate | 4.09 |
| White | 169009 |
| Black | 2061 |
| Asian | 1787 |
| Native | 219 |
| Hispanic/Latino | 5002 |
| Bachelor's or higher | 63571 |

## Districts

- [OH-07](/us/states/oh/districts/07.md) — 100% (congressional)
- [OH Senate District 22](/us/states/oh/districts/senate/22.md) — 100% (state senate)
- [OH House District 66](/us/states/oh/districts/house/66.md) — 60% (state house)
- [OH House District 67](/us/states/oh/districts/house/67.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
