---
type: Jurisdiction
title: "Bates County, MO"
classification: county
fips: "29013"
state: "MO"
demographics:
  population: 16186
  population_under_18: 3689
  population_18_64: 9366
  population_65_plus: 3131
  median_household_income: 60733
  poverty_rate: 15.86
  homeownership_rate: 74.93
  unemployment_rate: 5.94
  median_home_value: 170800
  gini_index: 0.4139
  vacancy_rate: 14.38
  race_white: 15006
  race_black: 346
  race_asian: 65
  race_native: 38
  hispanic: 416
  bachelors_plus: 2281
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/senate/31"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/125"
    rel: in-district
    area_weight: 0.6313
  - to: "us/states/mo/districts/house/62"
    rel: in-district
    area_weight: 0.3686
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Bates County, MO

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16186 |
| Under 18 | 3689 |
| 18–64 | 9366 |
| 65+ | 3131 |
| Median household income | 60733 |
| Poverty rate | 15.86 |
| Homeownership rate | 74.93 |
| Unemployment rate | 5.94 |
| Median home value | 170800 |
| Gini index | 0.4139 |
| Vacancy rate | 14.38 |
| White | 15006 |
| Black | 346 |
| Asian | 65 |
| Native | 38 |
| Hispanic/Latino | 416 |
| Bachelor's or higher | 2281 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 100% (congressional)
- [MO Senate District 31](/us/states/mo/districts/senate/31.md) — 100% (state senate)
- [MO House District 125](/us/states/mo/districts/house/125.md) — 63% (state house)
- [MO House District 62](/us/states/mo/districts/house/62.md) — 37% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
