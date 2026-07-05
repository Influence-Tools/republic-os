---
type: Jurisdiction
title: "Tazewell County, VA"
classification: county
fips: "51185"
state: "VA"
demographics:
  population: 39624
  population_under_18: 8764
  population_18_64: 11045
  population_65_plus: 19815
  median_household_income: 47313
  poverty_rate: 18.52
  homeownership_rate: 74.42
  unemployment_rate: 3.83
  median_home_value: 118300
  gini_index: 0.4733
  vacancy_rate: 17.59
  race_white: 36879
  race_black: 1268
  race_asian: 244
  race_native: 14
  hispanic: 535
  bachelors_plus: 6415
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/va/districts/senate/5"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/va/districts/house/43"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Tazewell County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39624 |
| Under 18 | 8764 |
| 18–64 | 11045 |
| 65+ | 19815 |
| Median household income | 47313 |
| Poverty rate | 18.52 |
| Homeownership rate | 74.42 |
| Unemployment rate | 3.83 |
| Median home value | 118300 |
| Gini index | 0.4733 |
| Vacancy rate | 17.59 |
| White | 36879 |
| Black | 1268 |
| Asian | 244 |
| Native | 14 |
| Hispanic/Latino | 535 |
| Bachelor's or higher | 6415 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 5](/us/states/va/districts/senate/5.md) — 100% (state senate)
- [VA House District 43](/us/states/va/districts/house/43.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
