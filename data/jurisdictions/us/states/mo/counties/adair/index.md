---
type: Jurisdiction
title: "Adair County, MO"
classification: county
fips: "29001"
state: "MO"
demographics:
  population: 25301
  population_under_18: 4740
  population_18_64: 16668
  population_65_plus: 3893
  median_household_income: 61536
  poverty_rate: 22.01
  homeownership_rate: 61.02
  unemployment_rate: 4.14
  median_home_value: 165700
  gini_index: 0.5515
  vacancy_rate: 19.87
  race_white: 22360
  race_black: 1123
  race_asian: 526
  race_native: 99
  hispanic: 755
  bachelors_plus: 7717
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/18"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/3"
    rel: in-district
    area_weight: 0.7118
  - to: "us/states/mo/districts/house/4"
    rel: in-district
    area_weight: 0.2881
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Adair County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25301 |
| Under 18 | 4740 |
| 18–64 | 16668 |
| 65+ | 3893 |
| Median household income | 61536 |
| Poverty rate | 22.01 |
| Homeownership rate | 61.02 |
| Unemployment rate | 4.14 |
| Median home value | 165700 |
| Gini index | 0.5515 |
| Vacancy rate | 19.87 |
| White | 22360 |
| Black | 1123 |
| Asian | 526 |
| Native | 99 |
| Hispanic/Latino | 755 |
| Bachelor's or higher | 7717 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 18](/us/states/mo/districts/senate/18.md) — 100% (state senate)
- [MO House District 3](/us/states/mo/districts/house/3.md) — 71% (state house)
- [MO House District 4](/us/states/mo/districts/house/4.md) — 29% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
